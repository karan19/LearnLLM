# Learning and Relearning in Boltzmann Machines

- **Authors:** Geoffrey E. Hinton, Terrence J. Sejnowski
- **Year:** 1986
- **Source:** https://doi.org/10.1038/333525a0

## Abstract
Boltzmann machines are stochastic recurrent networks that learn internal models of data by minimizing the difference between statistics measured in free-running and clamped phases. We describe learning rules, illustrate how hidden units discover distributed representations, and analyze the computational requirements of simulated annealing for escaping poor minima.

## ELI5
Training a Boltzmann machine feels like running a restaurant where chefs first cook whatever dishes they fancy, then cook again while copying a customer’s order. The learning rule compares the two kitchens: if a dish appears too often in imagination but not when the customer guides the meal, the recipe is damped; if it’s missing from free play but needed for the order, the recipe is encouraged. Hidden units act like sous-chefs inventing secret ingredients to satisfy both scenarios. By alternately daydreaming and following examples, the network settles on internal recipes that recreate the training data, showcasing how randomness plus feedback can sculpt deep representations.
