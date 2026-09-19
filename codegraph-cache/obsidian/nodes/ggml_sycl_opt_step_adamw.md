---
name: "ggml_sycl_opt_step_adamw"
type: "function"
file: "ggml/src/ggml-sycl/opt-step.cpp"
community: "ggml"
---

# ggml_sycl_opt_step_adamw

**Type:** `function`  **File:** `ggml/src/ggml-sycl/opt-step.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/opt-step.hpp]] _imports_
- [[nodes/ggml_is_contiguous]] _calls_
- [[nodes/ggml_are_same_shape]] _calls_
- [[nodes/ggml_nelements]] _calls_
- [[nodes/parallel_for]] _calls_

## Used By

- [[nodes/ggml_sycl_argmax]] _calls_
