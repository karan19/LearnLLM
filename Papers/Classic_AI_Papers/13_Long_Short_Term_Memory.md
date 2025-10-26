# Long Short-Term Memory

- **Authors:** Sepp Hochreiter, Jürgen Schmidhuber
- **Year:** 1997
- **Source:** https://www.bioinf.jku.at/publications/older/2604.pdf

## Abstract
We present a recurrent network architecture called Long Short-Term Memory (LSTM) that overcomes the vanishing gradient problem by introducing memory cells and multiplicative gates. LSTM is able to store information over long time intervals and solves tasks such as unbounded temporal distance problems and real-world sequence learning that defeat conventional RNNs.

## ELI5
Standard recurrent networks are forgetful goldfish—they quickly lose track of events that happened more than a few steps ago. LSTMs add a notebook with latches: a cell state stores important facts, an input gate decides what new info is worthy of ink, a forget gate erases stale notes, and an output gate decides when to read entries aloud. Because gradients flow along the notebook with almost no decay, the network can remember things said hundreds of words earlier, like whether a sentence started in the past tense. It’s the difference between relying on mental whispers and jotting reminders on sticky notes you can reread whenever needed.
