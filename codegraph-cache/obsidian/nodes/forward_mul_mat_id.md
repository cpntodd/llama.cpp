---
name: "forward_mul_mat_id"
type: "function"
file: "ggml/src/ggml-cpu/spacemit/ime.cpp"
community: "ggml"
---

# forward_mul_mat_id

**Type:** `function`  **File:** `ggml/src/ggml-cpu/spacemit/ime.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/q8_blk_size]] _calls_
- [[nodes/q8_hp_blk_size]] _calls_
- [[nodes/q8k_blk_size]] _calls_
- [[nodes/div_round_up]] _calls_
- [[nodes/quantize_a_row_i8]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/memcpy1d]] _calls_
- [[nodes/spine_barrier_wait]] _calls_
- [[nodes/repack]] _calls_
- [[nodes/ggml_type_name]] _calls_

## Used By

- [[nodes/block_type_has_zp]] _calls_
