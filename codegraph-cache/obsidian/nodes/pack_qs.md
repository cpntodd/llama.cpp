---
name: "pack_qs"
type: "function"
file: "ggml/src/ggml-cpu/amx/mmq.cpp"
community: "ggml"
---

# pack_qs

**Type:** `function`  **File:** `ggml/src/ggml-cpu/amx/mmq.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/bytes_from_nibbles_32]] _calls_
- [[nodes/transpose_8x8_32bit]] _calls_
- [[nodes/packNibbles]] _calls_
- [[nodes/bytes_from_nibbles_64]] _calls_
- [[nodes/transpose_16x16_32bit]] _calls_
- [[nodes/bytes_from_nibbles_128]] _calls_

## Used By

- [[nodes/pack_B]] _calls_
- [[nodes/s8s8_compensation]] _calls_
- [[nodes/unpack_mins_and_scales]] _calls_
