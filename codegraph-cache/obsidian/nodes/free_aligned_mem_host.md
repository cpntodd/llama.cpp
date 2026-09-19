---
name: "free_aligned_mem_host"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# free_aligned_mem_host

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_sycl_buffer_context]] _calls_
- [[nodes/device]] _calls_
- [[nodes/check_allow_gpu_index]] _calls_
- [[nodes/ggml_sycl_free_device]] _calls_
- [[nodes/release_extra_gpu]] _calls_

## Used By

- [[nodes/ggml_backend_sycl_host_buffer_free_buffer]] _calls_
