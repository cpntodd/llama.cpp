---
name: "check_max_size"
type: "function"
file: "tests/test-alloc.cpp"
community: "tests"
---

# check_max_size

**Type:** `function`  **File:** `tests/test-alloc.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/ggml_backend_buffer_get_type]] _calls_
- [[nodes/ggml_backend_buft_get_max_size]] _calls_
- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/test_max_size_too_many_tensors]] _calls_
- [[nodes/test_max_size_tensor_too_large]] _calls_
- [[nodes/test_fill_leftover_space]] _calls_
- [[nodes/test_view_inplace]] _calls_
- [[nodes/test_reuse_and_free]] _calls_
- [[nodes/test_merge_free_block]] _calls_
- [[nodes/test_multiple_buffer_types]] _calls_
