---
name: "ggml_opt_alloc"
type: "function"
file: "ggml/src/ggml-opt.cpp"
community: "ggml"
---

# ggml_opt_alloc

**Type:** `function`  **File:** `ggml/src/ggml-opt.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_graph_reset]] _calls_
- [[nodes/ggml_opt_build]] _calls_
- [[nodes/ggml_backend_sched_reset]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_backend_sched_alloc_graph]] _calls_

## Used By

- [[nodes/llama_set_param]] _calls_
- [[nodes/print_ok]] _calls_
- [[nodes/if]] _calls_
- [[nodes/ggml_opt_eval]] _calls_
