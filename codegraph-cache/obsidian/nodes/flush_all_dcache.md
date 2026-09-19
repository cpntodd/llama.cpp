---
name: "flush_all_dcache"
type: "function"
file: "ggml/src/ggml-hexagon/htp/htp-tensor.c"
community: "ggml"
---

# flush_all_dcache

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/htp-tensor.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_l2fetch_block]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_

## Used By

- [[nodes/htp_tensor_dirty_all]] _calls_
- [[nodes/htp_tensor_flush_all]] _calls_
