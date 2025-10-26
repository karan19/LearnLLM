# Sequence to Sequence Learning with Neural Networks

- **Authors:** Ilya Sutskever, Oriol Vinyals, Quoc V. Le
- **Year:** 2014
- **Source:** https://arxiv.org/abs/1409.3215

## Abstract
We present a general end-to-end approach to sequence learning that makes minimal assumptions on the structure of the sequence. An encoder recurrent neural network reads the input sequence into a fixed-length vector, and a decoder recurrent network generates the output sequence from that vector. The method achieves state-of-the-art results on English-to-French translation and is competitive on other tasks.

## ELI5
The seq2seq model behaves like a translator who listens to an entire sentence, takes a deep breath, and then speaks it in another language. The encoder RNN is the listener; it munches tokens one by one and compresses their meaning into a single thought vector. The decoder is the speaker; conditioned on that thought, it emits the translated words, updating its own hidden state as it goes. With some beam search to explore multiple phrasings, the system suddenly made neural machine translation practical and paved the way for later attention-based models. It proved that a single neural architecture could learn to map sequences to sequences without handcrafted linguistic rules.
