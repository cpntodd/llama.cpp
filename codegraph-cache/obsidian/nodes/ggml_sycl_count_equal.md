---
name: "ggml_sycl_count_equal"
type: "function"
file: "ggml/src/ggml-sycl/count-equal.cpp"
community: "ggml"
---

# ggml_sycl_count_equal

**Type:** `function`  **File:** `ggml/src/ggml-sycl/count-equal.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/get_current_device_id]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/min]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
