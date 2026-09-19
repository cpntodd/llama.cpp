---
name: "KERNEL_8x4"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# KERNEL_8x4

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/packNormal]] _calls_
- [[nodes/outer_product]] _calls_
- [[nodes/save_acc]] _calls_

## Used By

- [[nodes/kernel]] _calls_
- [[nodes/packNormalInt4]] _calls_
- [[nodes/KERNEL_Q0]] _calls_
- [[nodes/KERNEL_4x4]] _calls_
