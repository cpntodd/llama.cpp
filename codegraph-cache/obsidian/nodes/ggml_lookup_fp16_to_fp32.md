---
name: "ggml_lookup_fp16_to_fp32"
type: "function"
file: "ggml/src/ggml-cpu/simd-mappings.h"
community: "ggml"
---

# ggml_lookup_fp16_to_fp32

**Type:** `function`  **File:** `ggml/src/ggml-cpu/simd-mappings.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_compute_params]] _imports_
- [[nodes/vaddvq_f32]] _calls_

## Used By

- [[nodes/quantize_row_q1_0]] _imports_
- [[nodes/nearest_int]] _imports_
- [[nodes/f32_to_f16]] _imports_
- [[nodes/ggml_sve_sum_f32x2]] _imports_
- [[nodes/kernel_offs_fn3]] _imports_
- [[nodes/unhalf]] _imports_
- [[nodes/Unroll]] _imports_
- [[nodes/quantize_row_q8_0]] _imports_
- [[nodes/decode_q_Kx8_6bit_scales]] _imports_
- [[nodes/quantize_row_q8_0]] _imports_
- [[nodes/lsx_packs_w]] _imports_
- [[nodes/mul_sum_i8_pairs]] _imports_
- [[nodes/quantize_row_q8_0]] _imports_
- [[nodes/quantize_row_q8_0]] _imports_
- [[nodes/quantize_row_q8_0]] _imports_
- [[nodes/ggml_quantize_mat_q8_0_4x8]] _imports_
