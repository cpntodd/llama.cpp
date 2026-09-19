---
name: "same_tensor_data"
type: "function"
file: "tests/test-gguf.cpp"
community: "ggml"
---

# same_tensor_data

**Type:** `function`  **File:** `tests/test-gguf.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/string]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/data]] _calls_
- [[nodes/ggml_backend_dev_init]] _calls_
- [[nodes/get_random_gguf_context]] _calls_
- [[nodes/gguf_write_to_file_ptr]] _calls_
- [[nodes/gguf_get_version]] _calls_
- [[nodes/gguf_get_n_kv]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/all_kv_in_other]] _calls_
- [[nodes/all_tensors_in_other]] _calls_
- [[nodes/ggml_backend_buffer_free]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/gguf_free]] _calls_
- [[nodes/ggml_backend_free]] _calls_
- [[nodes/gguf_set_kv]] _calls_
