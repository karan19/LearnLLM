# Chapter 03: Multimodal Models

## Overview
Multimodal models learn from and reason over multiple sensory streams—text, images, audio, video, speech, 3D point clouds, etc. They align different encoders into a shared semantic space so tasks like image captioning, visual question answering (VQA), audiodescription, or video-grounded agents can be solved by a unified architecture. Modern LLM stacks increasingly embed vision (GPT‑4V), audio (GPT‑4o, Gemini), and action inputs, making multimodal literacy foundational.

*ELI5:* Imagine a toddler pointing at a dog and asking “What’s that sound?” A multimodal model tries to be that toddler’s brain—linking what it sees, hears, and reads so everything makes sense together.

## Taxonomy of multimodal systems
1. **Dual-encoder contrastive (CLIP-style)** – separate encoders for each modality trained with contrastive losses to align embeddings [Radford et al., 2021](https://arxiv.org/abs/2103.00020).
2. **Encoder-decoder fusion (ViLBERT, VisualBERT)** – cross-attention layers fuse modalities for token-level reasoning.
3. **Perceiver / Flamingo / PaLM‑E** – large transformer backbones ingest arbitrary modality tokens via generic cross-attn.
4. **Adapter-based LLMs (BLIP‑2, LLaVA, MiniGPT‑4)** – frozen LLM plus a visual projector that maps image features into the LLM token space.
5. **Unified autoregressive models (Gemini, GPT‑4V, Kosmos‑2)** – train on mixed sequences so the model natively predicts across modalities.
6. **Tool-augmented multimodal agents** – combine perception encoders with planners (e.g., RT‑2 robot policy, Voyager + vision).

*ELI5:* Some models keep separate notebooks for pictures and words and then check if page numbers match (contrastive). Others glue the notebooks together and read them line-by-line (fusion). The newest ones toss everything into one giant scrapbook.

## Core ingredients
### Data & alignment
- **Web-scale image–text pairs** (LAION, CC12M, COYO-700M) for contrastive pretraining.
- **Instruction datasets** (LLaVA-Instruct, MiniGPT-4 dialogues) to align vision encoders with chatty LLM outputs.
- **Synthetic QA generation** (self-instruct, GPT-generated descriptions) to cheaply expand multimodal conversations.
- **Fine-grained grounding sets** (RefCOCO, COCO Caption, TextCaps) for region-level or dense captioning.
- **Temporal datasets** (HowTo100M, Ego4D) for video + text alignment; **audio-text** corpora (AudioSet, Whisper) for speech.

*ELI5:* Feeding multimodal models is like teaching a kid: show them picture books (image–text), ask them “what’s happening here?” (instruction data), and sometimes show silent movies so they learn sequences.

### Architectures & fusion tricks
- **Vision backbone choices**: ViT, Swin, ConvNeXt. Feature pooling (CLS, Q-former) controls token count.
- **Vision-to-LLM adapters**: linear projection, Perceiver resampler (Flamingo), Q-former (BLIP‑2), Learned Query tokens (LLaVA).
- **Cross-attention patterns**: one-way (text attends to vision), two-way (co-attention), or alternating blocks.
- **Token budgeting**: patch merging, adaptive token dropping, region proposals.
- **Audio encoders**: spectrogram transformer (Whisper), wav2vec-style features.
- **Video handling**: frame sampling + temporal attention, 3D CNN features, or dual-branch “slowfast” streams.

*ELI5:* Think of the vision adapter as a translator whispering the picture details into the LLM’s ear, summarizing a high-res image into a handful of descriptive tokens.

## Representative models
| Model | Key idea | Notes |
|-------|----------|-------|
| CLIP | Contrastive pretraining on 400M image–text pairs | Great for zero-shot classification & retrieval |
| ALIGN / BASIC / SigLIP | Larger web corpora, better embeddings | Emphasis on multilingual + efficiency |
| Flamingo | Frozen LLM + Perceiver resampler + gated cross-attn | Handles interleaved image-text conversations |
| BLIP‑2 | Frozen LLM with Q-former bridging vision encoder to LLM | Efficient adaptation without LLM retraining |
| LLaVA / MiniGPT‑4 | Fine-tune Vicuna/LLaMA with image features + dialogue data | Popular open-source chatbots with vision |
| GPT‑4V / Gemini / Claude 3 | Proprietary unified multimodal LLMs | Accept image, audio, document inputs |
| PaLM‑E | Embodied multi-sensor transformer feeding robot policies | Links text instructions to robot actions |
| Kosmos‑2 | Multimodal grounding (pointing to regions) | Supports tasks like “circle the Eiffel Tower in the photo” |

## Skills & tasks
- **Image captioning & VQA** – describe images, answer questions; datasets: MSCOCO, VQAv2, OK-VQA, VizWiz.
- **Visual grounding** – refer expression comprehension, pointing to objects (RefCOCO, Flickr30k Entities).
- **Image retrieval / text-to-image search** – benchmark via Recall@k on Flickr30k, MSCOCO.
- **Document understanding** – parse charts, PDF text (DocVQA, InfographicVQA).
- **Video QA & Narration** – TVQA, HowTo100M, VideoCoCa tasks.
- **Audio QA & speech translation** – Whisper, AudioPaLM.
- **Embodied agents** – RL/robotics tasks linking vision, language, action (ALFRED, SayCan, RT‑2).

*ELI5:* Multi-skill training is like prepping a tour guide who can describe paintings, read menus, answer trivia, and follow map directions all at once.

## Challenges & mitigation
- **Hallucination & grounding**: models may describe non-existent elements; pair with detection modules or ask for bounding boxes.
- **Resolution limits**: large images can exhaust context windows—use tiling, adaptive zoom, or region selection.
- **Bias & fairness**: dataset artifacts amplify stereotypes; use debiasing datasets and auditing.
- **Licensing & privacy**: scraped data may contain PII; track provenance.
- **Evaluation gaps**: human preference studies often needed for open-ended outputs.

*ELI5:* Sometimes the model “sees” a unicorn in a photo of a horse because its imagination runs wild; giving it bounding box checklists helps keep it honest.

## Math snippets
- **Contrastive loss (InfoNCE)** for CLIP:  
  $$L = - \sum_i \log \frac{\exp(\langle v_i, t_i \rangle / \tau)}{\sum_j \exp(\langle v_i, t_j \rangle / \tau)}$$
  where $v_i$ and $t_i$ are normalized vision/text embeddings and $\tau$ is a temperature.
- **Q-former projection (BLIP‑2)**: learn query tokens $Q$ that attend image features $F$ and output $Z=\text{Transformer}(Q, F)$; map $Z$ through linear layer to LLM token embeddings.
- **Perceiver resampler**: latent array $l$ attends to modality inputs $x$ via cross-attn:  
  $$l' = \text{softmax}\left(\frac{lW_Q (xW_K)^T}{\sqrt{d}}\right) xW_V$$
  producing a fixed-size latent independent of input length.

## Experiments & projects
1. **CLIP zero-shot lab**: fine-tune OpenCLIP on a niche dataset (e.g., medical icons) and evaluate zero-shot classification vs. supervised baseline.
2. **LLaVA-style adapter**: use a vision encoder (e.g., ViT-L) + LoRA-tuned LLaMA to build a lightweight image chat demo on BLIP captions.
3. **Grounding evaluation**: prompt GPT‑4V or LLaVA to produce bounding boxes, compare IoU with ground truth; analyze hallucination rate.
4. **Multimodal retrieval**: implement text→image search by indexing vision embeddings with FAISS and evaluating Recall@k.
5. **Audio captioning**: combine Whisper embeddings with a small LLM to generate natural-language descriptions of AudioCaps clips.
6. **Safety probe**: stress-test the model on adversarial inputs (e.g., image-text mismatches) and log failure cases.

## References & further reading
- Radford et al., 2021 (CLIP)
- Alayrac et al., 2022 (Flamingo)
- Li et al., 2023 (BLIP‑2, LLaVA)
- OpenAI, 2023 (GPT‑4V)
- Google DeepMind, 2023 (Gemini, PaLM‑E)
- Kosmos-2, RT‑2, AudioPaLM papers
- Open-source repos: OpenCLIP, LLaVA, MiniGPT‑4, Kosmos-2, PaLM‑E demos, RT‑2 code snippets
