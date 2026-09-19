---
name: "dequantize_q4_K_block"
type: "function"
file: "ggml/src/ggml-et/et-kernels/src/quants.h"
community: "ggml"
---

# dequantize_q4_K_block

**Type:** `function`  **File:** `ggml/src/ggml-et/et-kernels/src/quants.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fp16_to_fp32]] _calls_
- [[nodes/get_scale_min_k4]] _calls_

## Used By

- [[nodes/copy_q4_K_row]] _calls_
