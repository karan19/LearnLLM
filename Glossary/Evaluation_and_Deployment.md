# Evaluation, Deployment & Operations Glossary

Terms covering how AI systems are measured, shipped, and maintained in production.

## Training / Validation / Test Split
**Definition:** Partitioning data to estimate generalization. Training for fitting, validation for hyperparameter tuning, test for final unbiased evaluation.
**ELI5:** Practice on one set of math problems, check progress on another, and save a final secret exam to see how well you truly learned.

## Cross-Validation
**Definition:** Repeatedly training on k−1 folds and validating on the remaining fold to obtain stable metrics when data is scarce.
**ELI5:** Rotate which slice of cake you save for tasting so each part gets judged once.

## Metric
**Definition:** Quantitative measure of performance (accuracy, F1, BLEU, ROUGE, CIDEr, CER, perplexity). Choice should align with business goals and statistical properties.
**ELI5:** The scoreboard that decides who wins—accuracy, speed, or style—depending on what matters.

## Perplexity
**Definition:** Exponential of average negative log-likelihood; measures how well a language model predicts tokens. Lower is better.
**ELI5:** A “how surprised was I?” meter—low surprise means the model guessed the next word easily.

## Calibration
**Definition:** Agreement between predicted probabilities and actual outcomes. Techniques like temperature scaling recalibrate logits post-training.
**ELI5:** If the model says “I’m 80% sure,” calibration checks that it’s right about 8 out of 10 times.

## A/B Test / Online Experiment
**Definition:** Controlled experiment that routes live traffic between variants to measure causal impact on user metrics.
**ELI5:** Show half your friends version A of an app, half version B, and see which group smiles more.

## Canary Deployment
**Definition:** Gradually rolling out a model to a small subset of users to catch regressions before full release.
**ELI5:** Send a canary into the mine first—if it’s safe, everyone else can enter.

## Latency vs. Throughput
**Definition:** Latency measures per-request response time; throughput measures requests processed per unit time. Often trade off via batching.
**ELI5:** Latency is how long you wait in line; throughput is how many people the store serves per minute.

## Inference Pipeline
**Definition:** Runtime system that handles preprocessing, model execution, post-processing, and response generation.
**ELI5:** The kitchen workflow from chopping veggies to plating the meal every time an order arrives.

## Serving Stack
**Definition:** Software/hardware combination used to host models (Triton, TorchServe, Ray Serve, custom microservices) with autoscaling and observability.
**ELI5:** The restaurant’s ovens, waitstaff, and order screens that keep meals coming out smoothly.

## Quantization-Aware Inference
**Definition:** Running models with reduced precision (INT8/FP8) to save memory/latency, possibly after quantization-aware training or post-training quantization.
**ELI5:** Store numbers with fewer digits so the model fits on a smaller device without forgetting its recipe.

## Distillation for Deployment
**Definition:** Compressing a large teacher into a smaller student to meet latency or hardware constraints while retaining accuracy.
**ELI5:** Have a master chef teach an apprentice so the trainee can cook fast on a food truck.

## Prompt Guardrails
**Definition:** Pre- and post-processing filters that sanitize user prompts/responses, detect policy violations, or inject system messages.
**ELI5:** Safety gloves that check questions and answers before they leave the factory.

## Monitoring / Observability
**Definition:** Continuous tracking of metrics (quality, drift, latency, cost) in production. Includes logging, tracing, dashboards, and alerting.
**ELI5:** A control room wall of gauges showing whether the system is healthy or needs attention.

## Data Drift Detection
**Definition:** Statistical checks (KL divergence, PSI, embeddings) to flag shifts in feature distributions that may degrade performance.
**ELI5:** Alarm bells that ring when the ingredients delivered to the kitchen suddenly change.

## Feedback Loop
**Definition:** Mechanism for collecting user outcomes, labels, or ratings to drive retraining or RLHF updates.
**ELI5:** Ask diners to rate the meal so you can tweak the recipe tomorrow.

## Red Teaming
**Definition:** Structured adversarial testing to expose safety, privacy, or robustness failures before deployment.
**ELI5:** Invite friendly hackers to poke holes in your system before real attackers try.

## Evaluation Harness
**Definition:** Automated suite that runs standardized benchmarks, regression tests, and custom probes against model candidates.
**ELI5:** A giant obstacle course every new model must complete before it’s allowed into production.

## Benchmarks
**Definition:** Public or internal datasets with well-defined metrics (MMLU, BIG-bench, HELM, VQA, ImageNet). Provide apples-to-apples comparisons.
**ELI5:** Official tournaments where different models compete under the same rules.

## Guarded Launch / Safety Case
**Definition:** Documentation and governance process demonstrating that risks are mitigated before scaling deployment.
**ELI5:** A checklist and signed permission slip proving the rocket is safe before liftoff.
