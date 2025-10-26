# Chapter 06: Explainable AI (XAI)

## Overview
Explainable AI seeks to make complex models—deep nets, transformers, multimodal systems—comprehensible to humans. Explanations improve trust, debugging, compliance (e.g., GDPR “right to explanation”), and safety. Methods span intrinsic interpretability (transparent models) and post-hoc techniques (attribution, counterfactuals, concept analysis).

*ELI5:* Imagine asking a magician to show how the trick works. XAI is the magician’s behind-the-scenes tour, revealing which cards were hidden up the sleeve.

## Taxonomy
1. **Scope**: global (how the whole model behaves) vs. local (why this specific prediction occurred).
2. **Timing**: ante-hoc (inherently interpretable models) vs. post-hoc (explain after training).
3. **Modality**: tabular, vision, text, multimodal.
4. **Faithfulness**: faithful (reflect causal influence) vs. plausibility (just sounds convincing).

## Toolbox by method family (with ELI5)
### Feature attribution
- **Gradients / Saliency maps**: $\mathbf{w} = \nabla_x f(x)$ highlights sensitivity.
  - *ELI5:* Press each piano key gently to see which note changes the song the most.
- **Integrated Gradients (IG)**: integrate gradients along the path from baseline $x'$ to input $x$ [Sundararajan et al., 2017].  
  $$IG_i(x) = (x_i - x'_i) \int_{\alpha=0}^1 \frac{\partial f(x'+\alpha(x-x'))}{\partial x_i} d\alpha$$
  - *ELI5:* Slowly raise the volume from silent to loud while tracking how much each instrument contributes.
- **DeepLIFT**: compares activations to a reference, propagating “contribution scores.”
- **Layer-wise Relevance Propagation (LRP)**: redistributes prediction score backward via conservation rules.

### Model-agnostic surrogates
- **LIME**: fit sparse linear model on perturbed samples near the instance.
  - *ELI5:* Ask “what if” questions around the input and fit a simple rule-of-thumb explaining that neighborhood.
- **SHAP**: compute Shapley value approximations to estimate each feature’s marginal contribution.  
  $$\phi_i = \sum_{S \subseteq F\setminus \{i\}} \frac{|S|!(|F|-|S|-1)!}{|F|!} [f(S \cup \{i\}) - f(S)]$$
  - *ELI5:* Imagine a team sharing bonus points based on who helped most; SHAP splits the credit fairly.

### Concept & example-based
- **Prototype / criticism sets**: select representative training examples (ProtoDash, influence functions) to justify predictions.
- **TCAV**: Concept Activation Vectors quantify sensitivity to human-defined concepts.
  - *ELI5:* Ask “How much does the model rely on stripes vs. spots to call something a zebra?”
- **Nearest neighbors**: show similar remembered cases from embedding space.

### Counterfactual explanations
- Generate minimal edits to flip prediction (e.g., replace “bachelor’s degree” with “master’s”). Methods: DiCE, CEM, gradient-based search.
  - *ELI5:* “If the bank denied your loan, what smallest change would have earned approval?”

### Attention & internal structure
- **Attention rollout**: multiply attention matrices to find token importance.
- **Activation patching / causal tracing**: swap activations between prompts to identify circuits (TransformerLens).
  - *ELI5:* Swap gears in the robot’s brain to see which gear controls a specific action.

### LLM-specific explainability
- **Rationales / scratchpads**: extract model-generated explanations; evaluate faithfulness vs. plausibility.
- **Faithfulness tests**: delete-attribution, contrast pairs, logit lens probes.
- **Judge models**: use verifiers to critique the original answer for missing citations or hallucinations.

### Multimodal explanations
- **Grad-CAM / Score-CAM** for vision tokens, extended to video/audio.
- **Text pointing**: align text spans with evidence sentences (RARR, attribution QA).
- **Multimodal saliency**: highlight both patches and caption tokens that contributed most.

## Evaluation metrics
- **Faithfulness**: deletion/insertion curves (remove top-k important features and observe performance drop).
- **Stability**: explanation consistency across similar inputs.
- **Human agreement**: how often humans agree with highlighted regions (Pointing Game, IOU).
- **Complexity**: measure sparsity or length of explanation (shorter often better).
- **Ground-truth tasks**: use synthetic data with known rules (e.g., `AND`/`OR` features) to verify explanation accuracy.

## Risks & best practices
- Beware of **spurious plausibility**: pretty heatmaps that don’t reflect internal causality.
- Provide **uncertainty** with explanations (“confidence of attribution”).
- Combine multiple views: attribution + counterfactual + examples.
- Keep user context in mind—domain experts need different detail than end users.

*ELI5:* A colorful highlight isn’t automatically truthful; double-check that removing the highlighted word actually changes the model’s answer.

## Experiments & code ideas
1. **Attribution sandbox**: run Integrated Gradients and LIME on the same classifier; compare deletion metrics.
2. **Counterfactual generator**: implement DiCE for a tabular model; evaluate actionability of suggested changes.
3. **LLM faithfulness test**: instruct an LLM to provide a rationale, then remove rationale tokens from the prompt and see if answer changes (testing dependency).
4. **Activation patching**: use TransformerLens to identify neurons responsible for factual recall vs. refusal.
5. **Multimodal Grad-CAM**: apply Grad-CAM to CLIP vision encoder and overlay heatmaps on images; verify with Pointing Game.
6. **Human study mock-up**: show explanations to colleagues and track whether they predict model output better with vs. without explanations.

## References & resources
- Ribeiro et al., 2016 — LIME
- Lundberg & Lee, 2017 — SHAP
- Sundararajan et al., 2017 — Integrated Gradients
- Kim et al., 2018 — TCAV
- Goh et al., 2021 — Interpretability in the Wild
- Nanda et al., 2023 — Activation Patching / TransformerLens
- Jacovi & Goldberg, 2020 — Faithfulness vs. Plausibility
- Toolkits: Captum, SHAP library, OmniXAI, TransformerLens, Tracr, Ecco
