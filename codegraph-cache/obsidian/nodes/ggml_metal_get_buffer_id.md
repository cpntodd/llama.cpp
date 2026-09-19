---
name: "ggml_metal_get_buffer_id"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_get_buffer_id

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml-metal-ops.h]] _imports_
- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/ggml_up32]] _imports_
- [[nodes/ggml-backend-impl.h]] _imports_
- [[nodes/ggml-metal-impl.h]] _imports_
- [[nodes/ggml_mem_range]] _imports_
- [[nodes/ggml_metal_device_deleter]] _imports_
- [[nodes/ggml_metal_tuning]] _imports_
- [[nodes/ggml_metal_op]] _calls_
- [[nodes/ggml_mem_ranges_init]] _calls_
- [[nodes/ggml_op_is_empty]] _calls_
- [[nodes/ggml_is_empty]] _calls_
- [[nodes/ggml_mem_ranges_free]] _calls_

## Used By

- [[nodes/ggml_metal_op_concat]] _calls_
- [[nodes/ggml_metal_op_repeat]] _calls_
- [[nodes/ggml_metal_op_acc]] _calls_
- [[nodes/ggml_metal_op_unary]] _calls_
- [[nodes/ggml_metal_op_glu]] _calls_
- [[nodes/ggml_metal_op_sum]] _calls_
- [[nodes/ggml_metal_op_sum_rows]] _calls_
- [[nodes/ggml_metal_op_cumsum]] _calls_
- [[nodes/ggml_metal_op_get_rows]] _calls_
- [[nodes/ggml_metal_op_set_rows_wide]] _calls_
- [[nodes/ggml_metal_op_set_rows]] _calls_
- [[nodes/ggml_metal_op_diag]] _calls_
- [[nodes/ggml_metal_op_lightning_indexer]] _calls_
- [[nodes/ggml_metal_op_dsv4_hc]] _calls_
- [[nodes/ggml_metal_op_soft_max]] _calls_
- [[nodes/ggml_metal_op_ssm_conv]] _calls_
- [[nodes/ggml_metal_op_ssm_scan]] _calls_
- [[nodes/ggml_metal_op_rwkv]] _calls_
- [[nodes/ggml_metal_op_gated_delta_net]] _calls_
- [[nodes/ggml_metal_op_solve_tri]] _calls_
- [[nodes/ggml_metal_op_set]] _calls_
- [[nodes/ggml_metal_op_cpy]] _calls_
- [[nodes/ggml_metal_op_pool_1d]] _calls_
- [[nodes/ggml_metal_op_fwht_impl]] _calls_
- [[nodes/ggml_metal_op_pool_2d]] _calls_
- [[nodes/ggml_metal_op_mul_mat]] _calls_
- [[nodes/ggml_metal_op_mul_mat_id]] _calls_
- [[nodes/ggml_metal_op_add_id]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext]] _calls_
- [[nodes/ggml_metal_op_bin]] _calls_
