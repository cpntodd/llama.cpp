---
name: "transfer_activation_chunk_threaded"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# transfer_activation_chunk_threaded

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_align_down]] _calls_
- [[nodes/fastdiv]] _calls_
- [[nodes/hmx_ceil_div]] _calls_
- [[nodes/hex_smin]] _calls_
- [[nodes/transfer_activation_chunk_worker_fn]] _calls_

## Used By

- [[nodes/hmx_matmul_worker_fn]] _calls_
- [[nodes/hmx_mm_batch_r3]] _calls_
