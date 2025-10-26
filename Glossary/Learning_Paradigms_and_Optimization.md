# Learning Paradigms & Optimization Glossary

Key vocabulary describing how models learn from data and how optimization procedures are configured.

## Supervised Learning
**Definition:** Training paradigm where models learn a mapping from inputs to labeled outputs by minimizing loss on labeled datasets.
**Key notes:** Dominant for classification/regression tasks; data labeling cost can be high.
**ELI5:** Like studying with flashcards—you see a question plus the correct answer and learn to match them.

## Unsupervised Learning
**Definition:** Techniques that discover structure in unlabeled data via clustering, density estimation, or representation learning.
**Key notes:** Includes autoencoders, k-means, and generative modeling without labels.
**ELI5:** Dump a box of mixed LEGO pieces on the floor and let the algorithm sort them into piles without any hints.

## Self-Supervised Learning (SSL)
**Definition:** Uses intrinsic signals (masking, contrastive pairs) from unlabeled data to create supervision. Models predict missing parts or discriminate augmentations.
**Key notes:** Enables pretraining on massive corpora; GPT/BERT objectives are SSL.
**ELI5:** Cover part of a sentence and ask the model to guess the missing words, teaching itself from the puzzle.

## Contrastive Learning
**Definition:** SSL strategy where models pull together related views and push apart unrelated samples in embedding space, often using InfoNCE loss.
**Key notes:** Underlies CLIP, SimCLR, and multimodal retrieval systems.
**ELI5:** Show two photos of the same dog and one of a cat; tell the model the dog photos belong together and the cat is different.

## Reinforcement Learning (RL)
**Definition:** Agents learn policies through trial-and-error interactions with an environment, optimizing cumulative reward.
**Key notes:** Techniques include Q-learning, policy gradients, actor-critic, and model-based RL.
**ELI5:** A video-game character tries moves and gets points or penalties, learning which actions lead to higher scores.

## Reinforcement Learning from Human Feedback (RLHF)
**Definition:** Alignment technique where a reward model trained on human preference data guides policy optimization (e.g., PPO) to produce aligned text.
**Key notes:** Requires data collection pipeline, reward modeling, and careful safety evaluations.
**ELI5:** People vote on which answer sounds better, and the model learns to favor the style humans prefer.

## Imitation / Behavioral Cloning
**Definition:** Learning a policy by mimicking expert demonstrations without explicit reward signals.
**Key notes:** Prone to compounding errors; often combined with RL fine-tuning.
**ELI5:** Watch a pro gamer play and copy every joystick move instead of figuring out the rules yourself.

## Curriculum Learning
**Definition:** Strategy that presents training data in a deliberate order (easy→hard) to stabilize optimization.
**Key notes:** Can speed convergence and improve robustness.
**ELI5:** Start math homework with simple problems before tackling the tricky ones so you build confidence.

## Transfer Learning
**Definition:** Leveraging knowledge from a source task/domain to improve performance on a target task, typically via fine-tuning pretrained models.
**Key notes:** Reduces data requirements and training cost.
**ELI5:** Learn to ride a scooter first, then switch to a bike—the balance skills transfer.

## Fine-Tuning
**Definition:** Continuing training of a pretrained model on task-specific data. Can be full-model, partial (adapter layers), or parameter-efficient.
**Key notes:** Requires careful learning rate schedules and overfitting guards.
**ELI5:** Take a prebuilt toy robot and teach it a new dance routine without rebuilding the whole robot.

## Low-Rank Adaptation (LoRA)
**Definition:** Parameter-efficient fine-tuning that injects trainable low-rank matrices into weight updates. Only the low-rank factors are optimized, reducing memory.
**Key notes:** Variants include QLoRA (with quantization) and DoRA (directional LoRA).
**ELI5:** Instead of rewiring the whole robot, plug in a small attachable chip that tweaks its moves.

## Quantized LoRA (QLoRA)
**Definition:** Combines 4-bit quantization of base model weights with 16-bit LoRA adapters to fit large models on commodity GPUs.
**Key notes:** Uses double quantization and paged optimizers to manage memory spikes.
**ELI5:** Shrink the robot’s memory to mini LEGO bricks, then add a small upgrade pack so it can still learn new tricks.

## Optimizer
**Definition:** Algorithm updating parameters using gradients (SGD, Adam, AdamW, Adan, Lion). Balances learning rate, momentum, and regularization.
**Key notes:** Choice affects convergence speed, stability, and generalization.
**ELI5:** The recipe that tells the model how big a step to take each time it learns from a mistake.

## Learning Rate Schedule
**Definition:** Time-varying function that adjusts the learning rate during training (e.g., warmup, cosine decay, step decay).
**Key notes:** Warmup mitigates unstable early updates; decay prevents oscillations later.
**ELI5:** Start by taking small careful steps, then speed up, then slow down again so you don’t overshoot the finish line.

## Batch Size / Microbatching
**Definition:** Number of samples processed per optimization step. Large batches improve throughput but may harm generalization.
**Key notes:** Gradient accumulation (microbatching) simulates large batches under memory constraints.
**ELI5:** Decide whether to grade homework one paper at a time or in stacks before updating the class average.

## Gradient Clipping
**Definition:** Technique that caps gradient norms or values to prevent exploding gradients and stabilize training.
**Key notes:** Common in sequence models and RL.
**ELI5:** If the “go this way” arrow gets too long, trim it so the model doesn’t leap off a cliff.

## Weight Decay
**Definition:** L2 penalty on parameters to discourage large weights, acting as regularization.
**Key notes:** Decoupled variants (AdamW) adjust implementation to better match theoretical intent.
**ELI5:** A gentle tug that keeps weights from growing like wild weeds.

## Early Stopping
**Definition:** Halting training when validation metrics stop improving to avoid overfitting.
**Key notes:** Requires held-out validation data and patience thresholds.
**ELI5:** Stop baking once the cake is done instead of risking a burnt crust.

## Hyperparameter Optimization (HPO)
**Definition:** Systematic search over hyperparameter space using grid, random, Bayesian, or evolutionary methods.
**Key notes:** Automated tools (Ray Tune, Optuna) orchestrate distributed experiments.
**ELI5:** Trying different oven temperatures and baking times until the cookies taste best.

## Meta-Learning
**Definition:** "Learning to learn"—models acquire priors that help them adapt quickly to new tasks (MAML, Reptile, meta-RL).
**Key notes:** Critical for few-shot learning and personalization.
**ELI5:** Practice learning multiple instruments so the next new instrument feels easier to pick up.

## Continual Learning
**Definition:** Training paradigms where models encounter non-stationary data streams and must avoid catastrophic forgetting.
**Key notes:** Techniques include rehearsal buffers, elastic weight consolidation, and modular networks.
**ELI5:** Keep reviewing old lessons while learning new ones so you don’t forget the alphabet when studying calculus.

## Federated Learning
**Definition:** Collaborative training where data stays on-device; only model updates are aggregated centrally.
**Key notes:** Preserves privacy but introduces non-IID data challenges and communication constraints.
**ELI5:** Each phone learns from its owner’s messages and shares only the lesson, not the private texts.
