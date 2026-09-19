---
name: "unary_mul_sycl"
type: "function"
file: "ggml/src/ggml-sycl/element_wise.cpp"
community: "ggml"
---

# unary_mul_sycl

**Type:** `function`  **File:** `ggml/src/ggml-sycl/element_wise.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ceil_div]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/unary_mul_flat_kernel]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/unary_mul_strided_kernel]] _calls_

## Used By

- [[nodes/ggml_sycl_op_unary_mul_fused]] _calls_
