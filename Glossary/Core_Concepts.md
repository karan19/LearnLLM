# Core Concepts Glossary

Foundational terminology that underpins most AI and ML discussions, from introductory vocabulary to advanced mathematical ideas.

## Artificial Intelligence (AI)
**Definition:** Broad field focused on building systems that can perceive, reason, learn, and act in ways that would normally require human intelligence. Includes symbolic, statistical, and learning-based approaches.
**Key notes:** Modern discourse often uses "AI" as an umbrella term that now leans heavily on machine learning techniques.
**ELI5:** Teaching computers to do smart chores—like seeing, talking, or planning—the way a helpful robot assistant would.

## Machine Learning (ML)
**Definition:** Subset of AI that uses data-driven algorithms to approximate functions or decision boundaries instead of hand-crafted rules. Models iteratively improve by minimizing an objective function on data.
**Key notes:** Includes supervised, unsupervised, self-supervised, and reinforcement learning paradigms.
**ELI5:** Letting a computer learn patterns from examples the way a kid learns by practicing instead of being told every rule.

## Deep Learning
**Definition:** Branch of ML that uses deep neural networks (many stacked layers) to automatically learn hierarchical representations. Enabled by GPU acceleration, large datasets, and differentiable programming.
**Key notes:** Powers modern breakthroughs in computer vision, NLP, speech, and recommendation.
**ELI5:** Imagine layers of digital LEGO blocks that stack up to recognize more and more complex shapes, sounds, or words.

## Neural Network
**Definition:** Differentiable function composed of layers of linear transformations plus nonlinear activations. Parameters (weights/biases) are optimized via gradient-based methods.
**Key notes:** Architecture choices (depth, width, connectivity) drive expressiveness and inductive bias.
**ELI5:** A giant web of digital “neurons” passing numbers to each other until they agree on an answer, like classmates whispering hints.

## Parameters vs. Hyperparameters
**Definition:** Parameters are learned values inside the model (weights); hyperparameters configure the training process or architecture (learning rate, depth, batch size).
**Key notes:** Hyperparameters are tuned externally through search or heuristics.
**ELI5:** Parameters are the knobs the model learns to turn by itself; hyperparameters are the knobs you set beforehand, like oven temperature for baking.

## Feature / Representation
**Definition:** Quantitative descriptors used by models. Learned representations capture patterns in data (e.g., embeddings), while engineered features are manually constructed from domain knowledge.
**Key notes:** Representation learning aims to automate feature discovery.
**ELI5:** Features are the important clues you feed a model—like color, shape, or sound—so it can recognize things.

## Embedding
**Definition:** Dense, low-dimensional vector that captures semantic relationships between discrete items (tokens, images, users). Learned jointly with the model or via dedicated objectives.
**Key notes:** Distance or cosine similarity in embedding space correlates with semantic similarity.
**ELI5:** Turning words or images into treasure-map coordinates so that similar things end up near each other on the map.

## Loss Function / Objective
**Definition:** Scalar function measuring mismatch between predictions and targets (e.g., cross-entropy, MSE). Training minimizes expected loss over the data distribution.
**Key notes:** Choice of loss encodes assumptions about noise, calibration, or ranking.
**ELI5:** A scorecard telling the model how wrong it was, so it can try to be less wrong next time.

## Gradient
**Definition:** Vector of partial derivatives of the loss with respect to model parameters. Indicates the direction of steepest ascent; negative gradient guides optimization.
**Key notes:** Computed efficiently via automatic differentiation.
**ELI5:** The gradient is the “go this way” arrow pointing downhill on the loss landscape so the model learns faster.

## Backpropagation
**Definition:** Algorithm that applies the chain rule to propagate gradients from outputs to earlier layers. Enables end-to-end training of deep networks.
**Key notes:** Requires differentiable operations; memory-saving variants include checkpointing and reversible layers.
**ELI5:** Like grading a group project backwards—start with the final score, then tell each teammate how much they helped so they know what to fix.

## Activation Function
**Definition:** Nonlinear transformation applied after linear layers to increase representational power (e.g., ReLU, GELU, SiLU). Prevents stacked linear layers from collapsing into a single linear map.
**Key notes:** Impacts gradient flow, sparsity, and model stability.
**ELI5:** A tiny rule that decides whether a digital neuron “wakes up” or stays quiet, making the network less boring and more expressive.

## Attention Mechanism
**Definition:** Weighted aggregation technique where a query interacts with key-value pairs to focus on relevant context. The weights sum to 1 (softmax) and enable dynamic receptive fields.
**Key notes:** Self-attention underpins Transformers; variants include multi-head, sparse, and linear attention.
**ELI5:** Like highlighting the most important words in a sentence so the model knows what to focus on when replying.

## Token / Tokenization
**Definition:** Discrete unit fed into language or multimodal models. Tokenization converts raw data (text, audio bytes, pixels) into tokens using rules like BPE, WordPiece, or SentencePiece.
**Key notes:** Token vocabulary determines context length, compression, and multilingual support.
**ELI5:** Slicing a long story into bite-sized puzzle pieces the model can swallow and process.

