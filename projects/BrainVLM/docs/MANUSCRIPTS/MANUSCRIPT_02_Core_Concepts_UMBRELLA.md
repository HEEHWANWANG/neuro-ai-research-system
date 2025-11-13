# Manuscript 02: Core Concepts - The UMBRELLA Framework

**Slides Covered**: Pages 10-16
**Word Count**: ~1500 words
**Date**: November 12, 2025

---

## UMBRELLA: Universal Framework for Multimodal Brain Representation Learning

UMBRELLA represents a paradigm shift in neuroimaging analysis: a universal framework that unifies multi-modal brain data (structural MRI, functional MRI, diffusion MRI) with language models to enable comprehensive brain analysis through text generation. The name itself—UMBRELLA—captures the framework's unifying vision: providing comprehensive coverage across brain imaging modalities, demographic factors, genetic predispositions, and clinical outcomes under a single architectural umbrella.

At its core, UMBRELLA transforms brain imaging analysis from a prediction problem into a language generation problem. Rather than training separate models for sex classification, age prediction, disease diagnosis, and biomarker quantification, UMBRELLA trains a single model to generate comprehensive textual descriptions that encompass all this information simultaneously.

## The Architecture: From Brain to Language

UMBRELLA's architecture follows a deceptively simple design:

```
Multi-Modal Brain Data → Tokenizers → Universal Encoder → LLM → Text Generation
```

**Input Pipeline**:
- **fMRI Tokenizer**: Converts functional MRI time-series into token sequences
- **sMRI Tokenizer**: Encodes structural brain morphology into tokens
- **dMRI Tokenizer**: Represents diffusion-weighted imaging and tractography as tokens
- **Text Tokenizer**: Standard language model tokenization for prompts and instructions

**Universal Encoder**: A shared representation space that aligns all brain imaging modalities with the language model's embedding space. This encoder leverages pre-trained vision transformers (specifically CLIP-ViT) fine-tuned on brain imaging data, enabling efficient transfer of visual understanding from natural images to neuroimaging.

**Large Language Model**: Open-source foundation models (Qwen, LLaMA, OpenAI CLIP) that have been pre-trained on massive text corpora, providing rich linguistic knowledge and reasoning capabilities.

**Output Generation**: Autoregressive text generation that produces comprehensive brain analysis, including demographic estimation, disease classification, biomarker quantification, genetic risk assessment, and confounder-adjusted disease effects.

### Example Input-Output Pair

**Input** (Multi-Modal Brain Scan + Prompt):
```
Question 1: You are a neurologist and now you are analyzing fMRI, sMRI, and dMRI.
Analyze the image and estimate age, sex, and intelligence score of subject from this image.

Question 2: Based on the above estimation, explain the cognitive ability of this subject
and estimate whether this subject will be diagnosed with MCI.
```

**Output** (Generated Text):
```
Answer 1: This subject is 66 years-old male with bad intelligence score.

Answer 2: Yes
```

This example illustrates UMBRELLA's core capability: generating multi-faceted analysis from brain imaging through natural language, enabling complex reasoning chains and integration with agentic AI systems.

## Text as the Universal Interface: A Strategic Choice

UMBRELLA's decision to use text as the universal interface stems from a profound observation about modern AI systems: **the power of current AI is rooted in language generation**. Large language models have demonstrated unprecedented capabilities in reasoning, planning, and problem-solving precisely because they operate in the linguistic domain.

### Why Text Matters for Neuroimaging

In diverse research domains beyond neuroscience, most data is stored in structured tables—formats that recent large language models can readily understand and process. By representing brain imaging information as text, UMBRELLA eliminates the need for training separate encoders for each type of auxiliary data:

- **Blood biomarkers**: "Amyloid-β: 850 pg/mL, Tau: 420 pg/mL"
- **Proteomics**: "APOE: ε4/ε4 genotype, TOMM40: T-allele carrier"
- **Microbiome**: "Gut diversity index: 3.2, Firmicutes/Bacteroidetes ratio: 1.8"
- **Digital phenotype**: "Daily step count: 6,500, Sleep quality: 6.2/10"
- **Assessments/Questionnaires**: "MMSE: 24/30, CDR: 0.5, Geriatric Depression Scale: 8/15"

This textual representation enables seamless integration of neuroimaging with multi-domain health data. A single language model can unify, analyze, and synthesize information across modalities without requiring specialized fusion architectures or modality-specific training procedures.

### Integration with Agentic AI Systems

