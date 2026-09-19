---
name: "transfer_output_chunk_worker_fn"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# transfer_output_chunk_worker_fn

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/dma_queue_pop]] _calls_

## Used By

- [[nodes/transfer_output_chunk_col_chunk_worker_fn]] _calls_
