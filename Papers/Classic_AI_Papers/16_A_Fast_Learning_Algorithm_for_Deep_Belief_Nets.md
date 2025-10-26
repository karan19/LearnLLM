# A Fast Learning Algorithm for Deep Belief Nets

- **Authors:** Geoffrey E. Hinton, Simon Osindero, Yee-Whye Teh
- **Year:** 2006
- **Source:** https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf

## Abstract
We show how to use complementary priors to eliminate explaining-away effects in deep directed belief networks and derive a fast, greedy algorithm that learns one layer at a time using restricted Boltzmann machines. The learned model is further fine-tuned with a contrastive version of the wake-sleep algorithm and achieves state-of-the-art generative and classification performance on handwritten digits.

## ELI5
Training a deep generative model all at once is like trying to choreograph a hundred dancers simultaneously—they keep bumping into each other. Hinton and colleagues propose teaching the troupe layer by layer: first pair up dancers into restricted Boltzmann machines that learn to improvise together, then stack those duos into taller formations. Each new layer learns to encode the statistics of the layer below, giving the whole network a sensible initialization. Finally, a gentle fine-tuning pass polishes the routine. The result is a deep model that can imagine crisp handwritten digits and label them accurately, all because the teachers organized rehearsal in digestible stages.
