---
name: "op_flash_attn_ext"
type: "function"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# op_flash_attn_ext

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/alibi_slope]] _calls_
- [[nodes/work_queue_run]] _calls_

## Used By

- [[nodes/execute_op]] _calls_
