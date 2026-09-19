---
name: "gated_delta_net_f32_pp_thread"
type: "function"
file: "ggml/src/ggml-hexagon/htp/gated-delta-net-ops.c"
community: "ggml"
---

# gated_delta_net_f32_pp_thread

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/gated-delta-net-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/fastdiv]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/hvx_copy_f32_au]] _calls_
- [[nodes/hvx_exp_f32]] _calls_
- [[nodes/hvx_vec_sub_f32_f32]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_store_u]] _calls_
- [[nodes/gdn_mul_dot_f32]] _calls_
- [[nodes/hvx_vec_get_f32]] _calls_
- [[nodes/gdn_mul_scalar_dot_f32]] _calls_
- [[nodes/hvx_copy_f32_uu]] _calls_
- [[nodes/block]] _calls_
- [[nodes/dma_queue_flush]] _calls_
