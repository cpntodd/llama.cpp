---
name: "htp_trace_event_stop"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-profile.h"
community: "ggml"
---

# htp_trace_event_stop

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-profile.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_trace_event]] _calls_

## Used By

- [[nodes/hvx_geglu_f32_aa]] _calls_
- [[nodes/sort1024_f32_hvx]] _calls_
- [[nodes/htp_argsort_f32_fallback]] _calls_
- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/fa_k_interleave_thread]] _calls_
- [[nodes/fa_v_interleave_thread]] _calls_
- [[nodes/fa_q_load_thread]] _calls_
- [[nodes/fa_o_store_thread_f32]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/flush_all_dcache]] _calls_
- [[nodes/l2flush_multi_worker]] _calls_
- [[nodes/htp_tensor_dirty_all]] _calls_
- [[nodes/htp_tensor_flush_all]] _calls_
- [[nodes/process_opbatch]] _calls_
- [[nodes/hmx_queue_process]] _calls_
- [[nodes/hvx_mm_4d]] _calls_
- [[nodes/name]] _calls_
- [[nodes/quantize_f32_q8_0_tiled_block]] _calls_
- [[nodes/quantize_f32_q8_1_tiled_block]] _calls_
- [[nodes/hvx_mm_2d]] _calls_
- [[nodes/hvx_mv_2d]] _calls_
- [[nodes/hvx_mm_id]] _calls_
- [[nodes/hvx_mv_id]] _calls_
- [[nodes/hvx_mm_matmul]] _calls_
- [[nodes/hvx_mm_ffn_2d]] _calls_
- [[nodes/convert_f16_worker_loop]] _calls_
- [[nodes/quantize_f32_worker_loop]] _calls_
- [[nodes/transfer_output_chunk_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_col_chunk_worker_fn]] _calls_
