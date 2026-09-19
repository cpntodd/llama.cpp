---
name: "ggml_threadpool_chunk_set"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_threadpool_chunk_set

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/atomic_store_explicit]] _calls_

## Used By

- [[nodes/__lasx_xvreplfr2vr_s]] _calls_
- [[nodes/forward_mul_mat]] _calls_
- [[nodes/ggml_wrap_index]] _calls_
- [[nodes/ggml_compute_forward_solve_tri]] _calls_
- [[nodes/compute_forward_f32]] _calls_
- [[nodes/compute_forward_qx]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/gemm_bloc_2x1]] _calls_
- [[nodes/forward_flash_attn_ext_f16]] _calls_
