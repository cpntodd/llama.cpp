---
name: "htp_iface_stop"
type: "function"
file: "ggml/src/ggml-hexagon/htp/main.c"
community: "ggml"
---

# htp_iface_stop

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/main.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_store]] _calls_
- [[nodes/dspqueue_close]] _calls_
- [[nodes/work_queue_free]] _calls_
- [[nodes/dma_queue_alias_free]] _calls_
- [[nodes/dma_queue_free]] _calls_
- [[nodes/hmx_queue_free]] _calls_
- [[nodes/vtcm_free]] _calls_

## Used By

- [[nodes/ggml_hexagon_measure_max_vmem]] _calls_
- [[nodes/htp_iface_start]] _calls_