## Context Window
**Definition:** Maximum sequence length a model can attend to in a single forward pass. Constrained by memory and quadratic attention cost.
**Key notes:** Techniques like RoPE extrapolation, ALiBi, and state-space models extend effective context.
**ELI5:** The size of the model’s “memory tray”—once it’s full, older words fall off the edge.

## Latent Space
**Definition:** Abstract continuous space where a model represents concepts. Points correspond to compressed descriptions; operations like interpolation or arithmetic can yield meaningful transformations.
**Key notes:** Exploited in VAEs, diffusion models, and embedding-based search.
**ELI5:** A secret garden where every point stands for an idea; walking around lets you morph one idea into another.

## Regularization
**Definition:** Strategies that constrain model capacity or encourage smoother solutions to prevent overfitting (e.g., weight decay, dropout, early stopping, data augmentation).
**Key notes:** Acts as implicit prior; interacts with optimization and data coverage.
**ELI5:** Gentle rules that stop the model from memorizing the answers sheet so it actually learns the subject.

## Overfitting & Underfitting
**Definition:** Overfitting occurs when a model memorizes noise and fails to generalize; underfitting occurs when the model is too simple to capture patterns.
**Key notes:** Diagnosed via train vs. validation performance gaps.
**ELI5:** Overfitting is memorizing the practice test; underfitting is barely studying the material—neither helps on exam day.

## Bias-Variance Trade-off
**Definition:** Statistical framework describing error decomposition: bias (systematic error) vs. variance (sensitivity to data fluctuations). Managing the trade-off leads to better generalization.
**Key notes:** Ensemble methods and regularization modulate this balance.
**ELI5:** Choosing between a robot that’s consistently wrong in the same way (bias) and one that gives different answers every time (variance); you want a happy medium.

## Probabilistic Modeling
**Definition:** Approaches that treat outputs and latent variables as probability distributions, enabling uncertainty estimation and principled reasoning under noise.
**Key notes:** Includes Bayesian inference, graphical models, and probabilistic programming.
**ELI5:** Instead of giving one answer, the model gives odds—like saying “there’s a 70% chance it rains today.”

## Information Bottleneck
**Definition:** Principle stating that optimal representations should capture task-relevant information while compressing everything else. Formalized via mutual information constraints.
**Key notes:** Inspires architecture choices and regularizers like β-VAE.
**ELI5:** Imagine squeezing juice through a straw—you only want the tasty parts to get through, not the pulp.

## Softmax
**Definition:** Function that converts a vector of logits into a probability distribution by exponentiating and normalizing. Used in attention weights and output layers.
**Key notes:** Sensitive to large logits; temperature scaling sharpens or flattens the distribution.
**ELI5:** Turning raw scores into percentages that add up to 100%, like converting exam points into grades.

## Cross-Entropy
**Definition:** Loss measuring divergence between target distribution and predicted probabilities. For classification, reduces to negative log-likelihood of the correct class.
**Key notes:** Pairs naturally with softmax outputs.
**ELI5:** Punishes the model more when it’s very confident but wrong—like a teacher saying “you shouted the wrong answer.”

## Entropy
**Definition:** Measure of uncertainty of a probability distribution (−Σ p log p). High entropy indicates diverse possible outcomes.
**Key notes:** Used in exploration bonuses, pruning low-information tokens, and evaluating sampling diversity.
**ELI5:** A messy toy box has high entropy; a neatly sorted one has low entropy.

## Temperature (Sampling)
**Definition:** Scalar that rescales logits before softmax; T>1 makes outputs more random, T<1 makes them more deterministic.
**Key notes:** Applied at inference to control creativity vs. adherence.
**ELI5:** A creativity knob—turn it up for wild ideas, down for safe answers.

## Top-k / Top-p Sampling
**Definition:** Decoding heuristics that restrict sampling to the k most probable tokens (top-k) or smallest set whose cumulative probability exceeds p (top-p nucleus).
**Key notes:** Balances diversity and coherence.
**ELI5:** Picking from the best few candy flavors in the jar so you still get variety without biting into something weird.

## Beam Search
**Definition:** Deterministic decoding that keeps the top B candidate sequences at each step, expanding them via best-first search.
**Key notes:** Improves likelihood-based metrics but can reduce diversity compared with sampling.
**ELI5:** Exploring multiple promising story endings in parallel and choosing the one that reads best at the end.

## Logit
**Definition:** Pre-softmax score output by a model for each class or token. Differences between logits, not absolute values, drive probabilities.
**Key notes:** Logit manipulation enables biasing outputs (logit biasing, logit lens).
**ELI5:** Raw point totals before you convert them into percentages—useful for tweaking outcomes directly.

## Layer Normalization / Batch Normalization
**Definition:** Normalization techniques that stabilize training by standardizing activations. LayerNorm normalizes across features per token; BatchNorm normalizes across batch+spatial dimensions.
**Key notes:** Transformers rely on LayerNorm (pre/post-norm variants) for gradient stability.
**ELI5:** Like making sure every kid in class starts at the same energy level so the group project goes smoothly.

## Residual Connection
**Definition:** Identity shortcut that adds input to the output of a block, enabling gradient flow through deep networks.
**Key notes:** Combined with normalization and attention/FFN blocks in Transformers.
**ELI5:** A side road that lets information skip traffic jams and arrive faster, keeping deep networks from getting stuck.
