---
name: "gemm_bloc_2x1"
type: "function"
file: "ggml/src/ggml-cpu/llamafile/sgemm.cpp"
community: "ggml"
---

# gemm_bloc_2x1

**Type:** `function`  **File:** `ggml/src/ggml-cpu/llamafile/sgemm.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/madd]] _calls_
- [[nodes/hsum]] _calls_
- [[nodes/gemm_bloc]] _calls_
- [[nodes/constexpr]] _calls_
- [[nodes/gemm_bloc_4x6]] _calls_
- [[nodes/gemm_bloc_4x5]] _calls_
- [[nodes/gemm_bloc_4x4]] _calls_
- [[nodes/gemm_bloc_4x3]] _calls_
- [[nodes/gemm_bloc_4x2]] _calls_
- [[nodes/gemm_bloc_4x1]] _calls_
- [[nodes/gemm_bloc_2x2]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/ggml_threadpool_chunk_set]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/BLOC_POS]] _calls_
- [[nodes/ggml_threadpool_chunk_add]] _calls_
