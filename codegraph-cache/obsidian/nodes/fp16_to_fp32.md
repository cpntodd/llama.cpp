---
name: "fp16_to_fp32"
type: "function"
file: "ggml/src/ggml-et/et-kernels/src/math_fp.h"
community: "ggml"
---

# fp16_to_fp32

**Type:** `function`  **File:** `ggml/src/ggml-et/et-kernels/src/math_fp.h`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/read_kv_f32]] _calls_
- [[nodes/dot_qk]] _calls_
- [[nodes/get_mask_val]] _calls_
- [[nodes/entry_point]] _calls_
- [[nodes/dequantize_q8_0_block]] _calls_
- [[nodes/dequantize_q4_0_block]] _calls_
- [[nodes/dequantize_q4_K_block]] _calls_
- [[nodes/compute_block_dot_product_q4_0]] _calls_
- [[nodes/compute_block_dot_product_q8_0]] _calls_
- [[nodes/compute_block_dot_product_f16_naive]] _calls_
- [[nodes/compute_block_dot_product_f16]] _calls_
- [[nodes/copy_f16_row]] _calls_
- [[nodes/dequantize_q8_0_block_cache_aligned]] _calls_
- [[nodes/copy_q4_0_row_cache_aligned]] _calls_
- [[nodes/copy_q4_K_row_cache_aligned]] _calls_
- [[nodes/get_mask_val]] _calls_
- [[nodes/get_mask_val_from_base]] _calls_
- [[nodes/im2col_load_src_elem]] _calls_
