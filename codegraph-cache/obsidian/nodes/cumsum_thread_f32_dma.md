---
name: "cumsum_thread_f32_dma"
type: "function"
file: "ggml/src/ggml-hexagon/htp/cumsum-ops.c"
community: "ggml"
---

# cumsum_thread_f32_dma

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/cumsum-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/dma_queue_push_vtcm_to_ddr]] _calls_
- [[nodes/dma_queue_push_ddr_to_vtcm]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/hvx_cumsum_row_f32]] _calls_
- [[nodes/dma_queue_flush]] _calls_
