## Base Model vs. Instruct Model
When a model finishes pre-training, it’s called a **Base Model**. It holds vast knowledge, but it’s not yet designed to be a helpful assistant. 
For example, if you used a raw base model and asked, “What is RAG?”, it might simply continue the sentence in a predictive way or give a generic, unhelpful definition. 
It’s powerful as a text predictor, but it isn’t specifically trained to follow instructions or engage in conversation.

To make it useful for applications like chatbots, search assistants, or copilots, we need an Instruct Model.

An **Instruct Model** is a base model that has received extra training. This training, known as fine-tuning, is done with a specific dataset of instruction-and-answer pairs. 
This process doesn’t teach the model new facts; instead, it teaches it how to behave. It learns user intent. 
It gives clear explanations and structures responses well. Models like ChatGPT and Claude are instruct models. 
They are designed from the ground up to be helpful and responsive, making them essential for task-oriented applications.

One way to turn a base model into an instruct model is by training it further on carefully chosen examples. This extra step is known as fine-tuning.
