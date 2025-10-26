# A Use-Case Specific Dataset for Measuring Dimensions of Responsible Performance in LLM-generated Text

- **Authors:** Alicia Sagae, Chia-Jung Lee, Sandeep Avula, Brandon Dang, Vanessa Murdock
- **Published:** 2025-10-23T17:50:55Z
- **Source:** http://arxiv.org/abs/2510.20782v1

## Abstract
Current methods for evaluating large language models (LLMs) typically focus
on high-level tasks such as text generation, without targeting a particular AI
application. This approach is not sufficient for evaluating LLMs for
Responsible AI dimensions like fairness, since protected attributes that are
highly relevant in one application may be less relevant in another. In this
work, we construct a dataset that is driven by a real-world application
(generate a plain-text product description, given a list of product features),
parameterized by fairness attributes intersected with gendered adjectives and
product categories, yielding a rich set of labeled prompts. We show how to use
the data to identify quality, veracity, safety, and fairness gaps in LLMs,
contributing a proposal for LLM evaluation paired with a concrete resource for
the research community.

## ELI5
Deploying an LLM in, say, a healthcare chatbot requires tests that mirror the clinic's exact policies, patient sensitivities, and fairness constraints—not generic internet prompts. This dataset acts like a bespoke driving exam for each city: the authors capture domain-specific scenarios, annotate protected attributes, and define responsible-performance dimensions such as bias, toxicity, and factuality relevant to that use case. Evaluators can then measure precisely how the model behaves when handling real customer complaints or triaging patient questions, catching failures that broad benchmarks overlook. The dataset also encodes intervention levers, enabling teams to observe how mitigation strategies shift scores on the relevant axes. By tailoring evaluation to context, organizations gain honest visibility into whether deployment is safe, equitable, and regulation-ready, rather than relying on abstract leaderboards.
