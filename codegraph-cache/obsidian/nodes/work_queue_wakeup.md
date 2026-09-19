---
name: "work_queue_wakeup"
type: "function"
file: "ggml/src/ggml-hexagon/htp/work-queue.c"
community: "ggml"
---

# work_queue_wakeup

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/work-queue.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_load_explicit]] _calls_
- [[nodes/atomic_store_explicit]] _calls_
- [[nodes/atomic_fetch_add_explicit]] _calls_

## Used By

- [[nodes/process_opbatch]] _calls_
