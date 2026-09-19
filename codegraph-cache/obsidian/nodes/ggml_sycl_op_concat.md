---
name: "ggml_sycl_op_concat"
type: "function"
file: "ggml/src/ggml-sycl/concat.cpp"
community: "ggml"
---

# ggml_sycl_op_concat

**Type:** `function`  **File:** `ggml/src/ggml-sycl/concat.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/concat_impl_q4_0_sycl]] _calls_
- [[nodes/concat_impl_q4_1_sycl]] _calls_
- [[nodes/concat_impl_q5_0_sycl]] _calls_
- [[nodes/concat_impl_q5_1_sycl]] _calls_
- [[nodes/concat_impl_q8_0_sycl]] _calls_
- [[nodes/ggml_type_name]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
- [[nodes/check_graph_compatibility]] _calls_
