---
name: "test_build_grammar_fails"
type: "function"
file: "tests/test-grammar-integration.cpp"
community: "common"
---

# test_build_grammar_fails

**Type:** `function`  **File:** `tests/test-grammar-integration.cpp`

**Community:** [[communities/common]]

## Depends On

- [[nodes/common_grammar_builder]] _imports_
- [[nodes/unicode_len_utf8]] _imports_
- [[nodes/llama_vocab]] _imports_
- [[nodes/common_json_item]] _imports_
- [[nodes/jinja]] _imports_
- [[nodes/build_grammar]] _calls_
- [[nodes/token]] _calls_

## Used By

- [[nodes/test_failure_left_recursion]] _calls_
