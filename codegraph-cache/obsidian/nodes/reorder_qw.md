---
name: "reorder_qw"
type: "function"
file: "ggml/src/ggml-sycl/ggml-sycl.cpp"
community: "ggml"
---

# reorder_qw

**Type:** `function`  **File:** `ggml/src/ggml-sycl/ggml-sycl.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/reorder_qw_q4_k_moe]] _calls_
- [[nodes/reorder_qw_q5_k_moe]] _calls_
- [[nodes/reorder_qw_q6_k_moe]] _calls_
- [[nodes/reorder_qw_q2_k]] _calls_
- [[nodes/reorder_qw_q3_k]] _calls_
- [[nodes/reorder_qw_q4_k]] _calls_
- [[nodes/reorder_qw_q5_k]] _calls_
- [[nodes/reorder_qw_q6_k]] _calls_

## Used By

- [[nodes/should_reorder_tensor]] _calls_
- [[nodes/opt_for_reorder_id]] _calls_
