---
name: "eval_support"
type: "function"
file: "tests/test-backend-ops.cpp"
community: "ggml"
---

# eval_support

**Type:** `function`  **File:** `tests/test-backend-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_
- [[nodes/op_desc]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/ggml_backend_supports_op]] _calls_
- [[nodes/ggml_backend_get_device]] _calls_
- [[nodes/ggml_backend_dev_backend_reg]] _calls_
- [[nodes/vars]] _calls_

## Used By

- [[nodes/run_fa_vec_slice]] _calls_
