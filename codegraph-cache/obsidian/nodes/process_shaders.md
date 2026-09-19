---
name: "process_shaders"
type: "function"
file: "ggml/src/ggml-vulkan/vulkan-shaders/vulkan-shaders-gen.cpp"
community: "ggml"
---

# process_shaders

**Type:** `function`  **File:** `ggml/src/ggml-vulkan/vulkan-shaders/vulkan-shaders-gen.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/matmul_shaders]] _calls_
- [[nodes/string_to_spv]] _calls_
- [[nodes/to_uppercase]] _calls_
- [[nodes/string_ends_with]] _calls_
- [[nodes/string_starts_with]] _calls_
- [[nodes/is_legacy_quant]] _calls_
- [[nodes/is_k_quant]] _calls_
- [[nodes/string]] _calls_

## Used By

- [[nodes/main]] _calls_
