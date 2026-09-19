---
name: "hvx_mm_id"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# hvx_mm_id

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_mm_run_quant_task]] _calls_
- [[nodes/htp_mm_q8_0_tiled_row_size]] _calls_
- [[nodes/htp_mm_get_weight_tile_size]] _calls_
- [[nodes/htp_mm_get_weight_aligned_tile_size]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
