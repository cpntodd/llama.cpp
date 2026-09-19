---
name: "llama_cast"
type: "function"
file: "src/llama-impl.h"
community: "ggml"
---

# llama_cast

**Type:** `function`  **File:** `src/llama-impl.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_fp16_to_fp32]] _calls_
- [[nodes/ggml_fp32_to_fp16]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/time_meas]] _calls_
- [[nodes/replace_all]] _calls_
- [[nodes/format]] _calls_
- [[nodes/llama_format_tensor_shape]] _calls_
- [[nodes/gguf_kv_to_str]] _calls_
