---
name: "ggml_graph_compute_check_for_work"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_graph_compute_check_for_work

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_graph_compute_poll_for_work]] _calls_
- [[nodes/ggml_graph_compute_thread_sync]] _calls_
- [[nodes/ggml_graph_compute_thread_ready]] _calls_

## Used By

- [[nodes/ggml_graph_compute_secondary_thread]] _calls_
