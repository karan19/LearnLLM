# Safety, Alignment & Governance Glossary

Key terminology for responsible AI development and risk management.

## Alignment
**Definition:** Ensuring model objectives and behaviors match human intent and societal values. Includes technical alignment (RLHF, constitutional AI) and organizational alignment (policies).
**ELI5:** Make sure the robot helper follows your house rules instead of inventing its own.

## Explainable AI (XAI)
**Definition:** Methods that make model decisions understandable (saliency maps, SHAP, counterfactuals). Aids trust and debugging.
**ELI5:** Ask the model to show its work so you can see why it picked an answer.

## Interpretability vs. Transparency
**Definition:** Interpretability focuses on explaining individual predictions; transparency covers visibility into data, training, and model limitations.
**ELI5:** Interpretability is “why did you mark this homework wrong?”; transparency is “what textbook and lessons did you use?”

## Fairness
**Definition:** Absence of unwarranted bias across demographic groups. Operationalized via parity metrics (equal opportunity, demographic parity) and domain-specific criteria.
**ELI5:** Make sure the automated referee treats every player equally, regardless of who they are.

## Bias Mitigation
**Definition:** Techniques (pre-, in-, post-processing) that reduce unwanted statistical biases. Includes reweighing, adversarial debiasing, and fairness-aware training.
**ELI5:** Adjust the scale so it doesn’t always lean toward one team’s score.

## Differential Privacy (DP)
**Definition:** Formal privacy guarantee ensuring that model outputs do not reveal much about any single data point. Implemented via noise addition and clipping during training (DP-SGD).
**ELI5:** Stir in a little noise so no one can tell whether your name was in the class roster.

## Membership Inference Attack
**Definition:** Adversary predicts whether a specific example was in the training set by probing model outputs. Signals overfitting or privacy leakage.
**ELI5:** Someone guesses if your picture was in the yearbook by how the model reacts—bad news if they can tell.

## Model Card
**Definition:** Standardized documentation describing intended use, performance, limitations, and ethical considerations of a model release.
**ELI5:** The nutrition label that tells users what’s inside the AI and when not to consume it.

## Responsible AI Policy
**Definition:** Organizational guidelines dictating acceptable use, review procedures, and compliance requirements for AI systems.
**ELI5:** Company rulebook that says what kinds of robot chores are allowed and who approves them.

## Red-Teaming / Adversarial Testing
**Definition:** Probing models with malicious prompts or inputs to surface safety, security, or content policy violations.
**ELI5:** Friendly pranksters try to trick the chatbot so engineers can patch the loopholes first.

## Content Moderation Policy
**Definition:** Rule set defining disallowed outputs (hate, self-harm, malware). Implemented via classifiers, prompts, or rule-based filters.
**ELI5:** A list of forbidden words and topics taped to the model’s monitor.

## Watermarking / Provenance
**Definition:** Techniques that embed signals into generated content to identify AI outputs (e.g., statistical watermarking, metadata standards like C2PA).
**ELI5:** A secret stamp hidden in AI-created images or text so you can prove who made it.

## Secure Enclave / Trusted Execution Environment (TEE)
**Definition:** Hardware-isolated environment that protects model weights and data during inference, mitigating model theft.
**ELI5:** A locked room inside the computer where the model can work without snoops peeking.

## Prompt Injection
**Definition:** Attack where retrieved or user-supplied text attempts to override system instructions in LLM workflows. Mitigated via content filtering and context segmentation.
**ELI5:** Someone slips a fake note into the instructions to hijack the conversation.

## Jailbreak
**Definition:** Crafted prompt designed to bypass safety filters and elicit disallowed outputs.
**ELI5:** Clever wording that sweet-talks the safety system into breaking its own rules.

## Model Collapse / Feedback Contamination
**Definition:** Degradation that occurs when models are trained predominantly on synthetic outputs, reducing diversity and accuracy.
**ELI5:** Copying your homework from your own old answers until the mistakes snowball.

## Governance Board / AI Review Committee
**Definition:** Cross-functional body that reviews high-risk AI deployments, ensuring compliance with regulations and ethical standards.
**ELI5:** The school board that must sign off before a new AI teacher enters the classroom.

## Regulatory Frameworks
**Definition:** External rules such as EU AI Act, NIST AI RMF, or sector-specific laws that dictate risk tiers, documentation, and oversight.
**ELI5:** Laws from the outside world that say “here’s how your robot must behave if you want to sell it.”
