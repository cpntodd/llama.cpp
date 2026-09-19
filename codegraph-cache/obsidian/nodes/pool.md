---
name: "pool"
type: "function"
file: "ggml/src/ggml-sycl/common.hpp"
community: "ggml"
---

# pool

**Type:** `function`  **File:** `ggml/src/ggml-sycl/common.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_pool_alloc]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/realloc]] _calls_

## Used By

- [[nodes/ggml_new_object]] _calls_
- [[nodes/build_sdpa]] _calls_
- [[nodes/if]] _calls_
- [[nodes/ggml_sycl_get_device]] _calls_
- [[nodes/engine_dnnl]] _calls_
- [[nodes/next_power_of_2]] _calls_
- [[nodes/ggml_sycl_op_argsort]] _calls_
- [[nodes/ggml_sycl_set_peer_access]] _calls_
- [[nodes/constexpr]] _calls_
- [[nodes/ggml_sycl_group_norm]] _calls_
- [[nodes/ggml_sycl_mul_mat_glu_mmvq_fused]] _calls_
- [[nodes/ggml_backend_sycl_reg_get_device]] _calls_
- [[nodes/convert_f32]] _calls_
- [[nodes/MKL_ACCUM]] _calls_
- [[nodes/ggml_sycl_op_out_prod]] _calls_
- [[nodes/ggml_sycl_op_conv_3d]] _calls_
- [[nodes/get_dequantize_V]] _calls_
- [[nodes/ggml_sycl_cross_entropy_loss]] _calls_
- [[nodes/ggml_cann_geglu]] _calls_
- [[nodes/ggml_cann_argsort]] _calls_
- [[nodes/ggml_cann_l2_norm]] _calls_
- [[nodes/ggml_cann_cross_entropy_loss]] _calls_
- [[nodes/ggml_cann_group_norm]] _calls_
- [[nodes/ggml_cann_solve_tri]] _calls_
- [[nodes/ggml_cann_max_pool2d]] _calls_
- [[nodes/ggml_cann_dup]] _calls_
- [[nodes/ggml_cann_diag_mask]] _calls_
- [[nodes/ggml_cann_im2col]] _calls_
- [[nodes/ggml_cann_timestep_embedding]] _calls_
- [[nodes/aclnn_pow_tensor_tensor]] _calls_
