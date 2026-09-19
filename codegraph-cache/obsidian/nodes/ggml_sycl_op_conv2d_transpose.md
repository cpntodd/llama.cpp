---
name: "ggml_sycl_op_conv2d_transpose"
type: "function"
file: "ggml/src/ggml-sycl/conv2d-transpose.cpp"
community: "ggml"
---

# ggml_sycl_op_conv2d_transpose

**Type:** `function`  **File:** `ggml/src/ggml-sycl/conv2d-transpose.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/conv2d-transpose.hpp]] _imports_
- [[nodes/dequantize_row_q4_K_sycl_reorder]] _imports_
- [[nodes/ggml_is_contiguous]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
