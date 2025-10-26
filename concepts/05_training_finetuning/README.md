# Layer 05 · Training & Fine-tuning Strategies

Connect theory to the workflows used to adapt and evaluate models.

## Agenda
1. Training stack overview (data → tokenizer → model → optimizer)
2. Fine-tuning patterns (full, adapters, LoRA, PEFT)
3. Evaluation and prompt iteration loops
4. Tooling landscape (Hugging Face, Lightning/Fabric, Weights & Biases)

## Key Concepts
- **Data curation:** Cleaning, deduping, and balancing domain examples.
- **Tokenization workflow:** Training custom tokenizers and inspecting merge rules.
- **Parameter-efficient tuning:** Why adapters/LoRA reduce cost and when they fail.
- **Evaluation axes:** Quality (win rate, BLEU), cost, latency, safety signals.

## Concept Drills
- Draw a flowchart detailing the life of a sample from raw text through tokenizer, model, optimizer update, and metrics logging.
- Compare full fine-tuning vs. LoRA on paper: list assumptions, advantages, risks, and when each is appropriate.
- Design a prompt evaluation matrix conceptually: define criteria, scoring rules, and how you would interpret disagreements.

## Reflection Questions
- Which bottleneck (data, compute, or modeling) most often dominates and why?
- How would you defend your chosen evaluation criteria to a skeptical reviewer?
- What evidence would convince you that a model is “good enough” for release even without hands-on experiments?
