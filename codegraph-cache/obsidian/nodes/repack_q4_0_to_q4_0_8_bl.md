---
name: "repack_q4_0_to_q4_0_8_bl"
type: "function"
file: "ggml/src/ggml-cpu/repack.cpp"
community: "ggml"
---

# repack_q4_0_to_q4_0_8_bl

**Type:** `function`  **File:** `ggml/src/ggml-cpu/repack.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nrows]] _calls_
- [[nodes/make_block_q4_0x8]] _calls_
- [[nodes/make_block_q8_0x4]] _calls_
- [[nodes/make_block_q1_0x4]] _calls_
- [[nodes/make_block_pq2_0x4]] _calls_

## Used By

- [[nodes/repack_mxfp4_to_mxfp4_8_bl]] _calls_
