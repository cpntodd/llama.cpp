---
name: "A"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# A

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/matmul]] _calls_
- [[nodes/mnpack]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/load_lo]] _calls_
- [[nodes/load_hi]] _calls_
- [[nodes/unhalf]] _calls_
- [[nodes/hsum]] _calls_

## Used By

- [[nodes/ggml_zendnn_make_matmul_params]] _calls_
- [[nodes/ggml_compute_forward_solve_tri_f32]] _calls_
- [[nodes/BLOC_POS]] _calls_
- [[nodes/params]] _calls_
- [[nodes/ggml_sycl_op_conv_3d]] _calls_
- [[nodes/ldmatrix]] _calls_
- [[nodes/ggml_cann_solve_tri]] _calls_
- [[nodes/ggml_et_op_solve_tri]] _calls_
- [[nodes/entry_point]] _calls_
- [[nodes/entry_point]] _calls_
- [[nodes/entry_point]] _calls_
