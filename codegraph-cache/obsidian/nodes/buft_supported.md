---
name: "buft_supported"
type: "function"
file: "src/llama-model.cpp"
community: "ggml"
---

# buft_supported

**Type:** `function`  **File:** `src/llama-model.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/format]] _calls_
- [[nodes/ggml_backend_buft_alloc_buffer]] _calls_
- [[nodes/ggml_backend_dev_supports_op]] _calls_

## Used By

- [[nodes/select_buft]] _calls_
