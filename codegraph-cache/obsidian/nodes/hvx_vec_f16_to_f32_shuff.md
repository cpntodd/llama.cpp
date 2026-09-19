---
name: "hvx_vec_f16_to_f32_shuff"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-base.h"
community: "ggml"
---

# hvx_vec_f16_to_f32_shuff

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-base.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_splat_f16]] _calls_

## Used By

- [[nodes/fa_o_store_thread_f32]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/tiled_vec_dot_mxfp4_32x1]] _calls_
- [[nodes/tiled_vec_dot_mxfp4_32x2]] _calls_
- [[nodes/hvx_vec_f16_to_f32]] _calls_
