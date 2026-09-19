---
name: "rvv_max_f32"
type: "function"
file: "ggml/src/ggml-cpu/spacemit/rvv_kernels.cpp"
community: "ggml"
---

# rvv_max_f32

**Type:** `function`  **File:** `ggml/src/ggml-cpu/spacemit/rvv_kernels.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/flash_attn_ext_supported_shape_vlen1024_vf16]] _calls_
- [[nodes/align_up]] _calls_
- [[nodes/reduce_sum_f32m4_vlen1024]] _calls_

## Used By

- [[nodes/memcpy2d]] _calls_
