---
name: "ggml_backend_hexagon_device_supports_op"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# ggml_backend_hexagon_device_supports_op

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_op_desc]] _calls_
- [[nodes/ggml_hexagon_supported_buffers]] _calls_
- [[nodes/ggml_hexagon_dump_op_supp]] _calls_
- [[nodes/ggml_hexagon_supported_binary]] _calls_
- [[nodes/ggml_hexagon_supported_mul_mat]] _calls_
- [[nodes/ggml_hexagon_supported_mul_mat_id]] _calls_
- [[nodes/ggml_hexagon_supported_add_id]] _calls_
- [[nodes/ggml_hexagon_supported_unary]] _calls_
- [[nodes/ggml_hexagon_supported_sum_rows]] _calls_
- [[nodes/ggml_hexagon_supported_softmax]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/ggml_hexagon_supported_activations]] _calls_
- [[nodes/ggml_hexagon_supported_rope]] _calls_
- [[nodes/ggml_hexagon_supported_flash_attn_ext]] _calls_
- [[nodes/ggml_hexagon_supported_set_rows]] _calls_
- [[nodes/ggml_hexagon_supported_get_rows]] _calls_
- [[nodes/ggml_hexagon_supported_cpy]] _calls_
- [[nodes/ggml_hexagon_supported_cont]] _calls_
- [[nodes/ggml_hexagon_supported_repeat]] _calls_
- [[nodes/ggml_hexagon_supported_argsort]] _calls_
- [[nodes/ggml_hexagon_supported_ssm_conv]] _calls_
- [[nodes/ggml_hexagon_supported_im2col]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_hexagon_supported_gated_delta_net]] _calls_
- [[nodes/ggml_hexagon_supported_cumsum]] _calls_
- [[nodes/ggml_hexagon_supported_concat]] _calls_
- [[nodes/ggml_hexagon_supported_fill]] _calls_
- [[nodes/ggml_hexagon_supported_diag]] _calls_
- [[nodes/ggml_hexagon_supported_solve_tri]] _calls_
