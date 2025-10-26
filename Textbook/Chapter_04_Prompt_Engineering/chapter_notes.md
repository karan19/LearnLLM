# Chapter 04: Prompt Engineering

## Overview
Prompt engineering is the art and science of steering language models through carefully crafted inputs. Well-designed prompts can elicit reasoning, control tone, call tools, or inject guardrails without retraining. In agentic systems, prompts act as policies—system messages, few-shot exemplars, scratchpads, and function signatures all shape model behavior.

*ELI5:* Talking to an LLM is like giving instructions to a very literal genie. If you ask vaguely, you get weird wishes. Prompt engineering teaches you how to word the wish so the genie does the right thing every time.

## Prompt layers in modern stacks
1. **System prompts / role instructions** – define persona, goals, safety policy.
2. **Context augmentation** – retrieved documents, memory, tool results.
3. **Few-shot exemplars** – demonstrations showing desired format.
4. **Scratchpads / chains** – encourage intermediate reasoning (CoT, tables).
5. **Tool/function specs** – JSON schema, function signatures for structured outputs.
6. **Post prompts** – evaluation or self-critique instructions.

*ELI5:* Building a good prompt is like packing a suitcase: you lay the foundation (system prompt), add outfits (context), tuck in example outfits (few-shot), place accessories (scratchpads), and label everything so customs (tools) understand what’s inside.

## Core strategies
### Zero-shot & instruction prompts
- Use clear task verbs (“Summarize”, “Classify”, “You are a helpful tax assistant…”).
- Provide constraints (length limits, citation formats, bullet counts).
- Specify refusal style for unsafe content.

*ELI5:* Think of a babysitter note saying “Pick up Sam at 3 pm, give him peanut-free snacks, read two stories.” The more explicit you are, the fewer phone calls you’ll get.

### Few-shot prompting
- Supply input/output exemplars showing structure, tags, edge cases.
- Arrange order from simplest to hardest to hint at generalization.
- Use delimiter tokens (```<<<Example>>>```) for clarity.

*ELI5:* Teach by example like flashcards—“When you see X, respond like Y.”

### Chain-of-Thought (CoT)
- Encourage step-by-step reasoning (“Let’s think step by step”).
- Provide sample scratchpads; ask the model to show workings before final answer.
- Helps with arithmetic, logic, law, safety analysis.

*ELI5:* Telling the model “show your work” reduces careless mistakes because it has to explain each step like in math class.

### Self-consistency / multi-sample prompts
- Instruct model to generate multiple candidate solutions, then vote or filter.
- “Generate three different solution paths before concluding.”

*ELI5:* Ask three different friends for advice and go with the consensus.

### Tool-aware prompts (ReAct, function calling)
- Interleave “Thought:” and “Action:” tokens to plan API calls.
- Provide JSON schema and enforce `finish`/`tool` actions with explicit instructions.
- Useful for retrieval, calculators, code execution.

*ELI5:* It’s like giving the genie a toolkit and saying “If you need a hammer, pick it up, tell me what you hammered, then continue.”

### Style & tone control
- Explicitly request persona (“You are a witty science communicator”).
- Provide sample tone; use negative instructions (“Avoid legal jargon”).
- Temperature/Top_p tweaks complement prompt style.

### Output structural prompts
- Demand JSON, tables, Markdown; show template.
- Use guard clauses: “If required data missing, output `"status":"needs_more_info"`.”

### Safety & refusal prompting
- Prepend safety system prompts (policy bullets).
- Provide refusal exemplars for disallowed content.
- Ask model to cite reasons for refusal.

## Prompt failure patterns & fixes
| Failure | Symptom | Fix |
|--------|---------|-----|
| Under-specified task | Generic responses | Add role, steps, constraints |
| Prompt drift | Model changes topic mid-agent loop | Re-assert goals every turn, include reminders |
| Format errors | JSON invalid | Provide schema + example, ask for fenced code block |
| Hallucination | Fabricated cites | Add instruction “Only cite from provided context; if missing, say ‘insufficient evidence’.” |
| Tool misuse | Wrong API call | Include action guidelines, error handling exemplars |

*ELI5:* If the genie keeps misunderstanding, rewrite the wish with bold instructions, show a sample wish, and specify what to do if the wish is impossible.

## Advanced techniques
- **Prompt decomposition**: break complex tasks into sequential prompts (plan → execute → review).
- **Automatic prompt search (APE, AutoPrompt, Promptbreeder)**: gradient-free or gradient-based methods discover optimal token sequences.
- **Self-instruct / synthetic prompt generation**: use an LLM to invent tasks and responses, then fine-tune smaller models.
- **Programmatic prompting**: frameworks like DSPy or Guidance treat prompts as typed programs with variables and assertions.
- **Guardrails / templating**: LangChain PromptTemplates, Guardrails AI `rail` files, Microsoft Presidio to sanitize inputs.
- **Context compression**: ask model to summarize retrieved docs before final prompt (LLM-powered index).

*ELI5:* Think of automatic prompt search as hiring a coach to try thousands of phrase variations until the genie responds perfectly.

## Math & scoring bits
- **Prompt quality heuristics**: measure with response reward model $R(y|x)$; iterate via hill-climbing.
- **Prompt ensemble scoring**:  
  $$\hat{y} = \arg\max_y \sum_{p \in \mathcal{P}} w_p \cdot R(y | p, x)$$
  where $\mathcal{P}$ is a set of prompt variants.
- **Cost trade-off**: expected tokens per call $E[T] = T_{prompt} + T_{response}$; compression reduces $T_{prompt}$.

## Experiments & practice
1. **Few-shot cookbook**: build a prompt template for classification with 0-,1-,3-shot examples; compare accuracy on a labeled dev set.
2. **CoT vs. direct answer**: run GSM8K prompts with/without “let’s think” and log accuracy/token cost.
3. **Self-consistency**: implement multi-sample voting (k=5) for a reasoning task; measure gains vs. extra tokens.
4. **Tool prompting sandbox**: create a ReAct-style agent that uses Wikipedia API; inspect traces for Thought/Action alignment.
5. **Prompt distillation**: use GPT-4 to critique and rewrite an initial prompt to be more explicit; compare outputs.
6. **Safety prompt audit**: feed adversarial queries (jailbreak attempts) to different system prompts; note failure cases.

## References
- Wei et al., 2022 — Chain-of-Thought
- Wang et al., 2023 — Self-Consistency
- Yao et al., 2023 — ReAct
- Kojima et al., 2022 — Zero-shot CoT
- Zhou et al., 2022 — Least-to-Most prompting
- Prompt engineering guides: OpenAI Cookbook, Anthropic Prompt Library, Microsoft Prompt Engineering Playbook
