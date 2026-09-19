---
name: "q8k_blk_size"
type: "function"
file: "ggml/src/ggml-cpu/spacemit/rvv_kernels.h"
community: "ggml"
---

# q8k_blk_size

**Type:** `function`  **File:** `ggml/src/ggml-cpu/spacemit/rvv_kernels.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/memcpy1d]] _calls_
- [[nodes/memcpy2d]] _calls_
- [[nodes/forward_rms_norm_f32]] _calls_
- [[nodes/forward_norm_f32]] _calls_
- [[nodes/forward_cont_with_permute]] _calls_
- [[nodes/forward_cpy_with_permute]] _calls_
- [[nodes/forward_get_rows]] _calls_
- [[nodes/forward_concat]] _calls_
- [[nodes/forward_binary]] _calls_
- [[nodes/forward_sum_rows]] _calls_
- [[nodes/forward_repeat_nrows]] _calls_
- [[nodes/forward_repeat_dim1]] _calls_
- [[nodes/quantize_a_row_i8_hp]] _calls_
- [[nodes/quantize_a_4row_i8_hp]] _calls_
- [[nodes/quantize_a_row_i8k]] _calls_
- [[nodes/quantize_a_4row_i8k]] _calls_

## Used By

- [[nodes/block_type_has_zp]] _calls_
- [[nodes/forward_mul_mat]] _calls_
- [[nodes/forward_mul_mat_id]] _calls_
- [[nodes/quantize_a_nrow_i8k_ref]] _calls_
- [[nodes/quantize_a_row_i8k]] _calls_
- [[nodes/quantize_a_4row_i8k]] _calls_
