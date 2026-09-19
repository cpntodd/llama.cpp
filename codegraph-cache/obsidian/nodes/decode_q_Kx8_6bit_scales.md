---
name: "decode_q_Kx8_6bit_scales"
type: "function"
file: "ggml/src/ggml-cpu/arch/arm/repack.cpp"
community: "ggml"
---

# decode_q_Kx8_6bit_scales

**Type:** `function`  **File:** `ggml/src/ggml-cpu/arch/arm/repack.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml-common.h]] _imports_
- [[nodes/ggml-backend-impl.h]] _imports_
- [[nodes/ggml_up32]] _imports_
- [[nodes/ggml_arm_arch_features_type]] _imports_
- [[nodes/ggml_compute_params]] _imports_
- [[nodes/ggml_lookup_fp16_to_fp32]] _imports_
- [[nodes/ggml]] _imports_
- [[nodes/nearest_int]] _imports_

## Used By

- [[nodes/ggml_gemv_q4_K_8x4_q8_K]] _calls_
- [[nodes/ggml_gemm_q4_K_8x4_q8_K]] _calls_
