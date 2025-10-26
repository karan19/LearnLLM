# Model Architectures Glossary

Definitions for popular and emerging neural architectures across modalities.

## Perceptron / Multilayer Perceptron (MLP)
**Definition:** Feed-forward network composed of stacked linear layers and nonlinear activations. Early neural network form; still widely used for tabular data and as submodules (FFNs) in Transformers.
**ELI5:** A stack of spreadsheet formulas that pass numbers forward until they produce an answer.

## Convolutional Neural Network (CNN)
**Definition:** Uses learnable convolutional filters to exploit local spatial structure. Key for vision tasks, time-series, and audio spectrograms.
**Key notes:** Concepts include kernels, stride, padding, pooling, residual and dense connections.
**ELI5:** Slide a tiny window over a picture like a magnifying glass that looks for edges, corners, or textures.

## Recurrent Neural Network (RNN)
**Definition:** Processes sequences step-by-step, maintaining hidden state that captures prior context. Variants include vanilla RNN, LSTM, and GRU.
**Key notes:** Struggles with long-range dependencies due to vanishing gradients.
**ELI5:** Reads a sentence one word at a time, carrying a memory backpack that stores what came before.

## Long Short-Term Memory (LSTM)
**Definition:** RNN variant with gating mechanisms (input, forget, output) that regulate information flow and mitigate vanishing gradients.
**Key notes:** Common in language, speech, and time-series prior to Transformers.
**ELI5:** A smarter memory backpack with valves that decide what to keep, forget, or share at each step.

## Gated Recurrent Unit (GRU)
**Definition:** Simplified LSTM with update and reset gates, fewer parameters, comparable performance on many tasks.
**ELI5:** A lightweight version of the memory backpack—fewer zippers, still keeps the essentials.

## Transformer
**Definition:** Architecture based on self-attention, feed-forward blocks, and layer normalization. Enables parallel sequence processing and scales effectively.
**Key notes:** Variants include encoder-only (BERT), decoder-only (GPT), and encoder-decoder (T5).
**ELI5:** Instead of reading one word at a time, it looks at the whole page and decides which words matter most at once.

## Encoder-Decoder (Seq2Seq)
**Definition:** Architecture with an encoder that processes inputs into a latent representation and a decoder that generates outputs conditioned on that representation.
**Key notes:** Used in translation, summarization, speech recognition.
**ELI5:** One part reads and summarizes the message; another part rewrites that summary in the target language.

## Retrieval-Augmented Generation (RAG)
**Definition:** Hybrid architecture combining neural generation with external knowledge retrieval. Encoder retrieves relevant documents; decoder conditions on them.
**Key notes:** Improves factuality and reduces hallucination; retrieval can be dense or sparse.
**ELI5:** Before answering, the model Googles relevant pages and then writes the reply using the fresh notes.

## Mixture of Experts (MoE)
**Definition:** Architecture where a gating network routes tokens to specialized expert networks, enabling sparse computation.
**Key notes:** Sharded across hardware to scale parameter counts without proportional compute.
**ELI5:** A manager sends each question to the specialist most qualified to answer, so not everyone works at once.

## Sparse Mixture-of-Experts Transformers
**Definition:** Transformer layers where feed-forward blocks are replaced with expert pools. Gating ensures each token activates only a subset of experts.
**Key notes:** Requires load-balancing losses and expert parallelism.
**ELI5:** Inside a Transformer, only a few mini-networks wake up per token, saving energy while keeping expertise.

## Graph Neural Network (GNN)
**Definition:** Operates on graph-structured data using message passing between nodes and edges. Captures relational inductive biases.
**Key notes:** Variants include GCN, GAT, GraphSAGE.
**ELI5:** Each friend in a social network tells their neighbors what they know, and everyone updates their opinion.

## Autoencoder (AE)
**Definition:** Symmetric encoder-decoder trained to reconstruct inputs, forcing a compressed latent representation.
**Key notes:** Denoising and sparse autoencoders improve robustness and interpretability.
**ELI5:** Squish a picture into a tiny code and then rebuild it to make sure no important details were lost.

## Variational Autoencoder (VAE)
**Definition:** Probabilistic AE that learns latent distributions by optimizing a reconstruction term plus KL divergence to a prior.
**Key notes:** Enables controlled sampling and latent arithmetic.
**ELI5:** Learn not just one secret code per image, but a whole cloud of possible codes so you can generate new variations.

## Generative Adversarial Network (GAN)
**Definition:** Consists of a generator and discriminator trained in a minimax game. Generator produces synthetic samples; discriminator distinguishes real vs fake.
**Key notes:** Challenges include mode collapse and training instability; variants (StyleGAN, BigGAN) improve fidelity.
**ELI5:** A forger tries to paint fake art while a detective tries to spot fakes; both improve as they duel.

## Diffusion Model
**Definition:** Probabilistic generative model that learns to reverse a noise-adding diffusion process via denoising steps.
**Key notes:** State-of-the-art for high-fidelity image/video/audio generation; variants include DDPM, DDIM, Score-based models, Latent Diffusion.
**ELI5:** Start with TV static and repeatedly clean it until a clear picture appears.

## Energy-Based Model (EBM)
**Definition:** Assigns scalar energies to configurations; lower energy implies higher probability. Learned via contrastive objectives.
**Key notes:** Flexible but challenging to normalize.
**ELI5:** Imagine a landscape where good answers sit in valleys; the model tries to shape the land so real data lands in the lowest spots.

## State-Space Model (SSM)
**Definition:** Represents sequences using linear dynamical systems with learned transition and emission matrices. Modern neural SSMs (S4, Mamba) offer long-context efficiency.
**ELI5:** Track a moving object by updating a simple physics equation each time step instead of remembering every past detail.

## Residual Network (ResNet)
**Definition:** Introduces identity skip connections to allow deeper networks by easing gradient flow.
**Key notes:** Building block in CNNs, Transformers (residual add), and diffusion UNets.
**ELI5:** Add shortcut ladders in a tall building so people (gradients) can bypass traffic jams between floors.

## Vision Transformer (ViT)
**Definition:** Applies Transformer encoder to image patches treated as tokens. Relies on large-scale pretraining and strong augmentations.
**ELI5:** Chop an image into puzzle tiles, treat each tile like a word, and let a Transformer read the picture like a sentence.

## Multimodal Transformer
**Definition:** Architectures that jointly attend over heterogeneous tokens (text, image patches, audio, video). Includes CLIP, Flamingo, GPT-4V-style models.
**ELI5:** A single brain that looks at pictures, listens to audio, and reads words all at once while making decisions.

## Graph Transformer
**Definition:** Combines attention with graph positional encodings to operate on graph data.
**ELI5:** Give each network node its own attention lens so it can weigh messages from specific neighbors differently.

## Retrieval-Enhanced Transformer (RETRO, Atlas)
**Definition:** Integrates k-nearest-neighbor retrieval into Transformer layers, supplying retrieved chunk embeddings as additional context.
**ELI5:** The model keeps a bookshelf nearby and flips to relevant paragraphs mid-thought.

## Hypernetwork
**Definition:** Network that generates weights for a primary network, enabling conditional parameterization or weight sharing across tasks.
**ELI5:** A mini factory that 3D-prints custom model pieces on demand for each task.

## Neural Architecture Search (NAS)
**Definition:** Automated exploration of architecture design spaces using reinforcement learning, evolutionary algorithms, or gradient-based search.
**Key notes:** Produces specialized models (EfficientNet, MobileNet variants) under latency/accuracy constraints.
**ELI5:** Let a robot architect try thousands of blueprints overnight and keep the design that scores best.
