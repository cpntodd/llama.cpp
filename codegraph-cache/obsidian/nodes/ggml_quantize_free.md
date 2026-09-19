---
name: "ggml_quantize_free"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_quantize_free

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_critical_section_start]] _calls_
- [[nodes/iq2xs_free_impl]] _calls_
- [[nodes/iq3xs_free_impl]] _calls_
- [[nodes/ggml_critical_section_end]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/llama_backend_free]] _calls_
- [[nodes/main]] _calls_
