---
name: "ggml_set_zero"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_set_zero

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_empty]] _calls_
- [[nodes/ggml_backend_tensor_memset]] _calls_
- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/llama_set_param]] _calls_
- [[nodes/ggml_graph_reset]] _calls_
