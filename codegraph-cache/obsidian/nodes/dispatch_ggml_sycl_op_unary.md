---
name: "dispatch_ggml_sycl_op_unary"
type: "function"
file: "ggml/src/ggml-sycl/element_wise.cpp"
community: "ggml"
---

# dispatch_ggml_sycl_op_unary

**Type:** `function`  **File:** `ggml/src/ggml-sycl/element_wise.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/stream]] _calls_
- [[nodes/ggml_nelements]] _calls_

## Used By

- [[nodes/dispatch_ggml_sycl_op_fused_glu]] _calls_
- [[nodes/ggml_sycl_op_log]] _calls_
- [[nodes/ggml_sycl_op_sqrt]] _calls_
- [[nodes/ggml_sycl_op_sin]] _calls_
- [[nodes/ggml_sycl_op_cos]] _calls_
- [[nodes/ggml_sycl_op_leaky_relu]] _calls_
- [[nodes/ggml_sycl_op_sqr]] _calls_
- [[nodes/ggml_sycl_op_clamp]] _calls_
- [[nodes/ggml_sycl_op_xielu]] _calls_
