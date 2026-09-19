---
name: "is_mergeable_mul_mat"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# is_mergeable_mul_mat

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_is_quantized]] _calls_
- [[nodes/mm_is_hmx_eligible]] _calls_

## Used By

- [[nodes/is_mergeable_mul_mat_pair]] _calls_
- [[nodes/is_qkv_mergeable]] _calls_
- [[nodes/try_fuse_node]] _calls_
