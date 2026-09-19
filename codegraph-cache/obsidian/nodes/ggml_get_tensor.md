---
name: "ggml_get_tensor"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_get_tensor

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_dup_tensor]] _calls_
- [[nodes/ggml_can_repeat]] _calls_
- [[nodes/ggml_can_repeat_rows]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_is_scalar]] _calls_
- [[nodes/ggml_is_padded_1d]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_set_op_params]] _calls_
- [[nodes/ggml_is_matrix]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_is_empty]] _calls_
- [[nodes/ggml_set_op_params_i32]] _calls_
- [[nodes/ggml_set_op_params_f32]] _calls_
- [[nodes/ggml_compute_softplus_f32]] _calls_
- [[nodes/ggml_is_contiguous_1]] _calls_

## Used By

- [[nodes/clip_image_convert_f32_to_u8]] _calls_
- [[nodes/load_tensors]] _calls_
- [[nodes/zeros]] _calls_
- [[nodes/print_info]] _calls_
- [[nodes/write]] _calls_
- [[nodes/gguf_merge]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/common_control_vector_load_one]] _calls_
- [[nodes/gguf_ex_read_1]] _calls_
- [[nodes/gguf_hash]] _calls_
- [[nodes/is_non_contiguous]] _calls_
