---
name: "rollback_allocation_locked"
type: "function"
file: "ggml/src/ggml-cpu/spacemit/spine_mem_pool.cpp"
community: "ggml"
---

# rollback_allocation_locked

**Type:** `function`  **File:** `ggml/src/ggml-cpu/spacemit/spine_mem_pool.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/find_chunk_locked]] _calls_
- [[nodes/insert_free_block_locked]] _calls_
- [[nodes/maybe_release_empty_chunk_locked]] _calls_

## Used By

- [[nodes/align_up_uintptr]] _calls_
