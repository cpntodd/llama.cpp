---
name: "hex_l2fetch"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-utils.h"
community: "ggml"
---

# hex_l2fetch

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-utils.h`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/sort1024_f32_hvx]] _calls_
- [[nodes/htp_argsort_f32_fallback]] _calls_
- [[nodes/hex_l2fetch_block]] _calls_
- [[nodes/quantize_row_f32_q8_1_flat]] _calls_
- [[nodes/tiled_vec_dot_mxfp4_32x2]] _calls_
- [[nodes/cpy_thread_f16_f32_sameshape]] _calls_
- [[nodes/cpy_thread_f32_f16_sameshape]] _calls_
- [[nodes/sum_rows_thread_f32]] _calls_
