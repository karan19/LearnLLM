# Chapter 05: Fine-Tuning Techniques

## Overview
Fine-tuning adapts pre-trained language models to new tasks, styles, or constraints. Techniques span full-parameter updates, parameter-efficient adapters (PEFT), quantization-aware methods (QLoRA), reinforcement learning (RLHF), and direct preference optimization. Choosing the right method balances data availability, compute, latency, safety, and IP control.

*ELI5:* Imagine buying a factory-made robot that can do many chores. Fine-tuning is teaching it your household rules—some people repaint the whole robot (full FT), others just add a smart backpack (adapters) or tweak its remote control (LoRA) so it behaves the way they like.

## Taxonomy
1. **Full fine-tuning** – update all weights on new data.
2. **Partial fine-tuning** – unfreeze selected layers (e.g., task head, last few blocks).
3. **Parameter-efficient fine-tuning (PEFT)** – add small trainable modules (adapters, LoRA, prefix tuning) while freezing the base model.
4. **Quantized PEFT (QLoRA)** – fine-tune low-bit models with LoRA adapters.
5. **Instruction/SFT** – supervised fine-tuning on curated instruction-response pairs.
6. **Preference optimization** – RLHF, DPO, IPO, RAFT align outputs with human preferences.
7. **Continual/Lifelong** – avoid catastrophic forgetting via rehearsal or elastic regularization.

## Techniques & ELI5 metaphors
- **Full FT**: re-train the entire network on your dataset.
  - *ELI5:* Rebuilding the whole robot so every joint fits your house—powerful but expensive.
- **Adapters (Houlsby, Pfeiffer)**: small bottleneck modules inserted between layers.
  - *ELI5:* Sew pockets onto the robot’s outfit; the original clothes stay the same but pockets hold new tricks.
- **LoRA / DoRA**: learn low-rank matrices ($\Delta W = A B^T$) or direction-only adjustments.
  - *ELI5:* Instead of rewiring the whole circuit, attach a dial that nudges the signal in a preferred direction.
- **Prefix / Prompt tuning**: optimize virtual tokens prepended to each layer.
  - *ELI5:* Slip sticky notes into the robot’s instruction manual without changing the manual itself.
- **QLoRA**: quantize base weights (4-bit) and train LoRA adapters with double quantization + paged optimizers [Dettmers et al., 2023].
  - *ELI5:* Shrink the robot into travel size, then give it detachable upgrades so it still learns new dances.
- **Instruction SFT**: train on curated question–answer pairs (e.g., Alpaca, Dolly) to follow natural language commands.
  - *ELI5:* Read the robot a etiquette book so it says “please” and “thank you.”
- **RLHF (PPO-style)**: policy fine-tuning guided by reward model trained on human preference comparisons.
  - *ELI5:* After each chore, humans give thumbs-up/down; the robot tweaks future behavior to earn more thumbs-up.
- **DPO / IPO / KTO**: direct preference optimization without RL—maximize likelihood gap between preferred vs. rejected responses.
  - *ELI5:* Instead of trial-and-error, you show the robot two transcripts (“do this, not that”) and it learns the difference directly.
- **Constraint-aware finetuning**: incorporate safety constraints (Safe RLHF, constitutional AI) or bias mitigation terms.
- **Continual FT**: methods like EWC, LwF keep Fisher-weighted penalties to prevent forgetting older tasks.

## Key equations
- **LoRA update**:  
  $$W' = W + \alpha \cdot \frac{1}{r} A B^T$$  
  where $A \in \mathbb{R}^{d \times r}$, $B \in \mathbb{R}^{r \times k}$, rank $r \ll d$.
- **DPO objective**: for preference pair $(y^+, y^-)$ and base policy $\pi_0$, learn policy $\pi_\theta$ maximizing  
  $$\mathcal{L}_{DPO} = \mathbb{E}[\log \sigma(\beta (\log \pi_\theta(y^+|x) - \log \pi_\theta(y^-|x) - \log \pi_0(y^+|x) + \log \pi_0(y^-|x)))]$$
- **EWC penalty**: add $\lambda \sum_i F_i (\theta_i - \theta_{i,old})^2$ where $F_i$ is Fisher information.

## Workflow checkpoints
1. **Data prep**: dedup, filter PII, normalize formats, ensure license compliance.
2. **Tokenizer alignment**: confirm new tokens (domain jargon) exist; extend vocab if needed.
3. **Training recipe**: select method (LoRA vs. full FT) based on GPU memory & dataset size.
4. **Eval suite**: track task metrics + safety/regression tests (MT-Bench, TruthfulQA, domain-specific sets).
5. **Deployment artifacts**: save adapters separately, log config (rank, alpha, quantization).

## Experiments & code labs
- **PEFT sweep**: train LoRA (rank 4/8/16) on a domain dataset (e.g., legal QA) and compare to full FT baseline.
- **QLoRA memory profiling**: quantize a 13B model with bitsandbytes, measure VRAM savings vs. BF16.
- **DPO vs. PPO**: run small-scale preference tuning on conversation dataset; compare stability and throughput.
- **Catastrophic forgetting test**: fine-tune on domain data, then re-evaluate on base benchmarks (MMLU) to quantify drift.
- **Adapter fusion**: train separate adapters for two domains, then merge via weighted sum (AdapterFusion) and test combined skill.

## References
- Hu et al., 2021 — LoRA
- Houlsby et al., 2019 — Adapters
- Lester et al., 2021 — Prompt/Prefix tuning
- Dettmers et al., 2023 — QLoRA
- Ouyang et al., 2022 — RLHF
- Rafailov et al., 2023 — DPO
- Alabdulmohsin et al., 2023 — DoRA
- Open-source repos: PEFT (Hugging Face), TRL, Axolotl, LlamaFactory
