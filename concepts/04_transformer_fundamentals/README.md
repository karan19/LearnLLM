# Layer 04 · Transformer Fundamentals

Master the core architecture that powers modern LLMs.

## Agenda
1. Refresher: probability, vectors, gradients
2. Transformer pipeline overview
3. Attention deep dive
4. Discussion prompts / self-check questions

## Key Concepts
- **Tokenization:** Byte-Pair Encoding, unigram models, and how token vocab affects context windows.
- **Embedding space:** Meaning of dimensionality, positional encodings (sinusoidal vs learned).
- **Self-attention math:** Query/Key/Value projections, scaling factor, softmax normalization.
- **Training objective:** Next-token prediction and cross-entropy loss; why it fosters emergent behavior.

## Concept Drills
- Re-derive scaled dot-product attention on paper and annotate each term with its intuition.
- Explain how residual connections and layer norm stabilize deep transformers without referencing code.
- Create a glossary entry for each new term you encounter, including analogies that make the idea memorable.

## Reflection Questions
- Where does inductive bias come from in transformers?
- Why does context length impact both memory and quality?
- Which parts of the math felt least intuitive, and what resources can clarify them?
