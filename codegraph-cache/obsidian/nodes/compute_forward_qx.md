---
name: "compute_forward_qx"
type: "function"
file: "ggml/src/ggml-cpu/kleidiai/kleidiai.cpp"
community: "ggml"
---

# compute_forward_qx

**Type:** `function`  **File:** `ggml/src/ggml-cpu/kleidiai/kleidiai.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/kleidiai_is_weight_header_valid]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/kleidiai_get_block_args]] _calls_
- [[nodes/is_sme_family]] _calls_
- [[nodes/kleidiai_sme_thread_cap]] _calls_
- [[nodes/align_up]] _calls_
- [[nodes/lcm_size]] _calls_
- [[nodes/ggml_is_numa]] _calls_
- [[nodes/ceil_div_size]] _calls_
- [[nodes/round_down]] _calls_
- [[nodes/get_offset]] _calls_
- [[nodes/ggml_threadpool_chunk_set]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/ggml_threadpool_chunk_add]] _calls_

## Used By

- [[nodes/transpose_f32kxn_f16nxk]] _calls_
