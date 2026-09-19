---
name: "mmap"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# mmap

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fastrpc_mmap]] _calls_

## Used By

- [[nodes/pimpl]] _calls_
- [[nodes/llama_prepare_model_devices]] _calls_
- [[nodes/DataType]] _imports_
- [[nodes/align_up_uintptr]] _calls_
- [[nodes/virtgpu_ioctl_gem_close]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl]] _calls_
- [[nodes/get_device_backend_and_type]] _calls_
- [[nodes/alloc]] _calls_
