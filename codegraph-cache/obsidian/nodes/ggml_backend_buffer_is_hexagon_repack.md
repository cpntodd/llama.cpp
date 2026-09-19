---
name: "ggml_backend_buffer_is_hexagon_repack"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# ggml_backend_buffer_is_hexagon_repack

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_buffer_is_hexagon]] _calls_
- [[nodes/ggml_hexagon_opqueue]] _calls_
- [[nodes/ggml_hexagon_shared_buffer]] _calls_
- [[nodes/push]] _calls_
- [[nodes/pop]] _calls_
- [[nodes/empty]] _calls_
- [[nodes/finalize_ranges]] _calls_
- [[nodes/fit_op]] _calls_
- [[nodes/add_op]] _calls_
- [[nodes/flush]] _calls_

## Used By

- [[nodes/same_shape]] _calls_
- [[nodes/add_tensor]] _calls_
- [[nodes/ggml_hexagon_supported_mul_mat]] _calls_
- [[nodes/ggml_hexagon_supported_mul_mat_id]] _calls_
