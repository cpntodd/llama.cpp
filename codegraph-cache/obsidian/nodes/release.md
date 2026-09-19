---
name: "release"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# release

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/is_processing]] _calls_
- [[nodes/n_tokens]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/prompt_clear]] _calls_
- [[nodes/reset]] _calls_

## Used By

- [[nodes/reset]] _calls_
- [[nodes/launch_slots_with_parent_task]] _calls_
- [[nodes/process_single_task]] _calls_
- [[nodes/iterate]] _calls_
- [[nodes/abort_all_slots]] _calls_
- [[nodes/pre_decode]] _calls_
- [[nodes/decode]] _calls_
- [[nodes/post_decode]] _calls_
- [[nodes/mtmd_input_chunk_save]] _calls_
- [[nodes/llama_prepare_model_devices]] _calls_
- [[nodes/path_str]] _calls_
- [[nodes/ggml_hexagon_is_hmx_weight_type]] _calls_
- [[nodes/ggml_hexagon_measure_max_vmem]] _calls_
- [[nodes/dmstart]] _calls_
- [[nodes/dmlink]] _calls_
