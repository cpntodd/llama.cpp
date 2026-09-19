---
name: "gdn_mul_dot_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/gated-delta-net-ops.c"
community: "ggml"
---

# gdn_mul_dot_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/gated-delta-net-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_add_f32_f32]] _calls_
- [[nodes/hvx_vec_store_u]] _calls_
- [[nodes/hvx_vec_reduce_sum_f32]] _calls_

## Used By

- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
