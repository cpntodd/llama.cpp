---
name: "hvx_cumsum_row_f32"
type: "function"
file: "ggml/src/ggml-hexagon/htp/cumsum-ops.c"
community: "ggml"
---

# hvx_cumsum_row_f32

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/cumsum-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hvx_prefix_scan_f32]] _calls_
- [[nodes/hvx_vec_store_u]] _calls_
- [[nodes/hvx_splat_last_f32]] _calls_
- [[nodes/hvx_vec_get_f32]] _calls_

## Used By

- [[nodes/cumsum_thread_f32_dma]] _calls_
- [[nodes/cumsum_thread_f32]] _calls_