By encoding neuroimaging analysis as language generation, UMBRELLA becomes immediately compatible with the most powerful AI paradigms:

- **Chain-of-Thought (CoT)**: The model can explain its reasoning step-by-step, enhancing interpretability
- **ReACT (Reasoning + Acting)**: UMBRELLA can integrate with tool-using agents that retrieve medical literature or query databases
- **Retrieval-Augmented Generation (RAG)**: The model can access up-to-date medical knowledge to inform diagnosis
- **Multi-Agent Systems**: UMBRELLA can serve as a specialized brain imaging agent within larger diagnostic workflows

This integration potential represents a strategic advantage: as AI systems evolve toward more sophisticated reasoning architectures, UMBRELLA remains compatible by virtue of operating in the language domain.

## Leveraging Pre-Trained Vision-Language Models: The Strategic Detour

A critical question arises: how can we align brain MRI embeddings with text embeddings when no large-scale brain imaging-text dataset exists?

Developing brain imaging versions of CLIP would require massive datasets (millions of brain scans paired with descriptive text) and enormous computational resources—a prohibitively expensive and risky endeavor. UMBRELLA takes a strategic detour: **directly projecting brain MRI images into pre-trained vision-language embedding spaces**.

### The Detour Strategy

Rather than training alignment from scratch, UMBRELLA leverages existing vision-language models:

1. **Start with CLIP-ViT**: A vision transformer pre-trained on 400M natural image-text pairs
2. **Freeze the encoder**: Keep CLIP's visual understanding intact
3. **Train adapter layers**: Learn lightweight projection modules that map brain imaging to CLIP's embedding space
4. **Connect to LLM**: Integrate with pre-trained language models through the aligned embeddings

This approach offers compelling advantages:

**Pros**:
- Cost-effective alignment of MRI images with text
- Leverages massive-scale pre-training from open-source models
- Easily expandable to new brain imaging modalities
- Integrable with existing LLM techniques (instruction tuning, RLHF)

**Cons**:
- Models trained on natural images, not neuroimaging
- Potential domain mismatch between natural and medical images
- Uncertainty about genuine feature learning vs shortcut solutions

The critical concern is whether models trained on natural images can "genuinely" learn meaningful visual features for brain MRI. This question motivates UMBRELLA's feasibility study, which we explore in Manuscript 03.

## The Revolutionary Core: Unified Language Generation Loss

Here lies UMBRELLA's most significant innovation—one that fundamentally distinguishes it from all prior multi-task learning approaches in medical imaging, including Med-Gemini.

### Traditional Multi-Task Learning (What UMBRELLA Does NOT Use)

Conventional multi-task learning for medical imaging employs explicit loss summation:

```
L_total = λ₁×L_disease + λ₂×L_age + λ₃×L_sex + λ₄×L_genetics + λ₅×L_biomarkers + ...
```

This approach suffers from critical limitations:
- Each new task requires a new loss function and hyperparameter (λ)
- Task weights must be manually tuned through expensive grid search
- Adding tasks destabilizes existing training (negative transfer)
- Scaling beyond 10-15 tasks becomes computationally intractable
- Loss function engineering dominates research effort

### UMBRELLA's Unified Language Generation Loss

UMBRELLA eliminates loss summation entirely:

```
L = CrossEntropyLoss(predicted_tokens, target_tokens)
```

All information—disease classification, age prediction, sex classification, genetic risk, biomarkers, cognitive outcomes, clinical reports, confounder-adjusted effects—is encoded as a unified text string:

```
"Disease: Alzheimer's disease | Age: 72 years | Sex: Female |
APOE: ε4/ε4 (high risk), AD-PRS: 0.72 | Hippocampus: -25% | MMSE: 24/30 |
Report: Medial temporal atrophy | Adjusted effect: Significant for disease"
```

The model learns to predict this text token-by-token, with a single cross-entropy loss optimizing prediction of ALL tokens simultaneously.

### Why This Works: Implicit Gradient Competition

Traditional multi-task learning achieves feature disentanglement through explicit gradient competition—carefully balanced loss weights force the model to allocate representational capacity to different tasks. UMBRELLA achieves the same disentanglement **implicitly through semantic structure**:

- **Age tokens** ("72", "years") naturally activate age-related features in the model
- **Disease tokens** ("Alzheimer's", "probable") naturally activate disease-specific features
- **Genetic tokens** ("APOE ε4/ε4") naturally activate genetic signature features

