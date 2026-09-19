---
name: "ggml_nbytes"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_nbytes

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_blck_size]] _calls_
- [[nodes/ggml_type_size]] _calls_

## Used By

- [[nodes/all_finite]] _calls_
- [[nodes/read_tensor_data]] _calls_
- [[nodes/copy_tensor]] _calls_
- [[nodes/merge_tensor]] _calls_
- [[nodes/clip_image_convert_f32_to_u8]] _calls_
- [[nodes/load_tensors]] _calls_
- [[nodes/clip_encode]] _calls_
- [[nodes/list_gen_state_slots]] _calls_
- [[nodes/print_usage]] _calls_
- [[nodes/save_tensor_for_layer]] _calls_
- [[nodes/concat_diff_tmp]] _calls_
- [[nodes/build_v_diff]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/zeros]] _calls_
- [[nodes/print_info]] _calls_
- [[nodes/write]] _calls_
- [[nodes/gguf_merge]] _calls_
- [[nodes/parse_k_cache_in_layer]] _calls_
- [[nodes/metadata]] _calls_
- [[nodes/if]] _calls_
- [[nodes/select_weight_buft]] _calls_
- [[nodes/hparams]] _calls_
- [[nodes/llama_sampler_logit_bias_backend_set_input]] _calls_
- [[nodes/llama_model_get_tok_embd]] _calls_
- [[nodes/llama_adapter_lora_init_impl]] _calls_
- [[nodes/ggml_gen_hadamard]] _calls_
- [[nodes/set_input_kq_mask_impl]] _calls_
- [[nodes/llama_model_quantize_impl]] _calls_
- [[nodes/ctx_type_to_graph_type]] _calls_
- [[nodes/needs_raw_logits]] _calls_
