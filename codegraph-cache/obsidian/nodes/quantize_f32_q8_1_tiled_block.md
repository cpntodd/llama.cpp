---
name: "quantize_f32_q8_1_tiled_block"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# quantize_f32_q8_1_tiled_block

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/htp_mm_q8_1_tiled_row_size]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
