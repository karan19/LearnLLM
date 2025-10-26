# Towards General Modality Translation with Contrastive and Predictive Latent Diffusion Bridge

- **Authors:** Nimrod Berman, Omkar Joglekar, Eitan Kosman, Dotan Di Castro, Omri Azencot
- **Published:** 2025-10-23T17:59:54Z
- **Source:** http://arxiv.org/abs/2510.20819v1

## Abstract
Recent advances in generative modeling have positioned diffusion models as
state-of-the-art tools for sampling from complex data distributions. While
these models have shown remarkable success across single-modality domains such
as images and audio, extending their capabilities to Modality Translation (MT),
translating information across different sensory modalities, remains an open
challenge. Existing approaches often rely on restrictive assumptions, including
shared dimensionality, Gaussian source priors, and modality-specific
architectures, which limit their generality and theoretical grounding. In this
work, we propose the Latent Denoising Diffusion Bridge Model (LDDBM), a
general-purpose framework for modality translation based on a latent-variable
extension of Denoising Diffusion Bridge Models. By operating in a shared latent
space, our method learns a bridge between arbitrary modalities without
requiring aligned dimensions. We introduce a contrastive alignment loss to
enforce semantic consistency between paired samples and design a
domain-agnostic encoder-decoder architecture tailored for noise prediction in
latent space. Additionally, we propose a predictive loss to guide training
toward accurate cross-domain translation and explore several training
strategies to improve stability. Our approach supports arbitrary modality pairs
and performs strongly on diverse MT tasks, including multi-view to 3D shape
generation, image super-resolution, and multi-view scene synthesis.
Comprehensive experiments and ablations validate the effectiveness of our
framework, establishing a new strong baseline in general modality translation.
For more information, see our project page:
https://sites.google.com/view/lddbm/home.

## ELI5
Imagine a magical post office staffed by artists who can smell a rose, hum its fragrance as a melody, then sculpt that melody into a tangible object for someone who cannot smell at all. The researchers teach this post office a single secret alphabet—a latent space—so smell tokens, sound tokens, and image tokens all live in the same diary and can be compared directly. Inside that diary, they play a hot-and-cold contrastive game to make sure matching pairs huddle together while mismatched ones drift apart, preserving meaning even when modalities look nothing alike on the surface. A predictive loss acts like a rehearsal director, asking the post office to guess what the finished package should look like before it leaves, which keeps translations faithful rather than fanciful. Because the whole process happens in this neutral latent lobby, the couriers never worry about mismatched dimensions or handcrafted bridges between senses. The end result feels like universal diplomacy for data: any modality can walk in, drop off its message, and pick up a faithful translation tailored to whatever friend is waiting outside.
