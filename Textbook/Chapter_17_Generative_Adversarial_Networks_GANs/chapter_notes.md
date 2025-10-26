# Chapter 17: Generative Adversarial Networks (GANs)

## Overview
GANs pit a generator $G$ against a discriminator $D$ in a minimax game: $G$ maps noise $z$ to data samples, while $D$ tries to distinguish real vs. fake. Goodfellow et al. (2014) showed this adversarial training can learn complex data distributions without explicit likelihoods ([Goodfellow et al., 2014](https://arxiv.org/abs/1406.2661)). Advances such as StyleGAN improved quality and control in image synthesis ([Karras et al., 2019](https://arxiv.org/abs/1812.04948)).

*ELI5:* Think of an art forger (generator) and a detective (discriminator). The forger keeps improving fake paintings until the detective can’t tell them apart from real ones.

## Objective
$$
\min_G \max_D \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log (1 - D(G(z)))]
$$
Variants: Wasserstein GAN replaces log loss with Earth-Mover distance; hinge loss, least-squares GAN, etc.

## Architectures
- **DCGAN**: convolutional G/D with batch norm, ReLU/LeakyReLU.
- **StyleGAN**: maps latent $z$ to intermediate $w$, modulates convolution weights for style control; introduces progressive growing and adaptive instance normalization.
- **Conditional GANs**: add labels or text embeddings (cGAN, StackGAN, ControlNet) to control outputs.
- **Diffusion hybrids**: GAN priors combined with diffusion denoisers for speed.

## Training tips
- Use spectral norm or gradient penalties to stabilize.
- Balance generator/discriminator learning rates and updates.
- Apply data augmentation (ADA) to improve generalization on limited datasets.
- Track metrics like FID, IS for image quality.

## Applications
- Image synthesis (faces, art, medical imaging).
- Super-resolution (SRGAN, ESRGAN).
- Data augmentation for rare classes.
- Domain translation (CycleGAN, pix2pix).
- Video, 3D generation (StyleGAN-V, GANverse3D).

## Experiments
1. Train a DCGAN on CIFAR-10; monitor FID vs. epochs.
2. Use conditional GAN to generate class-specific samples on Fashion-MNIST.
3. Fine-tune StyleGAN with transfer learning on a custom portrait dataset.
4. Compare WGAN-GP vs. vanilla GAN stability on a tabular dataset.

## References
- Goodfellow et al., 2014. *Generative Adversarial Networks.* arXiv:1406.2661.
- Karras, Laine, Aila. 2019. *StyleGAN.* arXiv:1812.04948.
- Arjovsky et al., 2017. *Wasserstein GAN.*
- Isola et al., 2017. *pix2pix.*
