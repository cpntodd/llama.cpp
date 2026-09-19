---
name: "KERNEL_4x4"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# KERNEL_4x4

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/packTranspose]] _calls_
- [[nodes/save_acc]] _calls_
- [[nodes/KERNEL_4x8]] _calls_
- [[nodes/KERNEL_8x4]] _calls_
- [[nodes/KERNEL_8x8]] _calls_
- [[nodes/MMA_16x8]] _calls_
- [[nodes/KERNEL]] _calls_
- [[nodes/add_save_acc]] _calls_
- [[nodes/matmul_tiled]] _calls_
- [[nodes/mnpack]] _calls_
- [[nodes/gemm_small]] _calls_
- [[nodes/kernel]] _calls_
- [[nodes/constexpr]] _calls_
- [[nodes/gemm]] _calls_
