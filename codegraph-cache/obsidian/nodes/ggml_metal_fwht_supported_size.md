---
name: "ggml_metal_fwht_supported_size"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-device.h"
community: "ggml"
---

# ggml_metal_fwht_supported_size

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-device.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_metal_library_get_pipeline_top_k]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_top_k_merge]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_bin]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_bin_one]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_l2_norm]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_group_norm]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_norm]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_rope]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_im2col]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_conv_transpose_1d]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_conv_transpose_2d]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_col2im_1d]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_snake]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_conv_2d]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_conv_2d_dw]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_conv_3d]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_upscale]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_pad]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_pad_reflect_1d]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_roll]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_arange]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_timestep_embedding]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_opt_step_adamw]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_opt_step_sgd]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_memset]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_count_equal]] _calls_
- [[nodes/ggml_metal_device_get]] _calls_

## Used By

- [[nodes/ggml_metal_op_can_fuse_fwht_signed]] _calls_
- [[nodes/ggml_metal_op_mul_mat]] _calls_
