---
name: "ggml_cann_dup"
type: "function"
file: "ggml/src/ggml-cann/aclnn_ops.cpp"
community: "ggml"
---

# ggml_cann_dup

**Type:** `function`  **File:** `ggml/src/ggml-cann/aclnn_ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/cann_copy]] _calls_
- [[nodes/ggml_cann_type_mapping]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_cann_create_scalar]] _calls_

## Used By

- [[nodes/ggml_cann_cpy]] _calls_
- [[nodes/ggml_cann_compute_forward]] _calls_
