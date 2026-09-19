---
name: "rvv_softmax_exp_inplace_f32"
type: "function"
file: "ggml/src/ggml-cpu/spacemit/rvv_kernels.cpp"
community: "ggml"
---

# rvv_softmax_exp_inplace_f32

**Type:** `function`  **File:** `ggml/src/ggml-cpu/spacemit/rvv_kernels.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/rvv_expf_approx_f32m2]] _calls_
- [[nodes/reduce_sum_f32m2_vlen1024]] _calls_

## Used By

- [[nodes/constexpr]] _calls_
- [[nodes/memcpy2d]] _calls_
