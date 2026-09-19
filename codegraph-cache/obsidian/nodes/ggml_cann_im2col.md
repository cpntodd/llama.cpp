---
name: "ggml_cann_im2col"
type: "function"
file: "ggml/src/ggml-cann/aclnn_ops.cpp"
community: "ggml"
---

# ggml_cann_im2col

**Type:** `function`  **File:** `ggml/src/ggml-cann/aclnn_ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_type_size]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_element_size]] _calls_
- [[nodes/ggml_cann_type_mapping]] _calls_
- [[nodes/ggml_cann_create_int_array]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/ggml_cann_compute_forward]] _calls_
