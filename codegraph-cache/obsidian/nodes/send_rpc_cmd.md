---
name: "send_rpc_cmd"
type: "function"
file: "ggml/src/ggml-rpc/ggml-rpc.cpp"
community: "ggml"
---

# send_rpc_cmd

**Type:** `function`  **File:** `ggml/src/ggml-rpc/ggml-rpc.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/rpc_cmd]] _calls_

## Used By

- [[nodes/negotiate_hello]] _calls_
- [[nodes/ggml_backend_rpc_buffer_free_buffer]] _calls_
- [[nodes/ggml_backend_rpc_buffer_init_tensor]] _calls_
- [[nodes/ggml_backend_rpc_buffer_set_tensor]] _calls_
- [[nodes/ggml_backend_rpc_buffer_get_tensor]] _calls_
- [[nodes/ggml_backend_rpc_buffer_cpy_tensor]] _calls_
- [[nodes/ggml_backend_rpc_buffer_clear]] _calls_
- [[nodes/ggml_backend_rpc_buffer_type_alloc_buffer]] _calls_
- [[nodes/get_alignment]] _calls_
- [[nodes/get_max_size]] _calls_
- [[nodes/ggml_backend_rpc_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_backend_rpc_graph_compute]] _calls_
- [[nodes/get_device_memory]] _calls_
- [[nodes/ggml_backend_rpc_get_device_count]] _calls_
