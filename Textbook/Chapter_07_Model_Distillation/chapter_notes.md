# Chapter 07: Model Distillation

## Overview
Knowledge distillation compresses a large “teacher” model into a smaller “student” while preserving performance. Benefits include lower latency, cost, and deployment footprint. Distillation applies to classification, sequence models, LLMs, multimodal encoders, and tool-augmented agents. Variants cover logit-matching, feature distillation, self-distillation, and multimodal/adapter distillation.

*ELI5:* Distillation is like having a master chef teach an apprentice all the signature recipes so the apprentice can cook just as well but using a smaller kitchen.

## Distillation variants
1. **Logit distillation (KD)** – minimize KL divergence between teacher and student outputs [Hinton et al., 2015].
2. **Feature distillation** – match intermediate representations (FitNets, attention transfer).
3. **Sequence-level / sequence-to-sequence distillation** – teacher generates pseudo-labels to train the student (used in MT, summarization).
4. **Self-distillation** – teacher and student share architecture (Born-Again Networks, Noisy Student).
5. **Task-specific distillation** – domain adaptation, multi-task teachers.
6. **LLM distillation** – compress a large LLM into smaller SFT or alignment-ready models (e.g., Alpaca, Orca, Vicuna).
7. **Adapter distillation** – distill LoRA or adapters into base weights, or fuse multiple adapters.

## Core formulas
- **Soft target loss**:  
  $$L_{KD} = T^2 \cdot \text{KL}(\sigma(z_t/T) \parallel \sigma(z_s/T))$$  
  where $z_t, z_s$ are teacher/student logits, temperature $T>1$ softens distributions.
- **Combined loss**:  
  $$L = \alpha L_{KD} + (1-\alpha)L_{CE}(y, \sigma(z_s))$$
- **Feature matching**: penalize $\|f_t^{(l)} - f_s^{(l)}\|_2^2$ for selected layers $l$.

## Design considerations & ELI5 analogies
- **Temperature scaling**: higher $T$ reveals dark knowledge (relative probabilities).  
  *ELI5:* The teacher whispers not just “Paris is correct” but also “London was a close second,” giving richer hints.
- **Capacity gap**: student needs enough capacity; else, focus on core layers.
- **Data choice**: use original train data, unlabeled data with pseudo-labels, or synthetic data from LLMs.
- **Progressive shrinking**: gradually reduce size (TinyBERT multi-stage)
- **Self-distillation**: same model teaches itself iteratively (Noisy Student).  
  *ELI5:* Do homework, review mistakes, rewrite notes in cleaner form.
- **Task distillation vs. alignment**: distill reasoning chains (e.g., Orca distills GPT-4 explanations into smaller LMs).

## LLM-specific distillation workflow
1. **Teacher generation**: gather high-quality instruction-responses from GPT-4 or domain experts.
2. **Filtering & scoring**: apply toxicity filters, deduplicate.
3. **Student fine-tuning**: train smaller LLM with KD loss and supervised data.
4. **Optional RLHF**: apply preference tuning if needed.
5. **Evaluation**: MT-Bench, MMLU, domain tests; compare to teacher baseline.

*ELI5:* Use a genius tutor (GPT-4) to write many solved examples. Feed them to a smaller student until it can answer similar questions without help.

## Experiments & code ideas
- **Soft vs. hard labels**: train a smaller classifier with/without KD and measure accuracy.
- **Feature distillation**: implement FitNet for a CNN; monitor intermediate feature alignment.
- **LLM instruction distillation**: collect 5k GPT-4 responses, fine-tune a 7B model, evaluate on AlpacaEval.
- **Adapter fusion**: distill multiple domain-specific adapters into a single student. Compare to ensemble.
- **Distillation under quantization**: combine QLoRA with KD to produce compact, accurate models.

## References
- Hinton et al., 2015 — Distilling the Knowledge…
- Romero et al., 2015 — FitNets
- Furlanello et al., 2018 — Born-Again Networks
- Clark et al., 2020 — DistilBERT
- Wang et al., 2020 — TinyBERT
- Li et al., 2023 — Orca/MiniGPT distillation
- Tooling: Hugging Face `distil`, DeepSpeed-MII, Microsoft LoRA distillation repos
