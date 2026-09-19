---
name: "init_fastdiv_values"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-fastdiv.h"
community: "ggml"
---

# init_fastdiv_values

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-fastdiv.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ceil]] _calls_
- [[nodes/log2]] _calls_

## Used By

- [[nodes/ggml_hexagon_measure_max_vmem]] _calls_
- [[nodes/ggml_hexagon_supported_gated_delta_net]] _calls_
- [[nodes/gated_delta_net_f32_pp_thread]] _calls_
- [[nodes/gated_delta_net_f32_tg_thread]] _calls_
- [[nodes/execute_op_rope_f32]] _calls_
- [[nodes/fa_softmax_thread]] _calls_
- [[nodes/htp_iface_start]] _calls_
- [[nodes/execute_op_binary]] _calls_
- [[nodes/transfer_output_chunk_col_chunk_worker_fn]] _calls_
- [[nodes/hmx_matmul_worker_fn]] _calls_
- [[nodes/hmx_mm_batch_r3]] _calls_
- [[nodes/init_softmax_ctx]] _calls_
- [[nodes/op_get_rows]] _calls_
- [[nodes/op_concat]] _calls_
- [[nodes/op_set_rows]] _calls_
