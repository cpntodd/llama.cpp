---
name: "print_mask"
type: "function"
file: "src/llama-graph.cpp"
community: "src"
---

# print_mask

**Type:** `function`  **File:** `src/llama-graph.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/no_init]] _imports_
- [[nodes/llama_meta_device_get_split_state]] _imports_
- [[nodes/llama_ubatch]] _imports_
- [[nodes/llama_cparams]] _imports_
- [[nodes/ring_buffer]] _imports_
- [[nodes/llama_cparams]] _imports_
- [[nodes/llama-kv-cache-iswa.h]] _imports_
- [[nodes/llama-kv-cache-dsa.h]] _imports_
- [[nodes/unified]] _imports_
- [[nodes/llama-kv-cache-msa.cpp]] _imports_
- [[nodes/dsv4_comp_size]] _imports_
- [[nodes/status]] _imports_
- [[nodes/status]] _imports_
- [[nodes/hparams]] _imports_
- [[nodes/jinja]] _imports_
- [[nodes/decltype]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/get_base]] _calls_

## Used By

- [[nodes/llama_model]] _imports_
- [[nodes/llama_ubatch]] _imports_
- [[nodes/llama_cparams]] _imports_
- [[nodes/llama_cparams]] _imports_
- [[nodes/ctx_type_to_graph_type]] _imports_
- [[nodes/llm_build_mamba_base]] _imports_
