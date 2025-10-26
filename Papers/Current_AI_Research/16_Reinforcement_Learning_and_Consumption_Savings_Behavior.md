# Reinforcement Learning and Consumption-Savings Behavior

- **Authors:** Brandon Kaplowitz
- **Published:** 2025-10-23T17:14:49Z
- **Source:** http://arxiv.org/abs/2510.20748v1

## Abstract
This paper demonstrates how reinforcement learning can explain two puzzling
empirical patterns in household consumption behavior during economic downturns.
I develop a model where agents use Q-learning with neural network approximation
to make consumption-savings decisions under income uncertainty, departing from
standard rational expectations assumptions. The model replicates two key
findings from recent literature: (1) unemployed households with previously low
liquid assets exhibit substantially higher marginal propensities to consume
(MPCs) out of stimulus transfers compared to high-asset households (0.50 vs
0.34), even when neither group faces borrowing constraints, consistent with
Ganong et al. (2024); and (2) households with more past unemployment
experiences maintain persistently lower consumption levels after controlling
for current economic conditions, a "scarring" effect documented by Malmendier
and Shen (2024). Unlike existing explanations based on belief updating about
income risk or ex-ante heterogeneity, the reinforcement learning mechanism
generates both higher MPCs and lower consumption levels simultaneously through
value function approximation errors that evolve with experience. Simulation
results closely match the empirical estimates, suggesting that adaptive
learning through reinforcement learning provides a unifying framework for
understanding how past experiences shape current consumption behavior beyond
what current economic conditions would predict.

## ELI5
Rather than assuming households have the perfect foresight economics textbooks grant them, this paper imagines each family as a reinforcement learning agent facing uncertain income. Every month, the agent decides how much to spend versus save, then experiences rewards or penalties depending on future shocks, slowly updating a policy much like a gamer learning a level by trial and error. Over many simulations, familiar macroeconomic patterns emerge: cautious saving after bad recessions, rebuilding buffers when volatility rises, and occasional overreactions that mirror observed anomalies. Because the policy is learned, not derived analytically, it captures behaviors economists struggle to encode in closed-form models. The study suggests that some puzzling consumption data might simply be households running approximate RL algorithms rather than optimizing equations, offering a bridge between behavioral observations and computational explanations.
