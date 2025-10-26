# Data & Modalities Glossary

Terminology describing data pipelines, modalities, and preprocessing workflows for AI systems.

## Dataset
**Definition:** Curated collection of examples (inputs/labels) used for training, validation, or testing. Should include metadata documenting provenance, licensing, and splits.
**ELI5:** A neatly labeled sticker book the model studies to learn what each sticker represents.

## Data Pipeline
**Definition:** End-to-end process that ingests raw data, validates quality, performs transformations, and serves batches to training jobs.
**Key notes:** Includes ETL stages, feature stores, and streaming ingestion.
**ELI5:** The assembly line that washes, chops, and plates ingredients before the model eats them.

## Data Augmentation
**Definition:** Techniques that create additional training samples via label-preserving transformations (cropping, noise, back-translation, MixUp).
**Key notes:** Improves generalization and robustness; policy search (AutoAugment) automates augmentation design.
**ELI5:** Take a photo, flip it, tilt it, or recolor it so the model sees more variety without needing new photos.

## Synthetic Data
**Definition:** Artificially generated samples (e.g., via simulators or generative models) used to supplement or replace real data.
**Key notes:** Helps cover rare scenarios or protect privacy; requires validation for distributional alignment.
**ELI5:** Create pretend driving scenes in a videogame so self-driving cars can practice without risking real crashes.

## Multimodal Data
**Definition:** Data combining multiple modalities (text, vision, audio, sensor streams). Requires aligned representations or temporal synchronization.
**ELI5:** A comic book with pictures, speech bubbles, and sound effects all telling the same story.

## Token Budget
**Definition:** Total number of tokens used for training or inference context. Budgeting matters for dataset cost, context window fits, and API pricing.
**ELI5:** The number of word “coins” you can spend before the model stops listening.

## Instruction / Prompt Dataset
**Definition:** Collections of request-response pairs used to teach models to follow instructions (e.g., Alpaca, Dolly, FLAN).
**Key notes:** Often curated via human annotation or synthetic generation with filtering.
**ELI5:** A stack of example conversations that show the model how polite helpers should respond.

## Alignment Dataset
**Definition:** Human preference rankings, policy critiques, or safety annotations used to align models with desired behaviors.
**ELI5:** People voting “good answer” or “bad answer” so the model learns what humans like.

## Metadata & Datasheets
**Definition:** Documentation artifacts that describe dataset motivation, collection process, risks, and recommended use (e.g., Datasheets for Datasets, Model Cards).
**ELI5:** The instruction manual and safety warnings that come with the dataset box.

## Data Leakage
**Definition:** Scenario where evaluation data contaminates training, leading to inflated metrics and poor real-world performance.
**ELI5:** Sneaking a peek at the test answers before exam day—scores look great but learning is fake.

## Class Imbalance
**Definition:** Unequal distribution of labels that can bias models. Mitigated via reweighting, resampling, or specialized losses (focal loss).
**ELI5:** Trying to learn about zoo animals when 95% of your photos are just elephants—you’ll think every animal has a trunk.

## Data Drift / Distribution Shift
**Definition:** Change in input or label distributions over time relative to training data. Leads to degraded model performance if unaddressed.
**ELI5:** The world changes—suddenly everyone wears new slang on T-shirts—and the model gets confused because it only studied old photos.

## Few-Shot / One-Shot Examples
**Definition:** Small number of labeled examples provided at inference (prompting) or during fine-tuning to adapt models quickly.
**ELI5:** Show the model one or two examples of a new card game and expect it to play along immediately.

## Contextual Embeddings
**Definition:** Token representations that depend on surrounding context, produced by models like BERT or GPT.
**ELI5:** The word “bank” feels different in “river bank” vs. “money bank,” so the embedding shifts based on the sentence.

## Vision-Language Pair
**Definition:** Matched image-text example used to train multimodal models (e.g., caption pairs, alt-text, interleaved documents).
**ELI5:** A postcard with a photo on the front and a matching description on the back.

## Audio Tokens / Units
**Definition:** Discrete representations of audio (HuBERT units, EnCodec tokens) enabling text-like modeling of speech.
**ELI5:** Chop speech into tiny sound blocks so the model can process audio like it processes words.

## Video Chunk / Clip Tokenization
**Definition:** Breaking video into spatiotemporal patches or tubelets fed into video transformers.
**ELI5:** Split a video into mini flipbook squares so the model can read it frame by frame.

## Knowledge Base / Vector Store
**Definition:** External memory containing embeddings of documents or facts, queried via similarity search to augment generation.
**ELI5:** A searchable notebook where similar ideas live on nearby pages ready to be quoted.

## RAG Corpus Maintenance
**Definition:** Processes for updating, deduplicating, and monitoring retrieval corpora to ensure freshness and prevent prompt injection via retrieved text.
**ELI5:** Regularly dust and reorganize the library so the model doesn’t pull outdated or malicious notes.

## Label Noise
**Definition:** Incorrect or inconsistent labels that introduce training noise; handled via robust loss functions, filtering, or confidence estimation.
**ELI5:** If some stickers in the book are mislabeled, the student learns the wrong names unless you fix or ignore them.
