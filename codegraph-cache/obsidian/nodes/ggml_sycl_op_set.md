---
name: "ggml_sycl_op_set"
type: "function"
file: "ggml/src/ggml-sycl/set.cpp"
community: "ggml"
---

# ggml_sycl_op_set

**Type:** `function`  **File:** `ggml/src/ggml-sycl/set.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/stream]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
