---
name: "fa_init_uniform"
type: "function"
file: "tools/tuning/fa-vec.cpp"
community: "ggml"
---

# fa_init_uniform

**Type:** `function`  **File:** `tools/tuning/fa-vec.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_quantize_requires_imatrix]] _calls_
- [[nodes/ggml_row_size]] _calls_

## Used By

- [[nodes/fa_init_tensors]] _calls_
