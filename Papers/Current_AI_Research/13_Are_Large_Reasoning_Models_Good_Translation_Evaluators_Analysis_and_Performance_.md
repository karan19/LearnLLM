# Are Large Reasoning Models Good Translation Evaluators? Analysis and Performance Boost

- **Authors:** Runzhe Zhan, Zhihong Huang, Xinyi Yang, Lidia S. Chao, Min Yang, Derek F. Wong
- **Published:** 2025-10-23T17:48:36Z
- **Source:** http://arxiv.org/abs/2510.20780v1

## Abstract
Recent advancements in large reasoning models (LRMs) have introduced an
intermediate "thinking" process prior to generating final answers, improving
their reasoning capabilities on complex downstream tasks. However, the
potential of LRMs as evaluators for machine translation (MT) quality remains
underexplored. We provides the first systematic analysis of LRM-as-a-judge in
MT evaluation. We identify key challenges, revealing LRMs require tailored
evaluation materials, tend to "overthink" simpler instances and have issues
with scoring mechanisms leading to overestimation. To address these, we propose
to calibrate LRM thinking by training them on synthetic, human-like thinking
trajectories. Our experiments on WMT24 Metrics benchmarks demonstrate that this
approach largely reduces thinking budgets by ~35x while concurrently improving
evaluation performance across different LRM scales from 7B to 32B (e.g.,
R1-Distill-Qwen-7B achieves a +8.7 correlation point improvement). These
findings highlight the potential of efficiently calibrated LRMs to advance
fine-grained automatic MT evaluation.

## ELI5
Traditional translation graders spit out scores without explaining themselves, leaving translators guessing about the underlying critique. Large reasoning models change the game by narrating their thought process before deciding on a score, much like a bilingual editor who annotates every line. This paper studies when those narrated judgments correlate with human experts and identifies failure modes—overconfidence, cultural blind spots, or inconsistent rationales. The authors introduce prompting tricks, calibration steps, and agreement filters that encourage the models to align their stories with real translation quality. Once tuned, these reasoning evaluators not only provide numeric ratings but also highlight specific sentences and reasoning chains that led to the verdict, offering actionable feedback. It turns evaluation from a mysterious thumbs-up/down into a guided workshop that helps both systems and humans improve.
