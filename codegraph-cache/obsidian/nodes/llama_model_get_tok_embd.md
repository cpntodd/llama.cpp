---
name: "llama_model_get_tok_embd"
type: "function"
file: "src/llama-model.cpp"
community: "ggml"
---

# llama_model_get_tok_embd

**Type:** `function`  **File:** `src/llama-model.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/size]] _calls_
- [[nodes/ggml_get_type_traits]] _calls_
- [[nodes/ggml_fp16_to_fp32_row]] _calls_
- [[nodes/ggml_bf16_to_fp32_row]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_type_name]] _calls_

## Used By

- [[nodes/ensure_cache]] _calls_
- [[nodes/pockettts_pack]] _calls_
