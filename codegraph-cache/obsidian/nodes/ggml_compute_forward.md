---
name: "ggml_compute_forward"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_compute_forward

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_empty]] _calls_
- [[nodes/ggml_cpu_extra_compute_forward]] _calls_
- [[nodes/ggml_compute_forward_sub]] _calls_
- [[nodes/ggml_compute_forward_mul]] _calls_
- [[nodes/ggml_compute_forward_div]] _calls_
- [[nodes/ggml_compute_forward_sqr]] _calls_
- [[nodes/ggml_compute_forward_sqrt]] _calls_
- [[nodes/ggml_compute_forward_log]] _calls_
- [[nodes/ggml_compute_forward_sin]] _calls_
- [[nodes/ggml_compute_forward_cos]] _calls_
- [[nodes/ggml_compute_forward_tri]] _calls_
- [[nodes/ggml_compute_forward_fill]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_compute_forward_solve_tri]] _calls_
- [[nodes/ggml_compute_forward_opt_step_sgd]] _calls_

## Used By

- [[nodes/ggml_graph_compute_thread]] _calls_
