---
name: "run_merge"
type: "function"
file: "tools/export-lora/export-lora.cpp"
community: "ggml"
---

# run_merge

**Type:** `function`  **File:** `tools/export-lora/export-lora.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/gguf_set_kv]] _calls_
- [[nodes/gguf_set_val_u32]] _calls_
- [[nodes/ggml_dup_tensor]] _calls_
- [[nodes/ggml_set_name]] _calls_
- [[nodes/gguf_get_meta_size]] _calls_
- [[nodes/zeros]] _calls_
- [[nodes/merge_tensor]] _calls_
- [[nodes/copy_tensor]] _calls_
- [[nodes/gguf_get_meta_data]] _calls_
- [[nodes/write]] _calls_

## Used By

- [[nodes/main]] _calls_
