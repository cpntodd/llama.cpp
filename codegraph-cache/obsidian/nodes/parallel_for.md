---
name: "parallel_for"
type: "function"
file: "ggml/src/ggml-cpu/amx/common.h"
community: "ggml"
---

# parallel_for

**Type:** `function`  **File:** `ggml/src/ggml-cpu/amx/common.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/balance211]] _calls_

## Used By

- [[nodes/convert_B_packed_format]] _calls_
- [[nodes/ggml_sycl_add_id]] _calls_
- [[nodes/ggml_sycl_op_rwkv_wkv6]] _calls_
- [[nodes/ggml_sycl_op_rwkv_wkv7]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_onednn_supported]] _calls_
- [[nodes/dw_calculate_input_coord]] _calls_
- [[nodes/ggml_sycl_op_set]] _calls_
- [[nodes/rope_yarn_ramp]] _calls_
- [[nodes/ggml_sycl_op_pool2d]] _calls_
- [[nodes/ggml_sycl_op_pool1d]] _calls_
- [[nodes/sigmoid_warp_inplace]] _calls_
- [[nodes/ggml_sycl_swap]] _calls_
- [[nodes/next_power_of_2]] _calls_
- [[nodes/ggml_sycl_op_mean]] _calls_
- [[nodes/ggml_sycl_op_diag_mask_inf]] _calls_
- [[nodes/ggml_sycl_group_norm]] _calls_
- [[nodes/sycl_ext_free]] _calls_
- [[nodes/reorder_qw_q4_k]] _calls_
- [[nodes/reorder_qw_q4_k_moe]] _calls_
- [[nodes/reorder_qw_q5_k_moe]] _calls_
- [[nodes/reorder_qw_q6_k_moe]] _calls_
- [[nodes/reorder_qw_q2_k]] _calls_
- [[nodes/reorder_qw_q3_k]] _calls_
- [[nodes/reorder_qw_q5_k]] _calls_
- [[nodes/reorder_qw_q6_k]] _calls_
- [[nodes/ggml_sycl_mul_mat_glu_mmvq_fused]] _calls_
- [[nodes/ggml_backend_sycl_comm_free]] _calls_
- [[nodes/dequantize_row_q4_K_sycl_reorder]] _calls_
- [[nodes/dequantize_row_q5_K_sycl_reorder]] _calls_
- [[nodes/dequantize_row_q6_K_sycl_reorder]] _calls_
