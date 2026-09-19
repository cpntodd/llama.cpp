---
name: "ggml_backend_is_cpu"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.cpp"
community: "ggml"
---

# ggml_backend_is_cpu

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_guid_matches]] _calls_
- [[nodes/ggml_backend_cpu_guid]] _calls_

## Used By

- [[nodes/print_debug_tensor]] _calls_
- [[nodes/ggml_backend_cpu_set_n_threads]] _calls_
- [[nodes/ggml_backend_cpu_set_threadpool]] _calls_
- [[nodes/ggml_backend_cpu_set_abort_callback]] _calls_
- [[nodes/ggml_backend_cpu_set_use_ref]] _calls_
