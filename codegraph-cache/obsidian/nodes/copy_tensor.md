---
name: "copy_tensor"
type: "function"
file: "tools/export-lora/export-lora.cpp"
community: "ggml"
---

# copy_tensor

**Type:** `function`  **File:** `tools/export-lora/export-lora.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_ne_string]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/read_tensor_data]] _calls_
- [[nodes/write]] _calls_
- [[nodes/zeros]] _calls_

## Used By

- [[nodes/run_merge]] _calls_
- [[nodes/ggml_backend_rpc_get_device_memory]] _calls_
- [[nodes/backends]] _calls_
