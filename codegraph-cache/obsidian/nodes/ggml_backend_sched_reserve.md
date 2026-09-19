---
name: "ggml_backend_sched_reserve"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "src"
---

# ggml_backend_sched_reserve

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_sched_synchronize]] _calls_
- [[nodes/ggml_backend_sched_split_graph]] _calls_
- [[nodes/ggml_gallocr_reserve_n]] _calls_
- [[nodes/ggml_backend_sched_reset]] _calls_

## Used By

- [[nodes/reserve_compute_meta]] _calls_
- [[nodes/needs_raw_logits]] _calls_
