---
name: "htp_argsort_f32_fallback"
type: "function"
file: "ggml/src/ggml-hexagon/htp/argsort-ops.c"
community: "ggml"
---

# htp_argsort_f32_fallback

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/argsort-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_round_up]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_l2fetch]] _calls_
- [[nodes/hvx_copy_f32_au]] _calls_
- [[nodes/quicksort_values_indices_asc]] _calls_
- [[nodes/quicksort_values_indices_desc]] _calls_
- [[nodes/hvx_copy_f32_ua]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
