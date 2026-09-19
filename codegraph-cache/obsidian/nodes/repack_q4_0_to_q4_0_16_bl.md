---
name: "repack_q4_0_to_q4_0_16_bl"
type: "function"
file: "ggml/src/ggml-cpu/repack.cpp"
community: "ggml"
---

# repack_q4_0_to_q4_0_16_bl

**Type:** `function`  **File:** `ggml/src/ggml-cpu/repack.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nrows]] _calls_
- [[nodes/make_block_q5_Kx8]] _calls_

## Used By

- [[nodes/repack_mxfp4_to_mxfp4_8_bl]] _calls_
- [[nodes/make_block_q4_1x16]] _calls_
- [[nodes/convert_mxfp4_to_5bit]] _calls_
