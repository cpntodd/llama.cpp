---
name: "quantize_row_f32_q8_1_flat"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-mm-kernels-flat.h"
community: "ggml"
---

# quantize_row_f32_q8_1_flat

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-mm-kernels-flat.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_round_up]] _calls_
- [[nodes/hvx_splat_f32_a]] _calls_
- [[nodes/hex_l2fetch]] _calls_
- [[nodes/hvx_copy_f32_aa]] _calls_
- [[nodes/quantize_row_f32_q8_0_flat]] _calls_
- [[nodes/hvx_copy_f32_au]] _calls_
- [[nodes/hvx_copy_f16_f32_au]] _calls_
- [[nodes/hvx_copy_f16_au]] _calls_
