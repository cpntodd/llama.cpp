---
name: "calc_block_size"
type: "function"
file: "ggml/src/ggml-hexagon/htp/binary-ops.c"
community: "ggml"
---

# calc_block_size

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/binary-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/fastdiv]] _calls_
- [[nodes/hvx_div_scalar_f16_aa]] _calls_

## Used By

- [[nodes/binary_job_scalar]] _calls_
- [[nodes/binary_job_vector_same_shape]] _calls_
- [[nodes/binary_job_vector_row_broadcast]] _calls_
- [[nodes/binary_job_vector_complex]] _calls_
- [[nodes/binary_job_element_repeat]] _calls_
- [[nodes/binary_job_add_id]] _calls_
