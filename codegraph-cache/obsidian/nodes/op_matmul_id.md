---
name: "op_matmul_id"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# op_matmul_id

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/hex_l2fetch_block]] _calls_
- [[nodes/hvx_reduce_max_i32]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/hvx_mm_init_vec_dot]] _calls_

## Used By

- [[nodes/execute_op]] _calls_
