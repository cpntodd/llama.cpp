---
name: "fastdiv"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-fastdiv.h"
community: "ggml"
---

# fastdiv

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-fastdiv.h`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/rope_job_f32]] _calls_
- [[nodes/flash_attn_ext_f16_thread]] _calls_
- [[nodes/fa_o_store_thread_f32]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/vec_dot_f16_f32_uu_1x1]] _calls_
- [[nodes/htp_tensor_dirty_all]] _calls_
- [[nodes/htp_tensor_flush_all]] _calls_
- [[nodes/calc_block_size]] _calls_
- [[nodes/binary_job_scalar]] _calls_
- [[nodes/binary_job_vector_same_shape]] _calls_
- [[nodes/binary_job_vector_row_broadcast]] _calls_
- [[nodes/binary_job_vector_complex]] _calls_
- [[nodes/binary_job_element_repeat]] _calls_
- [[nodes/binary_job_add_id]] _calls_
- [[nodes/hvx_mm_4d]] _calls_
- [[nodes/transfer_activation_chunk_col_chunk_worker_fn]] _calls_
- [[nodes/transfer_output_chunk_col_chunk_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_threaded]] _calls_
- [[nodes/fastmodulo]] _calls_
- [[nodes/softmax_job_f32]] _calls_
- [[nodes/get_rows_thread_f32_f32_dma]] _calls_
- [[nodes/get_rows_thread_f32_f32_hvx]] _calls_
- [[nodes/concat_generic]] _calls_
