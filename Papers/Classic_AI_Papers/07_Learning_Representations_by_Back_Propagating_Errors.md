# Learning Representations by Back-Propagating Errors

- **Authors:** David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams
- **Year:** 1986
- **Source:** https://doi.org/10.1038/323533a0

## Abstract
We show that a learning procedure based on back-propagating error derivatives through networks of differentiable units can efficiently discover internal representations that capture hidden structure in data. The algorithm is applied to tasks including the encoding of distributed representations of letters and the solution of difficult problems such as learning parity and the temporal XOR. The results demonstrate that multilayer networks trained with gradient descent can learn complex mappings that are inaccessible to single-layer perceptrons.

## ELI5
Rumelhart, Hinton, and Williams taught neural networks how to apologize properly. When the network makes a mistake, the output neuron figures out how bad the error was and passes a polite "my fault" message backward through each layer, scaled by how much each neuron contributed to the goof. It’s like tracing a spilled glass of juice back to the shaky waiter, the wobbly cart, and ultimately the cook who filled the cup too high. Each participant nudges their behavior in proportion to their blame. Repeating this ritual lets deep stacks of neurons coordinate and learn patterns—like parity—that single-layer perceptrons could never master. Backprop became the feedback conversation that allows today’s deep nets to grow wise layer by layer.
