---
name: "dma_queue_push_vtcm_to_ddr"
type: "function"
file: "ggml/src/ggml-hexagon/htp/dma-queue.h"
community: "ggml"
---

# dma_queue_push_vtcm_to_ddr

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/dma-queue.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/dma_queue_push]] _calls_
- [[nodes/dma_queue_push_single_1d]] _calls_

## Used By

- [[nodes/hvx_geglu_f32_aa]] _calls_
- [[nodes/rope_job_f32]] _calls_
- [[nodes/diag_thread_f32_dma]] _calls_
- [[nodes/cumsum_thread_f32_dma]] _calls_
- [[nodes/pad_job_per_thread_hvx_dma]] _calls_
- [[nodes/pad_job_per_thread_hvx_circular_dma]] _calls_
