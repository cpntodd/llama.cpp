---
name: "ggml_conv_2d_dw_knl_f32"
type: "function"
file: "ggml/src/ggml-cpu/ops.cpp"
community: "ggml"
---

# ggml_conv_2d_dw_knl_f32

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_is_contiguous_channels]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/weight2]] _calls_
- [[nodes/weight1]] _calls_
- [[nodes/bicubic]] _calls_
- [[nodes/ggml_wrap_around]] _calls_
- [[nodes/ggml_vec_cpy_f32]] _calls_
