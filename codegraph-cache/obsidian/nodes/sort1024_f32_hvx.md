---
name: "sort1024_f32_hvx"
type: "function"
file: "ggml/src/ggml-hexagon/htp/argsort-ops.c"
community: "ggml"
---

# sort1024_f32_hvx

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/argsort-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/bitonic_sort_generic_hvx]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_l2fetch]] _calls_
- [[nodes/hvx_copy_f32_au]] _calls_
- [[nodes/hvx_copy_f32_ua]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
