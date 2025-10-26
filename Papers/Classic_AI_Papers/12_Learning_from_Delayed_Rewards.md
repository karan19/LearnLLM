# Learning from Delayed Rewards

- **Authors:** Christopher J.C.H. Watkins
- **Year:** 1989
- **Source:** https://www.cs.rhul.ac.uk/home/chrisw/new_thesis.pdf

## Abstract
This thesis introduces Q-learning, a model-free reinforcement learning algorithm that learns optimal action-value functions by bootstrapping from experienced transitions. Under the assumption of finite Markov decision processes and sufficiently exploratory policies, Q-learning is proven to converge to the optimal value function even when actions are chosen using arbitrary (including greedy) policies.

## ELI5
Watkins imagined a treasure hunter exploring a maze who keeps track of how good each hallway-turn pair has been over time. Even if the reward only appears minutes later, the hunter updates the "quality" (Q) of the earlier moves by blending the surprise treasure with the best value of the next state. The beauty is that no map is needed; by wandering and scribbling on the Q-table, the explorer eventually knows which action is smartest in every corner. The math in the thesis shows that, as long as you keep trying everything sometimes, those scribbles converge to perfect guidance, giving reinforcement learning a rock-solid foundation.
