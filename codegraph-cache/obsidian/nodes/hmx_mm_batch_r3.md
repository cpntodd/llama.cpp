---
name: "hmx_mm_batch_r3"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# hmx_mm_batch_r3

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hmx_mm_batch_r2]] _calls_
- [[nodes/hex_is_aligned]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/hmx_init_column_scales]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/group]] _calls_
- [[nodes/transfer_activation_chunk_threaded]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/hmx_queue_push]] _calls_
- [[nodes/hmx_queue_make_desc]] _calls_
- [[nodes/hmx_queue_pop]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/transfer_output_chunk_scattered_worker_fn]] _calls_
- [[nodes/htp_mm_get_tiled_row_stride]] _calls_
- [[nodes/htp_mm_get_weight_tile_size]] _calls_
- [[nodes/htp_mm_get_weight_aligned_tile_size]] _calls_
- [[nodes/chunk]] _calls_
