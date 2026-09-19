---
name: "apir_backend_graph_compute"
type: "function"
file: "ggml/src/ggml-virtgpu/virtgpu-forward-backend.cpp"
community: "ggml"
---

# apir_backend_graph_compute

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/virtgpu-forward-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/apir_serialize_ggml_cgraph]] _calls_
- [[nodes/apir_encode_virtgpu_shmem_res_id]] _calls_
- [[nodes/apir_encode_size_t]] _calls_
- [[nodes/apir_new_encoder]] _calls_
- [[nodes/apir_encode_cgraph_data]] _calls_
- [[nodes/apir_decode_ggml_status]] _calls_
- [[nodes/remote_call_finish]] _calls_
- [[nodes/virtgpu_shmem_destroy]] _calls_

## Used By

- [[nodes/ggml_backend_remoting_graph_compute]] _calls_
