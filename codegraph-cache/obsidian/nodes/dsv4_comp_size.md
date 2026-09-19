---
name: "dsv4_comp_size"
type: "function"
file: "src/llama-kv-cache-dsv4.cpp"
community: "src"
---

# dsv4_comp_size

**Type:** `function`  **File:** `src/llama-kv-cache-dsv4.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/ggml_backend_buft_alloc_buffer]] _imports_
- [[nodes/no_init]] _imports_
- [[nodes/llama_ubatch]] _imports_
- [[nodes/llama-io.cpp]] _imports_
- [[nodes/llama_meta_device_get_split_state]] _imports_
- [[nodes/map]] _imports_

## Used By

- [[nodes/dsv4_make_k_only]] _calls_
- [[nodes/llama_meta_device_get_split_state]] _imports_
- [[nodes/print_mask]] _imports_
- [[nodes/dsv4_rope_attn_factor]] _imports_
