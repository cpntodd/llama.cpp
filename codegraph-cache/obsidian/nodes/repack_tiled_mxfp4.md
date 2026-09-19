---
name: "repack_tiled_mxfp4"
type: "function"
file: "ggml/src/ggml-hexagon/ggml-hexagon.cpp"
community: "ggml"
---

# repack_tiled_mxfp4

**Type:** `function`  **File:** `ggml/src/ggml-hexagon/ggml-hexagon.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/hex_round_up]] _calls_
- [[nodes/pack_mxfp4_quants]] _calls_
- [[nodes/ggml_nbytes]] _calls_
- [[nodes/repack_q4_0_tiled]] _calls_
- [[nodes/repack_q4_1_tiled]] _calls_
- [[nodes/repack_q8_0_tiled]] _calls_
- [[nodes/Q4_0]] _calls_
- [[nodes/repack_mxfp4_tiled]] _calls_
- [[nodes/repack_tiled_q4_0]] _calls_
- [[nodes/repack_tiled_q4_1]] _calls_
- [[nodes/repack_tiled_q8_0]] _calls_
