# Simple Context Compression: Mean-Pooling and Multi-Ratio Training

- **Authors:** Yair Feldman, Yoav Artzi
- **Published:** 2025-10-23T17:57:23Z
- **Source:** http://arxiv.org/abs/2510.20797v1

## Abstract
A common strategy to reduce the computational costs of using long contexts in
retrieval-augmented generation (RAG) with large language models (LLMs) is soft
context compression, where the input sequence is transformed into a shorter
continuous representation. We develop a lightweight and simple mean-pooling
approach that consistently outperforms the widely used compression-tokens
architecture, and study training the same compressor to output multiple
compression ratios. We conduct extensive experiments across in-domain and
out-of-domain QA datasets, as well as across model families, scales, and
compression ratios. Overall, our simple mean-pooling approach achieves the
strongest performance, with a relatively small drop when training for multiple
compression ratios. More broadly though, across architectures and training
regimes the trade-offs are more nuanced, illustrating the complex landscape of
compression methods.

## ELI5
An LLM asked to reason over thousands of supporting tokens is like a historian forced to reread an entire encyclopedia before answering each trivia question. The authors show you can instead pre-chew large chunks by averaging their embeddings (mean pooling), producing compact vectors that retain the gist while shedding fluff. They go further and train the compressor at multiple compression ratios, so the model becomes comfortable reading contexts that are 50%, 20%, or even 10% of their original length; it's as if the historian maintains full notebooks, half-page digests, and postcard summaries simultaneously. During training, the LLM sees all these variants, learning how to stitch answers together regardless of how condensed the clues are. The experiments suggest this simple approach outperforms more elaborate compression-token schemes and suffers only small accuracy drops even when context is aggressively shrunk. In practice, that means faster inference, smaller memory bills, and the freedom to decide on the fly how much detail to preserve without retraining separate models.
