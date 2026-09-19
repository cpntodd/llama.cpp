---
name: "quantize_block_f32_q8_0_tiled"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-mm-kernels-tiled.h"
community: "ggml"
---

# quantize_block_f32_q8_0_tiled

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-mm-kernels-tiled.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_reduce_max_f16]] _calls_
- [[nodes/hvx_vec_abs_f16]] _calls_
- [[nodes/hvx_vec_reduce_max2_f16]] _calls_
- [[nodes/hvx_vec_inverse_f16]] _calls_
- [[nodes/hvx_vec_i16_from_hf_rnd_sat]] _calls_
- [[nodes/hvx_vec_repl_f16]] _calls_

## Used By

- [[nodes/quantize_row_f32_q8_0_tiled]] _calls_
- [[nodes/tiled_vec_dot_mxfp4_32x2]] _calls_
