---
name: "bitonic_sort_generic_hvx"
type: "function"
file: "ggml/src/ggml-hexagon/htp/argsort-ops.c"
community: "ggml"
---

# bitonic_sort_generic_hvx

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/htp/argsort-ops.c`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/vec_cas]] _calls_
- [[nodes/bitonic_cas_32]] _calls_

## Used By

- [[nodes/sort32_f32_hvx]] _calls_
- [[nodes/sort64_f32_hvx]] _calls_
- [[nodes/sort128_f32_hvx]] _calls_
- [[nodes/sort256_f32_hvx]] _calls_
- [[nodes/sort512_f32_hvx]] _calls_
- [[nodes/sort1024_f32_hvx]] _calls_
