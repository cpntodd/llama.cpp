---
name: "ggml_graph_compute_thread_sync"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_graph_compute_thread_sync

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_fetch_add_explicit]] _calls_
- [[nodes/atomic_thread_fence]] _calls_

## Used By

- [[nodes/ggml_graph_compute_check_for_work]] _calls_
