---
name: "ggml_cpu_init"
type: "function"
file: "ggml/src/ggml-cpu/ggml-cpu.c"
community: "ggml"
---

# ggml_cpu_init

**Type:** `function`  **File:** `ggml/src/ggml-cpu/ggml-cpu.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_init]] _calls_
- [[nodes/ggml_free]] _calls_
- [[nodes/ggml_critical_section_start]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/ggml_gelu_f32]] _calls_
- [[nodes/ggml_gelu_quick_f32]] _calls_
- [[nodes/ggml_ue4m3_to_fp32]] _calls_
- [[nodes/getenv]] _calls_
- [[nodes/ggml_init_arm_arch_features]] _calls_
- [[nodes/ggml_init_riscv_arch_features]] _calls_
- [[nodes/ggml_critical_section_end]] _calls_

## Used By

- [[nodes/main]] _calls_
- [[nodes/main]] _calls_
- [[nodes/ggml_threadpool_resume]] _calls_
- [[nodes/ggml_graph_compute]] _calls_
- [[nodes/ggml_backend_cpu_init]] _calls_
- [[nodes/ggml_backend_cpu_reg_get_device]] _calls_
- [[nodes/ggml_backend_cpu_reg]] _calls_
