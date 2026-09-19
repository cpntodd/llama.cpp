---
name: "htp_mm_context"
type: "class"
file: "ggml/src/ggml-hexagon/htp/matmul-ops.c"
community: "ggml"
---

# htp_mm_context

**Type:** `class`  **File:** `ggml/src/ggml-hexagon/htp/matmul-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/jinja]] _imports_
- [[nodes/hex-dma.h]] _imports_
- [[nodes/hvx-utils.h]] _imports_
- [[nodes/hvx_vec_dump_f16_n]] _imports_
- [[nodes/OP_NAME]] _imports_
- [[nodes/hvx_vec_reduce_sum_n_i32]] _imports_
- [[nodes/ggml-common.h]] _imports_
- [[nodes/htp_mmap]] _imports_
- [[nodes/htp_status]] _imports_
- [[nodes/htp-vtcm.h]] _imports_
- [[nodes/transfer_activation_chunk_fp32_to_fp16]] _imports_
- [[nodes/quantize_block_f32_q8_1_tiled]] _imports_
- [[nodes/quantize_row_f32_q8_0_flat]] _imports_

## Used By

- [[nodes/htp_opnode]] _imports_
- [[nodes/ggml_hexagon_dump_op_exec]] _imports_
