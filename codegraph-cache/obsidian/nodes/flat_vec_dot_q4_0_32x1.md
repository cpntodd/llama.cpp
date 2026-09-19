---
name: "flat_vec_dot_q4_0_32x1"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-mm-kernels-flat.h"
community: "ggml"
---

# flat_vec_dot_q4_0_32x1

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-mm-kernels-flat.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_round_up]] _calls_
- [[nodes/hvx_vec_repl_f16]] _calls_
- [[nodes/hvx_vec_mul_f16_f16_to_f32_lower32]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_add_f32_f32]] _calls_
- [[nodes/hvx_vec_store_u]] _calls_
