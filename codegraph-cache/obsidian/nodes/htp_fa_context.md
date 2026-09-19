---
name: "htp_fa_context"
type: "class"
file: "ggml/src/ggml-hexagon/htp/flash-attn-ops.c"
community: "ggml"
---

# htp_fa_context

**Type:** `class`  **File:** `ggml/src/ggml-hexagon/htp/flash-attn-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/jinja]] _imports_
- [[nodes/hex-dma.h]] _imports_
- [[nodes/fastdiv_values]] _imports_
- [[nodes/hex_get_pmu]] _imports_
- [[nodes/hmx_queue_process]] _imports_
- [[nodes/hmx_init_column_scales]] _imports_
- [[nodes/hvx-utils.h]] _imports_
- [[nodes/hvx_vec_dump_f16_n]] _imports_
- [[nodes/hvx_splat_a]] _imports_
- [[nodes/hvx_vec_reduce_sum_n_i32]] _imports_
- [[nodes/alibi_slope]] _imports_
- [[nodes/htp-vtcm.h]] _imports_
- [[nodes/work_queue_task_s]] _imports_
- [[nodes/ggml-common.h]] _imports_
- [[nodes/htp_mmap]] _imports_
- [[nodes/htp_status]] _imports_
- [[nodes/hvx_dot_f16_f16_aa]] _imports_
- [[nodes/hmx-fa-kernels.h]] _imports_

## Used By

- [[nodes/htp_opnode]] _imports_
- [[nodes/ggml_hexagon_dump_op_exec]] _imports_
