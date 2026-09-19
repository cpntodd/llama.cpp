---
name: "llama_sampler_sample"
type: "function"
file: "src/llama-sampler.cpp"
community: "tests"
---

# llama_sampler_sample

**Type:** `function`  **File:** `src/llama-sampler.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/llama_get_sampled_token_ith]] _calls_
- [[nodes/llama_sampler_accept]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_get_sampled_probs_count_ith]] _calls_
- [[nodes/size]] _calls_
- [[nodes/llama_sampler_apply]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/completion_loop]] _calls_
- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/generate_tokens]] _calls_
- [[nodes/test_backend_top_k_sampling]] _calls_
- [[nodes/test_backend_temp_sampling]] _calls_
- [[nodes/test_backend_min_p_sampling]] _calls_
- [[nodes/test_backend_top_p_sampling]] _calls_
- [[nodes/test_backend_dist_sampling_and_cpu]] _calls_
- [[nodes/test_backend_set_sampler]] _calls_
- [[nodes/test_backend_cpu_mixed_batch]] _calls_
- [[nodes/test_backend_multi_sequence_multi_output_dist]] _calls_
- [[nodes/test_backend_multi_output_dist_transaction]] _calls_
- [[nodes/test_backend_multi_output_sampling_chain]] _calls_
- [[nodes/test_backend_multi_output_cpu_suffix]] _calls_
