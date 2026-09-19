---
name: "ggml_sycl_op_acc"
type: "function"
file: "ggml/src/ggml-sycl/element_wise.cpp"
community: "ggml"
---

# ggml_sycl_op_acc

**Type:** `function`  **File:** `ggml/src/ggml-sycl/element_wise.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/stream]] _calls_
- [[nodes/ggml_element_size]] _calls_
- [[nodes/ggml_is_contiguously_allocated]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_nelements]] _calls_

## Used By

- [[nodes/ggml_sycl_acc]] _calls_
