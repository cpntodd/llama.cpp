---
name: "handcrafted_check_tensor_data"
type: "function"
file: "tests/test-gguf.cpp"
community: "ggml"
---

# handcrafted_check_tensor_data

**Type:** `function`  **File:** `tests/test-gguf.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_row_size]] _calls_
- [[nodes/to_string]] _calls_
- [[nodes/gguf_get_tensor_offset]] _calls_
- [[nodes/gguf_find_tensor]] _calls_
- [[nodes/data]] _calls_
- [[nodes/gguf_get_data_offset]] _calls_
- [[nodes/handcrafted_file_type_name]] _calls_
- [[nodes/expect_context_not_null]] _calls_
- [[nodes/bool]] _calls_
- [[nodes/handcrafted_check_header]] _calls_
- [[nodes/handcrafted_check_kv]] _calls_
- [[nodes/handcrafted_check_tensors]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/gguf_free]] _calls_
