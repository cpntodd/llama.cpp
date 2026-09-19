---
name: "ceil_div"
type: "function"
file: "ggml/src/ggml-sycl/common.hpp"
community: "ggml"
---

# ceil_div

**Type:** `function`  **File:** `ggml/src/ggml-sycl/common.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gpu_has_xmx]] _calls_
- [[nodes/ggml_sycl_get_env]] _calls_

## Used By

- [[nodes/dequantize_row_nvfp4_sycl]] _calls_
- [[nodes/unary_mul_sycl]] _calls_
- [[nodes/dispatch_ggml_sycl_op_fused_glu]] _calls_
- [[nodes/ggml_sycl_op_arange]] _calls_
- [[nodes/ggml_sycl_op_log]] _calls_
- [[nodes/ggml_sycl_op_sqrt]] _calls_
- [[nodes/ggml_sycl_op_sin]] _calls_
- [[nodes/ggml_sycl_op_cos]] _calls_
- [[nodes/ggml_sycl_op_leaky_relu]] _calls_
- [[nodes/ggml_sycl_op_sqr]] _calls_
- [[nodes/ggml_sycl_op_clamp]] _calls_
- [[nodes/ggml_sycl_op_xielu]] _calls_
- [[nodes/cpy_blck_q_f32]] _calls_
- [[nodes/cpy_blck_f16_q5_0]] _calls_
- [[nodes/ggml_sycl_src_to_f32]] _calls_
- [[nodes/constexpr]] _calls_
