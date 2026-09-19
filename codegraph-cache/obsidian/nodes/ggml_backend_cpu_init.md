---
name: "ggml_backend_cpu_init"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.cpp"
community: "ggml"
---

# ggml_backend_cpu_init

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_cpu_init]] _calls_
- [[nodes/ggml_backend_cpu_guid]] _calls_
- [[nodes/ggml_backend_reg_dev_get]] _calls_
- [[nodes/ggml_backend_cpu_reg]] _calls_

## Used By

- [[nodes/base_model]] _calls_
- [[nodes/print_debug_tensor]] _calls_
- [[nodes/ggml_backend_cpu_device_init_backend]] _calls_
- [[nodes/ggml_et_cpu_compare_init_pre]] _calls_
