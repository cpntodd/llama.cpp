---
name: "ggml_cann_set_device"
type: "function"
file: "ggml/src/ggml-cann/ggml-cann.cpp"
community: "ggml"
---

# ggml_cann_set_device

**Type:** `function`  **File:** `ggml/src/ggml-cann/ggml-cann.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/getenv]] _calls_

## Used By

- [[nodes/ggml_cann_init]] _calls_
- [[nodes/weight_format_to_nz]] _calls_
- [[nodes/ggml_backend_cann_buffer_memset_tensor]] _calls_
- [[nodes/ggml_backend_cann_buffer_clear]] _calls_
- [[nodes/ggml_backend_cann_buffer_type_alloc_buffer]] _calls_
- [[nodes/ggml_backend_cann_free]] _calls_
- [[nodes/ggml_backend_cann_synchronize]] _calls_
- [[nodes/ggml_backend_cann_graph_compute]] _calls_
- [[nodes/ggml_backend_cann_device_event_new]] _calls_
- [[nodes/ggml_backend_cann_reg]] _calls_
- [[nodes/ggml_backend_cann_init]] _calls_
- [[nodes/ggml_backend_cann_get_device_description]] _calls_
- [[nodes/ggml_backend_cann_get_device_memory]] _calls_
