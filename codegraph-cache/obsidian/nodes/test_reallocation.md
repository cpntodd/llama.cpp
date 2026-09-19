---
name: "test_reallocation"
type: "function"
file: "tests/test-alloc.cpp"
community: "tests"
---

# test_reallocation

**Type:** `function`  **File:** `tests/test-alloc.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/dummy_backend_init]] _calls_
- [[nodes/make_context]] _calls_
- [[nodes/assign_names]] _calls_
- [[nodes/allocate_graph]] _calls_
- [[nodes/check_all_allocated]] _calls_
- [[nodes/allocated_total]] _calls_
- [[nodes/ggml_set_output]] _calls_
- [[nodes/ggml_build_forward_expand]] _calls_
- [[nodes/ggml_gallocr_alloc_graph]] _calls_
