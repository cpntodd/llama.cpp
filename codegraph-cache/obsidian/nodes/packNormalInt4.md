---
name: "packNormalInt4"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# packNormalInt4

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/process_q4_elements]] _calls_
- [[nodes/packNormal]] _calls_
- [[nodes/mnpack]] _calls_
- [[nodes/gemm_small]] _calls_
- [[nodes/KERNEL_4x8]] _calls_
- [[nodes/unhalf]] _calls_
- [[nodes/compute]] _calls_
- [[nodes/save_res]] _calls_
- [[nodes/KERNEL_8x4]] _calls_
- [[nodes/KERNEL_8x8]] _calls_
