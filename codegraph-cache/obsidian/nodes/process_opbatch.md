---
name: "process_opbatch"
type: "function"
file: "ggml/src/ggml-hexagon/htp/main.c"
community: "ggml"
---

# process_opbatch

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/main.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/profile_start]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_l2fetch_block]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/prep_op_bufs]] _calls_
- [[nodes/prep_tensors]] _calls_
- [[nodes/work_queue_wakeup]] _calls_
- [[nodes/hmx_queue_wakeup]] _calls_
- [[nodes/proc_op_req]] _calls_
- [[nodes/profile_stop]] _calls_
- [[nodes/hmx_queue_suspend]] _calls_
- [[nodes/hmx_queue_flush]] _calls_
- [[nodes/work_queue_suspend]] _calls_

## Used By

- [[nodes/process_ops]] _calls_
