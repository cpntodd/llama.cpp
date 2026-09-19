---
name: "ggml_is_numa"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_is_numa

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/ggml_numa_init]] _calls_
- [[nodes/ggml_set_f32_nd]] _calls_
- [[nodes/incr_ptr_aligned]] _calls_
- [[nodes/set_numa_thread_affinity]] _calls_
- [[nodes/clear_numa_thread_affinity]] _calls_
- [[nodes/forward_mul_mat]] _calls_
- [[nodes/ggml_wrap_index]] _calls_
- [[nodes/ggml_compute_forward_solve_tri]] _calls_
- [[nodes/compute_forward_f32]] _calls_
- [[nodes/compute_forward_qx]] _calls_
