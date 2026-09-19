---
name: "process_mtmd_chunk"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# process_mtmd_chunk

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/common_speculative_process]] _calls_
- [[nodes/llama_n_batch]] _calls_
- [[nodes/mtmd_input_chunk_get_n_tokens]] _calls_
- [[nodes/reset]] _calls_
- [[nodes/mtmd_batch_add_chunk]] _calls_
- [[nodes/mtmd_batch_encode]] _calls_
- [[nodes/mtmd_helper_log_set]] _calls_
- [[nodes/destroy]] _calls_

## Used By

- [[nodes/pre_decode]] _calls_
