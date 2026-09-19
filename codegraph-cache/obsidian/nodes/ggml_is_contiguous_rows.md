---
name: "ggml_is_contiguous_rows"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_is_contiguous_rows

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_type_size]] _calls_

## Used By

- [[nodes/ggml_can_out_prod]] _calls_
- [[nodes/ggml_calc_pool_output_size]] _calls_
- [[nodes/apply_unary_op]] _calls_
- [[nodes/apply_binary_op]] _calls_
- [[nodes/ggml_compute_forward_tri]] _calls_
- [[nodes/ggml_compute_forward_solve_tri]] _calls_
- [[nodes/ggml_webgpu_can_fuse_rms_norm_mul]] _calls_
- [[nodes/ggml_backend_webgpu_device_supports_op]] _calls_
- [[nodes/ggml_backend_cann_supports_op]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_sum_rows]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_norm]] _calls_
- [[nodes/ggml_metal_op_acc]] _calls_
- [[nodes/ggml_metal_op_unary]] _calls_
- [[nodes/ggml_metal_op_sum_rows]] _calls_
- [[nodes/ggml_metal_op_cumsum]] _calls_
- [[nodes/ggml_metal_op_add_id]] _calls_
- [[nodes/ggml_metal_op_bin]] _calls_
- [[nodes/ggml_metal_op_l2_norm]] _calls_
- [[nodes/ggml_metal_op_norm]] _calls_
- [[nodes/ggml_metal_op_argsort]] _calls_
- [[nodes/ggml_metal_op_top_k]] _calls_
- [[nodes/ggml_et_can_fuse]] _calls_
- [[nodes/ggml_backend_et_device_supports_op]] _calls_
- [[nodes/ggml_et_op_flash_attn_ext]] _calls_
- [[nodes/ggml_et_op_set_rows]] _calls_
- [[nodes/ggml_hexagon_supported_gated_delta_net]] _calls_
