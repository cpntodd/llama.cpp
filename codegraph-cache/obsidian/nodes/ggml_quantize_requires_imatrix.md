---
name: "ggml_quantize_requires_imatrix"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_quantize_requires_imatrix

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_quantize_init]] _calls_
- [[nodes/ggml_row_size]] _calls_
- [[nodes/quantize_q1_0]] _calls_
- [[nodes/quantize_q2_0]] _calls_
- [[nodes/quantize_pq2_0]] _calls_
- [[nodes/quantize_ptq1_0]] _calls_
- [[nodes/quantize_q4_0]] _calls_
- [[nodes/quantize_q4_1]] _calls_
- [[nodes/quantize_q5_0]] _calls_
- [[nodes/quantize_q5_1]] _calls_
- [[nodes/quantize_q8_0]] _calls_
- [[nodes/quantize_mxfp4]] _calls_
- [[nodes/quantize_nvfp4]] _calls_
- [[nodes/quantize_q2_K]] _calls_
- [[nodes/quantize_q3_K]] _calls_
- [[nodes/quantize_q4_K]] _calls_
- [[nodes/quantize_q5_K]] _calls_
- [[nodes/quantize_q6_K]] _calls_
- [[nodes/quantize_tq1_0]] _calls_
- [[nodes/quantize_tq2_0]] _calls_
- [[nodes/quantize_iq2_xxs]] _calls_
- [[nodes/quantize_iq2_xs]] _calls_
- [[nodes/quantize_iq3_xxs]] _calls_
- [[nodes/quantize_iq3_s]] _calls_
- [[nodes/quantize_iq2_s]] _calls_
- [[nodes/quantize_iq1_s]] _calls_
- [[nodes/quantize_iq1_m]] _calls_
- [[nodes/quantize_iq4_nl]] _calls_
- [[nodes/quantize_iq4_xs]] _calls_
- [[nodes/ggml_fp32_to_fp16_row]] _calls_

## Used By

- [[nodes/fa_init_uniform]] _calls_
- [[nodes/if]] _calls_
