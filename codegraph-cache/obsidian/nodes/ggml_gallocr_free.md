---
name: "ggml_gallocr_free"
type: "function"
file: "ggml/src/ggml-alloc.c"
community: "ggml"
---

# ggml_gallocr_free

**Type:** `function`  **File:** `ggml/src/ggml-alloc.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_vbuffer_free]] _calls_
- [[nodes/ggml_dyn_tallocr_free]] _calls_
- [[nodes/ggml_hash_set_free]] _calls_

## Used By

- [[nodes/merge_tensor]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/ggml_backend_sched_free]] _calls_
