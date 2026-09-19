---
name: "ggml_backend_sched_split_graph"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_sched_split_graph

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_free]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_graph_next_uid]] _calls_
- [[nodes/ggml_backend_sched_backend_id_from_cur]] _calls_
- [[nodes/backends]] _calls_
- [[nodes/ggml_is_view_op]] _calls_
- [[nodes/ggml_backend_sched_set_if_supported]] _calls_
- [[nodes/ggml_backend_supports_op]] _calls_
- [[nodes/ggml_backend_sched_buffer_supported]] _calls_
- [[nodes/realloc]] _calls_
- [[nodes/ggml_format_name]] _calls_
- [[nodes/ggml_set_input]] _calls_
- [[nodes/ggml_set_output]] _calls_
- [[nodes/ggml_backend_sched_graph_inputs_grow]] _calls_
- [[nodes/ggml_backend_sched_split_inputs_grow]] _calls_
- [[nodes/ggml_backend_sched_print_assignments]] _calls_
- [[nodes/max]] _calls_
- [[nodes/ggml_graph_view]] _calls_
- [[nodes/ggml_backend_graph_optimize]] _calls_

## Used By

- [[nodes/needs_raw_logits]] _calls_
- [[nodes/ggml_backend_sched_reserve_size]] _calls_
- [[nodes/ggml_backend_sched_reserve]] _calls_
- [[nodes/ggml_backend_sched_alloc_graph]] _calls_
