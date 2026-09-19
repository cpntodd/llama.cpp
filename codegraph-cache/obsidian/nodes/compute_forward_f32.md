---
name: "compute_forward_f32"
type: "function"
file: "ggml/src/ggml-cpu/kleidiai/kleidiai.cpp"
community: "ggml"
---

# compute_forward_f32

**Type:** `function`  **File:** `ggml/src/ggml-cpu/kleidiai/kleidiai.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/kleidiai_is_weight_header_valid]] _calls_
- [[nodes/ggml_is_numa]] _calls_
- [[nodes/round_down]] _calls_
- [[nodes/get_offset]] _calls_
- [[nodes/ggml_threadpool_chunk_set]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/kleidiai_chunk_cols]] _calls_
- [[nodes/ggml_threadpool_chunk_add]] _calls_

## Used By

- [[nodes/transpose_f32kxn_f16nxk]] _calls_
