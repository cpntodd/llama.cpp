---
name: "ggml_backend_is_metal"
type: "function"
file: "ggml/src/ggml-metal/ggml-metal.cpp"
community: "ggml"
---

# ggml_backend_is_metal

**Type:** `function`  **File:** `ggml/src/ggml-metal/ggml-metal.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_guid_matches]] _calls_
- [[nodes/ggml_backend_metal_guid]] _calls_

## Used By

- [[nodes/ggml_backend_metal_cpy_tensor_async]] _calls_
- [[nodes/ggml_backend_metal_set_n_cb]] _calls_
- [[nodes/ggml_backend_metal_set_abort_callback]] _calls_
- [[nodes/ggml_backend_metal_supports_family]] _calls_
- [[nodes/ggml_backend_metal_capture_next_compute]] _calls_
