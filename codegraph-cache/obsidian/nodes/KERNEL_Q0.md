---
name: "KERNEL_Q0"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# KERNEL_Q0

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/save_acc]] _calls_
- [[nodes/add_save_acc]] _calls_
- [[nodes/matmul_tiled]] _calls_
- [[nodes/constexpr]] _calls_
- [[nodes/packNormal_q4_fp16]] _calls_
- [[nodes/packNormal_q8_fp16]] _calls_
- [[nodes/gemm_small]] _calls_
- [[nodes/unhalf]] _calls_
- [[nodes/save_res]] _calls_
- [[nodes/kernel]] _calls_
- [[nodes/KERNEL_4x8]] _calls_
- [[nodes/KERNEL_8x4]] _calls_
- [[nodes/KERNEL_8x8]] _calls_
- [[nodes/gemm]] _calls_
