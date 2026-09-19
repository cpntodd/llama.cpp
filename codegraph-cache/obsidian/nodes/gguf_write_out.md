---
name: "gguf_write_out"
type: "function"
file: "ggml/src/gguf.cpp"
community: "ggml"
---

# gguf_write_out

**Type:** `function`  **File:** `ggml/src/gguf.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_get_n_kv]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/write]] _calls_
- [[nodes/write_tensor_meta]] _calls_
- [[nodes/pad]] _calls_

## Used By

- [[nodes/gguf_write_to_buf]] _calls_
- [[nodes/gguf_write_to_file_ptr]] _calls_
