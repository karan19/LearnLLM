# Chapter 01: Reasoning Models

## Overview
Reasoning models focus on making large language models (LLMs) perform deliberate, multi-step thinking instead of responding with a single pass of next-token prediction. Classical AI separated symbolic planners from statistical models, but modern LLMs blend both: they internalize linguistic priors while calling out to structured search, external tools, or formal programs when a task exceeds pure pattern matching. Mastering reasoning workflows is essential for safety-critical agents (planning, tool use, factual QA) and underpins many other chapters (RAG, evaluation, alignment).

## Reasoning model landscape
### 1. Prompt-based decomposition strategies
- **Chain-of-Thought (CoT)**: Provide a few exemplars that verbalize intermediate steps; large models then produce their own reasoning traces and achieve state-of-the-art accuracy on math word problems and commonsense benchmarks [Wei et al., 2022](https://arxiv.org/abs/2201.11903).
  - **ELI5:** Imagine a math teacher telling students, “Show your work.” Once an LLM sees examples of detailed scratch work, it copies the habit: it now solves new problems by narrating every little step, just like a student muttering through a word problem before giving the final answer.
- **Self-Consistency**: Sample multiple reasoning paths and marginalize over the answers to reduce hallucinated steps; boosts GSM8K by +17.9% absolute over greedy decoding [Wang et al., 2023](https://arxiv.org/abs/2203.11171).
  - **ELI5:** Instead of trusting the first solution it blurts out, the model plays detective by brainstorming several different stories, then chooses the ending that most stories agree on—like asking five friends to solve a riddle and trusting the majority.
- **Least-to-Most Prompting**: Ask the LLM to first solve simpler subproblems before combining them, which improves generalization to harder compositions (e.g., 99% on SCAN length split with only 14 exemplars) [Zhou et al., 2023](https://arxiv.org/abs/2205.10625).
  - **ELI5:** When faced with a giant Lego castle, the model first practices building small walls and towers. Once those bite-sized tasks are solid, it snaps them together into the big castle, letting it tackle puzzles tougher than the training examples.
- **Program-of-Thoughts (PoT)** and **DSPy-style planners**: Mix natural language reasoning with code-like symbolic instructions so the model can both narrate and formalize intermediate steps.
  - **ELI5:** It’s like writing a recipe with both friendly instructions (“stir until smooth”) and precise measurements (“set timer for 90 seconds”), keeping the chef creative yet organized.
- **Reflexion / Active Prompting**: Let the model critique its own earlier answers, reflect on mistakes, and re-prompt itself with lessons learned.
  - **ELI5:** After answering a quiz, the model reads its own paper, circles errors in red ink, and then tries again using those notes—just like a diligent student doing corrections.

### 2. Search and deliberation frameworks
- **Tree of Thoughts (ToT)**: Generalizes CoT by exploring multiple reasoning branches, self-evaluating partial thoughts, and performing lookahead/backtracking—dramatically improving tasks like Game of 24 (4% → 74% success on GPT-4) [Yao et al., 2023](https://arxiv.org/abs/2305.10601).
- **Graph of Thoughts (GoT)**: Treats intermediate thoughts as graph nodes so outputs from different branches can be merged, revisited, or upgraded with feedback loops; yields higher-quality solutions while lowering cost on tasks such as sorting (quality +62% vs. ToT) [Besta et al., 2024](https://arxiv.org/abs/2308.09687).
- **Heuristic search hybrids**: Techniques like beam search over reasoning traces, Monte-Carlo Tree Search, or policy/value-guided sampling fall under this bucket. They trade compute for robustness when single trajectories are brittle.
- **Multi‑Agent Debate / Socratic play**: Spin up two or more LLM agents that argue opposite sides, critique each other, or split roles (planner vs. executor) before converging on an answer.

  **ELI5 stories**
  - *ToT:* Picture a detective drawing a branching mind map on a whiteboard. She follows one lead, backtracks if it’s useless, and tries another, ensuring no promising clue is left unexplored.
  - *GoT:* Now imagine that same detective stringing yarn between pushpins on the board so clues from one branch can inform another—forming a web rather than a simple tree.
  - *Heuristic search:* Think of speed chess where you evaluate a handful of strong-looking moves ahead of time instead of exhaustively exploring every possibility.
  - *Debate:* Two robot lawyers argue over the best solution while a judge robot listens; they cancel out each other’s bad ideas and keep the gems.

### 3. Tool-augmented reasoning
- **Program-aided Language Models (PAL)**: LLM writes Python snippets as intermediate steps and offloads execution to an interpreter, yielding large gains on GSM8K and BIG-Bench Hard [Gao et al., 2023](https://arxiv.org/abs/2211.10435).
- **ReAct**: Interleaves “Reason” tokens with “Act” commands against APIs (e.g., Wikipedia search, embodied environments) to curb hallucinations and plan interactively [Yao et al., 2023](https://arxiv.org/abs/2210.03629).
- **Toolformer**: Shows that models can fine-tune themselves to call external calculators, search engines, or translation APIs with only a few demonstrations, improving zero-shot reasoning without hurting language quality [Schick et al., 2023](https://arxiv.org/abs/2302.04761).
- **AutoGPT / Voyager-style agents**: Wrap LLMs in loops that pick goals, write code or tool calls, execute them, and store memories for future subtasks.

  **ELI5 stories**
  - *PAL:* The model is a chef who writes a short recipe (Python) and lets a kitchen robot cook it perfectly before tasting the result.
  - *ReAct:* A journalist thinks aloud (“Maybe the answer is in last year’s article…”) then actually hits the archives API, reads the snippet, and keeps reasoning with the fresh info.
  - *Toolformer:* Give the model a Swiss Army knife and a short guide—soon it teaches itself when to flip out the calculator blade or flashlight without being micromanaged.
  - *AutoGPT agents:* An eager intern plans tasks, runs scripts, and jots down notes in a diary so tomorrow’s self can continue the project without forgetting yesterday’s lessons.

### 4. Training-time enhancers
- **Supervised fine-tuning on rationales**: Collecting verified reasoning traces (e.g., from CoT-enabled teachers) stabilizes student models and reduces compounding errors.
  - **ELI5:** A seasoned tutor hands the apprentice a notebook filled with worked examples; copying the full reasoning trains the apprentice to think like the tutor, not just mimic answers.
- **Reinforcement learning with reasoners**: Rewarding models for passing verifier checks, adhering to tool usage policies, or optimizing deliberate search objectives extends RLHF beyond surface-level helpfulness.
  - **ELI5:** Imagine giving gold stars only when the robot both solves the puzzle and explains why the solution is safe; the robot quickly learns that good behavior plus clear logic earns more stars than lucky guesses.
- **Distillation & verifiers**: Larger “reasoning teachers” can be distilled into smaller models by matching both the final answer and intermediate traces; verifiers filter inconsistent solutions for self-correction loops.
  - **ELI5:** It’s like having an older sibling check your homework—if they spot a shaky step, you fix it before turning it in, so the final paper looks polished even though you’re younger and smaller.
- **Reflexion / self-improvement loops**: During training, let models critique and revise outputs, storing “lessons learned” to avoid repeating the same mistake.

### 5. Evaluation patterns
- **Benchmarks**: GSM8K, SVAMP, MATH, StrategyQA, ARC-Challenge, BIG-Bench Hard, Game of 24, Mini Crosswords.
- **Diagnostics**: Track pass@k with and without self-consistency, cost per successful solution (important for ToT/GoT), and tool call accuracy (for PAL/ReAct/Toolformer).
- **Failure modes**: Look for branching factor explosion, inconsistent intermediate states, tool misuse, or degradation when exemplars are harder than test cases.
  - **ELI5:** Testing reasoning models is like grading a science fair: you don’t just check if the volcano erupts—you inspect the lab notes, materials budget, and whether the student broke any safety rules.

## Key Topics
- Prompt-based reasoning (CoT, self-consistency, least-to-most)
- Search-augmented inference (Tree/Graph of Thoughts, beam or Monte-Carlo search)
- Tool/program-assisted reasoning (PAL, ReAct, Toolformer, API planning)
- Training/verification techniques (reasoning SFT, verifier-assisted RL, distillation)
- Benchmarking & diagnostics for reasoning robustness

## Formulas or Derivations
- **Self-consistency decoding**: sample $m$ reasoning paths $\{r_i\}_{i=1}^m$ and pick the majority answer
  $$\hat{y}=\arg\max_{y} \sum_{i=1}^m \mathbb{1}[f(r_i)=y],$$
  where $f(\cdot)$ extracts the answer from each path. Increasing $m$ trades compute for stability [Wang et al., 2023](https://arxiv.org/abs/2203.11171).
- **Thought search objective**: maximize utility over a tree/graph $G=(V,E)$ of thoughts: find path $p$ that maximizes $U(p)=\sum_{t\in p} s(t)-\lambda c(t)$, where $s(t)$ is the model’s self-evaluation score and $c(t)$ is cost (tokens, tool latency). Practical systems approximate $U$ via beam pruning or heuristic scoring [Yao et al., 2023](https://arxiv.org/abs/2305.10601).

## Experiments & Code
- Reproduce CoT vs. self-consistency vs. least-to-most on GSM8K or SVAMP (start with open models such as Llama 3–8B or OpenHermes).
- Implement a minimal Tree-of-Thoughts loop that explores 3–5 candidate thoughts per depth on the Game of 24 task; log token and wall-clock budgets.
- Extend a PAL-style pipeline where the LLM emits Python, executes snippets in a sandbox, and reinserts results into the prompt; compare against pure CoT.
- Prototype a ReAct agent that calls a Wikipedia API for HotpotQA, tracking how often tool calls change the final answer.

## References
- [x] [Wei et al., 2022 — Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- [x] [Wang et al., 2023 — Self-Consistency Improves CoT](https://arxiv.org/abs/2203.11171)
- [x] [Zhou et al., 2023 — Least-to-Most Prompting](https://arxiv.org/abs/2205.10625)
- [x] [Yao et al., 2023 — Tree of Thoughts](https://arxiv.org/abs/2305.10601)
- [x] [Besta et al., 2024 — Graph of Thoughts](https://arxiv.org/abs/2308.09687)
- [x] [Gao et al., 2023 — Program-Aided Language Models](https://arxiv.org/abs/2211.10435)
- [x] [Yao et al., 2023 — ReAct](https://arxiv.org/abs/2210.03629)
- [x] [Schick et al., 2023 — Toolformer](https://arxiv.org/abs/2302.04761)
