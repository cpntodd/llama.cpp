---
name: "ggml_vec_soft_max_f32"
type: "function"
file: "ggml/src/ggml-cpu/vec.cpp"
community: "ggml"
---

# ggml_vec_soft_max_f32

**Type:** `function`  **File:** `ggml/src/ggml-cpu/vec.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_v_expf]] _calls_
- [[nodes/vaddvq_f32]] _calls_
- [[nodes/ggml_v_expf_m2]] _calls_

## Used By

- [[nodes/ggml_compute_forward_tri]] _calls_
- [[nodes/ggml_wrap_index]] _calls_
- [[nodes/ggml_dsv4_hc_comb_norm_rows]] _calls_
- [[nodes/ggml_sve_sum_f32x2]] _calls_
