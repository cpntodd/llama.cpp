---
name: "init_tensor_tril"
type: "function"
file: "tests/test-backend-ops.cpp"
community: "ggml"
---

# init_tensor_tril

**Type:** `function`  **File:** `tests/test-backend-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/rd]] _calls_
- [[nodes/ggml_backend_tensor_set]] _calls_
- [[nodes/data]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/ggml_get_type_traits]] _calls_
- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/ggml_fp16_to_fp32]] _calls_
- [[nodes/ggml_bf16_to_fp32]] _calls_

## Used By

- [[nodes/init_mul_mat_id_tensors]] _calls_
