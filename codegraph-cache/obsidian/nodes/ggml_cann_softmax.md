---
name: "ggml_cann_softmax"
type: "function"
file: "ggml/src/ggml-cann/aclnn_ops.cpp"
community: "ggml"
---

# ggml_cann_softmax

**Type:** `function`  **File:** `ggml/src/ggml-cann/aclnn_ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_cann_create_scalar]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_cann_type_mapping]] _calls_
- [[nodes/ggml_element_size]] _calls_
- [[nodes/aclnn_softmax]] _calls_

## Used By

- [[nodes/ggml_cann_flash_attn_ext]] _calls_
- [[nodes/ggml_cann_compute_forward]] _calls_
