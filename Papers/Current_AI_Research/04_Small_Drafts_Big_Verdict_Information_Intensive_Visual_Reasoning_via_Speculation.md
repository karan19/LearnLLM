# Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation

- **Authors:** Yuhan Liu, Lianhui Qin, Shengjie Wang
- **Published:** 2025-10-23T17:59:21Z
- **Source:** http://arxiv.org/abs/2510.20812v1

## Abstract
Large Vision-Language Models (VLMs) have achieved remarkable progress in
multimodal understanding, yet they struggle when reasoning over
information-intensive images that densely interleave textual annotations with
fine-grained graphical elements. The main challenges lie in precisely
localizing critical cues in dense layouts and multi-hop reasoning to integrate
dispersed evidence. We propose Speculative Verdict (SV), a training-free
framework inspired by speculative decoding that combines multiple lightweight
draft experts with a large verdict model. In the draft stage, small VLMs act as
draft experts to generate reasoning paths that provide diverse localization
candidates; in the verdict stage, a strong VLM synthesizes these paths to
produce the final answer, minimizing computational cost while recovering
correct answers. To further improve efficiency and accuracy, SV introduces a
consensus expert selection mechanism that forwards only high-agreement
reasoning paths to the verdict. Empirically, SV achieves consistent gains on
challenging information-intensive and high-resolution visual question answering
benchmarks, including InfographicVQA, ChartMuseum, ChartQAPro, and HR-Bench 4K.
By synthesizing correct insights from multiple partially accurate reasoning
paths, SV achieves both error correction and cost-efficiency compared to large
proprietary models or training pipelines. Code is available at
https://github.com/Tinaliu0123/speculative-verdict

## ELI5
Imagine covering a wall with the kind of chaotic infographic you see in museums: tiny fonts, curved arrows, micro bar charts, and footnotes crammed together. Instead of making one expensive model read every pixel, the authors recruit a handful of nimble interns—small vision-language models—to scan different neighborhoods of the poster and jot down what they think matters. These interns speculate freely, producing overlapping snippets about colors, captions, and numbers, even if some guesses are imperfect. A larger, more reliable detective model then collects these drafts, looks for consensus, and threads the best clues into a final coherent explanation, discarding noisy notes along the way. The entire workflow mimics speculative execution in computing, where cheap guesses keep pipelines busy and a heavyweight checker confirms the answer only when needed. Because the seniors only review high-agreement drafts, the system saves computation while actually improving accuracy on dense layouts that would otherwise overwhelm a single pass. It turns messy visual reasoning into a newsroom process with fact-checkers and editors who play to their strengths.
