---
name: "ggml_metal_op_bin"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_bin

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_metal_op_can_fuse_snake]] _calls_
- [[nodes/ggml_metal_op_snake_fused]] _calls_
- [[nodes/ggml_metal_op_can_fuse_fwht_signed]] _calls_
- [[nodes/ggml_metal_op_fwht_signed]] _calls_
- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/can_fuse]] _calls_
- [[nodes/ggml_are_same_layout]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_bin]] _calls_
- [[nodes/ggml_metal_op_concurrency_check]] _calls_
- [[nodes/ggml_metal_op_concurrency_reset]] _calls_
- [[nodes/ggml_nrows]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
