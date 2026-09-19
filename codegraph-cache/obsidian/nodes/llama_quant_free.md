---
name: "llama_quant_free"
type: "function"
file: "src/llama-quant.cpp"
community: "ggml"
---

# llama_quant_free

**Type:** `function`  **File:** `src/llama-quant.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/llama_model_default_params]] _calls_
- [[nodes/llm_arch_from_string]] _calls_
- [[nodes/tensor_allows_quantization]] _calls_
- [[nodes/metadata]] _calls_
- [[nodes/ggml_get_name]] _calls_
- [[nodes/init_quantize_state_counters]] _calls_
- [[nodes/llama_ftype_get_default_type]] _calls_
- [[nodes/llama_tensor_get_type]] _calls_

## Used By

- [[nodes/run_generate]] _calls_
- [[nodes/run_remote_tests]] _calls_
