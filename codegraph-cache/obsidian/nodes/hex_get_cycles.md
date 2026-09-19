---
name: "hex_get_cycles"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-utils.h"
community: "ggml"
---

# hex_get_cycles

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-utils.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fastdiv_values]] _imports_
- [[nodes/hex_dump_int8_line]] _imports_
- [[nodes/hex_ceil_pow2]] _imports_

## Used By

- [[nodes/OP_NAME]] _imports_
- [[nodes/work_queue_task_s]] _imports_
- [[nodes/l2flush_range]] _imports_
- [[nodes/htp_handle]] _imports_
- [[nodes/profile_start]] _calls_
- [[nodes/profile_stop]] _calls_
- [[nodes/hvx_div_mul_f16_const_using_f32]] _imports_
- [[nodes/hvx_vec_dump_f16_n]] _imports_
- [[nodes/hvx_vec_rsqrt_f32]] _imports_
- [[nodes/hmx_queue_signal]] _imports_
- [[nodes/hvx_vec_store_u]] _imports_
- [[nodes/hex_get_pmu]] _imports_
- [[nodes/htp_trace_event]] _calls_
- [[nodes/htp_diag_context]] _imports_
- [[nodes/hvx_vec_reduce_sum_n_i32]] _imports_
- [[nodes/dma_ring_s]] _imports_
