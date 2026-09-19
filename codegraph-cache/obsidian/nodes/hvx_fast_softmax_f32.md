---
name: "hvx_fast_softmax_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/softmax-ops.c"
community: "ggml"
---

# hvx_fast_softmax_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/softmax-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_reduce_max_f32]] _calls_
- [[nodes/hvx_vec_exp_f32]] _calls_
- [[nodes/hvx_vec_reduce_sum_f32]] _calls_
- [[nodes/hvx_vec_inverse_f32]] _calls_

## Used By

- [[nodes/softmax_job_f32]] _calls_
