---
name: "gguf_hash"
type: "function"
file: "examples/gguf-hash/gguf-hash.cpp"
community: "ggml"
---

# gguf_hash

**Type:** `function`  **File:** `examples/gguf-hash/gguf-hash.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/sha256_init]] _calls_
- [[nodes/gguf_get_n_tensors]] _calls_
- [[nodes/ggml_get_tensor]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/manifest_verify]] _calls_
- [[nodes/sha256_update]] _calls_
- [[nodes/sha256_final]] _calls_
- [[nodes/generate_uuidv5]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/gguf_free]] _calls_

## Used By

- [[nodes/main]] _calls_
