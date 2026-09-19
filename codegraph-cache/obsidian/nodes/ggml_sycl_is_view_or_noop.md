---
name: "ggml_sycl_is_view_or_noop"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# ggml_sycl_is_view_or_noop

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_empty]] _calls_
- [[nodes/skip]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_row_size]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_type_size]] _calls_

## Used By

- [[nodes/ggml_backend_sycl_graph_compute_impl]] _calls_
