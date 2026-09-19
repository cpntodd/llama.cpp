---
name: "matmul_tiled"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# matmul_tiled

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/packNormal]] _calls_
- [[nodes/KERNEL]] _calls_
- [[nodes/gemm]] _calls_

## Used By

- [[nodes/BLOC_POS]] _calls_
- [[nodes/KERNEL_Q0]] _calls_
- [[nodes/KERNEL_4x4]] _calls_
