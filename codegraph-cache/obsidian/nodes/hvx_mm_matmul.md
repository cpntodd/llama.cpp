---
name: "hvx_mm_matmul"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# hvx_mm_matmul

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/htp_mm_q8_1_flat_row_size]] _calls_
- [[nodes/htp_mm_q8_0_flat_row_size]] _calls_
- [[nodes/hvx_mm_init_vec_dot]] _calls_
- [[nodes/htp_mm_q8_1_tiled_row_size]] _calls_
- [[nodes/htp_mm_q8_0_tiled_row_size]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_

## Used By

- [[nodes/op_matmul]] _calls_
