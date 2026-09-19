---
name: "hmx_init_column_scales"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hmx-utils.h"
community: "ggml"
---

# hmx_init_column_scales

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hmx-utils.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_vec_store_u]] _imports_
- [[nodes/hex_is_aligned]] _calls_

## Used By

- [[nodes/transfer_activation_chunk_fp32_to_fp16]] _imports_
- [[nodes/htp_fa_context]] _imports_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/hmx_matmul_worker_fn]] _calls_
- [[nodes/hmx_mm_batch_r3]] _calls_
