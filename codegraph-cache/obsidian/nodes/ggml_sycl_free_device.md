---
name: "ggml_sycl_free_device"
type: "function"
file: "ggml/src/ggml-sycl/common.cpp"
community: "ggml"
---

# ggml_sycl_free_device

**Type:** `function`  **File:** `ggml/src/ggml-sycl/common.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_use_level_zero_device_alloc]] _calls_

## Used By

- [[nodes/release_extra_gpu]] _calls_
- [[nodes/ggml_sycl_get_device]] _calls_
- [[nodes/free_aligned_mem_host]] _calls_
- [[nodes/ggml_backend_sycl_host_buffer_type]] _calls_
- [[nodes/format_slots_in_alloc_order]] _calls_
- [[nodes/sycl_ext_free]] _calls_
