---
name: "hex_round_up"
type: "function"
file: "ggml/src/ggml-hexagon/htp/hex-common.h"
community: "ggml"
---

# hex_round_up

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/hex-common.h`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/repack_q4_0_tiled]] _calls_
- [[nodes/repack_tiled_q4_0]] _calls_
- [[nodes/repack_q4_1_tiled]] _calls_
- [[nodes/repack_tiled_q4_1]] _calls_
- [[nodes/repack_q8_0_tiled]] _calls_
- [[nodes/repack_tiled_q8_0]] _calls_
- [[nodes/repack_mxfp4_tiled]] _calls_
- [[nodes/repack_tiled_mxfp4]] _calls_
- [[nodes/ggml_backend_hexagon_buffer_type_get_alloc_size]] _calls_
- [[nodes/same_shape]] _calls_
- [[nodes/add_tensor]] _calls_
- [[nodes/ggml_hexagon_measure_max_vmem]] _calls_
- [[nodes/ggml_hexagon_supported_gated_delta_net]] _calls_
- [[nodes/if]] _calls_
- [[nodes/mm_is_hmx_eligible]] _calls_
- [[nodes/execute_op_activations_f32]] _calls_
- [[nodes/execute_op_rope_f32]] _calls_
- [[nodes/sort1024_f32_hvx]] _calls_
- [[nodes/htp_argsort_f32_fallback]] _calls_
- [[nodes/op_argsort]] _calls_
- [[nodes/hmx_flash_attn_ext]] _calls_
- [[nodes/op_flash_attn_ext]] _calls_
- [[nodes/quantize_row_f32_q8_0_flat]] _calls_
- [[nodes/quantize_row_f32_q8_1_flat]] _calls_
- [[nodes/flat_vec_dot_q4_0_32x1]] _calls_
- [[nodes/flat_vec_dot_q4_0_32x2]] _calls_
- [[nodes/flat_vec_dot_q4_1_32x1]] _calls_
- [[nodes/flat_vec_dot_q4_1_32x2]] _calls_
- [[nodes/flat_vec_dot_q8_0_32x1]] _calls_
- [[nodes/flat_vec_dot_q8_0_32x2]] _calls_
