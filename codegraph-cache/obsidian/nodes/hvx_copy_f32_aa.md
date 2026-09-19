---
name: "hvx_copy_f32_aa"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-copy.h"
community: "ggml"
---

# hvx_copy_f32_aa

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-copy.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_copy_aa]] _calls_

## Used By

- [[nodes/quantize_row_f32_q8_1_flat]] _calls_
- [[nodes/tiled_vec_dot_mxfp4_32x2]] _calls_
- [[nodes/pad_job_per_thread_hvx_dma]] _calls_
- [[nodes/pad_job_per_thread_hvx_circular_dma]] _calls_
