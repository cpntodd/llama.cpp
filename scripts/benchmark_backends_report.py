#!/usr/bin/env python3
"""Benchmark local GGUF models on Prism llama.cpp backends and render HTML.

The runner intentionally uses llama-bench's JSONL output for comparable
throughput numbers and its verbose diagnostics for device-placement evidence.
It has no third-party Python dependencies.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BACKENDS: dict[str, dict[str, Any]] = {
    "Vulkan0": {"label": "Vulkan", "color": "#6ea8fe", "env": {}},
    "SYCL0": {
        "label": "SYCL",
        "color": "#70d6a5",
        "env": {"ONEAPI_DEVICE_SELECTOR": "opencl:gpu"},
    },
    "OPENVINO0": {
        "label": "OpenVINO GPU",
        "color": "#f6bd60",
        "env": {"GGML_OPENVINO_DEVICE": "GPU"},
    },
}


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description=(
            "Run llama-bench for every local GGUF/backend combination and "
            "write a self-contained CSS/SVG HTML report."
        )
    )
    parser.add_argument("--models-dir", type=Path, default=Path("/home/oddsoul/models"))
    parser.add_argument("--model-regex", help="Only test model filenames matching this regex")
    parser.add_argument(
        "--backends",
        default=",".join(BACKENDS),
        help="Comma-separated device IDs (Vulkan0,SYCL0,OPENVINO0)",
    )
    parser.add_argument("--bench-bin", type=Path, help="Path to llama-bench")
    parser.add_argument("--repo-root", type=Path, default=root)
    parser.add_argument("--output", type=Path, default=Path("artifacts/benchmarks/backend-report.html"))
    parser.add_argument("--work-dir", type=Path, default=Path("artifacts/benchmarks/backend-runs"))
    parser.add_argument("-p", "--prompt-tokens", type=int, default=512)
    parser.add_argument("-n", "--generation-tokens", type=int, default=128)
    parser.add_argument("-r", "--repetitions", type=int, default=3)
    parser.add_argument("-b", "--batch-size", type=int, default=2048)
    parser.add_argument("-u", "--ubatch-size", type=int, default=512)
    parser.add_argument("--gpu-layers", type=int, default=99)
    parser.add_argument("--timeout", type=float, default=900.0, help="Per-case timeout in seconds")
    parser.add_argument("--oneapi-setvars", type=Path, default=Path("/opt/intel/oneapi/setvars.sh"))
    parser.add_argument("--force", action="store_true", help="Ignore cached case results")
    parser.add_argument("--dry-run", action="store_true", help="Plan cases without executing llama-bench")
    return parser.parse_args()


def resolve_path(path: Path, root: Path) -> Path:
    return path if path.is_absolute() else root / path


def find_bench_binary(args: argparse.Namespace) -> Path:
    if args.bench_bin:
        return resolve_path(args.bench_bin, args.repo_root).resolve()
    candidates = [
        args.repo_root / "build-intel-all/bin/llama-bench",
        args.repo_root / "build/bin/llama-bench",
        args.repo_root / "bin/llama-bench",
    ]
    which = shutil.which("llama-bench")
    if which:
        candidates.append(Path(which))
    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate.resolve()
    raise SystemExit("Could not find llama-bench; pass --bench-bin explicitly.")


def discover_models(models_dir: Path, pattern: str | None) -> list[Path]:
    if not models_dir.is_dir():
        raise SystemExit(f"Models directory does not exist: {models_dir}")
    models = sorted(p for p in models_dir.iterdir() if p.is_file() and p.suffix.lower() == ".gguf")
    if pattern:
        expression = re.compile(pattern, re.IGNORECASE)
        models = [model for model in models if expression.search(model.name)]
    if not models:
        raise SystemExit(f"No GGUF models found in {models_dir}")
    return models


def selected_backends(value: str) -> list[str]:
    result = [item.strip() for item in value.split(",") if item.strip()]
    unknown = [item for item in result if item not in BACKENDS]
    if unknown:
        raise SystemExit(f"Unknown backend(s): {', '.join(unknown)}. Choose from {', '.join(BACKENDS)}")
    if not result:
        raise SystemExit("At least one backend is required.")
    return result


def case_key(model: Path, backend: str) -> str:
    safe_model = re.sub(r"[^A-Za-z0-9_.-]+", "_", model.stem).strip("._")
    return f"{safe_model}__{backend}"


def settings_for(args: argparse.Namespace, model: Path, backend: str, bench_bin: Path) -> dict[str, Any]:
    return {
        "model": str(model),
        "backend": backend,
        "bench_bin": str(bench_bin),
        "prompt_tokens": args.prompt_tokens,
        "generation_tokens": args.generation_tokens,
        "repetitions": args.repetitions,
        "batch_size": args.batch_size,
        "ubatch_size": args.ubatch_size,
        "gpu_layers": args.gpu_layers,
        "timeout": args.timeout,
    }


def command_for(args: argparse.Namespace, model: Path, backend: str, bench_bin: Path) -> list[str]:
    return [
        str(bench_bin),
        "-m",
        str(model),
        "-p",
        str(args.prompt_tokens),
        "-n",
        str(args.generation_tokens),
        "-r",
        str(args.repetitions),
        "-ngl",
        str(args.gpu_layers),
        "-b",
        str(args.batch_size),
        "-ub",
        str(args.ubatch_size),
        "-dev",
        backend,
        "-o",
        "jsonl",
        "-v",
    ]


def shell_command(command: list[str], env_updates: dict[str, str], setvars: Path | None) -> str:
    exports = " ".join(f"export {key}={shlex.quote(value)};" for key, value in env_updates.items())
    source = ""
    if setvars and setvars.is_file():
        source = f"source {shlex.quote(str(setvars))} --force >/dev/null 2>&1;"
    # GNU time provides peak RSS without adding a Python dependency. If absent,
    # the benchmark still runs and the report marks RSS as unavailable.
    timed = ["/usr/bin/time", "-v", "--"] if Path("/usr/bin/time").exists() else []
    return f"{source}{exports}exec {shlex.join(timed + command)}"


def parse_jsonl(stdout: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and "avg_ts" in value:
            records.append(value)
    return records


def first_float(pattern: str, text: str) -> float | None:
    match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    return float(match.group(1)) if match else None


def parse_diagnostics(text: str, backend: str) -> dict[str, Any]:
    selected = re.search(r"llama_prepare_model_devices: using device ([^\s(]+)", text)
    openvino = re.search(r"OpenVINO: using device\s+(\w+)", text)
    offload = re.search(r"offloaded\s+(\d+)\s*/\s*(\d+)\s+layers", text)
    free = re.search(r"using device [^\n]*?-\s*([0-9]+)\s+MiB free", text)
    buffers = re.findall(
        r"(?:load_tensors:|sched_reserve:)\s+([A-Z0-9_]+)\s+(model|compute) buffer size\s*=\s*([0-9.]+)\s*MiB",
        text,
        re.IGNORECASE,
    )
    model_buffer = None
    compute_buffer = None
    for device, buffer_kind, size in buffers:
        if device == backend:
            if buffer_kind.lower() == "compute":
                compute_buffer = float(size)
            else:
                model_buffer = float(size)
    return {
        "selected_device": selected.group(1) if selected else None,
        "selected_device_description": None,
        # All dynamic modules initialize during device discovery. Only report
        # the OpenVINO plugin setting as evidence when OpenVINO is selected;
        # otherwise a Vulkan/SYCL case would misleadingly show CPU here.
        "openvino_device": openvino.group(1) if backend == "OPENVINO0" and openvino else None,
        "offloaded_layers": int(offload.group(1)) if offload else None,
        "total_layers": int(offload.group(2)) if offload else None,
        "device_free_mib": int(free.group(1)) if free else None,
        "model_buffer_mib": model_buffer,
        "compute_buffer_mib": compute_buffer,
        "load_time_ms": first_float(r"load time\s*=\s*([0-9.]+)\s*ms", text),
        "prompt_time_ms": first_float(r"prompt eval time\s*=\s*([0-9.]+)\s*ms", text),
        "generation_time_ms": first_float(r"eval time\s*=\s*([0-9.]+)\s*ms", text),
        "peak_rss_kib": first_float(r"Maximum resident set size \(kbytes\):\s*([0-9]+)", text),
    }


def run_case(
    args: argparse.Namespace,
    model: Path,
    backend: str,
    bench_bin: Path,
    work_dir: Path,
) -> dict[str, Any]:
    settings = settings_for(args, model, backend, bench_bin)
    key = case_key(model, backend)
    result_path = work_dir / f"{key}.json"
    if result_path.is_file() and not args.force:
        try:
            cached = json.loads(result_path.read_text())
            if cached.get("settings") == settings:
                cached["cached"] = True
                return cached
        except (OSError, json.JSONDecodeError):
            pass

    command = command_for(args, model, backend, bench_bin)
    spec = BACKENDS[backend]
    result: dict[str, Any] = {
        "key": key,
        "model": model.name,
        "model_path": str(model),
        "backend": backend,
        "backend_label": spec["label"],
        "settings": settings,
        "command": command,
        "environment": spec["env"],
        "started_at": datetime.now(timezone.utc).isoformat(),
        "cached": False,
        "status": "planned" if args.dry_run else "running",
    }
    if args.dry_run:
        return result

    started = time.monotonic()
    stdout = ""
    stderr = ""
    returncode: int | None = None
    timed_out = False
    try:
        completed = subprocess.run(
            ["bash", "-lc", shell_command(command, spec["env"], args.oneapi_setvars)],
            cwd=args.repo_root,
            text=True,
            capture_output=True,
            timeout=args.timeout,
            check=False,
        )
        stdout = completed.stdout or ""
        stderr = completed.stderr or ""
        returncode = completed.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        stderr += f"\nBenchmark exceeded timeout ({args.timeout:.0f}s)."
    elapsed = time.monotonic() - started
    records = parse_jsonl(stdout)
    diagnostics = parse_diagnostics(stderr + "\n" + stdout, backend)
    prompt_record = next((record for record in records if int(record.get("n_prompt", 0)) > 0), None)
    generation_record = next((record for record in records if int(record.get("n_gen", 0)) > 0), None)
    metadata = records[0] if records else {}
    device_reported = metadata.get("devices") == backend
    device_logged = diagnostics.get("selected_device") == backend
    openvino_gpu = backend != "OPENVINO0" or diagnostics.get("openvino_device") == "GPU"
    placement_verified = (device_reported or device_logged) and openvino_gpu
    status = "timeout" if timed_out else (
        "pass" if returncode == 0 and records and placement_verified else "fail"
    )
    if returncode == 0 and records and not placement_verified:
        stderr += "\nPlacement evidence was not verified for the requested backend."
    result.update(
        {
            "status": status,
            "returncode": returncode,
            "elapsed_seconds": round(elapsed, 3),
            "records": records,
            "prompt_tps": prompt_record.get("avg_ts") if prompt_record else None,
            "generation_tps": generation_record.get("avg_ts") if generation_record else None,
            "model_type": metadata.get("model_type"),
            "model_size_bytes": metadata.get("model_size"),
            "model_params": metadata.get("model_n_params"),
            "reported_devices": metadata.get("devices"),
            "reported_backends": metadata.get("backends"),
            "placement_verified": placement_verified,
            "diagnostics": diagnostics,
            "stdout": stdout[-12000:],
            "stderr": stderr[-16000:],
        }
    )
    result_path.write_text(json.dumps(result, indent=2) + "\n")
    return result


def fmt(value: Any, digits: int = 1, suffix: str = "") -> str:
    if value is None:
        return "—"
    if isinstance(value, (int, float)):
        return f"{value:,.{digits}f}{suffix}"
    return html.escape(str(value))


def svg_bar_chart(title: str, metric: str, results: list[dict[str, Any]], backends: list[str], unit: str) -> str:
    models = list(dict.fromkeys(item["model"] for item in results))
    values = {(item["model"], item["backend"]): item.get(metric) for item in results}
    finite = [float(value) for value in values.values() if isinstance(value, (int, float)) and value >= 0]
    maximum = max(finite, default=1.0)
    width = 1120
    left = 230
    chart_width = 820
    group_height = max(1, len(backends)) * 21 + 18
    height = 82 + max(1, len(models)) * group_height + 42
    parts = [
        f'<svg class="chart" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title)}">',
        f'<text class="chart-title" x="18" y="26">{html.escape(title)}</text>',
        f'<text class="chart-unit" x="{width - 18}" y="26" text-anchor="end">{html.escape(unit)}</text>',
    ]
    for index, backend in enumerate(backends):
        x = left + index * 145
        parts.append(f'<rect x="{x}" y="42" width="12" height="12" fill="{BACKENDS[backend]["color"]}"/>')
        parts.append(f'<text class="legend" x="{x + 18}" y="52">{html.escape(BACKENDS[backend]["label"])}</text>')
    for row, model in enumerate(models):
        y = 78 + row * group_height
        label = model if len(model) <= 31 else model[:28] + "…"
        parts.append(f'<text class="axis-label" x="{left - 14}" y="{y + group_height / 2:.1f}" text-anchor="end">{html.escape(label)}</text>')
        parts.append(f'<line class="grid" x1="{left}" y1="{y + group_height - 4}" x2="{left + chart_width}" y2="{y + group_height - 4}"/>')
        for index, backend in enumerate(backends):
            value = values.get((model, backend))
            bar_y = y + index * 21
            if isinstance(value, (int, float)) and value >= 0:
                bar = chart_width * float(value) / maximum if maximum else 0
                bar = max(2, bar)
                parts.append(f'<rect class="bar" x="{left}" y="{bar_y:.1f}" width="{bar:.1f}" height="13" fill="{BACKENDS[backend]["color"]}"><title>{html.escape(model)} / {html.escape(backend)}: {value:.2f} {html.escape(unit)}</title></rect>')
                parts.append(f'<text class="bar-value" x="{left + bar + 5:.1f}" y="{bar_y + 11:.1f}">{value:.1f}</text>')
            else:
                parts.append(f'<text class="missing" x="{left + 4}" y="{bar_y + 11:.1f}">{html.escape(BACKENDS[backend]["label"])}: failed</text>')
    parts.append(f'<text class="axis-note" x="{left}" y="{height - 10}">Scale maximum: {maximum:.1f} {html.escape(unit)}</text>')
    parts.append("</svg>")
    return "".join(parts)


def status_class(status: str) -> str:
    return {"pass": "ok", "fail": "bad", "timeout": "bad", "running": "warn", "planned": "warn"}.get(status, "muted")


def generate_html(
    args: argparse.Namespace,
    results: list[dict[str, Any]],
    models: list[Path],
    backends: list[str],
    bench_bin: Path,
) -> str:
    passed = sum(item.get("status") == "pass" for item in results)
    failed = sum(item.get("status") in {"fail", "timeout"} for item in results)
    cached = sum(bool(item.get("cached")) for item in results)
    generated = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    prompt_chart = svg_bar_chart("Prompt processing throughput", "prompt_tps", results, backends, "tokens/s")
    generation_chart = svg_bar_chart("Generation throughput", "generation_tps", results, backends, "tokens/s")
    wall_chart = svg_bar_chart("End-to-end benchmark wall time", "elapsed_seconds", results, backends, "seconds")

    rows: list[str] = []
    for item in results:
        diag = item.get("diagnostics", {})
        evidence = []
        if diag.get("selected_device"):
            evidence.append(f"selected {diag['selected_device']}")
        if diag.get("offloaded_layers") is not None:
            evidence.append(f"{diag['offloaded_layers']}/{diag['total_layers']} layers offloaded")
        if diag.get("openvino_device"):
            evidence.append(f"OpenVINO {diag['openvino_device']}")
        if not item.get("placement_verified", False) and item.get("status") not in {"planned", "running"}:
            evidence.append("placement unverified")
        note = "; ".join(evidence) or "see diagnostic log"
        rows.append(
            "<tr>"
            f"<td>{html.escape(item['model'])}</td>"
            f"<td><span class=\"backend-dot\" style=\"background:{BACKENDS[item['backend']]['color']}\"></span>{html.escape(item['backend_label'])}</td>"
            f"<td><span class=\"pill {status_class(item.get('status', ''))}\">{html.escape(item.get('status', 'unknown'))}</span></td>"
            f"<td>{fmt(item.get('prompt_tps'), 1)}</td><td>{fmt(item.get('generation_tps'), 1)}</td>"
            f"<td>{fmt(item.get('elapsed_seconds'), 1, ' s')}</td>"
            f"<td>{fmt(diag.get('peak_rss_kib'), 0, ' KiB')}</td>"
            f"<td>{html.escape(note)}</td></tr>"
        )

    details: list[str] = []
    for item in results:
        diagnostics = json.dumps(item.get("diagnostics", {}), indent=2)
        stderr = item.get("stderr", "")
        details.append(
            f"<details><summary>{html.escape(item['model'])} · {html.escape(item['backend'])} · {html.escape(item.get('status', 'unknown'))}</summary>"
            f"<h4>Command</h4><code>{html.escape(shlex.join(item.get('command', [])))}</code>"
            f"<h4>Parsed diagnostics</h4><pre>{html.escape(diagnostics)}</pre>"
            f"<h4>Last diagnostic output</h4><pre>{html.escape(stderr[-8000:])}</pre></details>"
        )

    model_names = ", ".join(html.escape(model.name) for model in models)
    backend_names = ", ".join(html.escape(backend) for backend in backends)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prism llama.cpp backend benchmark report</title>
<style>
:root {{ color-scheme: dark; --bg:#0c111b; --panel:#151d2d; --panel2:#1b2638; --text:#edf3ff; --muted:#9eacc2; --line:#2a3850; --accent:#8ab4ff; }}
* {{ box-sizing:border-box; }} body {{ margin:0; background:radial-gradient(circle at top,#17243b 0,#0c111b 46rem); color:var(--text); font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif; }}
main {{ max-width:1480px; margin:auto; padding:32px 22px 70px; }} h1 {{ margin:0 0 8px; font-size:clamp(28px,4vw,46px); letter-spacing:-.03em; }} h2 {{ margin:0 0 12px; font-size:22px; }} h3 {{ margin:26px 0 8px; }} p {{ color:var(--muted); }} code,pre {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
.lede {{ max-width:920px; font-size:17px; }} .meta {{ color:var(--muted); font-size:13px; }} .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:12px; margin:28px 0; }}
.card,.panel,details {{ background:color-mix(in srgb,var(--panel) 94%,transparent); border:1px solid var(--line); border-radius:14px; box-shadow:0 12px 35px #0003; }} .card {{ padding:18px; }} .card strong {{ display:block; font-size:30px; color:var(--accent); }} .card span {{ color:var(--muted); }}
.panel {{ padding:20px; margin:18px 0; overflow:auto; }} .charts {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(480px,1fr)); gap:16px; }} .chart {{ display:block; width:100%; min-width:500px; height:auto; }} .chart-title {{ fill:var(--text); font-size:17px; font-weight:650; }} .chart-unit,.legend,.axis-note {{ fill:var(--muted); font-size:12px; }} .axis-label,.bar-value {{ fill:var(--text); font-size:12px; }} .grid {{ stroke:var(--line); stroke-width:1; }} .missing {{ fill:#ff8d8d; font-size:11px; }}
table {{ width:100%; border-collapse:collapse; min-width:1080px; }} th,td {{ padding:10px 9px; text-align:left; border-bottom:1px solid var(--line); vertical-align:top; }} th {{ color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.06em; }} tr:hover {{ background:var(--panel2); }} .backend-dot {{ display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:7px; }} .pill {{ border-radius:999px; padding:3px 9px; font-size:12px; }} .ok {{ background:#174d3e; color:#8ff0c3; }} .bad {{ background:#5e2932; color:#ffb2b2; }} .warn {{ background:#5a471d; color:#ffdc86; }} .muted {{ background:#334057; color:#c0c9da; }}
details {{ margin:10px 0; padding:12px 15px; }} summary {{ cursor:pointer; color:var(--accent); }} pre {{ max-height:360px; overflow:auto; background:#090e17; border:1px solid var(--line); padding:12px; border-radius:8px; white-space:pre-wrap; font-size:12px; }} .callout {{ border-left:4px solid var(--accent); padding:12px 16px; background:#17243a; }} ul {{ color:var(--muted); }}
@media(max-width:650px) {{ main {{ padding:22px 12px 48px; }} .charts {{ display:block; }} .panel {{ padding:13px; }} }}
</style></head><body><main>
<header><h1>Prism llama.cpp backend benchmark</h1><p class="lede">A reproducible comparison of local GGUF models on Vulkan, SYCL, and OpenVINO GPU. The report combines throughput, wall time, memory diagnostics, layer offload evidence, and failure logs.</p><p class="meta">Generated {html.escape(generated)} · llama-bench: {html.escape(str(bench_bin))}</p></header>
<section class="cards"><div class="card"><strong>{len(models)}</strong><span>models discovered</span></div><div class="card"><strong>{len(backends)}</strong><span>backends tested</span></div><div class="card"><strong>{passed}</strong><span>passed cases</span></div><div class="card"><strong>{failed}</strong><span>failed or timed out</span></div><div class="card"><strong>{cached}</strong><span>cached cases</span></div></section>
<section class="panel"><h2>What this report measures</h2><div class="callout"><b>Selection proof:</b> verbose llama-bench output must say <code>llama_prepare_model_devices: using device ...</code>, and tensor/compute buffers must name the same device. OpenVINO must report <code>using device GPU</code>; otherwise it is a CPU comparison.</div><ul><li><b>Prompt tokens/s</b> measures prompt ingestion and is sensitive to batch size and memory bandwidth.</li><li><b>Generation tokens/s</b> measures autoregressive decode and is the main interactive-chat metric.</li><li><b>Wall time</b> includes model initialization and benchmark execution; use it to spot slow startup or compilation.</li><li><b>Peak RSS, model buffer, free device memory, and offloaded layers</b> expose memory pressure and accidental CPU fallback.</li><li>Missing bars mean the case failed, timed out, or produced no valid llama-bench JSON result. Expand its diagnostic entry below.</li></ul></section>
<section class="panel"><h2>Throughput and timing</h2><div class="charts">{prompt_chart}{generation_chart}{wall_chart}</div></section>
<section class="panel"><h2>Case matrix</h2><p class="meta">Models: {model_names}<br>Devices: {backend_names}<br>Configuration: {args.prompt_tokens} prompt tokens · {args.generation_tokens} generated tokens · {args.repetitions} repetitions · batch {args.batch_size} / microbatch {args.ubatch_size} · {args.gpu_layers} GPU layers</p><table><thead><tr><th>Model</th><th>Backend</th><th>Status</th><th>Prompt tok/s</th><th>Generation tok/s</th><th>Wall</th><th>Peak RSS</th><th>Placement evidence</th></tr></thead><tbody>{''.join(rows)}</tbody></table></section>
<section class="panel"><h2>Detailed diagnostics</h2><p>All cases are saved as JSON under the work directory. The excerpts below make backend selection and failure causes auditable without rerunning a test.</p>{''.join(details)}</section>
<section class="panel"><h2>Benchmark interpretation</h2><p>Compare backends only when the same model, quantization, context, batch sizes, GPU-layer count, warmup policy, and repetition count are used. A successful process start alone does not prove GPU execution: use the selected-device and buffer lines, then corroborate with render-node activity or GPU telemetry while generation is running. Backend modules may all appear in the general <code>backends</code> field because Prism dynamically loads them; the selected <code>dev</code> field is the meaningful comparison key.</p></section>
</main></body></html>"""


def main() -> int:
    args = parse_args()
    args.repo_root = args.repo_root.resolve()
    args.models_dir = resolve_path(args.models_dir, args.repo_root).resolve()
    args.output = resolve_path(args.output, args.repo_root).resolve()
    args.work_dir = resolve_path(args.work_dir, args.repo_root).resolve()
    args.oneapi_setvars = resolve_path(args.oneapi_setvars, args.repo_root).resolve()
    bench_bin = find_bench_binary(args)
    models = discover_models(args.models_dir, args.model_regex)
    backends = selected_backends(args.backends)
    args.work_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for model in models:
        for backend in backends:
            print(f"[{backend:10}] {model.name}", flush=True)
            results.append(run_case(args, model, backend, bench_bin, args.work_dir))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(generate_html(args, results, models, backends, bench_bin))
    summary = {status: sum(item.get("status") == status for item in results) for status in {"pass", "fail", "timeout", "planned"}}
    print(json.dumps({"report": str(args.output), "work_dir": str(args.work_dir), "summary": summary}, indent=2))
    return 0 if not any(item.get("status") in {"fail", "timeout"} for item in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
