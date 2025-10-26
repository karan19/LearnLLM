# Chapter 15: Transfer Learning

## Overview
Transfer learning reuses knowledge learned on a source task/domain to accelerate training on a target. Modern AI pipelines pretrain large models on generic corpora (ImageNet, Common Crawl) and fine-tune or prompt them for downstream tasks, reducing data requirements and compute. Key ingredients: selecting a source pretraining objective, adapting representations (feature reuse, fine-tuning, adapters), and measuring transferability. Research shows that pretraining on larger, diverse datasets yields strong zero-shot transfer, but domain mismatch still matters ([Yosinski et al., 2014](https://arxiv.org/abs/1411.1792); [Zhuang et al., 2019](https://arxiv.org/abs/1903.12355)).

*ELI5:* It’s like learning to ride a bicycle before trying a motorcycle—the balance skills transfer so you need fewer lessons.

## Transfer modalities
1. **Feature transfer**: freeze pretrained backbone, train new head (linear probe).
2. **Fine-tuning**: initialize with pretrained weights and keep training on target data; either full or partial layers.
3. **Adapter/LoRA transfer**: add lightweight modules for each target task.
4. **Zero-shot / few-shot transfer**: rely on prompts or similarity without task-specific training (e.g., CLIP, GPT-4 zero-shot reasoning).
5. **Domain adaptation**: align distributions between source and target (DANN, MMD, domain-specific normalization).

## Transferability factors
- **Task similarity**: similar label spaces or data modalities transfer better.
- **Dataset size**: small target datasets benefit more from pretrained features.
- **Layer depth**: early layers capture general patterns, later layers are more task-specific (Yosinski et al., 2014).
- **Pretext objective**: self-supervised objectives (SimCLR, MAE) often produce more general features than supervised pretraining.

## Adaptation strategies
| Strategy | Use case | Notes |
|----------|----------|-------|
| Linear probe | Quick evaluation of representation quality | Freeze backbone; low compute |
| Full fine-tune | High-capacity target, enough data | Risk of overfitting on small data |
| Partial unfreezing | Unfreeze top N layers; keep lower layers frozen | Balance adaptivity vs. stability |
| Adapters/LoRA | Multi-task or memory-constrained settings | Small per-task footprint |
| Prompt-based transfer | LLMs; encode task description in prompt | Minimal training |

## Domain adaptation tools
- **Feature alignment**: maximum mean discrepancy (MMD), adversarial domain discriminators (DANN), CORAL.
- **Style transfer/augmentation**: data augmentation to mimic target distribution.
- **Curriculum transfer**: move from synthetic to real data gradually.

## Evaluation
- **Transfer learning benchmarks**: VTAB, GLUE/SuperGLUE, ImageNet subsets, downstream detection/segmentation.
- **Metrics**: fine-tuned accuracy, few-shot performance, data efficiency curves.
- **Negative transfer**: measure if transfer hurts compared to training from scratch.

## Experiments & ideas
1. **Linear probe vs. fine-tune**: compare accuracy and training cost on a small dataset (e.g., Flowers-102) using a ViT-B pretrained on ImageNet.
2. **Adapter vs. full FT**: evaluate LoRA adapters vs. full FT on a multi-domain text benchmark; log parameter counts.
3. **Domain adaptation**: apply DANN to adapt from synthetic digits (SVHN) to MNIST; track feature alignment via t-SNE.
4. **Zero-shot CLIP transfer**: test CLIP zero-shot classification on a custom dataset and compare to few-shot fine-tuning.

## References
- Yosinski et al., 2014. *How transferable are features in deep neural networks?*
- Zhuang et al., 2019. *Local Aggregation for Unsupervised Learning of Visual Embeddings.* arXiv:1903.12355.
- Radford et al., 2021. *CLIP* (for zero-shot image-text transfer).
- Raffel et al., 2020. *T5* (text-to-text transfer).
