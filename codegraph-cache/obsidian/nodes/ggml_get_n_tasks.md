---
name: "ggml_get_n_tasks"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_get_n_tasks

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_empty]] _calls_
- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/ggml_nrows]] _calls_
- [[nodes/ggml_op_name]] _calls_
- [[nodes/ggml_graph_compute_secondary_thread]] _calls_

## Used By

- [[nodes/ggml_threadpool_resume]] _calls_
