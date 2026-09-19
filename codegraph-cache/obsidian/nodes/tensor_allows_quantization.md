---
name: "tensor_allows_quantization"
type: "function"
file: "src/llama-quant.cpp"
community: "ggml"
---

# tensor_allows_quantization

**Type:** `function`  **File:** `src/llama-quant.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/tensors]] _calls_
- [[nodes/ggml_n_dims]] _calls_
- [[nodes/ggml_get_name]] _calls_
- [[nodes/size]] _calls_
- [[nodes/types]] _calls_
- [[nodes/LLM_TN]] _calls_

## Used By

- [[nodes/llama_tensor_get_type]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/llama_quant_free]] _calls_
