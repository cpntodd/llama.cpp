---
name: "analyze_template"
type: "function"
file: "tests/test-chat-analysis.cpp"
community: "tests"
---

# analyze_template

**Type:** `function`  **File:** `tests/test-chat-analysis.cpp`

**Community:** [[communities/tests]]

## Depends On

- [[nodes/make_user_msg]] _calls_
- [[nodes/calculate_diff_split]] _calls_
- [[nodes/print_diff_split]] _calls_
- [[nodes/make_assistant_no_reasoning]] _calls_
- [[nodes/make_assistant_with_reasoning]] _calls_
- [[nodes/make_user_msg2]] _calls_
- [[nodes/make_assistant_no_tool]] _calls_
- [[nodes/make_assistant_one_tool]] _calls_
- [[nodes/make_user_msg2_continue]] _calls_
- [[nodes/make_assistant_two_tools]] _calls_
- [[nodes/make_assistant_one_tool_with_reasoning]] _calls_
- [[nodes/check_reasoning_variables]] _calls_

## Used By

- [[nodes/foreach_function]] _calls_
- [[nodes/mode_to_str]] _calls_
- [[nodes/common_chat_extra_context]] _calls_
- [[nodes/main]] _calls_
- [[nodes/debug_single_template]] _calls_
- [[nodes/test_nemotron_reasoning_detection]] _calls_
- [[nodes/test_nemotron_tool_format]] _calls_
- [[nodes/test_laguna_reasoning_detection]] _calls_
- [[nodes/test_laguna_tool_format]] _calls_
- [[nodes/test_laguna_stop_string]] _calls_
- [[nodes/test_laguna_s_reasoning_detection]] _calls_
- [[nodes/test_laguna_s_tool_format]] _calls_
- [[nodes/test_laguna_xs2_reasoning_detection]] _calls_
- [[nodes/test_laguna_xs2_tool_format]] _calls_
- [[nodes/test_cohere_reasoning_detection]] _calls_
- [[nodes/test_tool_format_cohere]] _calls_
- [[nodes/test_smollm3_reasoning_detection]] _calls_
- [[nodes/test_role_markers_all_templates]] _calls_
- [[nodes/test_bailing_v3_tool_format]] _calls_
