# Neuronlike Adaptive Elements That Can Solve Difficult Learning Control Problems

- **Authors:** Andrew G. Barto, Richard S. Sutton, Charles W. Anderson
- **Year:** 1983
- **Source:** https://doi.org/10.1109/TSSC.1983.300785

## Abstract
We describe adaptive critic designs in which a pair of interacting neuronlike elements learn to solve control problems by reinforcement. One element (the actor) selects actions; the other (the critic) learns to evaluate states by predicting future reinforcement. The method is demonstrated on the cart-pole balancing task, showing that the coupled system learns without an explicit model of the plant.

## ELI5
To balance a broomstick on a moving cart, these researchers built two cooperating neurons. The actor is impulsive—it pushes left or right based on its current instincts. The critic stands behind with a clipboard, watching the broom and shouting encouragement or warnings depending on whether the motion seems to lead toward success. When the broom nearly falls, the critic’s panic causes the actor to rethink the choices that led there; when the broom steadies, both reinforce the moves they just made. Over time the duo invents a balancing strategy even though no one ever tells them the physics equations. It’s like a coach-player pair inventing a drill from scratch with nothing but cheers and boos.
