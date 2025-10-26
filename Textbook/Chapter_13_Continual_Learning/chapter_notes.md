# Chapter 13: Continual Learning

## Overview
Continual learning (CL) trains models on a stream of tasks/domains without catastrophic forgetting—where learning new tasks erases old knowledge. Techniques range from regularization (penalize important weights) to replay (store or synthesize past data) and architectural expansion (add units). Kirkpatrick et al. (2017) introduced Elastic Weight Consolidation (EWC) to slow updates on parameters crucial to previous tasks by leveraging Fisher information ([Kirkpatrick et al., 2017](https://arxiv.org/abs/1612.00796)).

*ELI5:* Teaching a robot multiple chores one after another can cause it to forget earlier chores. Continual learning is like giving it a notebook or muscle memory so it remembers how to wash dishes even after learning to vacuum.

## Challenge taxonomy
- **Task-incremental**: task IDs known; evaluate per task.
- **Domain-incremental**: same label space, changing data distribution; no task IDs.
- **Class-incremental**: new classes arrive over time; inference must distinguish all classes.

## Method families
1. **Regularization-based**
   - *EWC*: adds quadratic penalty $ \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta_i^*)^2 $, where $F_i$ is Fisher info from previous task ([Kirkpatrick et al., 2017](https://arxiv.org/abs/1612.00796)).
   - *Synaptic Intelligence (SI)*: tracks online importance estimates.
   - *MAS*: Memory Aware Synapses using gradient of output norms.
2. **Replay-based**
   - *Experience replay*: store exemplars per task (iCaRL, GEM).
   - *Generative replay*: train a generator to recreate past data.
3. **Parameter isolation / expansion**
   - *Progressive Nets*: add new subnetworks per task with lateral connections.
   - *PackNet*: iterative pruning allocates weights to tasks.
4. **Prompt/adapter-based CL for LLMs**
   - Task-specific prompts or adapters keep shared backbone while swapping small modules; reduces interference.

## Key formulas
- **EWC loss:**  
  $$L = L_{\text{current}}(\theta) + \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta_i^*)^2$$
- **Replay budget:** determine memory size $M$; uniform or herding selection for exemplars.

## Practical tips
- Calibrate regularization strength ($\lambda$) per task to avoid blocking learning.
- For replay, ensure privacy constraints are satisfied; otherwise use synthetic replay.
- Evaluate forgetting by measuring drop in accuracy on earlier tasks after training on later tasks.
- For LLMs, consider LoRA adapters per task + gated routing to prevent interference.

## Experiments & ideas
1. **EWC vs. baseline:** train on Split MNIST sequentially; compare forgetting metrics.
2. **Replay memory sweep:** fix model but vary exemplar buffer size to observe trade-offs.
3. **Adapter-based CL:** assign distinct LoRA adapters for sequential domains; measure how well base tasks remain intact when swapping adapters.
4. **Generative replay with LLMs:** use a teacher LLM to regenerate past dataset items and fine-tune student sequentially.

## References
- Kirkpatrick et al., 2017. *Overcoming catastrophic forgetting in neural networks.* arXiv:1612.00796.
- Zenke et al., 2017. *Synaptic Intelligence.*
- Rebuffi et al., 2017. *iCaRL.*
- Rusu et al., 2016. *Progressive Neural Networks.*
