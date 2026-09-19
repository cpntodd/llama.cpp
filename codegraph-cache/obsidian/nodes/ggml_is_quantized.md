---
name: "ggml_is_quantized"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_is_quantized

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/fa_init_uniform]] _calls_
- [[nodes/llama_model_get_tok_embd]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/set_input_kq_mask_impl]] _calls_
- [[nodes/category_is_attn_v]] _calls_
- [[nodes/llama_tensor_get_type]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/llama_context_default_params]] _calls_
- [[nodes/llm_graph_context]] _calls_
- [[nodes/common_debug_cb_eval]] _calls_
- [[nodes/if]] _calls_
- [[nodes/init_tensor_tril]] _calls_
- [[nodes/type_a]] _calls_
- [[nodes/build_context]] _calls_
- [[nodes/ggml_get_tensor]] _calls_
- [[nodes/ggml_threadpool_resume]] _calls_
- [[nodes/ggml_backend_cpu_device_supports_op]] _calls_
- [[nodes/ggml_backend_cpu_kleidiai_buffer_type_get_alloc_size]] _calls_
- [[nodes/ggml_backend_rpc_buffer_init_tensor]] _calls_
- [[nodes/ggml_backend_rpc_buffer_type_get_alloc_size]] _calls_
- [[nodes/if]] _calls_
- [[nodes/ggml_backend_buffer_is_sycl]] _calls_
- [[nodes/ggml_backend_sycl_buffer_type_get_alloc_size]] _calls_
- [[nodes/next_power_of_2]] _calls_
- [[nodes/can_use_mul_mat_vec_q]] _calls_
- [[nodes/ggml_sycl_get_best_fattn_kernel]] _calls_
- [[nodes/ggml_webgpu_pad]] _calls_
- [[nodes/ggml_backend_webgpu_device_supports_op]] _calls_
