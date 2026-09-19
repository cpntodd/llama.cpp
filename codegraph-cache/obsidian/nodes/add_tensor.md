---
name: "add_tensor"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# add_tensor

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/same_shape]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/add_buffer]] _calls_
- [[nodes/ggml_backend_buffer_is_hexagon_repack]] _calls_
- [[nodes/ggml_hexagon_is_repack_type]] _calls_
- [[nodes/hex_round_up]] _calls_
- [[nodes/ggml_row_size]] _calls_
- [[nodes/ggml_backend_buffer_get_usage]] _calls_

## Used By

- [[nodes/add_op]] _calls_
