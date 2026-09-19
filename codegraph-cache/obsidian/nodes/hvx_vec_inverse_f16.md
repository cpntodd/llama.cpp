---
name: "hvx_vec_inverse_f16"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-inverse.h"
community: "ggml"
---

# hvx_vec_inverse_f16

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-inverse.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_recip_xp1_O3_unsigned]] _calls_

## Used By

- [[nodes/quantize_block_f32_q8_1_tiled]] _calls_
- [[nodes/quantize_block_f32_q8_0_tiled]] _calls_
- [[nodes/hvx_vec_fast_sigmoid_f16]] _calls_
- [[nodes/hvx_vec_inverse_f16_guard]] _calls_
