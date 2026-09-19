---
name: "BLOC_POS"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# BLOC_POS

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/tinyBLAS]] _calls_
- [[nodes/tinyBLAS_RVV]] _calls_
- [[nodes/params]] _calls_
- [[nodes/A]] _calls_
- [[nodes/matmul]] _calls_
- [[nodes/mnpack]] _calls_
- [[nodes/constexpr]] _calls_
- [[nodes/tinyBLAS_Q0_ARM]] _calls_
- [[nodes/tinyBLAS_Q0_AVX]] _calls_
- [[nodes/outer_product]] _calls_
- [[nodes/tinyBLAS_HP16_PPC]] _calls_
- [[nodes/matmul_tiled]] _calls_
- [[nodes/tinyBLAS_Q0_PPC]] _calls_
- [[nodes/tinyBLAS_PPC]] _calls_
- [[nodes/save_acc]] _calls_
- [[nodes/add_save_acc]] _calls_

## Used By

- [[nodes/gemm]] _calls_
- [[nodes/gemm_bloc_2x1]] _calls_
