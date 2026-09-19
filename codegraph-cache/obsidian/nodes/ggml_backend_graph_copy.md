---
name: "ggml_backend_graph_copy"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_graph_copy

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_hash_set_new]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_hash_set_free]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors]] _calls_
- [[nodes/ggml_backend_buffer_get_size]] _calls_
- [[nodes/graph_copy_init_tensor]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_
- [[nodes/ggml_hash_find]] _calls_

## Used By

- [[nodes/ggml_backend_compare_graph_backend]] _calls_
