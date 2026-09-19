---
name: "llama_batch_add"
type: "function"
file: "examples/llama.swiftui/llama.cpp.swift/LibLlama.swift"
community: "tests"
---

# llama_batch_add

**Type:** `function`  **File:** `examples/llama.swiftui/llama.cpp.swift/LibLlama.swift`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/Int32]] _calls_
- [[nodes/llama_batch_init]] _calls_
- [[nodes/llama_sampler_chain_default_params]] _calls_
- [[nodes/llama_sampler_chain_add]] _calls_
- [[nodes/llama_sampler_free]] _calls_
- [[nodes/llama_batch_free]] _calls_
- [[nodes/llama_model_free]] _calls_
- [[nodes/llama_free]] _calls_
- [[nodes/llama_backend_free]] _calls_
- [[nodes/llama_backend_init]] _calls_
- [[nodes/llama_model_default_params]] _calls_
- [[nodes/llama_context_default_params]] _calls_

## Used By

- [[nodes/multiple_choice_score]] _calls_
- [[nodes/completion_init]] _calls_
- [[nodes/completion_loop]] _calls_
- [[nodes/bench]] _calls_
