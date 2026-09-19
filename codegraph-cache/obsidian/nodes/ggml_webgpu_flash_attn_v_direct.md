---
name: "ggml_webgpu_flash_attn_v_direct"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu-shader-lib.hpp"
community: "ggml"
---

# ggml_webgpu_flash_attn_v_direct

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu-shader-lib.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_webgpu_flash_attn_k_direct]] _calls_
- [[nodes/ggml_get_op_params_f32]] _calls_
- [[nodes/string]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/operator]] _calls_
- [[nodes/ggml_webgpu_hash_combine]] _calls_
- [[nodes/ggml_webgpu_shader_lib]] _calls_

## Used By

- [[nodes/ggml_backend_webgpu_buffer_type_get_max_size]] _calls_
- [[nodes/ggml_backend_webgpu_device_supports_op]] _calls_
