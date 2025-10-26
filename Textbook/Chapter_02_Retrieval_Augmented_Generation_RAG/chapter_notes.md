# Chapter 02: Retrieval-Augmented Generation (RAG)

## Overview
Retrieval-Augmented Generation couples a parametric language model with an external knowledge source so the model can cite, refresh, and ground its answers. Instead of relying solely on memorized facts, the pipeline retrieves context from corpora (docs, APIs, databases) and conditions the generator on that evidence. RAG underpins enterprise chatbots, search copilots, and safety tooling where provenance and rapid updates matter.

*ELI5:* Think of the LLM as a storyteller with a short-term memory. RAG lets the storyteller run to the library mid-conversation, grab the right book page, and then continue talking while pointing at the paragraph it just read.

## Canonical pipeline
1. **Ingestion & chunking** – collect documents, normalize, split into passages, embed.
2. **Retrieval** – given a query, fetch top-k relevant chunks via sparse, dense, or hybrid search.
3. **Augmented generation** – stuff/fuse retrieved text into the model’s context window (or encode separately) before decoding an answer.
4. **Post-processing** – cite sources, re-rank answers, log feedback, and optionally update indexes.

*ELI5:* It’s like cooking: prep the pantry (ingestion), pick the freshest ingredients (retrieval), cook the dish (generation), then plate it nicely with labels (post-processing).

## Retrieval strategies
- **Sparse retrievers (BM25, SPLADE)**: rely on keyword overlaps and inverted indexes; strong zero-shot baseline and interpretable.
  - *ELI5:* A librarian who looks for exact words in the card catalog.
