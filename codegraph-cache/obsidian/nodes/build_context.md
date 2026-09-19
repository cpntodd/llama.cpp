---
name: "build_context"
type: "function"
file: "tests/test-kv-mean-center.cpp"
community: "tests"
---

# build_context

**Type:** `function`  **File:** `tests/test-kv-mean-center.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/llama_context_default_params]] _calls_
- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/llama_batch_free]] _calls_

## Used By

- [[nodes/test_regression_safety]] _calls_
- [[nodes/test_q4_0_gate]] _calls_
- [[nodes/test_softmax_invariance]] _calls_
