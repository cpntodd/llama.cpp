---
name: "ggml_metal_op_flash_attn_ext_extra_pad"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_flash_attn_ext_extra_pad

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_metal_op_flash_attn_ext_use_kv_f16]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_v_is_view_of_k]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_use_vec]] _calls_
- [[nodes/ggml_type_size]] _calls_

## Used By

- [[nodes/ggml_backend_metal_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext]] _calls_
