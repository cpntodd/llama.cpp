---
name: "hvx_vec_store_u"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-base.h"
community: "ggml"
---

# hvx_vec_store_u

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-base.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_get_cycles]] _imports_
- [[nodes/hvx-types.h]] _imports_

## Used By

- [[nodes/gdn_mul_dot_f32]] _calls_
- [[nodes/gdn_mul_scalar_dot_f32]] _calls_
- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/hvx_vec_repl]] _imports_
- [[nodes/hvx_vec_exp_f32]] _imports_
- [[nodes/hvx_exp_f32]] _calls_
- [[nodes/hvx_scale_f32_aa]] _imports_
- [[nodes/rope_yarn_ramp]] _calls_
- [[nodes/hvx_rope_neox_f32_aa]] _calls_
- [[nodes/hvx_rope_f32_aa]] _calls_
- [[nodes/OP_NAME]] _imports_
- [[nodes/hmx_init_column_scales]] _imports_
- [[nodes/flat_vec_dot_q4_0_32x1]] _calls_
- [[nodes/flat_vec_dot_q4_0_32x2]] _calls_
- [[nodes/flat_vec_dot_q4_1_32x1]] _calls_
- [[nodes/flat_vec_dot_q4_1_32x2]] _calls_
- [[nodes/flat_vec_dot_q8_0_32x1]] _calls_
- [[nodes/flat_vec_dot_q8_0_32x2]] _calls_
- [[nodes/flat_vec_dot_iq4nl_32x1]] _calls_
- [[nodes/flat_vec_dot_iq4nl_32x2]] _calls_
- [[nodes/flat_vec_dot_mxfp4_32x1]] _calls_
- [[nodes/flat_vec_dot_mxfp4_32x2]] _calls_
- [[nodes/vec_dot_f32_f32_aa_1x1]] _calls_
- [[nodes/vec_dot_f32_f32_uu_1x1]] _calls_
- [[nodes/vec_dot_f16_f16_aa_1x1]] _calls_
- [[nodes/vec_dot_f16_f16_uu_1x1]] _calls_
- [[nodes/vec_dot_f16_f32_uu_1x1]] _calls_
- [[nodes/quantize_block_f32_q8_1_tiled]] _calls_
- [[nodes/tiled_vec_dot_q4_0_32x1]] _calls_
