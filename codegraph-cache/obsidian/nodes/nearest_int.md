---
name: "nearest_int"
type: "function"
file: "ggml/src/ggml-cpu/repack.cpp"
community: "ggml"
---

# nearest_int

**Type:** `function`  **File:** `ggml/src/ggml-cpu/repack.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml-common.h]] _imports_
- [[nodes/ggml-backend-impl.h]] _imports_
- [[nodes/ggml_up32]] _imports_
- [[nodes/ggml_arm_arch_features_type]] _imports_
- [[nodes/ggml_compute_params]] _imports_
- [[nodes/ggml_lookup_fp16_to_fp32]] _imports_
- [[nodes/ggml]] _imports_
- [[nodes/arch-fallback.h]] _imports_
- [[nodes/ggml_quantize_mat_q8_0_4x4]] _calls_

## Used By

- [[nodes/ggml_backend_cpu_is_extra_buffer_type]] _imports_
- [[nodes/ggml_quantize_mat_q8_K_4x1_generic]] _calls_
- [[nodes/ggml_quantize_mat_q8_K_4x4_generic]] _calls_
- [[nodes/ggml_quantize_mat_q8_K_4x8_generic]] _calls_
- [[nodes/decode_q_Kx8_6bit_scales]] _imports_
- [[nodes/ggml_quantize_mat_q8_0_4x8]] _imports_
- [[nodes/QK_0]] _imports_
- [[nodes/ggml_threadpool]] _imports_
