---
name: "work_queue_free"
type: "function"
file: "ggml/src/ggml-hexagon/htp/work-queue.c"
community: "ggml"
---

# work_queue_free

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/work-queue.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_store_explicit]] _calls_
- [[nodes/atomic_fetch_add_explicit]] _calls_

## Used By

- [[nodes/work_queue_init]] _calls_
- [[nodes/htp_iface_stop]] _calls_
