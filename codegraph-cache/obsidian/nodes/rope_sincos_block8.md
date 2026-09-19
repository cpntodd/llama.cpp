---
name: "rope_sincos_block8"
type: "function"
file: "ggml/src/ggml-et/et-kernels/src/rope_f32.c"
community: "ggml"
---

# rope_sincos_block8

**Type:** `function`  **File:** `ggml/src/ggml-et/et-kernels/src/rope_f32.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/rope_ps_enter_fullmask]] _calls_
- [[nodes/rope_poly_sin_block8]] _calls_
- [[nodes/rope_ps_leave_fullmask]] _calls_
- [[nodes/rope_yarn_ramp]] _calls_
- [[nodes/et_logf]] _calls_
- [[nodes/et_fdiv]] _calls_
- [[nodes/et_cosf]] _calls_
- [[nodes/et_sinf]] _calls_
