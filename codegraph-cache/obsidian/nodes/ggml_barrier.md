---
name: "ggml_barrier"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_barrier

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_load_explicit]] _calls_
- [[nodes/atomic_fetch_add_explicit]] _calls_
- [[nodes/atomic_store_explicit]] _calls_
- [[nodes/ggml_thread_cpu_relax]] _calls_
- [[nodes/atomic_thread_fence]] _calls_

## Used By

- [[nodes/ggml_set_f32_nd]] _calls_
- [[nodes/incr_ptr_aligned]] _calls_
- [[nodes/ggml_graph_compute_thread]] _calls_
- [[nodes/__lasx_xvreplfr2vr_s]] _calls_
- [[nodes/forward_mul_mat]] _calls_
- [[nodes/forward_mul_mat_id]] _calls_
- [[nodes/ggml_compute_forward_tri]] _calls_
- [[nodes/rotate_pairs]] _calls_
- [[nodes/ggml_wrap_around]] _calls_
- [[nodes/ggml_wrap_index]] _calls_
- [[nodes/ggml_compute_forward_solve_tri]] _calls_
- [[nodes/ggml_dsv4_hc_comb_norm_rows]] _calls_
- [[nodes/compute_forward_f32]] _calls_
- [[nodes/compute_forward_fp16]] _calls_
- [[nodes/compute_forward_qx]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/gemm_bloc_2x1]] _calls_
- [[nodes/ggml_backend_amx_mul_mat]] _calls_
- [[nodes/forward_mul_mat]] _calls_
- [[nodes/forward_mul_mat_id]] _calls_
- [[nodes/forward_flash_attn_ext_f16]] _calls_
