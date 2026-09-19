---
name: "warmup"
type: "function"
file: "tools/mtmd/clip.cpp"
community: "ggml"
---

# warmup

**Type:** `function`  **File:** `tools/mtmd/clip.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/get_dummy_batch]] _calls_
- [[nodes/reserve_compute_meta]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/backend]] _calls_
- [[nodes/ggml_op_name]] _calls_

## Used By

- [[nodes/clip_init]] _calls_
- [[nodes/clip_encode]] _calls_
- [[nodes/time_cell_median]] _calls_
