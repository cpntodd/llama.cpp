---
name: "htp_tensor_dirty_all"
type: "function"
file: "ggml/src/ggml-hexagon/htp/htp-tensor.c"
community: "ggml"
---

# htp_tensor_dirty_all

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/htp-tensor.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/flush_all_dcache]] _calls_
- [[nodes/hex_align_down]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/fastdiv]] _calls_
- [[nodes/work_queue_run]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/hex_l2flush]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_

## Used By

- [[nodes/proc_op_req]] _calls_
- [[nodes/htp_tensor_flags]] _calls_
