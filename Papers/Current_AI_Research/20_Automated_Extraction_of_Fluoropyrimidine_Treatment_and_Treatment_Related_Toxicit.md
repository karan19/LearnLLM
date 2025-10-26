# Automated Extraction of Fluoropyrimidine Treatment and Treatment-Related Toxicities from Clinical Notes Using Natural Language Processing

- **Authors:** Xizhi Wu, Madeline S. Kreider, Philip E. Empey, Chenyu Li, Yanshan Wang
- **Published:** 2025-10-23T16:44:39Z
- **Source:** http://arxiv.org/abs/2510.20727v1

## Abstract
Objective: Fluoropyrimidines are widely prescribed for colorectal and breast
cancers, but are associated with toxicities such as hand-foot syndrome and
cardiotoxicity. Since toxicity documentation is often embedded in clinical
notes, we aimed to develop and evaluate natural language processing (NLP)
methods to extract treatment and toxicity information.
  Materials and Methods: We constructed a gold-standard dataset of 236 clinical
notes from 204,165 adult oncology patients. Domain experts annotated categories
related to treatment regimens and toxicities. We developed rule-based, machine
learning-based (Random Forest, Support Vector Machine [SVM], Logistic
Regression [LR]), deep learning-based (BERT, ClinicalBERT), and large language
models (LLM)-based NLP approaches (zero-shot and error-analysis prompting).
Models used an 80:20 train-test split.
  Results: Sufficient data existed to train and evaluate 5 annotated
categories. Error-analysis prompting achieved optimal precision, recall, and F1
scores (F1=1.000) for treatment and toxicities extraction, whereas zero-shot
prompting reached F1=1.000 for treatment and F1=0.876 for toxicities
extraction.LR and SVM ranked second for toxicities (F1=0.937). Deep learning
underperformed, with BERT (F1=0.873 treatment; F1= 0.839 toxicities) and
ClinicalBERT (F1=0.873 treatment; F1 = 0.886 toxicities). Rule-based methods
served as our baseline with F1 scores of 0.857 in treatment and 0.858 in
toxicities.
  Discussion: LMM-based approaches outperformed all others, followed by machine
learning methods. Machine and deep learning approaches were limited by small
training data and showed limited generalizability, particularly for rare
categories.
  Conclusion: LLM-based NLP most effectively extracted fluoropyrimidine
treatment and toxicity information from clinical notes, and has strong
potential to support oncology research and pharmacovigilance.

## ELI5
Fluoropyrimidine chemotherapy can relieve cancer but also triggers dangerous toxicities, and clinicians often bury both observations deep within free-text notes. The authors deploy NLP models that read those notes nightly, highlight every dosage change, and flag phrases describing side effects like hand-foot syndrome or cardiotoxicity. Each extracted fact is anchored to patient identifiers and timelines so care teams can visualize who received which regimen and how they responded. Because the system automates what used to be hours of manual chart review, oncologists can intervene quickly when subtle symptoms start to accumulate. It's like having a vigilant medical scribe who never gets tired, continuously stitching together treatment stories so no warning sign slips through the cracks.
