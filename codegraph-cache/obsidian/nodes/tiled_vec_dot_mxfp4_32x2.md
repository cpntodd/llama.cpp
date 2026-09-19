---
name: "tiled_vec_dot_mxfp4_32x2"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-mm-kernels-tiled.h"
community: "ggml"
---

# tiled_vec_dot_mxfp4_32x2

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-mm-kernels-tiled.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_f16_to_f32_shuff]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_add_f32_f32]] _calls_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_store_u]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/hvx_splat_f32_a]] _calls_
- [[nodes/hex_l2fetch]] _calls_
- [[nodes/hvx_copy_f32_aa]] _calls_
- [[nodes/quantize_row_f32_q8_0_tiled]] _calls_
- [[nodes/quantize_row_f32_q8_1_tiled]] _calls_
- [[nodes/quantize_block_f32_q8_0_tiled]] _calls_
- [[nodes/quantize_block_f32_q8_1_tiled]] _calls_
