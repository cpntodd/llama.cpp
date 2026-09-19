---
name: "llama_grammar_validate"
type: "function"
file: "tests/test-gbnf-validator.cpp"
community: "common"
---

# llama_grammar_validate

**Type:** `function`  **File:** `tests/test-gbnf-validator.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/unicode_len_utf8]] _imports_
- [[nodes/llama_vocab]] _imports_
- [[nodes/jinja]] _imports_
- [[nodes/unicode_cpts_from_utf8]] _calls_
- [[nodes/llama_grammar_accept]] _calls_
- [[nodes/unicode_cpt_to_utf8]] _calls_

## Used By

- [[nodes/main]] _calls_
