---
name: "rope_yarn_ramp"
type: "function"
file: "ggml/src/ggml-hexagon/htp/rope-ops.c"
community: "ggml"
---

# rope_yarn_ramp

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/rope-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_inverse_f32]] _calls_
- [[nodes/hvx_vec_cos_f32]] _calls_
- [[nodes/hvx_vec_sin_f32]] _calls_
- [[nodes/hvx_vec_store_u]] _calls_
- [[nodes/rope_corr_dims]] _calls_
