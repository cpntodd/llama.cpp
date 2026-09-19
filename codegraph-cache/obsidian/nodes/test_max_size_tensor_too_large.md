---
name: "test_max_size_tensor_too_large"
type: "function"
file: "tests/test-alloc.cpp"
community: "tests"
---

# test_max_size_tensor_too_large

**Type:** `function`  **File:** `tests/test-alloc.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/dummy_backend_init]] _calls_
- [[nodes/make_context]] _calls_
- [[nodes/assign_names]] _calls_
- [[nodes/allocate_graph]] _calls_
- [[nodes/check_all_allocated]] _calls_
- [[nodes/check_no_overlap]] _calls_
- [[nodes/check_max_size]] _calls_
- [[nodes/allocated_total]] _calls_
