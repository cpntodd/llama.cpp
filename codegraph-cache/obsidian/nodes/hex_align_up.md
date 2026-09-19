---
name: "hex_align_up"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-common.h"
community: "ggml"
---

# hex_align_up

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-common.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hmx_ceil_div]] _calls_

## Used By

- [[nodes/ggml_hexagon_measure_max_vmem]] _calls_
- [[nodes/transfer_activation_chunk_fp32_to_fp16]] _calls_
- [[nodes/fa_phase_k_interleave]] _calls_
- [[nodes/fa_v_interleave_thread]] _calls_
- [[nodes/fa_q_load_thread]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/work_queue_sizeof]] _calls_
- [[nodes/htp_tensor_dirty_all]] _calls_
- [[nodes/htp_tensor_flush_all]] _calls_
- [[nodes/htp_iface_start]] _calls_
- [[nodes/hmx_queue_sizeof]] _calls_
- [[nodes/hmx_queue_init]] _calls_
- [[nodes/hvx_mm_4d]] _calls_
- [[nodes/transfer_output_chunk_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_col_chunk_worker_fn]] _calls_
- [[nodes/transfer_output_chunk_col_chunk_worker_fn]] _calls_
- [[nodes/hmx_mm_batch_r3]] _calls_
- [[nodes/htp_mm_q8_0_flat_row_size]] _calls_
- [[nodes/htp_mm_q8_1_flat_row_size]] _calls_
- [[nodes/htp_mm_hmx_pipeline]] _calls_
