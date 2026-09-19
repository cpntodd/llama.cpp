---
name: "dma_queue_pop"
type: "function"
file: "ggml/src/ggml-hexagon/htp/dma-queue.h"
community: "ggml"
---

# dma_queue_pop

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/dma-queue.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/dmpoll]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_

## Used By

- [[nodes/hvx_geglu_f32_aa]] _calls_
- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/rope_job_f32]] _calls_
- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/fa_pop_mask_dma_gqa]] _calls_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/binary_job_scalar]] _calls_
- [[nodes/binary_job_vector_same_shape]] _calls_
- [[nodes/binary_job_vector_row_broadcast]] _calls_
- [[nodes/binary_job_vector_complex]] _calls_
- [[nodes/binary_job_element_repeat]] _calls_
- [[nodes/binary_job_add_id]] _calls_
- [[nodes/execute_op_binary]] _calls_
- [[nodes/hvx_mm_4d]] _calls_
- [[nodes/hvx_mm_2d]] _calls_
- [[nodes/hvx_mv_2d]] _calls_
- [[nodes/hvx_mm_id]] _calls_
- [[nodes/hvx_mv_id]] _calls_
- [[nodes/hvx_mm_qkv_2d]] _calls_
- [[nodes/hvx_mm_ffn_2d]] _calls_
- [[nodes/transfer_output_chunk_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_col_chunk_worker_fn]] _calls_
- [[nodes/hmx_matmul_worker_fn]] _calls_
- [[nodes/hmx_mm_batch_r3]] _calls_
- [[nodes/get_rows_thread_f32_f32_dma]] _calls_
- [[nodes/concat_2d_f32_transposed]] _calls_
- [[nodes/concat_2d_f16_transposed]] _calls_
- [[nodes/cumsum_thread_f32_dma]] _calls_
- [[nodes/dma_queue_flush]] _calls_
