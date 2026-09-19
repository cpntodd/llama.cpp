---
name: "apir_device_get_count"
type: "function"
file: "ggml/src/ggml-virtgpu/virtgpu-forward-device.cpp"
community: "ggml"
---

# apir_device_get_count

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/virtgpu-forward-device.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/virtgpu-forward-impl.h]] _imports_
- [[nodes/virtgpu_ioctl_gem_close]] _imports_
- [[nodes/apir_decode_int32_t]] _calls_
- [[nodes/remote_call_finish]] _calls_
- [[nodes/apir_decode_array_size_unchecked]] _calls_
- [[nodes/apir_decoder_alloc_array]] _calls_
- [[nodes/apir_decode_char_array]] _calls_
