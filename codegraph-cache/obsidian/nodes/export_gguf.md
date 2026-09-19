---
name: "export_gguf"
type: "function"
file: "tools/cvector-generator/cvector-generator.cpp"
community: "ggml"
---

# export_gguf

**Type:** `function`  **File:** `tools/cvector-generator/cvector-generator.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_set_val_str]] _calls_
- [[nodes/gguf_set_val_i32]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/gguf_write_to_file]] _calls_
- [[nodes/gguf_free]] _calls_

## Used By

- [[nodes/main]] _calls_
