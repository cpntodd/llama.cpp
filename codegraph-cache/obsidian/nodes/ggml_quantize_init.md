---
name: "ggml_quantize_init"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_quantize_init

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_critical_section_start]] _calls_
- [[nodes/iq2xs_init_impl]] _calls_
- [[nodes/iq3xs_init_impl]] _calls_
- [[nodes/ggml_critical_section_end]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/test_vec_dot_q]] _calls_
- [[nodes/main]] _calls_
- [[nodes/ggml_quantize_requires_imatrix]] _calls_
- [[nodes/quantize_row_iq2_xxs_impl]] _calls_
- [[nodes/quantize_row_iq2_xs_impl]] _calls_
- [[nodes/iq3xs_free_impl]] _calls_
- [[nodes/quantize_row_iq3_xxs_ref]] _calls_
- [[nodes/iq1_sort_helper]] _calls_
- [[nodes/quantize_iq1_s]] _calls_
- [[nodes/quantize_row_iq2_s_impl]] _calls_
