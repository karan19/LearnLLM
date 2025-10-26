# Chapter 20: Neural Architecture Search (NAS)

## Overview
Neural Architecture Search automates the design of neural network topologies by exploring a search space of building blocks and connections. Early work by Zoph & Le (2017) used reinforcement learning controllers to propose architectures trained on CIFAR-10, achieving performance comparable to human designs but at high compute cost ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)). Subsequent methods (ENAS, DARTS, AutoML-Zero) introduced parameter sharing and differentiable search to reduce cost ([Pham et al., 2018](https://arxiv.org/abs/1802.03268)).

*ELI5:* Instead of human engineers trying endless layer combinations by hand, NAS is like a robotic architect drawing blueprints, testing them, keeping what works, and iterating.

## NAS components
1. **Search space**: how candidate architectures are parameterized (cells, blocks, operations like conv3x3, skip connections).
2. **Search strategy**: how to explore the space (reinforcement learning, evolutionary algorithms, gradient-based, random search).
3. **Evaluation strategy**: how to estimate candidate performance (train-from-scratch, weight sharing, low-fidelity proxies).

## Classic methods
- **RL-based NAS (NASNet)**: controller RNN generates architecture descriptions; reward is validation accuracy. Expensive due to training each candidate from scratch ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)).
- **ENAS**: reuse weights across sampled subgraphs, cutting cost by 1000x while maintaining performance ([Pham et al., 2018](https://arxiv.org/abs/1802.03268)).
- **DARTS**: relax discrete choices to continuous parameters, enabling gradient descent over architectures.
- **Evolutionary NAS**: mutate architectures over generations (AmoebaNet).

## Modern trends
- **Differentiable NAS**: mix candidate ops with softmax weights and optimize jointly.
- **One-shot NAS**: train a supernet once; evaluate subnets via inherited weights.
- **Hardware-aware NAS**: include latency/energy in the objective (FBNet, Once-for-all).
- **AutoML for LLMs**: search for attention/head structures, mixture-of-experts routing.

## Challenges
- Search bias and overfitting to proxy tasks.
- Need for reproducibility and fair comparison (NAS-Bench benchmarks).
- Transferability: architectures found on CIFAR-10 should generalize to ImageNet.

## Workflow
1. Define search space (e.g., cell macro-graph with candidate ops).
2. Choose search strategy (RL, DARTS, evolutionary) and evaluation budget.
3. Run search to produce top architectures.
4. Retrain best candidates from scratch on target dataset.
5. Deploy/hardware-optimize final model.

## Experiments & ideas
- Implement DARTS on CIFAR-10; analyze learned architecture vs. manually-designed baseline.
- Perform ENAS search with limited GPU budget to observe parameter sharing benefits.
- Hardware-aware NAS: integrate latency predictor for mobile deployment.
- Benchmark on NAS-Bench-201 to compare search strategies under equal budgets.

## References
- Zoph, Le. 2017. *Neural Architecture Search with Reinforcement Learning.* arXiv:1611.01578.
- Pham et al., 2018. *Efficient NAS via Parameter Sharing (ENAS).* arXiv:1802.03268.
- Liu et al., 2018. *DARTS.*
- Cai et al., 2019. *Once-for-all Network.*
