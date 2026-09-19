---
name: "hvx_vec_mul_f32_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-base.h"
community: "ggml"
---

# hvx_vec_mul_f32_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-base.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_add_f32_f32]] _calls_
- [[nodes/hvx_vec_sub_f32_f32]] _calls_

## Used By

- [[nodes/hvx_geglu_f32_aa]] _calls_
- [[nodes/gdn_mul_dot_f32]] _calls_
- [[nodes/gdn_mul_scalar_dot_f32]] _calls_
- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/rope_yarn_ramp]] _calls_
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
- [[nodes/tiled_vec_dot_q4_0_32x1]] _calls_
- [[nodes/tiled_vec_dot_q4_0_32x2]] _calls_
- [[nodes/tiled_vec_dot_q4_1_32x1]] _calls_
- [[nodes/tiled_vec_dot_q4_1_32x2]] _calls_
- [[nodes/tiled_vec_dot_q8_0_32x1]] _calls_
- [[nodes/tiled_vec_dot_q8_0_32x2]] _calls_
- [[nodes/tiled_vec_dot_iq4nl_32x1]] _calls_
- [[nodes/tiled_vec_dot_iq4nl_32x2]] _calls_
- [[nodes/tiled_vec_dot_mxfp4_32x1]] _calls_
- [[nodes/tiled_vec_dot_mxfp4_32x2]] _calls_
- [[nodes/hvx_vec_cos_f32]] _calls_
- [[nodes/hvx_vec_sin_f32]] _calls_
- [[nodes/alibi_slope]] _calls_
- [[nodes/hvx_load_partial_f32]] _calls_
