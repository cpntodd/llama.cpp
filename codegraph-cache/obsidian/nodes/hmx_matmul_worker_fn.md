---
name: "hmx_matmul_worker_fn"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# hmx_matmul_worker_fn

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_is_aligned]] _calls_
- [[nodes/htp_mm_get_tiled_row_stride]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/hmx_init_column_scales]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/transfer_activation_chunk_threaded]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/hmx_queue_push]] _calls_
- [[nodes/hmx_queue_make_desc]] _calls_
- [[nodes/hmx_queue_pop]] _calls_
- [[nodes/chunk]] _calls_
