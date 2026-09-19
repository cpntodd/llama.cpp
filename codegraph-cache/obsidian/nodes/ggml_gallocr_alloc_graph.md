---
name: "ggml_gallocr_alloc_graph"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "tests"
---

# ggml_gallocr_alloc_graph

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_gallocr_needs_realloc]] _calls_
- [[nodes/ggml_gallocr_reserve]] _calls_
- [[nodes/ggml_vbuffer_reset]] _calls_
- [[nodes/ggml_gallocr_init_tensor]] _calls_

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/allocate_graph]] _calls_
- [[nodes/test_multiple_buffer_types]] _calls_
- [[nodes/test_buffer_size_zero]] _calls_
- [[nodes/test_reallocation]] _calls_
- [[nodes/ggml_backend_sched_alloc_splits]] _calls_
