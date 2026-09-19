---
name: "hvx_vec_f32_to_f16"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-base.h"
community: "ggml"
---

# hvx_vec_f32_to_f16

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-base.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_f32_to_f16_shuff]] _calls_

## Used By

- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/fa_softmax_thread]] _calls_
- [[nodes/hmx_fa_o_norm_worker]] _calls_
- [[nodes/hvx_div_mul_f16_const_using_f32]] _calls_
- [[nodes/hvx_vec_div_f16_using_f32]] _calls_
- [[nodes/hvx_copy_f32_uu]] _calls_
