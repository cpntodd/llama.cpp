---
name: "htp_mm_hmx_pipeline"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.h"
community: "ggml"
---

# htp_mm_hmx_pipeline

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_mm_get_tiled_row_stride]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/hex_smax]] _calls_
- [[nodes/htp_mm_round_up]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/htp_mm_get_weight_aligned_tile_size]] _calls_
- [[nodes/htp_mm_q8_1_flat_row_size]] _calls_
- [[nodes/htp_mm_q8_0_flat_row_size]] _calls_
- [[nodes/htp_mm_q8_1_tiled_row_size]] _calls_
- [[nodes/htp_mm_q8_0_tiled_row_size]] _calls_

## Used By

- [[nodes/ggml_hexagon_supported_gated_delta_net]] _calls_
