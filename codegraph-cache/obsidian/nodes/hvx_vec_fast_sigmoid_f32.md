---
name: "hvx_vec_fast_sigmoid_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-sigmoid.h"
community: "ggml"
---

# hvx_vec_fast_sigmoid_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-sigmoid.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_store_u]] _imports_
- [[nodes/hvx_vec_recip_xp1_O3_unsigned]] _imports_
- [[nodes/hvx_vec_exp_f32]] _imports_
- [[nodes/hvx_vec_truncate_f32]] _calls_
- [[nodes/hvx_vec_inverse_f32]] _calls_

## Used By

- [[nodes/htp_unary_context]] _imports_
