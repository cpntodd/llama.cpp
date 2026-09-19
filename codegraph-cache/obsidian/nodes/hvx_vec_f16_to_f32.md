---
name: "hvx_vec_f16_to_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-base.h"
community: "ggml"
---

# hvx_vec_f16_to_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-base.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_splat_f16]] _calls_
- [[nodes/hvx_vec_f16_to_f32_shuff]] _calls_

## Used By

- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/flat_vec_dot_mxfp4_32x1]] _calls_
- [[nodes/flat_vec_dot_mxfp4_32x2]] _calls_
