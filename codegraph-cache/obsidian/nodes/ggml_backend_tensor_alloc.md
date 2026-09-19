---
name: "ggml_backend_tensor_alloc"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_tensor_alloc

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_buffer_is_meta]] _calls_
- [[nodes/ggml_backend_buffer_get_alloc_size]] _calls_
- [[nodes/ggml_backend_buffer_get_size]] _calls_
- [[nodes/ggml_backend_buffer_init_tensor]] _calls_
- [[nodes/ggml_hash_insert]] _calls_
- [[nodes/ggml_hash_find]] _calls_
- [[nodes/ggml_set_name]] _calls_

## Used By

- [[nodes/select_weight_buft]] _calls_
- [[nodes/ggml_tallocr_alloc]] _calls_
- [[nodes/ggml_vbuffer_tensor_alloc]] _calls_
