---
name: "hvx_mm_run_quant_task"
type: "function"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# hvx_mm_run_quant_task

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_load]] _calls_

## Used By

- [[nodes/hvx_mm_4d]] _calls_
- [[nodes/hvx_mm_2d]] _calls_
- [[nodes/hvx_mv_2d]] _calls_
- [[nodes/hvx_mm_id]] _calls_
- [[nodes/hvx_mv_id]] _calls_
- [[nodes/hvx_mm_qkv_2d]] _calls_
- [[nodes/hvx_mm_ffn_2d]] _calls_
