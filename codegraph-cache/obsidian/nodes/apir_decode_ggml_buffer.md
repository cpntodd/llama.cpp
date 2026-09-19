---
name: "apir_decode_ggml_buffer"
type: "function"
file: "ggml/src/ggml-virtgpu/backend/shared/apir_cs_ggml.h"
community: "ggml"
---

# apir_decode_ggml_buffer

**Type:** `function`  **File:** `ggml/src/ggml-virtgpu/backend/shared/apir_cs_ggml.h`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/apir_decoder_read]] _calls_
- [[nodes/apir_decoder_set_fatal]] _calls_

## Used By

- [[nodes/backend_buffer_get_base]] _calls_
- [[nodes/backend_buffer_set_tensor]] _calls_
- [[nodes/backend_buffer_get_tensor]] _calls_
- [[nodes/backend_buffer_cpy_tensor]] _calls_
- [[nodes/backend_buffer_clear]] _calls_
- [[nodes/backend_buffer_free_buffer]] _calls_
- [[nodes/apir_decode_ggml_tensor_inplace]] _calls_
