---
name: "ggml_graph_dump_dot"
type: "function"
file: "ggml/src/ggml.c"
community: "ggml"
---

# ggml_graph_dump_dot

**Type:** `function`  **File:** `ggml/src/ggml.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_fopen]] _calls_
- [[nodes/ggml_graph_get_grad]] _calls_
- [[nodes/ggml_graph_get_parent]] _calls_
- [[nodes/ggml_graph_find]] _calls_
- [[nodes/ggml_type_name]] _calls_
- [[nodes/ggml_is_matrix]] _calls_
- [[nodes/ggml_op_symbol]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/ggml_get_i32_1d]] _calls_
- [[nodes/ggml_get_f32_1d]] _calls_
- [[nodes/ggml_graph_dump_dot_node_edge]] _calls_
- [[nodes/ggml_graph_dump_dot_leaf_edge]] _calls_

## Used By

- [[nodes/print_debug_tensor]] _calls_
- [[nodes/needs_raw_logits]] _calls_
