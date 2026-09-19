---
name: "ggml_metal_op_mul_mat"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_mul_mat

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_metal_fwht_supported_size]] _calls_
- [[nodes/ggml_metal_op_fwht]] _calls_
- [[nodes/getenv]] _calls_
- [[nodes/ggml_metal_op_mul_mat_q1_0_pc_supported]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_q1_0_planes]] _calls_
- [[nodes/ggml_metal_op_concurrency_reset]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_mul_mv_q1_0_pc]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_mul_mv_ext]] _calls_
- [[nodes/ggml_is_transposed]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_mul_mm]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_mul_mv]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
