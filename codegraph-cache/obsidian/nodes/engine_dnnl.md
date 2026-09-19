---
name: "engine_dnnl"
type: "function"
file: "ggml/src/ggml-sycl/common.hpp"
community: "ggml"
---

# engine_dnnl

**Type:** `function`  **File:** `ggml/src/ggml-sycl/common.hpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/make_engine]] _calls_
- [[nodes/stream_dnnl]] _calls_
- [[nodes/pool]] _calls_
- [[nodes/get_size]] _calls_
- [[nodes/realloc]] _calls_
- [[nodes/stream]] _calls_

## Used By

- [[nodes/build_sdpa]] _calls_
- [[nodes/to_dt]] _calls_
