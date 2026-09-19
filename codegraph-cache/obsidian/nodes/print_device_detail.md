---
name: "print_device_detail"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# print_device_detail

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_device_info]] _calls_
- [[nodes/get_major_version]] _calls_
- [[nodes/get_minor_version]] _calls_
- [[nodes/get_global_mem_size]] _calls_
- [[nodes/get_max_compute_units]] _calls_
- [[nodes/get_max_work_group_size]] _calls_
- [[nodes/get_max_sub_group_size]] _calls_

## Used By

- [[nodes/ggml_backend_sycl_print_sycl_devices]] _calls_
