---
name: "accept_prompt"
type: "function"
file: "tests/test-backend-sampler.cpp"
community: "tests"
---

# accept_prompt

**Type:** `function`  **File:** `tests/test-backend-sampler.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/llama_vocab_bos]] _calls_
- [[nodes/llama_sampler_accept]] _calls_
- [[nodes/tokens]] _calls_
- [[nodes/data]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/decode]] _calls_
- [[nodes/idx_for_seq]] _calls_
- [[nodes/llama_sampler_apply]] _calls_
- [[nodes/llama_sampler_chain_add]] _calls_
- [[nodes/llama_sampler_chain_default_params]] _calls_
- [[nodes/llama_synchronize]] _calls_
- [[nodes/llama_get_sampled_logits_count_ith]] _calls_
- [[nodes/llama_get_sampled_candidates_count_ith]] _calls_
- [[nodes/assign]] _calls_

## Used By

- [[nodes/find_backend_logit]] _calls_
- [[nodes/test_penalty_parameter_values]] _calls_
