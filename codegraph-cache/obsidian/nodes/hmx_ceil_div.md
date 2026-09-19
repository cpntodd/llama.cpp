---
name: "hmx_ceil_div"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-common.h"
community: "ggml"
---

# hmx_ceil_div

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-common.h`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/htp_argsort_f32_fallback]] _calls_
- [[nodes/fa_phase_k_interleave]] _calls_
- [[nodes/fa_v_interleave_thread]] _calls_
- [[nodes/fa_q_load_thread]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/fa_softmax_thread]] _calls_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/transfer_output_chunk_scattered_worker_fn]] _calls_
- [[nodes/transfer_output_chunk_col_chunk_worker_fn]] _calls_
- [[nodes/transfer_activation_chunk_threaded]] _calls_
- [[nodes/hmx_matmul_worker_fn]] _calls_
- [[nodes/hmx_mm_batch_r3]] _calls_
- [[nodes/hex_align_up]] _calls_
- [[nodes/hvx_fa_compute_vtcm_usage]] _calls_
- [[nodes/op_concat]] _calls_
