---
name: "ggml_sycl_op_xielu"
type: "function"
file: "ggml/src/ggml-sycl/element_wise.cpp"
community: "ggml"
---

# ggml_sycl_op_xielu

**Type:** `function`  **File:** `ggml/src/ggml-sycl/element_wise.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_op_params_f32]] _calls_
- [[nodes/dispatch_ggml_sycl_op_unary]] _calls_
- [[nodes/ceil_div]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/unary_op_xielu_kernel]] _calls_

## Used By

- [[nodes/ggml_sycl_xielu]] _calls_
