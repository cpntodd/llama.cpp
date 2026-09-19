---
name: "ggml_dyn_tallocr_alloc"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "ggml"
---

# ggml_dyn_tallocr_alloc

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/aligned_offset]] _calls_
- [[nodes/block]] _calls_
- [[nodes/ggml_dyn_tallocr_new_chunk]] _calls_
- [[nodes/ggml_dyn_tallocr_remove_block]] _calls_
- [[nodes/add_allocated_tensor]] _calls_
- [[nodes/ggml_buffer_address_less]] _calls_
- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/ggml_gallocr_allocate_node]] _calls_
