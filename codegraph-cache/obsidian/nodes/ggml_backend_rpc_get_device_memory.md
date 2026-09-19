---
name: "ggml_backend_rpc_get_device_memory"
type: "function"
file: "ggml/src/ggml-rpc/ggml-rpc.cpp"
community: "ggml"
---

# ggml_backend_rpc_get_device_memory

**Type:** `function`  **File:** `ggml/src/ggml-rpc/ggml-rpc.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_device_memory]] _calls_
- [[nodes/rpc_server]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_backend_get_default_buffer_type]] _calls_
- [[nodes/ggml_backend_buft_get_alloc_size]] _calls_
- [[nodes/ggml_backend_buft_alloc_buffer]] _calls_
- [[nodes/get_alignment]] _calls_
- [[nodes/ggml_backend_buft_get_alignment]] _calls_
- [[nodes/get_max_size]] _calls_
- [[nodes/ggml_backend_buft_get_max_size]] _calls_
- [[nodes/ggml_backend_buffer_free]] _calls_
- [[nodes/ggml_backend_buffer_clear]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_buffer_get_size]] _calls_
- [[nodes/ggml_backend_tensor_memset]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/fnv_hash]] _calls_
- [[nodes/string]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/copy_tensor]] _calls_
- [[nodes/ggml_backend_buffer_copy_tensor]] _calls_
- [[nodes/graph_compute]] _calls_
- [[nodes/device]] _calls_
- [[nodes/n_nodes]] _calls_
- [[nodes/tensors]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_

## Used By

- [[nodes/ggml_backend_rpc_device_get_memory]] _calls_
