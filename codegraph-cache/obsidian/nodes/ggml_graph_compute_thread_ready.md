---
name: "ggml_graph_compute_thread_ready"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_graph_compute_thread_ready

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_load_explicit]] _calls_

## Used By

- [[nodes/ggml_graph_compute_poll_for_work]] _calls_
- [[nodes/ggml_graph_compute_check_for_work]] _calls_
