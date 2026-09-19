---
name: "pockettts_pack"
type: "function"
file: "tools/mtmd/mtmd-helper-gen.cpp"
community: "tools"
---

# pockettts_pack

**Type:** `function`  **File:** `tools/mtmd/mtmd-helper-gen.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/ensure_cache]] _calls_
- [[nodes/encode_speaker]] _calls_
- [[nodes/prepare_text]] _calls_
- [[nodes/string]] _calls_
- [[nodes/push_embd_row]] _calls_
- [[nodes/arm_chunk_budget]] _calls_
- [[nodes/decode_embd_batch]] _calls_
- [[nodes/get_view]] _calls_
- [[nodes/mtmd_gen_inp_default]] _calls_
- [[nodes/mtmd_gen_audio_process]] _calls_
- [[nodes/finish_chunk]] _calls_
- [[nodes/flush_gen_wav]] _calls_
- [[nodes/assign]] _calls_
- [[nodes/write_wav16]] _calls_
- [[nodes/find_special_token]] _calls_
- [[nodes/llama_model_get_tok_embd]] _calls_
- [[nodes/mtmd_gen_audio_get_info]] _calls_
- [[nodes/qwen3tts_gen_audio_pipeline]] _calls_
- [[nodes/pockettts_gen_audio_pipeline]] _calls_
- [[nodes/mtmd_helper_gen_audio]] _calls_
