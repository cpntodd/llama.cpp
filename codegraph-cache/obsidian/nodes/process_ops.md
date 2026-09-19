---
name: "process_ops"
type: "function"
file: "ggml/src/ggml-hexagon/htp/main.c"
community: "ggml"
---

# process_ops

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/main.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/vtcm_acquire]] _calls_
- [[nodes/atomic_load]] _calls_
- [[nodes/process_opbatch]] _calls_
- [[nodes/vtcm_release]] _calls_

## Used By

- [[nodes/htp_packet_callback]] _calls_
- [[nodes/htp_main_thread]] _calls_
