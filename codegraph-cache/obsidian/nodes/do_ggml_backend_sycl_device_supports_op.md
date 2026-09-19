---
name: "do_ggml_backend_sycl_device_supports_op"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# do_ggml_backend_sycl_device_supports_op

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/ggml_is_contiguous_1]] _calls_
- [[nodes/ggml_is_permuted]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_supported]] _calls_

## Used By

- [[nodes/ggml_backend_sycl_device_supports_op]] _calls_
