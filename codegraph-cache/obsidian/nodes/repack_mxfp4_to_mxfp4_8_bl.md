---
name: "repack_mxfp4_to_mxfp4_8_bl"
type: "function"
file: "ggml/src/ggml-cpu/repack.cpp"
community: "ggml"
---

# repack_mxfp4_to_mxfp4_8_bl

**Type:** `function`  **File:** `ggml/src/ggml-cpu/repack.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nrows]] _calls_
- [[nodes/make_block_mxfp4x8]] _calls_
- [[nodes/repack]] _calls_
- [[nodes/repack_q4_0_to_q4_0_4_bl]] _calls_
- [[nodes/repack_q4_0_to_q4_0_8_bl]] _calls_
- [[nodes/repack_q4_K_to_q4_K_8_bl]] _calls_
- [[nodes/repack_q2_K_to_q2_K_8_bl]] _calls_
- [[nodes/repack_q6_K_to_q6_K_8_bl]] _calls_
- [[nodes/repack_iq4_nl_to_iq4_nl_4_bl]] _calls_
- [[nodes/repack_iq4_nl_to_iq4_nl_8_bl]] _calls_
- [[nodes/repack_mxfp4_to_mxfp4_4_bl]] _calls_
- [[nodes/repack_q4_0_to_q4_0_16_bl]] _calls_
- [[nodes/repack_q4_K_to_q4_K_16_bl]] _calls_
- [[nodes/repack_iq4_nl_to_iq4_nl_16_bl]] _calls_
- [[nodes/repack_q2_K_to_q2_K_16_bl]] _calls_
- [[nodes/ggml_gemv_q4_0_4x4_q8_0]] _calls_
- [[nodes/ggml_gemv_q4_0_4x8_q8_0]] _calls_
- [[nodes/ggml_gemv_q4_K_8x4_q8_K]] _calls_
- [[nodes/ggml_gemv_iq4_nl_4x4_q8_0]] _calls_
- [[nodes/ggml_gemv_mxfp4_4x4_q8_0]] _calls_
- [[nodes/ggml_gemv_q4_0_16x1_q8_0]] _calls_
- [[nodes/ggml_gemv_q4_K_16x1_q8_K]] _calls_
- [[nodes/ggml_gemv_iq4_nl_16x1_q8_0]] _calls_
- [[nodes/ggml_gemv_q8_0_16x1_q8_0]] _calls_
- [[nodes/ggml_gemv_q2_K_16x1_q8_K]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/ggml_gemm_q4_0_4x4_q8_0]] _calls_
- [[nodes/ggml_gemm_q4_0_4x8_q8_0]] _calls_
- [[nodes/ggml_gemm_q4_K_8x4_q8_K]] _calls_
- [[nodes/ggml_gemm_iq4_nl_4x4_q8_0]] _calls_
