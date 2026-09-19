---
name: "ggml_backend_webgpu_device_supports_op"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_backend_webgpu_device_supports_op

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_webgpu_supported_qtype]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_webgpu_flash_attn_float_vec4_aligned]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_webgpu_flash_attn_k_direct]] _calls_
- [[nodes/ggml_webgpu_flash_attn_v_direct]] _calls_
- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_is_contiguous_channels]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_op_name]] _calls_
- [[nodes/ggml_type_name]] _calls_
