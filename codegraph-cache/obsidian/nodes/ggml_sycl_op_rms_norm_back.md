---
name: "ggml_sycl_op_rms_norm_back"
type: "function"
file: "ggml/src/ggml-sycl/norm.cpp"
community: "ggml"
---

# ggml_sycl_op_rms_norm_back

**Type:** `function`  **File:** `ggml/src/ggml-sycl/norm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nrows]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/stream]] _calls_
- [[nodes/min]] _calls_
- [[nodes/max]] _calls_
- [[nodes/parallel_for]] _calls_
- [[nodes/warp_reduce_sum]] _calls_
- [[nodes/x]] _calls_

## Used By

- [[nodes/ggml_sycl_rms_norm_back]] _calls_
