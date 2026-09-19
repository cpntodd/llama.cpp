---
name: "apir_decode_ggml_tensor"
type: "function"
file: "ggml/src/ggml-virtgpu/backend/shared/apir_cs_ggml.h"
community: "ggml"
---

# apir_decode_ggml_tensor

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/backend/shared/apir_cs_ggml.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/apir_decode_apir_rpc_tensor_inplace]] _calls_
- [[nodes/ggml_tensor_overhead]] _calls_
- [[nodes/ggml_init]] _calls_

## Used By

- [[nodes/backend_buffer_set_tensor]] _calls_
- [[nodes/backend_buffer_get_tensor]] _calls_
- [[nodes/backend_buffer_cpy_tensor]] _calls_
