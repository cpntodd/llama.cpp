---
name: "ggml_backend_buffer_is_sycl"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_backend_buffer_is_sycl

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/exit]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_buft_get_alloc_size]] _calls_
- [[nodes/queues_wait_and_throw]] _calls_
- [[nodes/mmap]] _calls_

## Used By

- [[nodes/ggml_sycl_is_l0_discrete_gpu]] _calls_
- [[nodes/next_power_of_2]] _calls_
- [[nodes/ggml_backend_sycl_free]] _calls_
