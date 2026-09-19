---
name: "packNormal_q4_fp16"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# packNormal_q4_fp16

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/unpack_q4_to_q8]] _calls_
- [[nodes/convert_and_scale_q8]] _calls_
- [[nodes/vector_permute_store_fp16]] _calls_

## Used By

- [[nodes/KERNEL_Q0]] _calls_
