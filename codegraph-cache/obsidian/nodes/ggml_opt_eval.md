---
name: "ggml_opt_eval"
type: "function"
file: "ggml/src/ggml-opt.cpp"
community: "ggml"
---

# ggml_opt_eval

**Type:** `function`  **File:** `ggml/src/ggml-opt.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_data_f32]] _calls_
- [[nodes/ggml_backend_sched_graph_compute]] _calls_
- [[nodes/ggml_is_scalar]] _calls_
- [[nodes/ggml_backend_tensor_get]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/ggml_opt_static_graphs]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/ggml_opt_alloc]] _calls_
- [[nodes/ggml_opt_dataset_get_batch]] _calls_
- [[nodes/ggml_opt_result_loss]] _calls_
- [[nodes/ggml_opt_result_accuracy]] _calls_
- [[nodes/ggml_time_init]] _calls_
- [[nodes/ggml_opt_init]] _calls_
- [[nodes/ggml_opt_dataset_shuffle]] _calls_
- [[nodes/ggml_opt_result_init]] _calls_
- [[nodes/ggml_opt_result_reset]] _calls_
- [[nodes/ggml_opt_free]] _calls_
- [[nodes/ggml_opt_result_free]] _calls_

## Used By

- [[nodes/llama_set_param]] _calls_
- [[nodes/print_ok]] _calls_
- [[nodes/if]] _calls_
