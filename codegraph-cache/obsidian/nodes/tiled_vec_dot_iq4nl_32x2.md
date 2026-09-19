---
name: "tiled_vec_dot_iq4nl_32x2"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hvx-mm-kernels-tiled.h"
community: "ggml"
---

# tiled_vec_dot_iq4nl_32x2

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hvx-mm-kernels-tiled.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_mul_f16_f16_to_f32_lower32]] _calls_
- [[nodes/hvx_vec_mul_f32_f32]] _calls_
- [[nodes/hvx_vec_add_f32_f32]] _calls_
- [[nodes/hvx_vec_store_u]] _calls_
