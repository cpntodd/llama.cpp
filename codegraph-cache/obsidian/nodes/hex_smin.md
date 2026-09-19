---
name: "hex_smin"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-common.h"
community: "ggml"
---

# hex_smin

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-common.h`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/fa_k_interleave_thread]] _calls_
- [[nodes/fa_v_interleave_thread]] _calls_
- [[nodes/fa_q_load_thread]] _calls_
- [[nodes/fa_o_store_thread_f32]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/fa_softmax_thread]] _calls_
- [[nodes/fa_pop_mask_dma_gqa]] _calls_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/hvx_mm_ffn_2d]] _calls_
- [[nodes/convert_f16_worker_loop]] _calls_
- [[nodes/quantize_f32_worker_loop]] _calls_
- [[nodes/transfer_output_chunk_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_col_chunk_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_gathered_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_gathered_worker_flat_fn]] _calls_
- [[nodes/transfer_output_chunk_scattered_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_threaded]] _calls_
- [[nodes/hmx_matmul_worker_fn]] _calls_
- [[nodes/hmx_mm_batch_r3]] _calls_
- [[nodes/htp_mm_hmx_pipeline]] _calls_
