---
name: "apir_device_buffer_from_ptr"
type: "function"
file: "ggml/src/ggml-virtgpu/virtgpu-forward-device.cpp"
community: "ggml"
---

# apir_device_buffer_from_ptr

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/virtgpu-forward-device.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/virtgpu_shmem_create]] _calls_
- [[nodes/apir_encode_virtgpu_shmem_res_id]] _calls_
- [[nodes/apir_encode_size_t]] _calls_
- [[nodes/apir_decode_apir_buffer_host_handle_t]] _calls_
- [[nodes/apir_decode_apir_buffer_type_host_handle]] _calls_
- [[nodes/remote_call_finish]] _calls_

## Used By

- [[nodes/ggml_backend_remoting_device_get_buffer_from_ptr_type]] _calls_
