---
name: "ggml_vec_dot_f32"
type: "function"
file: "ggml/src/ggml-cpu/vec.cpp"
community: "ggml"
---

# ggml_vec_dot_f32

**Type:** `function`  **File:** `ggml/src/ggml-cpu/vec.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_cpu_get_sve_cnt]] _calls_

## Used By

- [[nodes/ggml_arm_arch_features_type]] _imports_
- [[nodes/constexpr]] _imports_
- [[nodes/ggml_compute_forward_tri]] _calls_
- [[nodes/rotate_pairs]] _calls_
- [[nodes/ggml_wrap_around]] _calls_
- [[nodes/ggml_wrap_index]] _calls_
- [[nodes/ggml_compute_forward_solve_tri]] _calls_
- [[nodes/ggml_compute_forward_fwht]] _calls_
- [[nodes/ggml_sve_sum_f32x2]] _calls_
- [[nodes/ggml_vec_norm_f32]] _calls_
- [[nodes/ggml_threadpool]] _imports_
