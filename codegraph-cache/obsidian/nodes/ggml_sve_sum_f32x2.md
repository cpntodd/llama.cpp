---
name: "ggml_sve_sum_f32x2"
type: "function"
file: "ggml/src/ggml-cpu/vec.h"
community: "ggml"
---

# ggml_sve_sum_f32x2

**Type:** `function`  **File:** `ggml/src/ggml-cpu/vec.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_up32]] _imports_
- [[nodes/ggml_lookup_fp16_to_fp32]] _imports_
- [[nodes/ggml_graph_next_uid]] _imports_
- [[nodes/ggml_arm_arch_features_type]] _imports_
- [[nodes/ggml_vec_dot_f32]] _calls_
- [[nodes/ggml_vec_dot_bf16]] _calls_
- [[nodes/ggml_vec_dot_f16]] _calls_
- [[nodes/ggml_vec_silu_f32]] _calls_
- [[nodes/ggml_vec_cvar_f32]] _calls_
- [[nodes/ggml_vec_soft_max_f32]] _calls_
- [[nodes/ggml_vec_log_soft_max_f32]] _calls_

## Used By

- [[nodes/ggml_vec_dot_f16]] _calls_
- [[nodes/ggml_vec_dot_f16_unroll]] _calls_
