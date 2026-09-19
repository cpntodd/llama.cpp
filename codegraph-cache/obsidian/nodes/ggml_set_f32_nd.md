---
name: "ggml_set_f32_nd"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_set_f32_nd

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_row_size]] _calls_
- [[nodes/ggml_get_op_params_i32]] _calls_
- [[nodes/ggml_compute_forward_fwht]] _calls_
- [[nodes/ggml_type_size]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_cpu_fp16_to_fp32]] _calls_
- [[nodes/atomic_store_explicit]] _calls_
- [[nodes/ggml_barrier]] _calls_
- [[nodes/ggml_is_numa]] _calls_
- [[nodes/atomic_fetch_add_explicit]] _calls_

## Used By

- [[nodes/save_tensor_for_layer]] _calls_
- [[nodes/build_v_diff]] _calls_
- [[nodes/convert_weights_ak_to_gg]] _calls_
- [[nodes/ggml_set_f32_1d]] _calls_
