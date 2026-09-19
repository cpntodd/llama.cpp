---
name: "ggml_backend_tensor_set"
type: "function"
file: "ggml/src/ggml-backend.cpp"
community: "ggml"
---

# ggml_backend_tensor_set

**Type:** `function`  **File:** `ggml/src/ggml-backend.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_nbytes]] _calls_

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/load_tensors]] _calls_
- [[nodes/clip_encode]] _calls_
- [[nodes/list_gen_state_slots]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/fa_init_uniform]] _calls_
- [[nodes/fa_init_kq_mask]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/llama_sampler_dist_backend_set_input]] _calls_
- [[nodes/llama_sampler_penalties_backend_set_input]] _calls_
- [[nodes/llama_sampler_logit_bias_backend_set_input]] _calls_
- [[nodes/params]] _calls_
- [[nodes/llama_adapter_lora_init_impl]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/dsv4_set_i64]] _calls_
- [[nodes/dsv4_set_i32]] _calls_
- [[nodes/needs_raw_logits]] _calls_
- [[nodes/llama_set_param]] _calls_
- [[nodes/init_tensor_uniform]] _calls_
- [[nodes/if]] _calls_
- [[nodes/init_tensor_kq_mask]] _calls_
- [[nodes/init_tensor_tril]] _calls_
- [[nodes/print_test_result_locked]] _calls_
- [[nodes/eval_grad]] _calls_
- [[nodes/init_set_rows_row_ids]] _calls_
- [[nodes/tensor_range]] _calls_
- [[nodes/n_cache_rows]] _calls_
- [[nodes/blk]] _calls_
- [[nodes/init_mul_mat_id_tensors]] _calls_
- [[nodes/is_non_contiguous]] _calls_
