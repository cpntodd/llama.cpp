---
name: "fastmodulo"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-fastdiv.h"
community: "ggml"
---

# fastmodulo

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-fastdiv.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fastdiv]] _calls_

## Used By

- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/transfer_activation_chunk_fp32_to_fp16]] _calls_
- [[nodes/rope_job_f32]] _calls_
- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/fa_q_load_thread]] _calls_
- [[nodes/fa_o_store_thread_f32]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/hmx_fa_o_norm_worker]] _calls_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/binary_job_scalar]] _calls_
- [[nodes/binary_job_vector_complex]] _calls_
- [[nodes/binary_job_element_repeat]] _calls_
- [[nodes/hvx_mm_id]] _calls_
- [[nodes/softmax_job_f32]] _calls_
- [[nodes/set_rows_thread_f32_f32]] _calls_
- [[nodes/set_rows_thread_f16_f32]] _calls_
