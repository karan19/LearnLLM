# The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain

- **Authors:** Frank Rosenblatt
- **Year:** 1958
- **Source:** https://doi.org/10.1038/181321a0

## Abstract
This paper introduces the perceptron, a simple neural network that computes weighted sums of sensed inputs and adjusts those weights with an error-driven learning rule. The perceptron is shown to converge to solutions that correctly classify linearly separable patterns, and hardware implementations using photoelectric sensors demonstrate visual pattern recognition. The work suggests that statistical decision-making principles can be realized in distributed, adaptive networks similar to biological neurons.

## ELI5
Rosenblatt’s perceptron is like a tiny voting committee of sensors staring at a sheet of paper. Each sensor casts a vote based on whether it sees ink or blank space, and a knob controls how loudly that vote counts. If the perceptron mislabels a picture—calling a circle a triangle—the knobs get tweaked: sensors that should have spoken up get amplified, and those that misled get quieted. After repeated practice on example flashcards, the committee lines its votes up so well that a single yes/no threshold separates circles from triangles every time. The beauty is in its simplicity: the machine teaches itself by nudging weights, showing how recognition could emerge without a hand-coded rulebook.
