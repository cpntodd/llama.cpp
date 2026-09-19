---
name: "remote_call_finish"
type: "function"
file: "ggml/src/ggml-virtgpu/virtgpu.cpp"
community: "ggml"
---

# remote_call_finish

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/virtgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/apir_encoder_get_fatal]] _calls_
- [[nodes/apir_decoder_get_fatal]] _calls_
- [[nodes/start_timer]] _calls_
- [[nodes/atomic_load_explicit]] _calls_
- [[nodes/os_time_sleep]] _calls_
- [[nodes/stop_timer]] _calls_

## Used By

- [[nodes/apir_backend_graph_compute]] _calls_
- [[nodes/apir_buffer_type_get_alignment]] _calls_
- [[nodes/apir_buffer_type_get_max_size]] _calls_
- [[nodes/apir_device_get_count]] _calls_
- [[nodes/apir_device_get_type]] _calls_
- [[nodes/apir_device_get_memory]] _calls_
- [[nodes/apir_device_supports_op]] _calls_
- [[nodes/apir_device_get_buffer_type]] _calls_
- [[nodes/apir_device_buffer_from_ptr]] _calls_
- [[nodes/apir_buffer_clear]] _calls_
- [[nodes/apir_buffer_free_buffer]] _calls_
- [[nodes/virtgpu_handshake]] _calls_
- [[nodes/virtgpu_load_library]] _calls_
- [[nodes/virtgpu_ioctl]] _calls_
