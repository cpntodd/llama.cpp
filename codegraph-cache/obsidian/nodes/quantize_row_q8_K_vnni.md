---
name: "quantize_row_q8_K_vnni"
type: "function"
file: "ggml/src/ggml-cpu/amx/mmq.cpp"
community: "ggml"
---

# quantize_row_q8_K_vnni

**Type:** `function`  **File:** `ggml/src/ggml-cpu/amx/mmq.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/transpose_16x4_32bit]] _calls_
- [[nodes/quantize_row_q8_K_ref]] _calls_
