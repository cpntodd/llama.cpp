---
name: "transfer_activation_chunk_worker_fn"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# transfer_activation_chunk_worker_fn

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_smin]] _calls_
- [[nodes/htp_trace_event_start]] _calls_
- [[nodes/transfer_activation_chunk_fp32_to_fp16]] _calls_
- [[nodes/htp_trace_event_stop]] _calls_

## Used By

- [[nodes/transfer_activation_chunk_threaded]] _calls_
