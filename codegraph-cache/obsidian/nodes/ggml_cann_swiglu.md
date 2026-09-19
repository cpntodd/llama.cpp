---
name: "ggml_cann_swiglu"
type: "function"
file: "ggml/src/ggml-cann/aclnn_ops.cpp"
community: "ggml"
---

# ggml_cann_swiglu

**Type:** `function`  **File:** `ggml/src/ggml-cann/aclnn_ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_up32]] _imports_
- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/aclnn_add]] _imports_
- [[nodes/aclnn_div]] _imports_
- [[nodes/aclnn_exp]] _imports_
- [[nodes/aclnn_fill_scalar]] _imports_
- [[nodes/aclnn_mul]] _imports_
- [[nodes/aclnn_pow_tensor_tensor]] _imports_
- [[nodes/aclnn_reduce_sum]] _imports_
- [[nodes/aclnn_softmax]] _imports_
- [[nodes/aclnn_sub]] _imports_
- [[nodes/ggml-common.h]] _imports_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_element_size]] _calls_
- [[nodes/ggml_cann_type_mapping]] _calls_

## Used By

- [[nodes/ggml_cann_error]] _imports_
- [[nodes/ggml_cann_compute_forward]] _calls_
