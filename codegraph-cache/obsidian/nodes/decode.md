---
name: "decode"
type: "function"
file: "tests/test-backend-sampler.cpp"
community: "tests"
---

# decode

**Type:** `function`  **File:** `tests/test-backend-sampler.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/llama_batch_init]] _calls_
- [[nodes/llama_vocab_bos]] _calls_
- [[nodes/data]] _calls_
- [[nodes/llama_batch_free]] _calls_

## Used By

- [[nodes/test_template_cpp]] _calls_
- [[nodes/test_backend_greedy_sampling]] _calls_
- [[nodes/test_backend_top_k_sampling]] _calls_
- [[nodes/test_backend_temp_sampling]] _calls_
- [[nodes/test_backend_temp_ext_sampling]] _calls_
- [[nodes/test_backend_min_p_sampling]] _calls_
- [[nodes/test_backend_top_p_sampling]] _calls_
- [[nodes/test_backend_multi_sequence_sampling]] _calls_
- [[nodes/test_backend_dist_sampling]] _calls_
- [[nodes/test_backend_dist_sampling_and_cpu]] _calls_
- [[nodes/test_backend_logit_bias_sampling]] _calls_
- [[nodes/accept_prompt]] _calls_
- [[nodes/test_backend_mixed_sampling]] _calls_
- [[nodes/test_backend_set_sampler]] _calls_
- [[nodes/test_backend_cpu_mixed_batch]] _calls_
- [[nodes/test_backend_multi_output_dist_transaction]] _calls_
