# Chapter 18: Federated Learning (FL)

## Overview
Federated learning trains models across many clients (phones, hospitals) without centralizing raw data. Each client computes local updates on its private data, then a server aggregates updates (e.g., FedAvg) to produce a global model. This enables privacy-preserving, on-device personalization while minimizing bandwidth ([McMahan et al., 2017](https://arxiv.org/abs/1602.05629)).

*ELI5:* Imagine thousands of students solving homework at home. Instead of sending their notebooks to the teacher, they only send summaries of what they learned. The teacher averages those summaries to improve the shared lesson plan.

## Core protocol (FedAvg)
1. **Server initialization**: broadcast model parameters $w_0$ to participating clients.
2. **Client update**: each client $k$ runs local SGD on its dataset for $E$ epochs, producing $w_k$.
3. **Aggregation**: server averages updates weighted by client dataset size:
   $$w_{t+1} = \sum_k \frac{n_k}{N} w_k$$
4. Repeat rounds until convergence.

## Challenges
- **Statistical heterogeneity**: non-IID data across clients leads to slower convergence.
- **System heterogeneity**: varying hardware, connectivity, participation.
- **Privacy & security**: risk of gradient leakage; need differential privacy, secure aggregation.
- **Communication cost**: large models (LLMs) require compression or sparsification of updates.

## Solutions & extensions
- **Personalization**: fine-tune local layers, meta-learning (FedAvgM, FedProx) to handle heterogeneity.
- **Secure aggregation**: cryptographic protocols ensuring server sees only aggregated updates.
- **Differential privacy (FedSGD-DP)**: add noise per-client or server-level.
- **Compression**: quantize or sparsify gradients before upload.
- **Federated analytics**: compute statistics (counts, histograms) securely.

## Applications
- Keyboard next-word prediction (Gboard), health data modeling, IoT sensor networks, collaborative recommendation.

## Experiments
1. Simulate FedAvg on MNIST with non-IID partitions (each client sees digits 0–1, 2–3, etc.); observe accuracy vs. centralized training.
2. Evaluate differential privacy: add Gaussian noise to updates and measure privacy-utility trade-off.
3. Implement secure aggregation via simple masking to understand protocol flow.
4. Test personalization: freeze shared layers, fine-tune local heads per client.

## References
- McMahan et al., 2017. *Communication-Efficient Learning of Deep Networks from Decentralized Data.* arXiv:1602.05629.
- Li et al., 2019. *FedProx.*
- Bonawitz et al., 2017. *Practical Secure Aggregation.*
