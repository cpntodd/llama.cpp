---
name: "process_token"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# process_token

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/push_back]] _calls_
- [[nodes/validate_utf8]] _calls_
- [[nodes/size]] _calls_
- [[nodes/find_stopping_strings]] _calls_
- [[nodes/llama_vocab_is_eog]] _calls_
- [[nodes/add_token]] _calls_
- [[nodes/send_partial_response]] _calls_
- [[nodes/n_tokens]] _calls_
- [[nodes/has_budget]] _calls_
- [[nodes/n_remaining]] _calls_

## Used By

- [[nodes/pre_decode]] _calls_
- [[nodes/post_decode]] _calls_
