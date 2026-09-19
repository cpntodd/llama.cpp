---
name: "eval_perf"
type: "function"
file: "tests/test-backend-ops.cpp"
community: "ggml"
---

# eval_perf

**Type:** `function`  **File:** `tests/test-backend-ops.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_graph_overhead_custom]] _calls_
- [[nodes/use_weight_context]] _calls_
- [[nodes/ggml_init]] _calls_
- [[nodes/op_desc]] _calls_
- [[nodes/matches_filter]] _calls_
- [[nodes/ggml_backend_supports_op]] _calls_
- [[nodes/vars]] _calls_
- [[nodes/ggml_backend_alloc_ctx_tensors]] _calls_
- [[nodes/ggml_backend_buffer_set_usage]] _calls_
- [[nodes/buf]] _calls_
- [[nodes/initialize_tensors]] _calls_
- [[nodes/ggml_new_graph_custom]] _calls_
- [[nodes/ggml_build_forward_expand]] _calls_
- [[nodes/ggml_backend_graph_compute]] _calls_
- [[nodes/ggml_status_to_string]] _calls_
- [[nodes/ggml_backend_dev_type]] _calls_
- [[nodes/ggml_backend_get_device]] _calls_
- [[nodes/op_flops]] _calls_
- [[nodes/ggml_graph_size]] _calls_
- [[nodes/ggml_graph_n_nodes]] _calls_
- [[nodes/op_size]] _calls_
- [[nodes/ggml_graph_add_node]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_is_view_op]] _calls_
- [[nodes/ggml_graph_node]] _calls_
- [[nodes/ggml_time_us]] _calls_

## Used By

- [[nodes/run_fa_vec_slice]] _calls_
