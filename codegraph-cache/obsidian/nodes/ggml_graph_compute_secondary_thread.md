---
name: "ggml_graph_compute_secondary_thread"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_graph_compute_secondary_thread

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_thread_apply_priority]] _calls_
- [[nodes/ggml_thread_cpumask_is_valid]] _calls_
- [[nodes/ggml_thread_apply_affinity]] _calls_
- [[nodes/ggml_graph_compute_check_for_work]] _calls_
- [[nodes/ggml_graph_compute_thread]] _calls_
- [[nodes/atomic_load_explicit]] _calls_
- [[nodes/atomic_store_explicit]] _calls_
- [[nodes/ggml_threadpool_resume_locked]] _calls_
- [[nodes/ggml_aligned_malloc]] _calls_
- [[nodes/ggml_thread_cpumask_next]] _calls_

## Used By

- [[nodes/ggml_get_n_tasks]] _calls_
