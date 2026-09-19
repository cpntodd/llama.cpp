---
name: "dispatch_ggml_sycl_op_fused_glu"
type: "function"
file: "ggml/src/ggml-sycl/element_wise.cpp"
community: "ggml"
---

# dispatch_ggml_sycl_op_fused_glu

**Type:** `function`  **File:** `ggml/src/ggml-sycl/element_wise.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/stream]] _calls_
- [[nodes/ggml_is_contiguous_1]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_element_size]] _calls_
- [[nodes/dispatch_ggml_sycl_op_unary]] _calls_
- [[nodes/ceil_div]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/unary_op_flat_kernel]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/unary_gated_op_flat_kernel]] _calls_
