---
name: "ggml_gallocr_new_n"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "tests"
---

# ggml_gallocr_new_n

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_backend_buft_get_alignment]] _calls_
- [[nodes/ggml_backend_buft_get_max_size]] _calls_
- [[nodes/ggml_dyn_tallocr_new]] _calls_

## Used By

- [[nodes/test_multiple_buffer_types]] _calls_
- [[nodes/test_buffer_size_zero]] _calls_
- [[nodes/ggml_backend_sched_compute_splits]] _calls_
- [[nodes/ggml_gallocr_new]] _calls_
