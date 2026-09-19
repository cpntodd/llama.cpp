---
name: "transfer_output_chunk_scattered_worker_fn"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# transfer_output_chunk_scattered_worker_fn

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_smin]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/htp_mm_get_weight_tile_size]] _calls_
- [[nodes/htp_mm_get_weight_aligned_tile_size]] _calls_

## Used By

- [[nodes/hmx_mm_batch_r3]] _calls_
