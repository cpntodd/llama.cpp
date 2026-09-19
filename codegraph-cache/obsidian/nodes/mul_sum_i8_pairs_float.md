---
name: "mul_sum_i8_pairs_float"
type: "function"
file: "ggml/src/ggml-cpu/arch/x86/quants.c"
community: "ggml"
---

# mul_sum_i8_pairs_float

**Type:** `function`  **File:** `ggml/src/ggml-cpu/arch/x86/quants.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/mul_sum_us8_pairs_float]] _calls_
- [[nodes/packNibbles]] _calls_

## Used By

- [[nodes/mul_add_epi8_sse]] _calls_
- [[nodes/ggml_vec_dot_q4_0_q8_0]] _calls_
- [[nodes/ggml_vec_dot_q5_0_q8_0]] _calls_
- [[nodes/ggml_vec_dot_q8_0_q8_0]] _calls_
