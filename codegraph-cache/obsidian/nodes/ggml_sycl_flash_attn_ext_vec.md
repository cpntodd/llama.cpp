---
name: "ggml_sycl_flash_attn_ext_vec"
type: "function"
file: "ggml/src/ggml-sycl/fattn.cpp"
community: "ggml"
---

# ggml_sycl_flash_attn_ext_vec

**Type:** `function`  **File:** `ggml/src/ggml-sycl/fattn.cpp`

**Community:** [[communities/ggml]]

## Depends On

- [[nodes/_abort]] _imports_
- [[nodes/KeyValuePair]] _imports_
- [[nodes/dequantize_V_f16]] _imports_
- [[nodes/syclex]] _imports_
- [[nodes/syclex]] _imports_
- [[nodes/ggml_sycl_flash_attn_ext_onednn_supported]] _imports_

## Used By

- [[nodes/mkl_fa_kv_desc_mode]] _imports_
- [[nodes/ggml_sycl_flash_attn_ext]] _calls_
