---
name: "ggml_backend_sched_alloc_graph"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_sched_alloc_graph

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_sched_split_graph]] _calls_
- [[nodes/ggml_backend_sched_alloc_splits]] _calls_

## Used By

- [[nodes/clip_encode]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/ggml_backend_sched_graph_compute_async]] _calls_
- [[nodes/ggml_opt_alloc]] _calls_
