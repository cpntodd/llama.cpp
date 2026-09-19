---
name: "ggml_backend_sched_graph_compute_async"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_sched_graph_compute_async

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_sched_reset]] _calls_
- [[nodes/ggml_backend_sched_alloc_graph]] _calls_
- [[nodes/ggml_backend_sched_compute_splits]] _calls_

## Used By

- [[nodes/needs_raw_logits]] _calls_
- [[nodes/ggml_backend_sched_graph_compute]] _calls_
