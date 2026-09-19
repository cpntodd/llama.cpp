---
name: "virtgpu_shmem_create"
type: "function"
file: "ggml/src/ggml-virtgpu/virtgpu-shm.cpp"
community: "ggml"
---

# virtgpu_shmem_create

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/virtgpu-shm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/align64]] _calls_
- [[nodes/virtgpu_ioctl_gem_close]] _calls_

## Used By

- [[nodes/if]] _calls_
- [[nodes/apir_device_buffer_from_ptr]] _calls_
- [[nodes/if]] _calls_
- [[nodes/virtgpu_load_library]] _calls_
