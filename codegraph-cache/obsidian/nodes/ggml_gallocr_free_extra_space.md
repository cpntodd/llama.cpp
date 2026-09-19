---
name: "ggml_gallocr_free_extra_space"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "ggml"
---

# ggml_gallocr_free_extra_space

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_gallocr_hash_get]] _calls_
- [[nodes/ggml_backend_buft_get_alloc_size]] _calls_
- [[nodes/aligned_offset]] _calls_
- [[nodes/ggml_dyn_tallocr_free_bytes]] _calls_

## Used By

- [[nodes/ggml_gallocr_allocate_node]] _calls_
