---
name: "ggml_webgpu_row_norm"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_row_norm

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_webgpu_u32_from_f32]] _calls_
- [[nodes/ggml_get_op_params_f32]] _calls_
- [[nodes/get_row_norm_pipeline]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/get_rope_pipeline]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/get_glu_pipeline]] _calls_
- [[nodes/ggml_webgpu_tensor_buf]] _calls_

## Used By

- [[nodes/ggml_webgpu_upscale]] _calls_
