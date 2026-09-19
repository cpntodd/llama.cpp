---
name: "ggml_gallocr_allocate_node"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "ggml"
---

# ggml_gallocr_allocate_node

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_gallocr_hash_get]] _calls_
- [[nodes/ggml_gallocr_is_allocated]] _calls_
- [[nodes/ggml_impl_is_view]] _calls_
- [[nodes/ggml_op_can_inplace]] _calls_
- [[nodes/ggml_gallocr_is_own]] _calls_
- [[nodes/ggml_are_same_layout]] _calls_
- [[nodes/ggml_gallocr_free_extra_space]] _calls_
- [[nodes/ggml_backend_buft_get_alloc_size]] _calls_
- [[nodes/ggml_dyn_tallocr_alloc]] _calls_

## Used By

- [[nodes/ggml_gallocr_alloc_graph_impl]] _calls_
