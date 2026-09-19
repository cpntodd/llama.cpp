---
name: "hvx_exp_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-exp.h"
community: "ggml"
---

# hvx_exp_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-exp.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_is_aligned]] _calls_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_neg_f32]] _calls_
- [[nodes/hvx_vec_exp_f32_guard]] _calls_
- [[nodes/hvx_vec_store_u]] _calls_

## Used By

- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/hvx_softmax_f32]] _calls_
- [[nodes/tile_gelu_f32]] _calls_
