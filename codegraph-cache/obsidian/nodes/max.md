---
name: "max"
type: "function"
file: "ggml/src/ggml-sycl/dpct/helper.hpp"
community: "ggml"
---

# max

**Type:** `function`  **File:** `ggml/src/ggml-sycl/dpct/helper.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/has]] _calls_
- [[nodes/get_current_device_id]] _calls_
- [[nodes/get_offset]] _calls_
- [[nodes/host_buffer]] _calls_
- [[nodes/_buf]] _calls_
- [[nodes/get_ptr]] _calls_
- [[nodes/get_size]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/get_pitch]] _calls_
- [[nodes/get_y]] _calls_
- [[nodes/gemm]] _calls_
- [[nodes/get_value]] _calls_

## Used By

- [[nodes/ggml_backend_meta_buffer_type_get_alignment]] _calls_
- [[nodes/ggml_backend_meta_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_backend_meta_buffer_type_alloc_buffer]] _calls_
- [[nodes/ggml_backend_meta_graph_compute]] _calls_
- [[nodes/ggml_backend_sched_split_graph]] _calls_
- [[nodes/rope_yarn_ramp]] _calls_
- [[nodes/downsample_sycl_global_range]] _calls_
- [[nodes/check_usm_system]] _calls_
- [[nodes/t2f32]] _calls_
- [[nodes/ggml_sycl_flash_attn_ext_mkl]] _calls_
- [[nodes/to_dt]] _calls_
- [[nodes/get_dequantize_V]] _calls_
- [[nodes/cpy_blck_f32_q2_0]] _calls_
- [[nodes/clamp_u8]] _calls_
- [[nodes/clamp_i8]] _calls_
- [[nodes/make_qx_quants_sycl]] _calls_
- [[nodes/make_q3_quants_sycl]] _calls_
- [[nodes/cpy_blck_f32_q4_1]] _calls_
- [[nodes/ggml_sycl_op_rms_norm_back]] _calls_
- [[nodes/get_device_backend_and_type]] _calls_
- [[nodes/min]] _calls_
