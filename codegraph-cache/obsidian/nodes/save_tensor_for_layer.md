---
name: "save_tensor_for_layer"
type: "function"
file: "tools/cvector-generator/cvector-generator.cpp"
community: "ggml"
---

# save_tensor_for_layer

**Type:** `function`  **File:** `tools/cvector-generator/cvector-generator.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/ggml_get_name]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_get_f32_nd]] _calls_
- [[nodes/ggml_format_name]] _calls_
- [[nodes/ggml_set_f32_nd]] _calls_

## Used By

- [[nodes/cb_eval]] _calls_
