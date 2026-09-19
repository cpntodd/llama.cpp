---
name: "write_output_files"
type: "function"
file: "ggml/src/ggml-vulkan/vulkan-shaders/vulkan-shaders-gen.cpp"
community: "ggml"
---

# write_output_files

**Type:** `function`  **File:** `ggml/src/ggml-vulkan/vulkan-shaders/vulkan-shaders-gen.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/make_generic_stringstream]] _calls_
- [[nodes/basename]] _calls_
- [[nodes/read_binary_file]] _calls_
- [[nodes/string]] _calls_
- [[nodes/is_legacy_quant]] _calls_
- [[nodes/is_k_quant]] _calls_
- [[nodes/write_file_if_changed]] _calls_
- [[nodes/write_binary_file]] _calls_

## Used By

- [[nodes/main]] _calls_
