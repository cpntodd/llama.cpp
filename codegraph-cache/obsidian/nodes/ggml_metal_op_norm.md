---
name: "ggml_metal_op_norm"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_norm

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_metal_get_buffer_id]] _calls_
- [[nodes/can_fuse]] _calls_
- [[nodes/ggml_is_contiguous_rows]] _calls_
- [[nodes/ggml_op_name]] _calls_
- [[nodes/ggml_metal_op_concurrency_check]] _calls_
- [[nodes/ggml_metal_op_concurrency_reset]] _calls_
- [[nodes/ggml_metal_library_get_pipeline_norm]] _calls_

## Used By

- [[nodes/ggml_metal_op_encode_impl]] _calls_
