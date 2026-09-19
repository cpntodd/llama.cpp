---
name: "ggml_backend_buft_is_host"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_buft_is_host

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/load_tensors]] _calls_
- [[nodes/common_memory_breakdown_print]] _calls_
- [[nodes/ggml_backend_meta_buffer_type_is_host]] _calls_
- [[nodes/ggml_backend_buffer_is_host]] _calls_
- [[nodes/ggml_backend_zendnn_device_supports_buft]] _calls_
- [[nodes/ggml_backend_cpu_device_supports_buft]] _calls_
- [[nodes/ggml_backend_cpu_repack_buffer_type_get_alignment]] _calls_
- [[nodes/ggml_backend_cpu_kleidiai_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_backend_amx_buffer_type_get_alignment]] _calls_
- [[nodes/ggml_backend_cpu_riscv64_spacemit_nbytes]] _calls_
- [[nodes/ggml_backend_blas_device_supports_buft]] _calls_
- [[nodes/ggml_backend_openvino_device_supports_buft]] _calls_
