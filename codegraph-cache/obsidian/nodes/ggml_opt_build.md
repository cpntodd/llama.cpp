---
name: "ggml_opt_build"
type: "function"
file: "ggml/src/ggml-opt.cpp"
community: "ggml"
---

# ggml_opt_build

**Type:** `function`  **File:** `ggml/src/ggml-opt.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_set_input]] _calls_
- [[nodes/ggml_set_output]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/ggml_backend_buffer_free]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_dup_tensor]] _calls_
- [[nodes/ggml_set_loss]] _calls_
- [[nodes/ggml_build_forward_expand]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/ggml_graph_dup]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors]] _calls_
- [[nodes/ggml_backend_sched_get_backend]] _calls_
- [[nodes/ggml_graph_reset]] _calls_
- [[nodes/ggml_format_name]] _calls_
- [[nodes/ggml_graph_get_grad]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors_from_buft]] _calls_
- [[nodes/ggml_backend_cpu_buffer_type]] _calls_

## Used By

- [[nodes/ggml_opt_init]] _calls_
- [[nodes/ggml_opt_alloc]] _calls_
