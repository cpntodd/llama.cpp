---
name: "free_buffers"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "ggml"
---

# free_buffers

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_backend_buffer_free]] _calls_
- [[nodes/ggml_backend_buft_alloc_buffer]] _calls_
- [[nodes/realloc]] _calls_
- [[nodes/ggml_tallocr_new]] _calls_
- [[nodes/ggml_get_next_tensor]] _calls_
- [[nodes/ggml_tallocr_alloc]] _calls_
- [[nodes/ggml_backend_view_init]] _calls_
- [[nodes/ggml_get_no_alloc]] _calls_
- [[nodes/ggml_backend_buft_get_alignment]] _calls_
- [[nodes/ggml_backend_buft_get_max_size]] _calls_
- [[nodes/ggml_get_first_tensor]] _calls_
- [[nodes/ggml_backend_buft_get_alloc_size]] _calls_
- [[nodes/ggml_backend_multi_buffer_alloc_buffer]] _calls_
