---
name: "work_queue_run"
type: "function"
file: "ggml/src/ggml-hexagon/htp/work-queue.h"
community: "ggml"
---

# work_queue_run

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/work-queue.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/work_queue_run_async]] _calls_

## Used By

- [[nodes/fa_phase_k_interleave]] _calls_
- [[nodes/fa_v_interleave_thread]] _calls_
- [[nodes/fa_q_load_thread]] _calls_
- [[nodes/fa_o_store_thread_f16]] _calls_
- [[nodes/fa_softmax_thread]] _calls_
- [[nodes/op_flash_attn_ext]] _calls_
- [[nodes/htp_tensor_dirty_all]] _calls_
- [[nodes/htp_tensor_flush_all]] _calls_
- [[nodes/op_im2col]] _calls_
