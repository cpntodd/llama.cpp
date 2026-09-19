---
name: "hmx_queue_process"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hmx-queue.c"
community: "ggml"
---

# hmx_queue_process

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hmx-queue.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/jinja]] _imports_
- [[nodes/atomic_load]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_
- [[nodes/atomic_store]] _calls_

## Used By

- [[nodes/transfer_activation_chunk_fp32_to_fp16]] _imports_
- [[nodes/htp_fa_context]] _imports_
- [[nodes/htp_handle]] _imports_
- [[nodes/hmx_queue_thread]] _calls_
- [[nodes/htp_mmap]] _imports_
