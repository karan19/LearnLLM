# Chapter 10: Low-Rank Adaptation (LoRA & Friends)

## Overview
Low-Rank Adaptation (LoRA) freezes a pre-trained Transformer and learns rank-decomposed updates for selected weight matrices, drastically reducing trainable parameters while preserving inference latency. Introduced by Hu et al. (2021), LoRA has become a default parameter-efficient tuning method for LLMs, vision-language models, and agents. Extensions such as DoRA and QLoRA improve stability, accuracy, and memory usage ([Hu et al., 2021](https://arxiv.org/abs/2106.09685); [Liu et al., 2024](https://arxiv.org/abs/2402.09353); [Dettmers et al., 2023](https://arxiv.org/abs/2305.14314)).

*ELI5:* Instead of rewriting an entire book (all weights), LoRA adds a thin transparent sheet with a few handwritten tweaks. The original pages stay intact, and you can swap sheets for different tasks.

## Mechanics
- For a weight matrix $W \in \mathbb{R}^{d \times k}$, LoRA learns low-rank matrices $A \in \mathbb{R}^{d \times r}$ and $B \in \mathbb{R}^{r \times k}$ (rank $r \ll \min(d,k)$). The adapted weight is $W' = W + \alpha / r \cdot A B$.
- Only $A$ and $B$ require gradients; $W$ remains frozen, lowering VRAM and optimizer states.
- Typically applied to query/key/value/projector matrices in attention and to feed-forward projections.
- Multiple LoRA adapters can be merged or composed by simple matrix addition.

## Design knobs
| Hyperparameter | Effect |
|----------------|--------|
| Rank $r$ | Capacity vs. memory; common values 4–64 |
| Scaling $\alpha$ | Rescales $AB$ contribution; often equals $r$ |
| Target modules | `q_proj`, `k_proj`, `v_proj`, `o_proj`, MLP weights |
| Dropout | Optional to regularize updates |
| Precision | Many setups keep adapters in FP16/BF16 even if base is 4-bit (QLoRA) |

## Extensions
- **DoRA (Weight-Decomposed LoRA)**: separates magnitude and direction of weights; applies LoRA to direction while learning scalar magnitudes, bridging gap to full fine-tuning and improving stability on LLaMA/LLaVA tasks ([Liu et al., 2024](https://arxiv.org/abs/2402.09353)).
- **QLoRA**: quantizes base weights to 4-bit NF4 and trains LoRA adapters in 16-bit, enabling 65B models to fine-tune on a single GPU without accuracy loss ([Dettmers et al., 2023](https://arxiv.org/abs/2305.14314)).
- **LoRA + adapters**: combine with Prefix Tuning or use LoRA inside convolutional layers for vision/robotics.
- **Adapter merging**: LoRA weights can be merged into base weights permanently or stored separately for adapter fusion.

## Training workflow
1. Choose base model and LoRA target modules (e.g., `q_proj`, `v_proj`).
2. Initialize low-rank matrices with small random values; set scaling.
3. Freeze base model; train LoRA params on domain/instruction data with standard optimizers (AdamW) and modest LR (1e-4 to 5e-4).
4. (Optional) Apply gradient checkpointing or 4-bit base weights for memory savings.
5. Save adapters separately; optionally merge into base for deployment.

## Evaluation & diagnostics
- Compare to full fine-tuning baseline (if feasible) on accuracy/perplexity.
- Monitor training/validation loss to detect underfitting (increase rank) or overfitting (add regularization).
- Profile inference latency to confirm no overhead vs. base model.
- Stress-test adapter composition (multiple tasks) to ensure merging order doesn’t degrade quality.

## Experiments & projects
1. **Rank sweep:** fine-tune a 7B LLaMA on instruction data with ranks 4, 8, 16; chart MT-Bench scores vs. memory usage.
2. **QLoRA vs. LoRA:** run both on the same dataset to quantify trade-offs in VRAM vs. performance.
3. **DoRA replication:** apply DoRA adapters to a multimodal model (LLaVA) and measure improvements on vision-language benchmarks.
4. **Adapter merging:** train domain-specific adapters (legal, medical) and test weighted merges for multi-domain coverage.
5. **Catastrophic forgetting check:** evaluate base benchmarks before/after merging adapters to verify base behavior preserved.

## References
- Hu et al., 2021. *LoRA: Low-Rank Adaptation of Large Language Models.* arXiv:2106.09685.
- Dettmers et al., 2023. *QLoRA: Efficient Finetuning of Quantized LLMs.* arXiv:2305.14314.
- Liu et al., 2024. *DoRA: Weight-Decomposed Low-Rank Adaptation.* arXiv:2402.09353.
- PEFT library (Hugging Face), LoRA repos from Microsoft/NVIDIA.
