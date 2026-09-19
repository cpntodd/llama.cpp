---
name: "hvx_copy_f32_ua"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-copy.h"
community: "ggml"
---

# hvx_copy_f32_ua

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-copy.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_copy_ua]] _calls_

## Used By

- [[nodes/sort1024_f32_hvx]] _calls_
- [[nodes/htp_argsort_f32_fallback]] _calls_
- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/hvx_mm_4d]] _calls_
- [[nodes/hvx_mv_2d]] _calls_
- [[nodes/pad_job_per_thread_hvx_dma]] _calls_
- [[nodes/pad_job_per_thread_hvx_circular_dma]] _calls_
