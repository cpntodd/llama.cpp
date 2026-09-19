---
name: "ggml_webgpu_upscale"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_upscale

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/get_upscale_pipeline]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/compute_2d_workgroups]] _calls_
- [[nodes/ggml_is_empty]] _calls_
- [[nodes/ggml_op_name]] _calls_
- [[nodes/ggml_webgpu_cpy]] _calls_
- [[nodes/ggml_webgpu_repeat]] _calls_
- [[nodes/ggml_webgpu_can_fuse_rms_norm_mul]] _calls_
- [[nodes/ggml_webgpu_row_norm]] _calls_
- [[nodes/ggml_webgpu_scale]] _calls_
- [[nodes/ggml_webgpu_unary_op]] _calls_
- [[nodes/ggml_webgpu_pad]] _calls_
- [[nodes/ggml_webgpu_argmax]] _calls_
- [[nodes/ggml_webgpu_argsort]] _calls_
- [[nodes/ggml_webgpu_cumsum]] _calls_
- [[nodes/ggml_webgpu_sum_rows]] _calls_
- [[nodes/double]] _calls_
