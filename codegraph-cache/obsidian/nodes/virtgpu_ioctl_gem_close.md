---
name: "virtgpu_ioctl_gem_close"
type: "function"
file: "ggml/src/ggml-virtgpu/virtgpu-shm.cpp"
community: "ggml"
---

# virtgpu_ioctl_gem_close

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/virtgpu-shm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/virtgpu_handshake]] _imports_
- [[nodes/ggml_backend_remoting_device_context]] _imports_
- [[nodes/virtgpu_ioctl]] _calls_
- [[nodes/mmap]] _calls_

## Used By

- [[nodes/virtgpu_shmem_destroy]] _calls_
- [[nodes/virtgpu_shmem_create]] _calls_
- [[nodes/apir_device_get_count]] _imports_
- [[nodes/apir_buffer_context_t]] _imports_
- [[nodes/virt_gpu_result_t]] _imports_
