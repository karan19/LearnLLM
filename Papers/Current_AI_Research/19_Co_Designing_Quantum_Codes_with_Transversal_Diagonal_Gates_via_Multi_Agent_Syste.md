# Co-Designing Quantum Codes with Transversal Diagonal Gates via Multi-Agent Systems

- **Authors:** Xi He, Sirui Lu, Bei Zeng
- **Published:** 2025-10-23T16:45:39Z
- **Source:** http://arxiv.org/abs/2510.20728v1

## Abstract
We present a multi-agent, human-in-the-loop workflow that co-designs quantum
codes with prescribed transversal diagonal gates. It builds on the Subset-Sum
Linear Programming (SSLP) framework (arXiv:2504.20847), which partitions basis
strings by modular residues and enforces $Z$-marginal Knill-Laflamme (KL)
equalities via small LPs. The workflow is powered by GPT-5 and implemented
within TeXRA (https://texra.ai)-a multi-agent research assistant platform that
supports an iterative tool-use loop agent and a derivation-then-edit workflow
reasoning agent. We work in a LaTeX-Python environment where agents reason,
edit documents, execute code, and synchronize their work to Git/Overleaf.
Within this workspace, three roles collaborate: a Synthesis Agent formulates
the problem; a Search Agent sweeps/screens candidates and exactifies numerics
into rationals; and an Audit Agent independently checks all KL equalities and
the induced logical action. As a first step we focus on distance $d=2$ with
nondegenerate residues. For code dimension $K\in\{2,3,4\}$ and $n\le6$ qubits,
systematic sweeps yield certificate-backed tables cataloging attainable cyclic
logical groups-all realized by new codes-e.g., for $K=3$ we obtain order $16$
at $n=6$. From verified instances, Synthesis Agent abstracts recurring
structures into closed-form families and proves they satisfy the KL equalities
for all parameters. It further demonstrates that SSLP accommodates residue
degeneracy by exhibiting a new $((6,4,2))$ code implementing the transversal
controlled-phase $diag(1,1,1,i)$. Overall, the workflow recasts
diagonal-transversal feasibility as an analytical pipeline executed at scale,
combining systematic enumeration with exact analytical reconstruction. It
yields reproducible code constructions, supports targeted extensions to larger
$K$ and higher distances, and leads toward data-driven classification.

## ELI5
Designing quantum error-correcting codes that allow transversal diagonal gates is like crafting safes that can be opened by applying the same gentle twist to every dial simultaneously. The search space is huge, so the authors enlist multiple specialized agents plus human oversight to explore code parameters collaboratively. One agent proposes candidate partitions of basis states, another enforces algebraic constraints from the SSLP framework, and yet another evaluates whether the resulting code admits the desired transversal operations. They iterate, sharing partial blueprints and pruning dead ends, until a feasible design emerges. This cooperative workflow mirrors an engineering studio where architects, structural analysts, and locksmiths pass sketches back and forth until all requirements align. The final codes balance theoretical elegance with practical gate implementations, pushing quantum architectures closer to scalable fault tolerance.
