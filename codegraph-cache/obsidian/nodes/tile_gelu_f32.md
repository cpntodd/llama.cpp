---
name: "tile_gelu_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/unary-ops.c"
community: "ggml"
---

# tile_gelu_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/unary-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_sigmoid_f32_aa]] _calls_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_store_a]] _calls_
- [[nodes/tile_scale_f32]] _calls_
- [[nodes/tile_clamp_f32]] _calls_
- [[nodes/hvx_sqr_f32_aa]] _calls_
- [[nodes/hvx_sqrt_f32_aa]] _calls_
- [[nodes/hvx_scale_f32_aa]] _calls_
- [[nodes/hvx_exp_f32]] _calls_
- [[nodes/tile_silu_f32]] _calls_
- [[nodes/tile_unary_softplus_f32]] _calls_
- [[nodes/hvx_tanh_f32_aa]] _calls_
