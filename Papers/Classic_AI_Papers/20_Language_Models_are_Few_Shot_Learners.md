# Language Models are Few-Shot Learners

- **Authors:** Tom B. Brown et al.
- **Year:** 2020
- **Source:** https://arxiv.org/abs/2005.14165

## Abstract
We train GPT-3, an autoregressive language model with 175 billion parameters, and show that it achieves strong performance on many NLP tasks in the zero-, one-, and few-shot settings without gradient updates. We detail scaling laws, architectural choices, and evaluation across translation, question answering, cloze tasks, and more, highlighting both capabilities and societal implications.

## ELI5
GPT-3 is like a voracious reader that has digested almost everything on the public internet. When you hand it a new task, you don’t retrain it—you simply give a couple of examples in the prompt and it infers the pattern on the fly, like saying "Translate: cat → gato, dog → perro, so rabbit → ?" Its massive parameter count lets it memorize intricate statistical structure, and the paper shows that just scaling up the same architecture unlocks few-shot abilities, coding skills, and reasoning tricks. The authors also discuss the risks, pointing out that such a powerful parrot needs careful deployment to avoid amplifying biases or misinformation.
