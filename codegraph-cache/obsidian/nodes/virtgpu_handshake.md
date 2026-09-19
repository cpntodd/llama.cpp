---
name: "virtgpu_handshake"
type: "function"
file: "ggml/src/ggml-virtgpu/virtgpu.cpp"
community: "ggml"
---

# virtgpu_handshake

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/virtgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_remoting_device_context]] _imports_
- [[nodes/apir_encode_uint32_t]] _calls_
- [[nodes/log_call_duration]] _calls_
- [[nodes/apir_backend_initialize_error]] _calls_
- [[nodes/apir_decode_uint32_t]] _calls_
- [[nodes/remote_call_finish]] _calls_

## Used By

- [[nodes/virtgpu_ioctl_gem_close]] _imports_
- [[nodes/ggml_backend_remoting_device_context]] _imports_
- [[nodes/virtgpu_load_library]] _calls_
