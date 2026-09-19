---
name: "ggml_can_fuse"
type: "function"
file: "ggml/src/ggml-impl.h"
community: "ggml"
---

# ggml_can_fuse

**Type:** `function`  **File:** `ggml/src/ggml-impl.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_can_fuse_ext]] _calls_

## Used By

- [[nodes/ggml_threadpool_resume]] _calls_
- [[nodes/ggml_sycl_op_unary_mul_fused]] _calls_
- [[nodes/ggml_webgpu_can_fuse_rms_norm_mul]] _calls_
- [[nodes/ggml_backend_cann_synchronize]] _calls_
- [[nodes/ggml_graph_optimize]] _calls_
- [[nodes/ggml_et_can_fuse]] _calls_
- [[nodes/try_fuse_node]] _calls_
- [[nodes/ggml_backend_hexagon_graph_optimize]] _calls_
