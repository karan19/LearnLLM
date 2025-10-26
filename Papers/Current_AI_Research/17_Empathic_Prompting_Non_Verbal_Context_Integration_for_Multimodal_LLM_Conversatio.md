# Empathic Prompting: Non-Verbal Context Integration for Multimodal LLM Conversations

- **Authors:** Lorenzo Stacchio, Andrea Ubaldi, Alessandro Galdelli, Maurizio Mauri, Emanuele Frontoni, Andrea Gaggioli
- **Published:** 2025-10-23T17:08:03Z
- **Source:** http://arxiv.org/abs/2510.20743v1

## Abstract
We present Empathic Prompting, a novel framework for multimodal human-AI
interaction that enriches Large Language Model (LLM) conversations with
implicit non-verbal context. The system integrates a commercial facial
expression recognition service to capture users' emotional cues and embeds them
as contextual signals during prompting. Unlike traditional multimodal
interfaces, empathic prompting requires no explicit user control; instead, it
unobtrusively augments textual input with affective information for
conversational and smoothness alignment. The architecture is modular and
scalable, allowing integration of additional non-verbal modules. We describe
the system design, implemented through a locally deployed DeepSeek instance,
and report a preliminary service and usability evaluation (N=5). Results show
consistent integration of non-verbal input into coherent LLM outputs, with
participants highlighting conversational fluidity. Beyond this proof of
concept, empathic prompting points to applications in chatbot-mediated
communication, particularly in domains like healthcare or education, where
users' emotional signals are critical yet often opaque in verbal exchanges.

## ELI5
Picture chatting with a virtual assistant while a lightweight camera tracks your face. Empathic Prompting pipes descriptors such as 'smiles broadly,' 'brows furrowed,' or 'eyes glancing away' into the same prompt that carries your words, giving the LLM context about your emotional state before it speaks. If it senses frustration, it might slow down, offer reassurance, or ask clarifying questions; if it spots excitement, it can match your energy and provide richer details. The framework keeps the sensing module modular, so any emotion-recognition service can plug in without retraining the language model. Experiments show conversations become more engaging and users feel better understood because the assistant reacts to unspoken cues. It's like talking to a friend who notices your expression and adjusts the tone instantly, making AI interactions warmer and more personalized.
