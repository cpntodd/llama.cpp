---
name: "ggml_hexagon_supported_gated_delta_net"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# ggml_hexagon_supported_gated_delta_net

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_hexagon_is_hmx_weight_type]] _calls_
- [[nodes/matmul]] _calls_
- [[nodes/htp_mm_get_weight_aligned_tile_size]] _calls_
- [[nodes/htp_mm_hmx_pipeline]] _calls_
- [[nodes/htp_mm_get_weight_tile_size]] _calls_
- [[nodes/htp_mm_q8_1_tiled_row_size]] _calls_
- [[nodes/htp_mm_q8_0_tiled_row_size]] _calls_
- [[nodes/init_fastdiv_values]] _calls_
- [[nodes/htp_mm_q8_1_flat_row_size]] _calls_
- [[nodes/htp_mm_q8_0_flat_row_size]] _calls_
- [[nodes/ggml_hexagon_is_repack_type]] _calls_
- [[nodes/hex_round_up]] _calls_

## Used By

- [[nodes/ggml_backend_hexagon_device_supports_op]] _calls_
