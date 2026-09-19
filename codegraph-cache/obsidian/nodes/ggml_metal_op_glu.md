---
name: "ggml_metal_op_glu"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_glu

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_glu]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_get_op_params_f32]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
