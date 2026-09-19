---
name: "op_matmul"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# op_matmul

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hmx_mm_op_matmul]] _calls_
- [[nodes/hvx_mm_matmul]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/htp_mm_q8_1_tiled_row_size]] _calls_
- [[nodes/htp_mm_q8_0_tiled_row_size]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_

## Used By

- [[nodes/execute_op]] _calls_
