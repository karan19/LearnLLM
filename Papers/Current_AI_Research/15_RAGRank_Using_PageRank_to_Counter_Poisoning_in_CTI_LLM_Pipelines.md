# RAGRank: Using PageRank to Counter Poisoning in CTI LLM Pipelines

- **Authors:** Austin Jia, Avaneesh Ramesh, Zain Shamsi, Daniel Zhang, Alex Liu
- **Published:** 2025-10-23T17:43:00Z
- **Source:** http://arxiv.org/abs/2510.20768v1

## Abstract
Retrieval-Augmented Generation (RAG) has emerged as the dominant
architectural pattern to operationalize Large Language Model (LLM) usage in
Cyber Threat Intelligence (CTI) systems. However, this design is susceptible to
poisoning attacks, and previously proposed defenses can fail for CTI contexts
as cyber threat information is often completely new for emerging attacks, and
sophisticated threat actors can mimic legitimate formats, terminology, and
stylistic conventions. To address this issue, we propose that the robustness of
modern RAG defenses can be accelerated by applying source credibility
algorithms on corpora, using PageRank as an example. In our experiments, we
demonstrate quantitatively that our algorithm applies a lower authority score
to malicious documents while promoting trusted content, using the standardized
MS MARCO dataset. We also demonstrate proof-of-concept performance of our
algorithm on CTI documents and feeds.

## ELI5
Retrieval-augmented LLMs for cyber threat intelligence often rely on corpora that adversaries might pollute with misleading reports. RAGRank defends this pipeline by treating the corpus as a graph where documents cite, support, or resemble one another, much like websites linking across the early internet. By running a PageRank-style algorithm, trustworthy, well-referenced intel bubbles up, while isolated or suspicious documents sink, reducing the chance that a poisoned note becomes the context for an LLM answer. The system can further fuse metadata such as publication source, analyst reputation, or temporal freshness to refine the ranking. Analysts thus receive cleaner context, and attackers find it harder to manipulate the model with a few malicious uploads. It's essentially spam filtering for knowledge bases, repurposed to keep security chatbots from quoting the enemy.
