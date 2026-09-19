---
name: "ggml_metal_op_concurrency_reset"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_concurrency_reset

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_mem_ranges_reset]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
- [[nodes/ggml_metal_op_acc]] _calls_
- [[nodes/ggml_metal_op_cumsum]] _calls_
- [[nodes/ggml_metal_op_ssm_conv]] _calls_
- [[nodes/ggml_metal_op_gated_delta_net]] _calls_
- [[nodes/ggml_metal_op_set]] _calls_
- [[nodes/ggml_metal_op_fwht_signed]] _calls_
- [[nodes/ggml_metal_op_mul_mat]] _calls_
- [[nodes/ggml_metal_op_mul_mat_id]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext]] _calls_
- [[nodes/ggml_metal_op_bin]] _calls_
- [[nodes/ggml_metal_op_norm]] _calls_
- [[nodes/ggml_metal_op_snake_fused]] _calls_
- [[nodes/ggml_metal_op_argsort]] _calls_
- [[nodes/ggml_metal_op_top_k]] _calls_
- [[nodes/ggml_metal_op_count_equal]] _calls_
