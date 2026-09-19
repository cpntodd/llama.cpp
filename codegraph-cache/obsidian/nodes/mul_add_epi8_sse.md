---
name: "mul_add_epi8_sse"
type: "function"
file: "ggml/src/ggml-cpu/arch/x86/quants.c"
community: "ggml"
---

# mul_add_epi8_sse

**Type:** `function`  **File:** `ggml/src/ggml-cpu/arch/x86/quants.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/bytes_from_bits_32]] _calls_
- [[nodes/bytes_from_nibbles_32]] _calls_
- [[nodes/sum_i16_pairs_float]] _calls_
- [[nodes/mul_sum_us8_pairs_float]] _calls_
- [[nodes/mul_sum_i8_pairs_float]] _calls_

## Used By

- [[nodes/ggml_vec_dot_q4_0_q8_0]] _calls_
- [[nodes/ggml_vec_dot_iq1_s_q8_K]] _calls_
- [[nodes/ggml_vec_dot_iq1_m_q8_K]] _calls_
- [[nodes/ggml_vec_dot_iq4_xs_q8_K]] _calls_