- **Dense retrievers (DPR, Contriever, GTR, OpenAI text-embedding-3)**: encode queries/passages into vectors and use inner-product search; better at semantic matching [Karpukhin et al., 2020](https://arxiv.org/abs/2004.04906).
  - *ELI5:* Instead of matching literal words, the librarian compares vibes—“this feels like medieval history, grab those shelves.”
- **Multi-vector retrievers (ColBERT, DeepImpact)**: store token-level vectors so fine-grained signals survive.
- **Hybrid search**: combine sparse and dense scores (weighted sum or learned fusion) to cover exact names plus semantics.
  - *ELI5:* Two librarians, one literal and one intuitive, whisper their rankings to make a joint shortlist.
- **Query rewriting & intent detection**: expand or rewrite user prompts (e.g., HyDE hallucinated queries [Gao et al., 2023](https://arxiv.org/abs/2212.10496)) to capture hidden context.
- **Routing & collection selection**: classification gates choose the right datasource (docs vs. code vs. tables).

## Indexing & storage patterns
- **Vector databases**: FAISS, ScaNN, Milvus, Pinecone, Weaviate; support IVF/HNSW/product quantization for latency vs. recall trade-offs.
- **Chunking**: fixed windows, semantic splits, overlap/stride, hierarchical (page → section → paragraph). Choose chunk sizes that balance recall (bigger) vs. precision (smaller).
  - *ELI5:* Cutting a cake into slices: too thin and each bite lacks frosting; too thick and people struggle to eat it.
- **Metadata filtering**: store structured tags (source, date, language) for scoped retrieval.
- **Freshness & streaming ingestion**: watch for stale embeddings; schedule re-embeds when docs change.

## Augmented generation techniques
- **Naïve stuffing / few-shot context**: concatenate top-k passages into the prompt; simple but context-limited.
- **Fusion-in-Decoder (FiD)**: encode each passage separately and fuse inside the decoder, improving factuality [Izacard & Grave, 2021](https://arxiv.org/abs/2007.11662).
- **RAG-Token vs. RAG-Sequence**: original Facebook models condition per-token vs. per-sequence on different retrieved docs [Lewis et al., 2020](https://arxiv.org/abs/2005.11401).
- **Re-ranking & filtering**: cross-encoders or LLM judges drop irrelevant passages before generation.
- **Chain-of-Note / self-citation**: ask the model to jot short bullet notes tied to each source before final synthesis.
- **Tool-aware generation (ReAct-style RAG)**: the model iteratively retrieves during decoding rather than a single upfront fetch.

*ELI5:* Think of the model as a chef making stew. Simple stuffing is dumping all ingredients at once. FiD lets the chef taste and season each ingredient separately before blending, producing a more balanced dish.

## Advanced variants & research directions
- **HyDE**: hallucinate a hypothetical answer and use it as the query, leading to better dense retrieval scores [Gao et al., 2023](https://arxiv.org/abs/2212.10496).
- **Self-RAG / Retrieval-Augmented RLHF**: have the model decide when to retrieve, critique the passages, and even reject them.
- **Graph RAG / knowledge graphs**: convert corpora into entities/relations, traverse subgraphs, then ground the response.
- **Multi-hop RAG**: sequentially retrieve supporting facts for intermediate questions (e.g., HotpotQA pipelines with query planning).
- **Agentic RAG**: integrate planners (e.g., AutoGPT) that decompose tasks, call multiple retrievers, and cache intermediate findings.
- **Evaluation-aware RAG**: RARR, Zeus, and other methods verify outputs against retrieved evidence and regenerate if unsupported.

*ELI5:* If standard RAG is a student flipping to a single textbook page, advanced RAG is a debate team: they brainstorm guesses (HyDE), look up multiple books in order (multi-hop), draw concept maps (Graph RAG), and have a referee double-check citations before handing in the assignment.

## Evaluation & monitoring
- **Answer quality**: EM/F1 for QA, BLEU/ROUGE for generation, or LLM-as-a-judge grading with citation matching.
- **Grounding metrics**: support coverage (did we retrieve all gold facts?), attribution accuracy (does each sentence cite a passage?), hallucination scores (TruthfulQA-style probes).
- **Latency/cost**: tokens added by retrieved context, retrieval QPS, cache hit ratios.
- **User feedback loops**: thumbs-up/down linked to passages to drive reranker or retriever fine-tuning.

*ELI5:* Testing RAG is like grading a research paper—you check correctness, make sure every claim has a footnote, and note how long it took the student to finish.

## Key formulas
- **Dense retrieval score**:  
  $$ s(q, d_i) = \text{sim}(f_q(q), f_d(d_i)) $$  
  where $f_q, f_d$ are encoder functions (often shared) and sim is dot-product or cosine. Top-k is returned via Approximate Nearest Neighbor search.
- **Hybrid fusion**:  
  $$ s_{hybrid}(q, d) = \alpha \cdot s_{dense}(q,d) + (1-\alpha) \cdot s_{sparse}(q,d) $$
- **FiD aggregation**: given retrieved docs $\{d_i\}$, encode each independently and let the decoder attend over concatenated encoder states:  
  $$ P(y|x,\{d_i\}) = \prod_t P\left(y_t \mid y_{<t}, x, \text{Enc}(d_1), \dots, \text{Enc}(d_k)\right). $$

## Experiments & code ideas
1. **Retriever comparison**: Evaluate BM25 vs. DPR vs. hybrid on a small wiki subset; log recall@k and average latency.
2. **Chunk-size sweep**: Re-embed a sample corpus with 256, 512, and 1024-token chunks; measure answer accuracy vs. context length.
3. **HyDE ablation**: Implement hypothetical document expansion for dense retrieval and compare it to vanilla DPR queries on NaturalQuestions.
4. **FiD vs. stuffing**: Fine-tune a small FiD (e.g., LlamaIndex or Hugging Face FiD-T5) and compare against simple prompt stuffing for HotpotQA.
5. **Grounding evaluator**: Build a lightweight LLM judge that checks each generated sentence for presence in retrieved passages; use it to trigger automatic regeneration.

## References
- [x] [Lewis et al., 2020 — Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)
- [x] [Karpukhin et al., 2020 — Dense Passage Retrieval](https://arxiv.org/abs/2004.04906)
- [x] [Izacard & Grave, 2021 — Leveraging Pre-trained Checkpoints for Retrieval-Augmented Generation (FiD)](https://arxiv.org/abs/2007.11662)
- [x] [Gao et al., 2023 — Hypothetical Document Embeddings (HyDE)](https://arxiv.org/abs/2212.10496)
- [x] Tooling docs: FAISS, Pinecone, Milvus, LlamaIndex, LangChain (various)
