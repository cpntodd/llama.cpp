---
name: "ggml_openvino_model_cache_dir"
type: "function"
file: "ggml/src/ggml-openvino/model-cache.cpp"
community: "ggml"
---

# ggml_openvino_model_cache_dir

**Type:** `function`  **File:** `ggml/src/ggml-openvino/model-cache.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/string]] _calls_
- [[nodes/make_dirs]] _calls_
- [[nodes/fnv1a_u64]] _calls_
- [[nodes/fnv1a]] _calls_
- [[nodes/for_each_weight]] _calls_
- [[nodes/weight_fingerprint]] _calls_
- [[nodes/ov_version_string]] _calls_

## Used By

- [[nodes/ov_graph_compute_dynamic]] _calls_
