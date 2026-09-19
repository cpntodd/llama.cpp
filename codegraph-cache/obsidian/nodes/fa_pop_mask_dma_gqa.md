---
name: "fa_pop_mask_dma_gqa"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# fa_pop_mask_dma_gqa

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/dma_queue_pop]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/dma_queue_push]] _calls_

## Used By

- [[nodes/hmx_flash_attn_ext]] _calls_
