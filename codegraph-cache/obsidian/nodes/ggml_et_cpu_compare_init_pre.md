---
name: "ggml_et_cpu_compare_init_pre"
type: "function"
file: "ggml/src/ggml-et/ggml-et-cpu-compare.cpp"
community: "ggml"
---

# ggml_et_cpu_compare_init_pre

**Type:** `function`  **File:** `ggml/src/ggml-et/ggml-et-cpu-compare.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_et_cpu_compare_config]] _imports_
- [[nodes/ggml_compute_params]] _imports_
- [[nodes/ops.md]] _imports_
- [[nodes/ggml_backend_buffer_get_size]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/device]] _calls_
- [[nodes/ggml_backend_cpu_init]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_et_cpu_compare_free]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_op_name]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_
- [[nodes/ggml_backend_graph_compute]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_fp16_to_fp32]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_

## Used By

- [[nodes/ggml_et_op_sqr]] _calls_
- [[nodes/ggml_et_op_sum_rows]] _calls_
- [[nodes/ggml_et_op_mean]] _calls_
- [[nodes/ggml_et_op_clamp]] _calls_
- [[nodes/ggml_et_op_unary]] _calls_
- [[nodes/ggml_et_op_elmap]] _calls_
- [[nodes/ggml_et_op_glu]] _calls_
- [[nodes/ggml_et_op_mul_mat_id]] _calls_
- [[nodes/ggml_et_op_rope]] _calls_
- [[nodes/ggml_et_op_rms_norm]] _calls_
- [[nodes/ggml_et_op_norm]] _calls_
- [[nodes/ggml_et_op_l2_norm]] _calls_
- [[nodes/ggml_et_op_group_norm]] _calls_
- [[nodes/ggml_et_op_im2col]] _calls_
- [[nodes/ggml_et_op_softmax]] _calls_
- [[nodes/ggml_et_op_get_rows]] _calls_
- [[nodes/ggml_et_op_cont]] _calls_
- [[nodes/ggml_et_op_cumsum]] _calls_
- [[nodes/ggml_et_op_cpy]] _calls_
- [[nodes/ggml_et_op_concat]] _calls_
- [[nodes/ggml_et_op_repeat]] _calls_
- [[nodes/ggml_et_op_ssm_conv]] _calls_
- [[nodes/ggml_et_op_rwkv_wkv6]] _calls_
- [[nodes/ggml_et_op_rwkv_wkv7]] _calls_
- [[nodes/ggml_et_op_gated_delta_net]] _calls_
- [[nodes/ggml_et_op_set_rows]] _calls_
- [[nodes/ggml_et_op_pad]] _calls_
