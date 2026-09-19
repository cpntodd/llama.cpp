---
name: "ggml_webgpu_cpy"
type: "function"
file: "ggml/src/ggml-webgpu/ggml-webgpu.cpp"
community: "ggml"
---

# ggml_webgpu_cpy

**Type:** `function`  **File:** `ggml/src/ggml-webgpu/ggml-webgpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_cpy_pipeline]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_webgpu_tensor_misalignment]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/compute_2d_workgroups]] _calls_
- [[nodes/get_set_pipeline]] _calls_

## Used By

- [[nodes/ggml_webgpu_upscale]] _calls_
