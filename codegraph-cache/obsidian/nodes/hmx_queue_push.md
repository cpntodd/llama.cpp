---
name: "hmx_queue_push"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hmx-queue.h"
community: "ggml"
---

# hmx_queue_push

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hmx-queue.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_load]] _calls_
- [[nodes/atomic_store]] _calls_
- [[nodes/hmx_queue_signal]] _calls_
- [[nodes/hmx_queue_make_desc]] _calls_

## Used By

- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/hmx_matmul_worker_fn]] _calls_
- [[nodes/hmx_mm_batch_r3]] _calls_
