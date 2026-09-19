---
name: "pad_job_per_thread_hvx_dma"
type: "function"
file: "ggml/src/ggml-hexagon/htp/pad-ops.c"
community: "ggml"
---

# pad_job_per_thread_hvx_dma

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/pad-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/dma_queue_push_vtcm_to_ddr]] _calls_
- [[nodes/dma_queue_push_ddr_to_vtcm]] _calls_
- [[nodes/dma_queue_pop]] _calls_
- [[nodes/hvx_splat_f32_a]] _calls_
- [[nodes/hvx_copy_f32_aa]] _calls_
- [[nodes/hvx_copy_f32_ua]] _calls_
- [[nodes/dma_queue_flush]] _calls_
