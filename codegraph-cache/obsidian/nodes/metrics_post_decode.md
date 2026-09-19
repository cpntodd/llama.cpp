---
name: "metrics_post_decode"
type: "function"
file: "tools/server/server-context.cpp"
community: "tools"
---

# metrics_post_decode

**Type:** `function`  **File:** `tools/server/server-context.cpp`

**Community:** [[communities/tools]]

## Depends On

- [[nodes/is_processing]] _calls_
- [[nodes/n_tokens]] _calls_
- [[nodes/metrics_queue_prompt]] _calls_
- [[nodes/metrics_flush_prompt]] _calls_
- [[nodes/ggml_time_us]] _calls_

## Used By

- [[nodes/decode]] _calls_
