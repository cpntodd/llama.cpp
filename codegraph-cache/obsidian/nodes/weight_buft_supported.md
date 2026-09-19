---
name: "weight_buft_supported"
type: "function"
file: "src/llama-model-loader.cpp"
community: "ggml"
---

# weight_buft_supported

**Type:** `function`  **File:** `src/llama-model-loader.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/format]] _calls_
- [[nodes/ggml_op_name]] _calls_
- [[nodes/ggml_backend_buft_alloc_buffer]] _calls_
- [[nodes/ggml_backend_dev_supports_op]] _calls_
- [[nodes/ggml_backend_buffer_free]] _calls_

## Used By

- [[nodes/select_weight_buft]] _calls_
