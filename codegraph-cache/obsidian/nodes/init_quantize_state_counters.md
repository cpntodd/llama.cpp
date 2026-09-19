---
name: "init_quantize_state_counters"
type: "function"
file: "src/llama-quant.cpp"
community: "ggml"
---

# init_quantize_state_counters

**Type:** `function`  **File:** `src/llama-quant.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/tensor_get_category]] _calls_
- [[nodes/category_is_attn_v]] _calls_

## Used By

- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/llama_quant_free]] _calls_
