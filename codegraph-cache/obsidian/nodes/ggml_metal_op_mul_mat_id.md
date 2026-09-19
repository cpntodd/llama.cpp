---
name: "ggml_metal_op_mul_mat_id"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_mul_mat_id

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_transposed]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_metal_op_mul_mat_id_extra_tpe]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_mul_mm_id_map0]] _calls_
- [[nodes/ggml_metal_op_concurrency_reset]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_mul_mm_id]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_mul_mv_id]] _calls_
- [[nodes/ggml_is_quantized]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
