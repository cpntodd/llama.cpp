---
name: "dma_queue_flush"
type: "function"
file: "ggml/src/ggml-hexagon/htp/dma-queue.h"
community: "ggml"
---

# dma_queue_flush

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/dma-queue.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/dma_queue_pop]] _calls_

## Used By

- [[nodes/hvx_geglu_f32_aa]] _calls_
- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/rope_job_f32]] _calls_
- [[nodes/binary_job_scalar]] _calls_
- [[nodes/binary_job_vector_same_shape]] _calls_
- [[nodes/binary_job_vector_row_broadcast]] _calls_
- [[nodes/binary_job_vector_complex]] _calls_
- [[nodes/binary_job_element_repeat]] _calls_
- [[nodes/binary_job_add_id]] _calls_
- [[nodes/diag_thread_f32_dma]] _calls_
- [[nodes/get_rows_thread_f32_f32_dma]] _calls_
- [[nodes/cumsum_thread_f32_dma]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/pad_job_per_thread_hvx_dma]] _calls_
- [[nodes/pad_job_per_thread_hvx_circular_dma]] _calls_
