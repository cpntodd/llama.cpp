---
name: "ggml_sycl_topk_moe_fusion"
type: "function"
file: "ggml/src/ggml-sycl/topk-moe.cpp"
community: "ggml"
---

# ggml_sycl_topk_moe_fusion

**Type:** `function`  **File:** `ggml/src/ggml-sycl/topk-moe.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/ggml_get_unary_op]] _calls_
- [[nodes/ggml_backend_buft_get_alloc_size]] _calls_
- [[nodes/ggml_nrows]] _calls_

## Used By

- [[nodes/ggml_sycl_fuse_topk_moe]] _calls_
