# Chapter 19: Reinforcement Learning (RL)

## Overview
Reinforcement learning optimizes policies by interacting with an environment, receiving rewards, and learning to maximize expected return. Deep RL integrates neural networks as function approximators, enabling agents to master high-dimensional tasks such as Atari games and Go ([Mnih et al., 2013](https://arxiv.org/abs/1312.5602)).

*ELI5:* Teaching a dog tricks by giving treats when it performs correctly. Over time the dog learns which actions earn rewards.

## RL formulation
- **State $s_t$**, **action $a_t$**, **reward $r_t$**, **policy $\pi(a|s)$**.
- Objective: maximize expected discounted return $\mathbb{E}[\sum_{t} \gamma^t r_t]$.

## Key algorithms
1. **Value-based**
   - *Q-learning*: learn $Q(s,a)$; choose $\arg\max_a Q(s,a)$.
   - *Deep Q-Network (DQN)*: approximates $Q$ with CNN; uses experience replay and target networks ([Mnih et al., 2013](https://arxiv.org/abs/1312.5602)).
2. **Policy gradient**
   - *REINFORCE*: update via $\nabla J(\theta) = \mathbb{E}[\nabla_\theta \log \pi_\theta(a|s) R]$.
   - *Actor-Critic*: actor updates policy, critic estimates value to reduce variance (A2C, A3C).
3. **Advanced methods**
   - *PPO*: clipped surrogate objective for stable updates.
   - *SAC*: entropy-regularized continuous control.
   - *AlphaZero*: combines tree search with policy/value nets.

## Enhancements
- **Experience replay**: store transitions and sample minibatches.
- **Target networks**: stabilize $Q$ updates.
- **Reward shaping / curriculum**: guide learning with intermediate goals.
- **Imitation + RL**: DAgger, RLHF for aligning LLMs with human preferences.

## Evaluation metrics
- Average episodic return, success rate, sample efficiency, stability (variance across seeds).

## Experiments
1. Implement DQN on CartPole; compare training with/without experience replay.
2. Run PPO on a continuous-control task (Pendulum) to illustrate policy gradient stability.
3. Combine imitation + RL: pretrain policy via behavior cloning on expert data, then fine-tune with RL.
4. Analyze reward shaping: add intermediate rewards to sparse-reward environment and measure convergence speed.

## References
- Sutton & Barto, 2018. *Reinforcement Learning: An Introduction.*
- Mnih et al., 2013. *Playing Atari with Deep RL.* arXiv:1312.5602.
- Schulman et al., 2017. *Proximal Policy Optimization.*
- Haarnoja et al., 2018. *Soft Actor-Critic.*
