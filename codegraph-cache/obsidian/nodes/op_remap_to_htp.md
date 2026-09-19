---
name: "op_remap_to_htp"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# op_remap_to_htp

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_get_glu_op]] _calls_
- [[nodes/ggml_op_desc]] _calls_
- [[nodes/ggml_op_is_empty]] _calls_
- [[nodes/ggml_is_empty]] _calls_

## Used By

- [[nodes/ggml_backend_hexagon_graph_compute]] _calls_
