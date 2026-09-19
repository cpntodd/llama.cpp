---
name: "mul_sum_i8_pairs"
type: "function"
file: "ggml/src/ggml-cpu/arch/x86/quants.c"
community: "ggml"
---

# mul_sum_i8_pairs

**Type:** `function`  **File:** `ggml/src/ggml-cpu/arch/x86/quants.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml-common.h]] _imports_
- [[nodes/ggml-quants.h]] _imports_
- [[nodes/ggml_up32]] _imports_
- [[nodes/ggml_arm_arch_features_type]] _imports_
- [[nodes/ggml_lookup_fp16_to_fp32]] _imports_
- [[nodes/quant_shape_to_byte_shape]] _imports_
- [[nodes/ggml_compute_params]] _imports_
- [[nodes/jinja]] _imports_

## Used By

- [[nodes/ggml_vec_dot_q4_0_q8_0]] _calls_
- [[nodes/ggml_vec_dot_nvfp4_q8_0]] _calls_