The model learns that different token positions correspond to different types of information. Features naturally cluster by semantic meaning without explicit loss engineering. This is not a shortcut or approximation—it is a fundamentally different mechanism for multi-task learning that leverages the rich semantic structure of natural language.

### Extensibility: The Killer Advantage

Consider adding a new confounder (e.g., scanner type) to the model:

**Traditional Approach**:
```python
# Step 1: Define new loss
L_scanner = CrossEntropyLoss(scanner_pred, scanner_label)

# Step 2: Add to summation with new weight
L_total = λ_disease×L_disease + ... + λ_scanner×L_scanner

# Step 3: Re-tune ALL weights (λ₁, ..., λ_N+1)
# Step 4: Validate no negative transfer
# Time: Days to weeks
```

**UMBRELLA Approach**:
```python
# Step 1: Extend target text
text = "... | Scanner: Siemens 3T Prisma | ..."

# Step 2: Train with SAME loss
L = CrossEntropyLoss(generated_text, target_text)

# Time: Hours (data preparation only)
# NO new hyperparameters, NO re-tuning, NO architectural changes
```

This extensibility is not merely convenient—it is transformative. UMBRELLA can scale from 8 tasks to 25 to 100+ confounders with identical training procedures. Traditional approaches become intractable beyond ~15 tasks due to combinatorial hyperparameter spaces.

## From Prediction Framework to Text Generation Framework

UMBRELLA's shift from prediction to text generation enables qualitative new capabilities:

### 1. Language-Centric Scalability

As language model size increases, UMBRELLA's performance improves—a property inherited from foundation model scaling laws. Similarly, as modality encoder size increases (larger vision transformers), representation quality improves. This scaling behavior mirrors successful vision-language models, providing a clear path to continuous improvement.

### 2. Complex Reasoning Through Language

Text generation enables chain-of-thought reasoning:
```
"First, analyzing brain volume relative to age (72 years):
The hippocampus shows 25% volume reduction, which exceeds normal aging (expected: 10-15%).
Given APOE ε4/ε4 genotype (doubles Alzheimer's risk), this suggests disease-specific atrophy.
Conclusion: Probable Alzheimer's disease with confounder adjustment."
```

This reasoning cannot be expressed in traditional classification outputs.

### 3. Natural Multi-Turn Interaction

UMBRELLA supports conversational analysis:
```
User: "What's unusual about this brain scan?"
UMBRELLA: "Asymmetric hippocampal atrophy, more severe on the left."
User: "Could this be normal aging?"
UMBRELLA: "Unlikely. At age 72, expected atrophy is 10-15%, not 30%."
User: "What genetic factors contribute?"
UMBRELLA: "The patient carries APOE ε4/ε4, which increases risk 12-fold."
```

This interaction paradigm enables collaborative analysis between clinicians and AI.

## Strategic Positioning: UMBRELLA vs Med-Gemini

Med-Gemini, Google's medical multi-modal foundation model, uses **data-proportional loss weighting**—a form of explicit loss summation where task weights are set by dataset size rather than manual tuning. This simplifies hyperparameter selection but does not solve the fundamental scaling problem.

UMBRELLA's unified language generation loss provides:
- **Superior extensibility**: Trivial to add 100+ confounders
- **Zero hyperparameters**: No task-specific weights to tune
- **Explicit confounder modeling**: Med-Gemini excludes demographics; UMBRELLA explicitly represents them
- **Semantic interpretability**: Text outputs inherently more interpretable than numerical predictions

UMBRELLA is not competing with Med-Gemini—it is advancing beyond Med-Gemini's paradigm by eliminating loss function engineering altogether.

## The Critical Validation Question

UMBRELLA's feasibility hinges on a single question: **Can natural image pre-trained vision encoders genuinely learn meaningful features from brain MRI?**

If the answer is no—if brain imaging requires fundamentally different visual understanding than natural images—then the strategic detour through CLIP fails, and UMBRELLA must pursue expensive from-scratch training. If the answer is yes, UMBRELLA achieves cost-effective alignment while inheriting the reasoning capabilities of large language models.

The next manuscript presents UMBRELLA's comprehensive feasibility study, which provides strong empirical evidence that natural image encoders transfer surprisingly well to brain imaging, validating the framework's foundational assumptions.

---

**Next**: Manuscript 03 details the experimental methodology, datasets, model comparisons, and prompt engineering strategies that validate UMBRELLA's feasibility for neuroimaging analysis.
