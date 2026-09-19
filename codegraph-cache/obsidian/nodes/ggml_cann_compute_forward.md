---
name: "ggml_cann_compute_forward"
type: "function"
file: "ggml/src/ggml-cann/ggml-cann.cpp"
community: "ggml"
---

# ggml_cann_compute_forward

**Type:** `function`  **File:** `ggml/src/ggml-cann/ggml-cann.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_cann_repeat]] _calls_
- [[nodes/ggml_cann_get_rows]] _calls_
- [[nodes/ggml_cann_set_rows]] _calls_
- [[nodes/ggml_cann_dup]] _calls_
- [[nodes/ggml_cann_acc]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_cann_op_unary]] _calls_
- [[nodes/ggml_cann_elu]] _calls_
- [[nodes/ggml_cann_step]] _calls_
- [[nodes/ggml_cann_softplus]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/ggml_cann_geglu]] _calls_
- [[nodes/ggml_cann_swiglu]] _calls_
- [[nodes/ggml_cann_geglu_quick]] _calls_
- [[nodes/ggml_cann_norm]] _calls_
- [[nodes/ggml_cann_group_norm]] _calls_
- [[nodes/ggml_cann_l2_norm]] _calls_
- [[nodes/ggml_cann_cross_entropy_loss]] _calls_
- [[nodes/ggml_cann_concat]] _calls_
- [[nodes/ggml_cann_upsample_nearest2d]] _calls_
- [[nodes/ggml_cann_pad]] _calls_
- [[nodes/ggml_cann_arange]] _calls_
- [[nodes/ggml_cann_timestep_embedding]] _calls_
- [[nodes/ggml_cann_leaky_relu]] _calls_
- [[nodes/ggml_cann_rms_norm]] _calls_
- [[nodes/ggml_cann_mul_mat]] _calls_
- [[nodes/ggml_cann_mul_mat_id]] _calls_
- [[nodes/ggml_cann_scale]] _calls_
- [[nodes/ggml_cann_clamp]] _calls_
- [[nodes/ggml_cann_cpy]] _calls_

## Used By

- [[nodes/ggml_backend_cann_synchronize]] _calls_
