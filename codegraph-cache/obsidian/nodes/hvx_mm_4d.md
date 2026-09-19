---
name: "hvx_mm_4d"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# hvx_mm_4d

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/fastdiv]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/hvx_mm_run_quant_task]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/dma_queue_pop_nowait]] _calls_
- [[nodes/hvx_copy_f32_ua]] _calls_
- [[nodes/hex_round_up]] _calls_
