---
name: "fa_softmax_thread"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# fa_softmax_thread

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_inverse_f32]] _calls_
- [[nodes/hvx_vec_f32_to_f16]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/work_queue_run]] _calls_
