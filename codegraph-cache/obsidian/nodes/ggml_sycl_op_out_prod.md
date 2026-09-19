---
name: "ggml_sycl_op_out_prod"
type: "function"
file: "ggml/src/ggml-sycl/outprod.cpp"
community: "ggml"
---

# ggml_sycl_op_out_prod

**Type:** `function`  **File:** `ggml/src/ggml-sycl/outprod.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/outprod.hpp]] _imports_
- [[nodes/dequantize_row_q4_K_sycl_reorder]] _imports_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/alloc]] _calls_
- [[nodes/ggml_get_to_fp32_sycl]] _calls_
- [[nodes/ggml_is_transposed]] _calls_
- [[nodes/each]] _calls_
- [[nodes/gemm]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
