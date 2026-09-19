---
name: "work_queue_run_async"
type: "function"
file: "ggml/src/ggml-hexagon/htp/work-queue.c"
community: "ggml"
---

# work_queue_run_async

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/work-queue.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_load_explicit]] _calls_
- [[nodes/atomic_store_explicit]] _calls_
- [[nodes/atomic_fetch_add_explicit]] _calls_
- [[nodes/hex_pause]] _calls_
- [[nodes/atomic_thread_fence]] _calls_

## Used By

- [[nodes/work_queue_run]] _calls_
