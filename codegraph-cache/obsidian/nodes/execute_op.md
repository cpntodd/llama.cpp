---
name: "execute_op"
type: "function"
file: "ggml/src/ggml-hexagon/htp/main.c"
community: "ggml"
---

# execute_op

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/main.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/op_matmul]] _calls_
- [[nodes/op_matmul_id]] _calls_
- [[nodes/op_matmul_qkv]] _calls_
- [[nodes/op_matmul_ffn]] _calls_
- [[nodes/op_binary]] _calls_
- [[nodes/op_unary]] _calls_
- [[nodes/op_activations]] _calls_
- [[nodes/op_softmax]] _calls_
- [[nodes/op_rope]] _calls_
- [[nodes/op_flash_attn_ext]] _calls_
- [[nodes/op_set_rows]] _calls_
- [[nodes/op_get_rows]] _calls_
- [[nodes/op_sum_rows]] _calls_
- [[nodes/op_cpy]] _calls_
- [[nodes/op_repeat]] _calls_
- [[nodes/op_argsort]] _calls_
- [[nodes/op_ssm_conv]] _calls_
- [[nodes/op_cumsum]] _calls_
- [[nodes/op_fill]] _calls_
- [[nodes/op_diag]] _calls_
- [[nodes/op_solve_tri]] _calls_
- [[nodes/op_pad]] _calls_
- [[nodes/op_im2col]] _calls_
- [[nodes/op_concat]] _calls_
- [[nodes/op_gated_delta_net]] _calls_

## Used By

- [[nodes/proc_op_req]] _calls_
