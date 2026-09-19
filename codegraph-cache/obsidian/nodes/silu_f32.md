---
name: "silu_f32"
type: "function"
file: "ggml/src/ggml-et/et-kernels/src/glu_f32.c"
community: "ggml"
---

# silu_f32

**Type:** `function`  **File:** `ggml/src/ggml-et/et-kernels/src/glu_f32.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/exp]] _calls_
- [[nodes/et_expf]] _calls_
- [[nodes/et_fdiv]] _calls_
- [[nodes/tanh]] _calls_
- [[nodes/sqrt]] _calls_

## Used By

- [[nodes/block_swiglu]] _calls_
