---
name: "softmax_job_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/softmax-ops.c"
community: "ggml"
---

# softmax_job_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/softmax-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_is_aligned]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/fastdiv]] _calls_
- [[nodes/hvx_fast_softmax_f32]] _calls_
- [[nodes/hvx_scale_f32]] _calls_
- [[nodes/hvx_reduce_max_f32]] _calls_
- [[nodes/hvx_softmax_f32]] _calls_
