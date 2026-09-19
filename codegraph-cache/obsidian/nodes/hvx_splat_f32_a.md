---
name: "hvx_splat_f32_a"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-copy.h"
community: "ggml"
---

# hvx_splat_f32_a

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-copy.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_splat_a]] _calls_
- [[nodes/hvx_vec_splat_f32]] _calls_

## Used By

- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/fa_q_load_thread]] _calls_
- [[nodes/quantize_row_f32_q8_1_flat]] _calls_
- [[nodes/tiled_vec_dot_mxfp4_32x2]] _calls_
- [[nodes/pad_job_per_thread_hvx_dma]] _calls_
