---
name: "ggml_graph_compute_thread"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_graph_compute_thread

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_cpu_riscv64_spacemit_set_numa_thread_affinity]] _calls_
- [[nodes/set_numa_thread_affinity]] _calls_
- [[nodes/atomic_load_explicit]] _calls_
- [[nodes/ggml_op_is_empty]] _calls_
- [[nodes/ggml_compute_forward]] _calls_
- [[nodes/atomic_store_explicit]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/ggml_backend_cpu_riscv64_spacemit_clear_numa_thread_affinity_threaded]] _calls_

## Used By

- [[nodes/ggml_graph_compute_secondary_thread]] _calls_
- [[nodes/ggml_graph_compute]] _calls_
