---
name: "ggml_webgpu_hash_combine"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu-shader-lib.hpp"
community: "ggml"
---

# ggml_webgpu_hash_combine

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu-shader-lib.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_up32]] _imports_
- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/pre_wgsl]] _imports_
- [[nodes/jinja]] _imports_

## Used By

- [[nodes/compute_2d_workgroups]] _imports_
- [[nodes/ggml_webgpu_tensor_equal]] _calls_
- [[nodes/operator]] _calls_
- [[nodes/ggml_webgpu_flash_attn_v_direct]] _calls_
