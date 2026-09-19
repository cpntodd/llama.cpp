---
name: "handcrafted_check_tensors"
type: "function"
file: "tests/test-gguf.cpp"
community: "ggml"
---

# handcrafted_check_tensors

**Type:** `function`  **File:** `tests/test-gguf.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_find_key]] _calls_
- [[nodes/gguf_get_val_u32]] _calls_
- [[nodes/to_string]] _calls_
- [[nodes/gguf_find_tensor]] _calls_
- [[nodes/string]] _calls_
- [[nodes/gguf_get_tensor_type]] _calls_
- [[nodes/gguf_get_tensor_offset]] _calls_
- [[nodes/ggml_row_size]] _calls_

## Used By

- [[nodes/handcrafted_check_tensor_data]] _calls_
