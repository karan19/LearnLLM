# Chapter 08: Quantization

## Overview
Quantization reduces numerical precision (e.g., FP16 → INT8/4) to shrink memory footprint and speed up inference. Large language models (LLMs) benefit greatly: quantized weights fit on smaller GPUs/CPUs and serve more concurrent requests. Techniques include post-training quantization (PTQ), quantization-aware training (QAT), mixed precision, and adaptive rounding.

*ELI5:* Storing model weights in fewer digits is like compressing a song from WAV to MP3—you lose some fidelity, but it takes far less space and streams faster.

## Precision levels
- **FP32 (full precision)**: training baseline; 4 bytes per parameter.
- **FP16/BF16**: half precision; common for training/inference.
- **INT8**: 1 byte; widely supported.
- **INT4, INT3, INT2**: ultra-low-bit weights; require special kernels (e.g., GPTQ, AWQ).
- **FP8**: emerging standard (Hopper GPUs) balancing range and precision.

## Quantization pipeline
1. **Calibration data**: representative inputs to estimate ranges.
2. **Range selection**: min-max, percentile clipping, KL divergence.
3. **Quantize weights/activations**: map float values to discrete levels using scale & zero-point.
4. **Dequantization during compute**: convert back to higher precision for ops if needed.
5. **Fine-tuning (optional)**: QAT to recover accuracy.

*ELI5:* To convert a recipe from grams to teaspoons, you first look at typical ingredient sizes (calibration), set a conversion table (scales), rewrite the recipe (quantization), then convert back when cooking (dequantization).

## Methods & math
- **Uniform quantization**:  
  $$q = \text{round}\left(\frac{x}{s}\right) + z, \quad \hat{x} = s (q - z)$$  
  where scale $s$ and zero-point $z$ map floats to integers.
- **Symmetric vs. asymmetric**: symmetric uses $z=0$, asymmetric handles non-zero means.
- **Per-tensor vs. per-channel**: per-channel scales yield better accuracy for weight matrices.
- **Activation quantization**: dynamic range depends on input; may use per-token or per-timestep scales.
- **GPTQ (Frantar et al., 2023)**: solves least-squares problem to minimize output error during weight quantization.
- **AWQ**: activation-aware weight quantization—identify “salient” channels to keep in higher precision.
- **SmoothQuant**: balance ranges by scaling activations/weights before quantization for LLMs (Xiao et al., 2022).
- **ZeroQuant**: QAT-style approach training from scratch for inference efficiency.

## Trade-offs
| Precision | Pros | Cons |
|-----------|------|------|
| FP16/BF16 | Minimal accuracy loss; hardware support | Still large models |
| INT8 | Good balance; supported on CPUs/GPUs | Might need QAT for small models |
| INT4 | Significant savings | Sensitive to outliers; needs custom kernels |
| Mixed precision | Keep sensitive layers in FP16, others INT4 | Complexity in deployment |

*ELI5:* Think of painting with fewer colors. INT8 is like having 256 crayons—pretty good. INT4 only gives you 16 crayons, so you must be careful choosing shades or the picture looks off.

## LLM-focused techniques
- **GPTQ**: post-training INT4 quantization with error compensation.
- **LLM.int8()**: mixed INT8 inference (Dettmers et al., 2022) using row/column-wise decomposition to handle outliers.
- **SmoothQuant / AWQ**: pre-process weights/activations to reduce variance before quantization.
- **BitNet b1.58**: trains binary weight LLM with 1.58 bits using ternary values.
- **FP8 training**: NVIDIA Hopper supports FP8 Tensor Cores; use loss scaling & calibration.
- **Device-specific**: Apple MLX, Qualcomm AI Stack, ARM Ethos support 4/8-bit LLMs.

## Integration with PEFT
- Combine quantized base model with LoRA/QLoRA adapters: base in 4-bit, adapters in 16-bit for updates.
- **ExLlama, AutoGPTQ, bitsandbytes** provide inference kernels to load quantized weights with adapters.

## Experiments & labs
1. **INT8 PTQ**: quantize a 7B model with `bitsandbytes` LLM.int8 and compare perplexity vs. FP16.
2. **INT4 GPTQ**: use AutoGPTQ to quantize a model; benchmark throughput on single GPU.
3. **SmoothQuant**: apply to a base LLaMA, measure accuracy drop, compare to naïve INT8.
4. **QLoRA fine-tune**: train adapters on a domain dataset with 4-bit base weights, evaluate memory savings.
5. **Layer sensitivity analysis**: quantize individual layers to INT4 to see which ones tolerate low precision.
6. **Hardware profiling**: run quantized models on CPU (GGML/GGUF) vs. GPU to measure latency.

## References & tooling
- Jacob et al., 2018 — INT8 quantization for mobile nets
- Dettmers et al., 2022 — LLM.int8()
- Frantar et al., 2023 — GPTQ
- Xiao et al., 2022 — SmoothQuant
- Lin et al., 2023 — AWQ
- Dettmers et al., 2023 — QLoRA
- BitNet b1.58 paper (2023)
- Toolkits: bitsandbytes, AutoGPTQ, GPTQ-for-LLaMA, ExLlama, GGML/GGUF, Intel Neural Compressor, TensorRT-LLM
