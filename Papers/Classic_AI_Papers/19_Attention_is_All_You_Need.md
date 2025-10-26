# Attention Is All You Need

- **Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
- **Year:** 2017
- **Source:** https://arxiv.org/abs/1706.03762

## Abstract
The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose the Transformer, a simple network architecture based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show superior quality, improved parallelism, and reduced training cost. The model also generalizes well to other NLP tasks.

## ELI5
Transformers translate by playing a smart version of the party game "spot who matters." Every word in a sentence looks at every other word and assigns attention scores, deciding who provides the most context. Instead of passing information sequentially the way RNNs do, all words talk at once through attention matrices, which GPUs can compute amazingly quickly. Stacking these layers with feed-forward blocks gives the model the ability to track long-range relationships like "The animal that chased the dog was a bear" without forgetting who chased whom. The result is a model that learns languages faster, parallelizes better, and becomes the backbone of nearly every modern LLM.
