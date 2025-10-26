# Chapter 14: Self-Supervised Learning (SSL)

## Overview
Self-supervised learning trains models using pretext tasks defined on unlabeled data, unlocking vast corpora (images, audio, text) without manual annotation. SSL has become the foundation of modern foundation models: BERT’s masked language modeling, SimCLR/BYOL for vision, wav2vec for speech. In 2020, SimCLR showed that carefully designed contrastive learning can match supervised pretraining on ImageNet ([Chen et al., 2020](https://arxiv.org/abs/2002.05709)).

*ELI5:* SSL is like solving puzzles you invent yourself—jigsawing an image or guessing missing words—so you get smarter even without a teacher.

## Paradigms
1. **Contrastive learning** (SimCLR, MoCo): maximize agreement between augmented views of the same sample while pushing apart different samples.
2. **Masked prediction** (BERT, MAE): mask parts of input and ask model to reconstruct.
3. **Predictor-less/self-distillation** (BYOL, SimSiam): paired networks learn from each other without negative samples.
4. **Clustering & prototype methods** (SwAV, DINO): assign samples to prototypes and enforce consistency.
5. **Generative SSL**: autoencoders, VAEs, diffusion models reconstruct inputs.

## SimCLR recipe (Chen et al., 2020)
- Two random augmentations per image (crop, color jitter, blur).
- Encoder (ResNet) followed by MLP projection head.
- NT-Xent loss:  
  $$
  \ell_{i,j} = -\log \frac{\exp(\text{sim}(z_i, z_j)/\tau)}{\sum_{k \neq i} \exp(\text{sim}(z_i, z_k)/\tau)}
  $$
  where $z_i$, $z_j$ are projections of a positive pair, $\tau$ is temperature.
- Large batch sizes and strong augmentations are critical.

## Masked modeling highlights
- **BERT**: randomly mask 15% of tokens; train transformer to predict them.
- **MAE**: mask 75% of image patches; reconstruct with lightweight decoder.
- **data2vec / BEiT**: combine masked prediction with teacher-student objectives.

## Applications
- **Vision**: SimCLR, BYOL, DINO pretraining improves downstream classification, detection, segmentation.
- **NLP**: Masked language modeling (BERT), next sentence prediction, sequence denoising (T5).
- **Audio**: wav2vec 2.0 learns speech features for ASR.
- **Multimodal**: CLIP uses contrastive loss between images and text (Chapter 3).

## Tips for practice
- Choose augmentations relevant to domain (time warps for audio, cropping for vision).
- Use temperature and batch size to control contrastive hardness.
- For masked modeling, high mask ratios encourage global reasoning; keep decoder lightweight.
- Evaluate representations via linear probes or few-shot fine-tuning.

## Experiments & projects
1. **SimCLR mini-reproduction:** train on CIFAR-10 to study impact of augmentation combinations.
2. **Linear probe vs. fine-tune:** freeze SSL-pretrained encoder and train linear classifier; compare to full fine-tuning.
3. **Masked autoencoder ablation:** vary mask ratios (50–90%) to observe reconstruction quality vs. downstream accuracy.
4. **Contrastive for language:** apply InfoNCE loss on sentence pairs (SimCSE) to learn sentence embeddings.

## References
- Chen et al., 2020. *SimCLR: A Simple Framework for Contrastive Learning of Visual Representations.* arXiv:2002.05709.
- Devlin et al., 2018. *BERT.*
- He et al., 2020. *MoCo v2.*
- Grill et al., 2020. *BYOL.*
- He et al., 2022. *Masked Autoencoders Are Scalable Vision Learners.*
