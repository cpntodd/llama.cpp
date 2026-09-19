---
name: "ggml_sycl_op_swiglu_oai"
type: "function"
file: "ggml/src/ggml-sycl/element_wise.cpp"
community: "ggml"
---

# ggml_sycl_op_swiglu_oai

**Type:** `function`  **File:** `ggml/src/ggml-sycl/element_wise.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/stream]] _calls_
- [[nodes/ggml_is_contiguous_1]] _calls_
- [[nodes/ggml_element_size]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_get_op_params_f32]] _calls_
- [[nodes/ggml_nelements]] _calls_

## Used By

- [[nodes/ggml_sycl_swiglu_oai]] _calls_
