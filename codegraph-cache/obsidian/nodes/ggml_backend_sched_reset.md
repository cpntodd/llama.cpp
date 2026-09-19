---
name: "ggml_backend_sched_reset"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_sched_reset

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_hash_set_reset]] _calls_

## Used By

- [[nodes/clip_encode]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/ggml_backend_sched_compute_splits]] _calls_
- [[nodes/ggml_backend_sched_reserve_size]] _calls_
- [[nodes/ggml_backend_sched_reserve]] _calls_
- [[nodes/ggml_backend_sched_graph_compute_async]] _calls_
- [[nodes/ggml_opt_alloc]] _calls_
