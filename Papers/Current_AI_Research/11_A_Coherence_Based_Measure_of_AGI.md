# A Coherence-Based Measure of AGI

- **Authors:** Fares Fourati
- **Published:** 2025-10-23T17:51:42Z
- **Source:** http://arxiv.org/abs/2510.20784v1

## Abstract
Recent work by \citet{hendrycks2025agidefinition} formalized
\textit{Artificial General Intelligence} (AGI) as the arithmetic mean of
proficiencies across cognitive domains derived from the Cattell--Horn--Carroll
(CHC) model of human cognition. While elegant, this definition assumes
\textit{compensability} -- that exceptional ability in some domains can offset
failure in others. True general intelligence, however, should reflect
\textit{coherent sufficiency}: balanced competence across all essential
domains. We propose a coherence-aware measure of AGI based on the integral of
generalized means over a continuum of compensability exponents. This
formulation spans arithmetic, geometric, and harmonic regimes, and the
resulting \textit{area under the curve} (AUC) quantifies robustness under
varying compensability assumptions. Unlike the arithmetic mean, which rewards
specialization, the AUC penalizes imbalance and captures inter-domain
dependency. Applied to published CHC-based domain scores for GPT-4 and GPT-5,
the coherence-adjusted AUC reveals that both systems remain far from general
competence despite high arithmetic scores (e.g., GPT-5 at~24\%). Integrating
the generalized mean thus yields a principled, interpretable, and stricter
foundation for measuring genuine progress toward AGI.

## ELI5
If we judged students solely by averaging their math, music, and language grades, we might miss whether they actually understand how these disciplines interlock. This paper proposes a new AGI score that values coherence—the extent to which proficiency in one cognitive domain reinforces others—over brute averages. It leans on the Cattell–Horn–Carroll model of human cognition, translating its web of abilities into machine tests that should rise together if a single general intelligence factor exists. An AI that aces logic but flounders in memory or learning transfer would score lower than one that shows balanced, mutually supportive gains across the board. The metric discourages cherry-picking benchmarks and rewards architectures that genuinely integrate skills rather than silo them. In effect, it asks whether an AI's mental gears mesh smoothly like a well-engineered clock instead of being a pile of unrelated cogs.
