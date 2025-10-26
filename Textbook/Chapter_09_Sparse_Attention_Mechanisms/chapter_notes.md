# Chapter 09: Sparse Attention Mechanisms

## Overview
Standard Transformer self-attention scales as $O(L^2)$ in memory and compute, where $L$ is sequence length. Sparse attention restricts the connectivity pattern so the cost grows near-linearly, enabling processing of multi-thousand-token documents, genomics sequences, and video/audio streams. Recent architectures such as Longformer, Reformer, and BigBird all show that carefully designed sparse patterns maintain accuracy while drastically lowering resource use ([Beltagy et al., 2020](https://arxiv.org/abs/2004.05150); [Kitaev et al., 2020](https://arxiv.org/abs/2001.04451); [Zaheer et al., 2020](https://arxiv.org/abs/2007.14062)).

*ELI5:* Imagine students in a huge classroom. In dense attention, every student whispers to everyone else, causing chaos. Sparse attention sets up a seating chart—students only chat with neighbors plus a few representatives—so information still flows but the room stays quiet.

## Design patterns
1. **Local / sliding-window attention** – tokens attend to neighbors within a window $w$ (Longformer). Complexity $O(L \cdot w)$.
2. **Global tokens** – select special tokens (e.g., CLS, question words) that attend to all positions while others stay local. Keeps long-range context with few global nodes ([Beltagy et al., 2020](https://arxiv.org/abs/2004.05150)).
3. **Block / dilated patterns** – group tokens into blocks and add strided connections (Sparse Transformer, BigBird).
4. **Random / hashed connections** – use locality-sensitive hashing to create dynamic sparse neighbors (Reformer).
5. **Mixture patterns** – BigBird combines local, random, and global edges to guarantee theoretical expressiveness ([Zaheer et al., 2020](https://arxiv.org/abs/2007.14062)).
6. **Kernel/linear attention** – approximate softmax with kernels (Performer) or flash attention (exact but memory-efficient). Though not strictly sparse, they reduce cost and often pair with sparsity.

*ELI5:* Local attention is passing notes to the students sitting next to you. Global tokens are class reps passing info to everyone. Random connections are like occasionally calling a distant friend to keep the network connected.

## Key math
- **Local attention complexity:**  
  $$\text{Cost} = O(L \cdot w)$$  where $w \ll L$.
- **LSH attention (Reformer):** uses hash buckets to limit comparisons to items with same hash, yielding $O(L \log L)$ expected complexity.
- **BigBird block sparse pattern:** ensures each token has at least $O(\log L)$ random connections plus local/global, enabling universal approximation and Turing completeness similar to dense attention ([Zaheer et al., 2020](https://arxiv.org/abs/2007.14062)).

## Implementation considerations
- **Hardware friendliness:** block-sparse matmuls map better to GPUs than purely random sparsity.
- **Sequence padding:** need chunked batching to keep windows aligned.
- **Attention masks:** frameworks like Hugging Face provide Longformer/BigBird attention masks; for custom patterns, build boolean masks or use Triton kernels.
- **Gradient checkpointing:** pairs well to reduce memory further.
- **Hybrid with retrieval:** combine sparse attention with retrieval-Augmented models to handle extremely long context windows (e.g., local attention + memory tokens).

## Experiments & ideas
1. **Window sweep:** fine-tune Longformer on a QA dataset varying window sizes (128/256/512) to observe accuracy vs. throughput.
2. **BigBird vs. dense baseline:** evaluate perplexity on WikiText for both models at 4k tokens.
3. **Reformer hash buckets:** test different hash bucket counts to balance speed vs. accuracy on character-level language modeling.
4. **Global token ablation:** remove global tokens from Longformer and inspect performance drop on summarization to see their impact.
5. **Visualization:** plot attention heatmaps for sparse patterns to ensure connectivity.

## References
- Beltagy, Peters, Cohan. 2020. *Longformer: The Long-Document Transformer.* arXiv:2004.05150.
- Kitaev, Kaiser, Levskaya. 2020. *Reformer: The Efficient Transformer.* arXiv:2001.04451.
- Zaheer et al. 2020. *BigBird: Transformers for Longer Sequences.* arXiv:2007.14062.
