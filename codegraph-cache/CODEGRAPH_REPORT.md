# CodeGraph Report
_Generated: 2026-09-18T06:59:48.479017Z_

**13398 nodes** · **23312 edges** · **5476 communities**

## God Nodes

_Highest-degree concepts everything flows through:_

- **jinja** `common/jinja/string.cpp` — 243 connections
- **move** `tools/ui/src/lib/hooks/use-picker-navigation.svelte.ts` — 241 connections
- **string** `common/jinja/string.h` — 177 connections
- **ggml_nbytes** `ggml/src/ggml.c` — 158 connections
- **ggml_type_name** `ggml/src/ggml.c` — 158 connections

## Community Clusters

### ggml (240 nodes)
Members: ggml_backend_cann_event_record, parallel_for, ggml_sycl_add_id, op, ggml_sycl_add …

### ggml (193 nodes)
Members: print_tensor_info, tensors, ggml_backend_alloc_ctx_tensors, ggml_backend_alloc_ctx_tensors_from_buft_size, ggml_backend_meta_context …

### src (188 nodes)
Members: init_model, load, loadModel, prepare, get_n_tokens …

### common (169 nodes)
Members: common_models_handler_is_preset_repo, common_params_print_usage, get_default_local_path, build_chat_peg_parser, after_common_suffix …

### ggml (136 nodes)
Members: common_control_vector_load_one, common_http_get_free_port, common_imatrix_load, common_speculative_type_from_name, my_llama_file …

### tools (133 nodes)
Members: print_usage, licenses, llama_update, version, common_arg_utils …

### tools (132 nodes)
Members: types, client, rdma_conn, is_valid_fd, post_rx …

### ggml (120 nodes)
Members: ggml_tallocr, ggml_context_deleter, ggml-cuda.h, ggml_tensor, ggml-opencl.h …

### ggml (120 nodes)
Members: ggml_metal_library_get_pipeline_arange, ggml_metal_library_get_pipeline_base, ggml_metal_library_get_pipeline_bin_one, ggml_metal_library_get_pipeline_col2im_1d, ggml_metal_library_get_pipeline_conv_2d …

### ggml (119 nodes)
Members: ggml_backend_blas_device_supports_op, ggml_backend_blas_graph_compute, ggml_backend_blas_mul_mat, ggml_backend_blas_out_prod, ggml_cann_need_bcast …

## Surprising Connections

- **TOKENIZER_TYPE** →(imports)→ **ai_should_log**
- **TOKENIZER_TYPE** →(imports)→ **common_json_item**
- **split_str_to_n_bytes** →(imports)→ **ai_should_log**
- **split_str_to_n_bytes** →(imports)→ **gguf.py**
- **GGMLFormat** →(imports)→ **ai_should_log**
- **GGMLFormat** →(imports)→ **gguf.py**
- **PartialLoraTensor** →(imports)→ **ai_should_log**
- **PartialLoraTensor** →(imports)→ **common_json_item**

## Suggested Questions

- What does jinja depend on?
- What uses jinja?
- What is the relationship between TOKENIZER_TYPE and other modules?
- What is the relationship between GGMLFormat and other modules?
- Which files have the most connections?

## Confidence Breakdown

- **EXTRACTED**: 13025 edges
- **INFERRED**: 10287 edges

## Knowledge Gaps

**Isolated nodes** (5158 with no edges):
  - `ty.toml` in `ty.toml`
  - `AGENTS.md` in `AGENTS.md`
  - `CONTRIBUTING.md` in `CONTRIBUTING.md`
  - `pyproject.toml` in `pyproject.toml`
  - `Makefile` in `Makefile`
  - `CLAUDE.md` in `CLAUDE.md`
  - `pyrightconfig.json` in `pyrightconfig.json`
  - `CMakeLists.txt` in `CMakeLists.txt`
  - …and 5150 more

**Thin communities** (5158 single-node clusters):
  - `.pre-commit-config.yaml` in `.pre-commit-config.yaml`
  - `AGENTS.md` in `AGENTS.md`
  - `CLAUDE.md` in `CLAUDE.md`
  - `CMakeLists.txt` in `CMakeLists.txt`
  - `CMakePresets.json` in `CMakePresets.json`
  - …and 5153 more

_No ambiguous edges._
