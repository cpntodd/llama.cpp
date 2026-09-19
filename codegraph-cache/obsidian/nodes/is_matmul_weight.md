---
name: "is_matmul_weight"
type: "function"
file: "ggml/src/ggml-cann/aclnn_ops.h"
community: "ggml"
---

# is_matmul_weight

**Type:** `function`  **File:** `ggml/src/ggml-cann/aclnn_ops.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/acl_tensor.h]] _imports_
- [[nodes/KeyValuePair]] _imports_
- [[nodes/aclnn_cos]] _imports_
- [[nodes/aclnn_exp]] _imports_
- [[nodes/aclnn_sin]] _imports_
- [[nodes/ggml_get_name]] _calls_
- [[nodes/binary_op]] _calls_
- [[nodes/unary_op]] _calls_

## Used By

- [[nodes/ggml_cann_mat_mul_fp]] _calls_
- [[nodes/weight_format_to_nz]] _calls_
- [[nodes/ggml_backend_cann_buffer_type_get_alignment]] _calls_
- [[nodes/ggml_backend_cann_free]] _calls_
