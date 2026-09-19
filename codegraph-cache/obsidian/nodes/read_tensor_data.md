---
name: "read_tensor_data"
type: "function"
file: "tools/export-lora/export-lora.cpp"
community: "ggml"
---

# read_tensor_data

**Type:** `function`  **File:** `tools/export-lora/export-lora.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_
- [[nodes/gguf_find_tensor]] _calls_
- [[nodes/gguf_get_data_offset]] _calls_
- [[nodes/gguf_get_tensor_offset]] _calls_
- [[nodes/read]] _calls_
- [[nodes/file_input]] _calls_
- [[nodes/gguf_free]] _calls_
- [[nodes/ggml_free]] _calls_

## Used By

- [[nodes/copy_tensor]] _calls_
- [[nodes/merge_tensor]] _calls_
