---
name: "KERNEL"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# KERNEL

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/MMA_16x8]] _calls_
- [[nodes/save_acc]] _calls_
- [[nodes/add_save_acc]] _calls_

## Used By

- [[nodes/matmul_tiled]] _calls_
- [[nodes/KERNEL_4x4]] _calls_
