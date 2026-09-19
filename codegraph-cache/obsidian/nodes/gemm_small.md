---
name: "gemm_small"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# gemm_small

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/packNormal]] _calls_
- [[nodes/outer_product]] _calls_

## Used By

- [[nodes/packNormalInt4]] _calls_
- [[nodes/KERNEL_Q0]] _calls_
- [[nodes/KERNEL_4x4]] _calls_
