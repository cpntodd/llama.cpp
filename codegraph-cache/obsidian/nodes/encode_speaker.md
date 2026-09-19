---
name: "encode_speaker"
type: "function"
file: "tools/mtmd/mtmd-helper-gen.cpp"
community: "tools"
---

# encode_speaker

**Type:** `function`  **File:** `tools/mtmd/mtmd-helper-gen.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/mtmd_support_audio]] _calls_
- [[nodes/mtmd_input_chunks_size]] _calls_
- [[nodes/mtmd_input_chunk_get_type]] _calls_
- [[nodes/mtmd_encode_chunk]] _calls_
- [[nodes/llama_model_n_embd_inp]] _calls_
- [[nodes/mtmd_input_chunk_get_n_tokens]] _calls_
- [[nodes/assign]] _calls_
- [[nodes/mtmd_input_chunks_free]] _calls_

## Used By

- [[nodes/write_wav16]] _calls_
- [[nodes/pockettts_pack]] _calls_
- [[nodes/count_words]] _calls_
