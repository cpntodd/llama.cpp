---
name: "ggml_metal_op_can_fuse_fwht_signed"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal-ops.cpp"
community: "ggml"
---

# ggml_metal_op_can_fuse_fwht_signed

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/n_nodes]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/gf_index]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_metal_fwht_supported_size]] _calls_

## Used By

- [[nodes/ggml_metal_op_bin]] _calls_
