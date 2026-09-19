---
name: "lasx_extracti128"
type: "function"
file: "ggml/src/ggml-cpu/arch/loongarch/quants.c"
community: "ggml"
---

# lasx_extracti128

**Type:** `function`  **File:** `ggml/src/ggml-cpu/arch/loongarch/quants.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/lasx_extracti128_lo]] _calls_
- [[nodes/lasx_extracti128_hi]] _calls_

## Used By

- [[nodes/quantize_row_q8_0]] _calls_
- [[nodes/quantize_row_q8_1]] _calls_
- [[nodes/ggml_vec_dot_q4_K_q8_K]] _calls_
- [[nodes/ggml_vec_dot_q5_K_q8_K]] _calls_
- [[nodes/ggml_vec_dot_iq2_xs_q8_K]] _calls_
- [[nodes/ggml_vec_dot_iq3_s_q8_K]] _calls_
