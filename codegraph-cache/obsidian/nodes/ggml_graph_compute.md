---
name: "ggml_graph_compute"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_graph_compute

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_cpu_init]] _calls_
- [[nodes/ggml_threadpool_params_default]] _calls_
- [[nodes/atomic_store_explicit]] _calls_
- [[nodes/ggml_thread_apply_priority]] _calls_
- [[nodes/ggml_thread_cpumask_is_valid]] _calls_
- [[nodes/ggml_thread_apply_affinity]] _calls_
- [[nodes/ggml_graph_compute_thread]] _calls_
- [[nodes/clear_numa_thread_affinity]] _calls_
- [[nodes/ggml_threadpool_free]] _calls_

## Used By

- [[nodes/ggml_graph_compute_helper]] _calls_
- [[nodes/graph_compute]] _calls_
- [[nodes/test_barrier]] _calls_
- [[nodes/test_active]] _calls_
- [[nodes/test_multi_graph]] _calls_
- [[nodes/ggml_graph_compute_with_ctx]] _calls_
- [[nodes/ggml_backend_cpu_graph_plan_compute]] _calls_
- [[nodes/ggml_backend_cpu_graph_compute]] _calls_
