---
name: "hvx_copy_f32_uu"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-copy.h"
community: "ggml"
---

# hvx_copy_f32_uu

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-copy.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_copy_uu]] _calls_
- [[nodes/hvx_vec_f32_to_f16]] _calls_

## Used By

- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/hvx_rope_f32_aa]] _calls_
- [[nodes/get_rows_thread_f32_f32_hvx]] _calls_
- [[nodes/pad_job_per_thread_hvx]] _calls_
- [[nodes/pad_job_per_thread_hvx_circular]] _calls_
- [[nodes/pad_job_per_thread_hvx_circular_dma]] _calls_
- [[nodes/set_rows_thread_f32_f32]] _calls_
