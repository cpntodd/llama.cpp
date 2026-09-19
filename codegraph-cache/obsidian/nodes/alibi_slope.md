---
name: "alibi_slope"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-flash-attn.h"
community: "ggml"
---

# alibi_slope

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-flash-attn.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx-utils.h]] _imports_
- [[nodes/hvx_vec_splat_f32]] _calls_
- [[nodes/hvx_vec_add_f32_f32]] _calls_
- [[nodes/hvx_vec_sub_f32_f32]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_pow_const_base_f32]] _calls_

## Used By

- [[nodes/htp_fa_context]] _imports_
- [[nodes/hmx_fa_o_norm_worker]] _calls_
- [[nodes/op_flash_attn_ext]] _calls_
