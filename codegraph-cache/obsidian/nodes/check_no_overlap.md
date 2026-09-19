---
name: "check_no_overlap"
type: "function"
file: "tests/test-alloc.cpp"
community: "tests"
---

# check_no_overlap

**Type:** `function`  **File:** `tests/test-alloc.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_graph_n_nodes]] _calls_
- [[nodes/ggml_graph_node]] _calls_
- [[nodes/memory_overlap]] _calls_
- [[nodes/can_reuse_memory]] _calls_

## Used By

- [[nodes/test_max_size_too_many_tensors]] _calls_
- [[nodes/test_max_size_tensor_too_large]] _calls_
- [[nodes/test_tensor_larger_than_max_size]] _calls_
- [[nodes/test_not_enough_chunks]] _calls_
- [[nodes/test_fill_leftover_space]] _calls_
- [[nodes/test_view_inplace]] _calls_
- [[nodes/test_reuse_and_free]] _calls_
- [[nodes/test_merge_free_block]] _calls_
- [[nodes/test_prefer_already_allocated_memory]] _calls_
- [[nodes/test_multiple_buffer_types]] _calls_
