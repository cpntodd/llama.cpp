---
name: "mul_sum_us8_pairs_float"
type: "function"
file: "ggml/src/ggml-cpu/arch/x86/quants.c"
community: "ggml"
---

# mul_sum_us8_pairs_float

**Type:** `function`  **File:** `ggml/src/ggml-cpu/arch/x86/quants.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/sum_i16_pairs_float]] _calls_

## Used By

- [[nodes/mul_sum_i8_pairs_float]] _calls_
- [[nodes/mul_add_epi8_sse]] _calls_
- [[nodes/ggml_vec_dot_q4_1_q8_1]] _calls_
- [[nodes/ggml_vec_dot_q5_1_q8_1]] _calls_
