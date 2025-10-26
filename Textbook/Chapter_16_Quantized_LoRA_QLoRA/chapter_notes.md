# Chapter 16: Quantized LoRA (QLoRA)

## Overview
QLoRA (Dettmers et al., 2023) enables efficient fine-tuning of large language models by freezing the base model in 4-bit NormalFloat (NF4) quantization while training LoRA adapters in higher precision (BF16/FP16). This reduces memory usage by ~75% compared to full FP16 fine-tuning, letting a single 48GB GPU fine-tune models up to 65B parameters without noticeable quality loss ([Dettmers et al., 2023](https://arxiv.org/abs/2305.14314)).

*ELI5:* Imagine shrinking a giant encyclopedia down to microfilm (4-bit) so it fits in your backpack, then adding sticky-note annotations (LoRA adapters) in regular handwriting. You only edit the sticky notes, not the microfilm, which keeps the original intact and portable.

## Components
1. **Base model quantization**
   - NF4 (NormalFloat4): 4-bit data type learned from the quantization distribution.
   - Double quantization: quantize the quantization constants to reduce metadata overhead.
   - Paged optimizers: manage optimizer states offloaded to CPU/RAM, enabling larger models.
2. **LoRA adapters**
   - Inject rank-$r$ low-rank updates into attention/MLP weights.
   - Adapters trained in 16-bit precision to avoid information loss.
3. **Training pipeline**
   - Quantize weights once; freeze them.
   - Train LoRA parameters using gradient checkpointing + paged optimizers.
   - Optionally apply gradient clipping and low learning rates (e.g., 2e-4).

## Advantages
- **Memory efficiency**: QLoRA reduces VRAM from ~780GB (full FT 65B) to ~48GB.
- **Performance**: LLaMA-65B QLoRA fine-tuned on instruction data matches or surpasses full FT baselines on benchmarks like Vicuna, MT-Bench.
- **Modularity**: LoRA adapters remain small (<1% of original parameters), enabling multiple task-specific adapters.

## Practical tips
- Use NF4 for weights, FP16 for activations and LoRA; ensure hardware supports 4-bit (bitsandbytes).
- Monitor gradients: low precision can cause instability; gradient clipping (1.0) helps.
- Keep rank modest (e.g., 64) to balance capacity and memory.
- Use `bnb.optim.Adam8bit` or paged AdamW to store optimizer states efficiently.
- After training, optionally merge LoRA into 4-bit weights when converting to GGUF or CPU inference.

## Workflow summary
1. Load base model via `bitsandbytes` with 4-bit quantization.
2. Attach LoRA adapters (via PEFT) to target modules.
3. Train with deepspeed or standard HF Trainer using paged optimizers.
4. Evaluate on validation tasks; compare to FP16 baselines.
5. Save adapters separately; share quantized base + adapters for reproducibility.

## Experiments & labs
- **QLoRA vs. LoRA**: fine-tune a 13B model with both approaches on the same dataset; report accuracy vs. VRAM usage.
- **Rank ablation**: test ranks {16, 32, 64, 128} to find sweet spot for a given dataset.
- **Quantization sensitivity**: compare NF4, Int4, and BF16 base weights to gauge accuracy drop.
- **Adapter swap**: train multiple adapters (chat, code) on the same 4-bit base and hot-swap them at inference.

## References & tooling
- Dettmers et al., 2023. *QLoRA: Efficient Finetuning of Quantized LLMs.* arXiv:2305.14314.
- bitsandbytes library for NF4 quantization/paged optimizers.
- Hugging Face PEFT for attaching LoRA/QLoRA adapters.
