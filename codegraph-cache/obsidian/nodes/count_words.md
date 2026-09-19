---
name: "count_words"
type: "function"
file: "tools/mtmd/mtmd-helper-gen.cpp"
community: "tools"
---

# count_words

**Type:** `function`  **File:** `tools/mtmd/mtmd-helper-gen.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/encode_speaker]] _calls_
- [[nodes/mtmd_support_audio]] _calls_
- [[nodes/mtmd_input_chunks_size]] _calls_
- [[nodes/mtmd_input_chunk_get_type]] _calls_
- [[nodes/mtmd_encode_chunk]] _calls_
- [[nodes/llama_model_n_embd_inp]] _calls_
- [[nodes/mtmd_input_chunk_get_n_tokens]] _calls_
- [[nodes/assign]] _calls_
- [[nodes/mtmd_input_chunks_free]] _calls_
- [[nodes/flush_gen_wav]] _calls_
- [[nodes/mtmd_gen_inp_default]] _calls_
- [[nodes/mtmd_gen_audio_process]] _calls_

## Used By

- [[nodes/prepare_text]] _calls_
