---
name: "fa_phase_k_interleave"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# fa_phase_k_interleave

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_align_up]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/work_queue_run]] _calls_
- [[nodes/fa_k_interleave_thread]] _calls_

## Used By

- [[nodes/hmx_flash_attn_ext]] _calls_
