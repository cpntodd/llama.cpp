---
name: "ggml_backend_et_graph_compute"
type: "function"
file: "ggml/src/ggml-et/ggml-et.cpp"
community: "ggml"
---

# ggml_backend_et_graph_compute

**Type:** `function`  **File:** `ggml/src/ggml-et/ggml-et.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_et_uberkernel_begin_graph]] _calls_
- [[nodes/ggml_et_can_fuse]] _calls_
- [[nodes/ggml_et_op_sqr]] _calls_
- [[nodes/ggml_et_op_unary]] _calls_
- [[nodes/ggml_et_op_sum_rows]] _calls_
- [[nodes/ggml_et_op_mean]] _calls_
- [[nodes/ggml_et_op_clamp]] _calls_
- [[nodes/ggml_et_op_mul]] _calls_
- [[nodes/ggml_et_op_add]] _calls_
- [[nodes/ggml_et_op_sub]] _calls_
- [[nodes/ggml_et_op_cumsum]] _calls_
- [[nodes/ggml_et_op_mul_mat_id]] _calls_
- [[nodes/ggml_et_op_rope]] _calls_
- [[nodes/ggml_et_op_rms_norm]] _calls_
- [[nodes/ggml_et_op_norm]] _calls_
- [[nodes/ggml_et_op_l2_norm]] _calls_
- [[nodes/ggml_et_op_group_norm]] _calls_
- [[nodes/ggml_et_op_scale]] _calls_
- [[nodes/ggml_et_op_glu]] _calls_
- [[nodes/ggml_et_op_softmax]] _calls_
- [[nodes/ggml_et_op_im2col]] _calls_
- [[nodes/ggml_et_op_conv_2d]] _calls_
- [[nodes/ggml_et_op_flash_attn_ext]] _calls_
- [[nodes/ggml_et_op_get_rows]] _calls_
- [[nodes/ggml_et_op_cont]] _calls_
- [[nodes/ggml_et_op_cpy]] _calls_
- [[nodes/ggml_et_op_concat]] _calls_
- [[nodes/ggml_et_op_repeat]] _calls_
- [[nodes/ggml_et_op_ssm_conv]] _calls_
- [[nodes/ggml_et_op_ssm_scan]] _calls_
