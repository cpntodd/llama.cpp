---
name: "hellaswag_score"
type: "function"
file: "tools/perplexity/perplexity.cpp"
community: "src"
---

# hellaswag_score

**Type:** `function`  **File:** `tools/perplexity/perplexity.cpp`

**Community:** [[communities/src]]

## Depends On

- [[nodes/llama_vocab_type]] _calls_
- [[nodes/llama_n_ctx]] _calls_
- [[nodes/llama_vocab_n_tokens]] _calls_
- [[nodes/llama_n_seq_max]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/common_batch_clear]] _calls_
- [[nodes/llama_memory_clear]] _calls_
- [[nodes/llama_get_memory]] _calls_
- [[nodes/decode_helper]] _calls_
- [[nodes/double]] _calls_
- [[nodes/sqrt]] _calls_
- [[nodes/llama_batch_free]] _calls_
- [[nodes/stream]] _calls_
- [[nodes/back]] _calls_
- [[nodes/move]] _calls_

## Used By

- [[nodes/llama_perplexity]] _calls_
