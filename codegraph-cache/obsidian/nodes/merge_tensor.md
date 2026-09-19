---
name: "merge_tensor"
type: "function"
file: "tools/export-lora/export-lora.cpp"
community: "ggml"
---

# merge_tensor

**Type:** `function`  **File:** `tools/export-lora/export-lora.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_ne_string]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_dup_tensor]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors]] _calls_
- [[nodes/read_tensor_data]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_get_type_traits]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_graph_overhead]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/ggml_new_graph]] _calls_
- [[nodes/string_starts_with]] _calls_
- [[nodes/ggml_build_forward_expand]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/ggml_gallocr_alloc_graph]] _calls_
- [[nodes/ggml_backend_cpu_set_n_threads]] _calls_
- [[nodes/ggml_backend_graph_compute]] _calls_
- [[nodes/ggml_graph_node]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/write]] _calls_
- [[nodes/zeros]] _calls_
- [[nodes/ggml_backend_buffer_free]] _calls_
- [[nodes/lora_merge_ctx]] _calls_
- [[nodes/ggml_gallocr_free]] _calls_
- [[nodes/ggml_backend_free]] _calls_
- [[nodes/gguf_free]] _calls_

## Used By

- [[nodes/run_merge]] _calls_
