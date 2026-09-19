---
name: "time_cell_median"
type: "function"
file: "tools/tuning/bench.cpp"
community: "ggml"
---

# time_cell_median

**Type:** `function`  **File:** `tools/tuning/bench.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/main]] _imports_
- [[nodes/fill_templated_filename]] _imports_
- [[nodes/ggml_backend_graph_compute]] _calls_
- [[nodes/warmup]] _calls_
- [[nodes/ggml_backend_synchronize]] _calls_
- [[nodes/ggml_time_us]] _calls_
- [[nodes/assign]] _calls_
