---
name: "hvx_vec_get_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-base.h"
community: "ggml"
---

# hvx_vec_get_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-base.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_store_a]] _calls_

## Used By

- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/vec_dot_f32_f32_aa_1x1]] _calls_
- [[nodes/hvx_vec_reduce_max2_f32]] _calls_
- [[nodes/hvx_cumsum_row_f32]] _calls_
