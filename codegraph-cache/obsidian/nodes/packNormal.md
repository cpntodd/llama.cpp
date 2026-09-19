---
name: "packNormal"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# packNormal

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/vector_permute_store]] _calls_
- [[nodes/mnpack]] _calls_

## Used By

- [[nodes/KERNEL_4x8]] _calls_
- [[nodes/KERNEL_8x4]] _calls_
- [[nodes/KERNEL_8x8]] _calls_
- [[nodes/gemm_small]] _calls_
- [[nodes/gemm_Mx8]] _calls_
- [[nodes/matmul_tiled]] _calls_
- [[nodes/packNormalInt4]] _calls_
