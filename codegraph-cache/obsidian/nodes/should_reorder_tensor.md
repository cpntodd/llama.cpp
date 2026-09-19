---
name: "should_reorder_tensor"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# should_reorder_tensor

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_sycl_supports_reorder_dmmv]] _calls_
- [[nodes/ggml_sycl_supports_reorder_mmvq]] _calls_
- [[nodes/ggml_sycl_supports_reorder_mul_mat_sycl]] _calls_
- [[nodes/reorder_qw]] _calls_

## Used By

- [[nodes/ggml_sycl_mul_mat]] _calls_
