# Chapter 12: Knowledge Distillation (KD)

## Overview
Knowledge distillation transfers the behavior of a large “teacher” network to a compact “student” by matching soft outputs, features, or generated sequences. Hinton, Vinyals, and Dean (2015) formalized KD with temperature-scaled soft targets, enabling smaller models to inherit generalization patterns (“dark knowledge”) from teachers ([Hinton et al., 2015](https://arxiv.org/abs/1503.02531)). KD now powers mobile deployment (DistilBERT, TinyBERT) and cross-domain adaptation (Orca distilling GPT-4 reasoning).

*ELI5:* Picture a master painter guiding an apprentice by showing not only the final painting but also which brush strokes were almost chosen. The apprentice learns subtle preferences, not just correct answers.

## Core ingredients
1. **Teacher outputs**: logits or probability distribution over classes/tokens.
2. **Student architecture**: smaller, faster, or structured differently (CNN → transformer, multilingual, etc.).
3. **Loss functions**:
   - Soft target loss: temperature-scaled KL divergence.
   - Hard target loss: standard cross-entropy on ground truth.
   - Auxiliary losses: feature matching, intermediate hints.
4. **Temperature ($T$)**: softens teacher distribution to expose relative confidence.

### KD loss
$$
L = \alpha \cdot T^2 \cdot \text{KL}(\sigma(z_t/T) \parallel \sigma(z_s/T)) + (1-\alpha) \cdot L_{\text{CE}}(y, \sigma(z_s))
$$
where $z_t, z_s$ are teacher/student logits, $y$ ground-truth labels, and $\alpha$ blends soft vs. hard supervision.

## Variants
- **Response-based KD**: match teacher probabilities (classic KD, DistilBERT).
- **Feature-based KD**: align intermediate layers (FitNets, TinyBERT).
- **Relation-based KD**: preserve pairwise relations (RKD) or attention maps.
- **Sequence-level KD**: teacher generates sequences to train smaller seq2seq (English → translation distillation, summarization).
- **Multi-teacher KD**: ensemble of teachers, weighted averaging of logits.
- **Self-distillation**: same architecture acts as teacher for itself (Born-Again Networks).

## Practical steps
1. Train/obtain teacher checkpoint.
2. Prepare student architecture with lower capacity.
3. Choose datasets (can include unlabeled data to benefit from teacher’s pseudo-labels).
4. Configure KD loss hyperparameters $\alpha$, $T$.
5. Train student; optionally iterate (teacher → student → new teacher).
6. Evaluate on downstream tasks; compare inference latency and accuracy.

## Tips & pitfalls
- Higher $T$ (e.g., 2–10) reveals more nuanced teacher signals; too high = uniform distribution.
- Student must have sufficient capacity; otherwise rely on feature-level hints.
- For LLM reasoning, combine CoT outputs from teacher with KD to instill reasoning traces.
- Distillation pairs well with pruning/quantization for compound compression.

## Experiments & ideas
- DistilBERT-style experiment: distill a 12-layer BERT teacher into a 6-layer student on GLUE; measure parameter reduction vs. score drop.
- Sequence KD: have a GPT-4 teacher produce explanations for math problems and train a 13B student; evaluate on GSM8K.
- Multi-teacher: combine two domain experts (medical, financial) to build a balanced student.
- KD + unlabeled data: use teacher to pseudo-label a large corpus, then distill to a small model for better robustness.

## References
- Hinton, Vinyals, Dean. 2015. *Distilling the Knowledge in a Neural Network.* arXiv:1503.02531.
- Sanh et al., 2019. *DistilBERT.*
- Jiao et al., 2020. *TinyBERT.*
- Xu et al., 2023. *Orca: Progressive Learning from Complex Explanation Traces of GPT-4.*
