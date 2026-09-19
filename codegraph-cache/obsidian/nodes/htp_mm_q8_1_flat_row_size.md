---
name: "htp_mm_q8_1_flat_row_size"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.h"
community: "ggml"
---

# htp_mm_q8_1_flat_row_size

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_align_up]] _calls_

## Used By

- [[nodes/ggml_hexagon_supported_gated_delta_net]] _calls_
- [[nodes/name]] _calls_
- [[nodes/hvx_mm_matmul]] _calls_
- [[nodes/op_matmul_qkv]] _calls_
- [[nodes/op_matmul_ffn]] _calls_
- [[nodes/htp_mm_hmx_pipeline]] _calls_
