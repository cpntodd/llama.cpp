---
name: "ggml_metal_op_flash_attn_ext_extra_kv_f16"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_flash_attn_ext_extra_kv_f16

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_metal_op_flash_attn_ext_use_kv_f16]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_kv_f16_k_size]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_v_is_view_of_k]] _calls_

## Used By

- [[nodes/ggml_backend_metal_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext]] _calls_
