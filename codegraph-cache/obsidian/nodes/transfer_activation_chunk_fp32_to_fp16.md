---
name: "transfer_activation_chunk_fp32_to_fp16"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hmx-mm-kernels-tiled.h"
community: "ggml"
---

# transfer_activation_chunk_fp32_to_fp16

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hmx-mm-kernels-tiled.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hmx_init_column_scales]] _imports_
- [[nodes/hmx_queue_process]] _imports_
- [[nodes/hex_align_up]] _calls_
- [[nodes/hvx_vec_f32_to_f16_shuff]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/hvx_vec_splat_f16]] _calls_

## Used By

- [[nodes/htp_mm_context]] _imports_
- [[nodes/transfer_activation_chunk_worker_fn]] _calls_
