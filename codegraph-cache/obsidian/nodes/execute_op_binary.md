---
name: "execute_op_binary"
type: "function"
file: "ggml/src/ggml-hexagon/htp/binary-ops.c"
community: "ggml"
---

# execute_op_binary

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/binary-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_round_up]] _calls_
- [[nodes/dma_queue_push]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/dma_queue_pop]] _calls_

## Used By

- [[nodes/op_binary]] _calls_
