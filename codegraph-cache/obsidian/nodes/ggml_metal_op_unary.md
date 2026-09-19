---
name: "ggml_metal_op_unary"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_unary

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/ggml_get_op_params_f32]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_unary]] _calls_
- [[nodes/ggml_nelements]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
