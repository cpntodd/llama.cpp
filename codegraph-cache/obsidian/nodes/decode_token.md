---
name: "decode_token"
type: "function"
file: "tests/test-backend-sampler.cpp"
community: "tests"
---

# decode_token

**Type:** `function`  **File:** `tests/test-backend-sampler.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/llama_batch_init]] _calls_
- [[nodes/llama_batch_free]] _calls_
- [[nodes/update_batch_info]] _calls_

## Used By

- [[nodes/test_backend_greedy_sampling]] _calls_
- [[nodes/test_backend_min_p_sampling]] _calls_
- [[nodes/test_backend_top_p_sampling]] _calls_
- [[nodes/test_backend_cpu_mixed_batch]] _calls_
