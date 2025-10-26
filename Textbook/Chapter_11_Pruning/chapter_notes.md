# Chapter 11: Pruning

## Overview
Pruning removes redundant parameters or connections from neural networks, reducing storage, latency, and energy while keeping accuracy. Classical approaches magnitude-prune weights post-training (“Deep Compression”), while modern methods adapt sparsity during fine-tuning (Movement Pruning) or identify sparse subnetworks early (Lottery Ticket Hypothesis). Pruning is especially valuable for deploying LLMs and vision models on edge devices ([Han et al., 2016](https://arxiv.org/abs/1510.00149); [Frankle & Carbin, 2019](https://arxiv.org/abs/1803.03635); [Sanh et al., 2020](https://arxiv.org/abs/2005.07683)).

*ELI5:* Think of a neural network as a dense jungle of vines. Pruning trims away vines that don’t carry fruit so the remaining paths are easier to navigate.

## Pruning dimensions
1. **Unstructured vs. structured:**
   - *Unstructured* removes individual weights; yields high sparsity but needs sparse kernels.
   - *Structured* removes entire neurons, channels, or heads; easier to accelerate but coarser.
2. **Training stage:** pre-training, post-training, or during fine-tuning.
3. **Criteria:** magnitude, gradient (movement), importance scores, sensitivity analysis.

## Key methods
- **Magnitude pruning:** remove weights with smallest absolute value, optionally iteratively with fine-tuning (Deep Compression pipeline) ([Han et al., 2016](https://arxiv.org/abs/1510.00149)).
- **Lottery Ticket Hypothesis (LTH):** find sparse subnetworks (“winning tickets”) that, when reinitialized with original weights, train to same accuracy as dense models ([Frankle & Carbin, 2019](https://arxiv.org/abs/1803.03635)).
- **Movement pruning:** track weight updates during fine-tuning; prune weights moving toward zero, adapting better to transfer learning ([Sanh et al., 2020](https://arxiv.org/abs/2005.07683)).
- **Structured pruning:** remove attention heads, MLP channels, or convolution filters based on saliency; integrate with distillation to preserve performance.
- **Dynamic sparsity:** methods like RigL regrow connections during training to reach high sparsity without losing accuracy.

## Math snippets
- **Magnitude criterion:**  
  $$\mathcal{M} = \{w_i : |w_i| < \tau \}$$  remove weights below threshold $\tau$.
- **Movement score (Sanh et al., 2020):** accumulate sign-adjusted gradients $m_i = \sum_t g_i^{(t)} \cdot w_i^{(t)}$; prune smallest $m_i$.
- **Sparsity:** $s = 1 - \frac{\text{nonzero weights}}{\text{total weights}}$; typical regimes 50–95%.

## Practical workflow
1. **Baseline training:** start from dense checkpoint.
2. **Choose pruning schedule:** one-shot vs. iterative.
3. **Apply mask:** zero out selected weights; optionally remove from storage.
4. **Fine-tune / recover:** retrain remaining weights to regain accuracy.
5. **Export:** store sparse format (CSR) or physically remove channels for structured pruning.
6. **Benchmark:** measure latency on target hardware; evaluate accuracy and calibration.

## Tips & pitfalls
- Over-pruning can induce catastrophic accuracy drops; gradually increase sparsity with retraining.
- Use mixed objectives (magnitude + movement) for robustness.
- Pair pruning with quantization/distillation for compound gains.
- Ensure inference frameworks support desired sparsity (e.g., NVIDIA cuSPARSELt for 50% structured 2:4 sparsity).
- Monitor layer-wise sensitivity; some layers (embedding, final projection) may require dense weights.

## Experiments & projects
1. **Iterative magnitude pruning:** prune a classifier to 80% sparsity in 10 stages; track accuracy curve.
2. **Lottery ticket search:** implement one cycle of LTH on a small transformer to observe winning ticket behavior.
3. **Movement pruning for LLM fine-tuning:** apply Hugging Face `movement_pruner` during domain adaptation; compare to magnitude pruning.
4. **Structured head pruning:** drop low-importance attention heads in LLaMA and benchmark perplexity vs. speed.
5. **Sparse inference profiling:** deploy pruned model via ONNX Runtime with sparsity support; measure throughput gains.

## References
- Han, Mao, Dally. 2016. *Deep Compression.* arXiv:1510.00149.
- Frankle & Carbin. 2019. *The Lottery Ticket Hypothesis.* arXiv:1803.03635.
- Sanh, Wolf, Rush. 2020. *Movement Pruning.* arXiv:2005.07683.
- Additional tooling: Hugging Face Optimum, SparseML, cuSPARSELt demos.
