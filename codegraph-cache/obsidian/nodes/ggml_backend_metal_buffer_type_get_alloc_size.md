---
name: "ggml_backend_metal_buffer_type_get_alloc_size"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal.cpp"
community: "ggml"
---

# ggml_backend_metal_buffer_type_get_alloc_size

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_metal_op_mul_mat_extra_q1_0_planes]] _calls_
- [[nodes/ggml_metal_op_mul_mat_id_extra_tpe]] _calls_
- [[nodes/ggml_metal_op_mul_mat_id_extra_ids]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_extra_pad]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_extra_blk]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_extra_tmp]] _calls_
- [[nodes/ggml_metal_op_flash_attn_ext_extra_kv_f16]] _calls_
- [[nodes/ggml_nelements]] _calls_

## Used By

- [[nodes/ggml_backend_metal_buffer_type_shared_get_alloc_size]] _calls_
- [[nodes/ggml_backend_metal_buffer_type_private_get_alloc_size]] _calls_
- [[nodes/ggml_backend_metal_buffer_type_mapped_get_alloc_size]] _calls_
