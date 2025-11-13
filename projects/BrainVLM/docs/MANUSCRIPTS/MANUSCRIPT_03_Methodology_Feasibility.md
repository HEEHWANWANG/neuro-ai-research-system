# Manuscript 03: Methodology - Feasibility Study Design

**Slides Covered**: Pages 17-32
**Word Count**: ~1750 words
**Date**: November 12, 2025

---

## Research Objectives and Workflow Design

UMBRELLA's feasibility study addresses a fundamental question: Can pre-trained vision-language models, trained exclusively on natural images, successfully learn meaningful features from brain MRI and support text generation for neuroimaging analysis?

This investigation follows a systematic three-phase workflow:

### Phase 1: Feasibility Check
- **Modality alignment approach validation**: BLIP-2 cross-attention vs LLaVA concatenation
- **Prompt engineering optimization**: Question-answer (QnA) vs description formats, with and without chain-of-thought reasoning
- **Multi-modal brain data unification**: Strategies for combining fMRI, sMRI, and dMRI
- **Parameter-efficient fine-tuning**: Which components to freeze vs train (vision encoder, language encoder, adapter layers)
- **Single-dataset validation**: Assessing model performance within individual datasets

### Phase 2: Large-Scale Training
- **Data preparation**: Preprocessing pipelines for ABCD, UKB, HCP, GARD datasets
- **Code preparation**: Implementing BLIP-2 and LLaVA architectures for 3D brain imaging
- **Large-scale training**: Multi-GPU distributed training on 50K+ brain scans
- **Iterative refinement**: Addressing failures and optimizing training procedures

### Phase 3: Inference and Evaluation
- **Within-dataset evaluation**: Testing model performance on held-out test sets from the same dataset
- **Dataset-specific performance**: Evaluating how well models learn representations for each individual dataset
- **Performance stratification**: Age, sex, and disease-specific validation within each dataset

---

## Datasets and Experimental Design

### Dataset Characteristics

The feasibility study leverages four large-scale neuroimaging datasets, with **each dataset evaluated independently**:

**ABCD (Adolescent Brain Cognitive Development)**:
- **Sample size**: 11,316 subjects
- **Modalities**: Structural MRI (T1-weighted), diffusion MRI
- **Age range**: 9-13 years (adolescents)
- **Targets**: Sex classification, BMI regression
- **Experimental design**: Train and test on ABCD data only (within-dataset evaluation)

**UKB (UK Biobank)**:
- **Sample size**: 42,794 subjects
- **Modalities**: Structural MRI (T1-weighted)
- **Age range**: 45-82 years (middle-aged to elderly)
- **Targets**: Sex classification, age regression
- **Experimental design**: Train and test on UKB data only (within-dataset evaluation)

**HCP (Human Connectome Project)**:
- **Sample size**: 1,200+ subjects
- **Modalities**: Functional MRI (resting-state)
- **Age range**: 22-37 years (young adults)
- **Targets**: Sex classification
- **Experimental design**: Train and test on HCP data only (within-dataset fMRI evaluation)

**GARD (Gwangju Alzheimer's and Related Dementias)**:
- **Sample size**: 4,328 subjects (balanced)
- **Modalities**: Structural MRI (T1-weighted)
- **Age range**: 60+ years (elderly with cognitive impairment)
- **Targets**: Sex classification, healthy control vs MCI classification
- **Experimental design**: Train and test on GARD data only (within-dataset clinical evaluation)

Combined, these datasets span ages 9-82, encompassing developmental, adult, and aging populations across healthy and clinical cohorts. **Each dataset is evaluated independently to assess model performance within specific domains.**

### Experimental Design: Single-Domain, Single-Modality Validation

**Critical methodological note**: The feasibility study does NOT test cross-dataset transfer learning (e.g., UKB → GARD) or cross-modality transfer (e.g., sMRI → fMRI). Instead, experiments evaluate:

1. **Within-dataset generalization**: How well models learn representations when training and testing on the same dataset
2. **Dataset-specific performance**: Whether natural image pre-trained encoders can adapt to different brain imaging datasets independently
3. **Modality-specific learning**: Whether models trained on sMRI generalize within sMRI data, and fMRI models within fMRI data
4. **Proof-of-concept validation**: Can vision-language models work for neuroimaging at all, within controlled single-domain scenarios?

**What this experimental design demonstrates**:
- Models can learn discriminative features from individual brain imaging datasets
- Natural image pre-training provides some benefit when fine-tuning on brain data
- Different datasets have different difficulty levels and sample size requirements
- Single-modality experiments establish baseline performance for each modality independently

**What this experimental design does NOT demonstrate**:
- Cross-dataset transfer learning (e.g., training on UKB and testing on GARD)
- Cross-modality transfer learning (e.g., training on sMRI and testing on fMRI)
- Unified representation learning across multiple datasets simultaneously
- True generalization across different brain imaging domains

**Future work implication**: The single-domain results provide proof-of-concept that UMBRELLA's architecture can work for neuroimaging. True validation of UMBRELLA's "universal" framework requires future experiments demonstrating cross-dataset and cross-modality transfer learning.

### Model Comparison Framework

The study systematically compares five architectural approaches:

**Baseline: 3D CNN**
- Custom 3D convolutional neural network trained from scratch on each dataset
- 12 million trainable parameters
- Represents standard neuroimaging analysis approach
- **Performance expectation**: Strong on limited data, domain-optimized

**ViT from Scratch**
- Vision Transformer trained from scratch on each brain imaging dataset
- Image size: 96³ voxels, patch size: 16³
- 1 billion trainable parameters
- **Performance expectation**: Data-hungry, poor with limited samples

**CLIP-ViT (Pre-trained, No LLM)**
- CLIP vision encoder fine-tuned on each brain imaging dataset
- Image size: 96³ voxels, patch size: 16³
- 1.2 million trainable parameters (frozen encoder + learned projection)
- **Performance expectation**: Efficient transfer from natural images within each dataset

**BLIP-2 (Vision-Language Model)**
- CLIP vision encoder + Q-Former + frozen LLM, fine-tuned on each dataset
- Image size: 120³ voxels, patch size: 10³
- Two-stage training: Q-Former pre-training, then LLM instruction tuning
- Cross-attention alignment between vision and language
- **Performance expectation**: Flexible text generation, requires staged training

**LLaVA (Vision-Language Model)**
- CLIP vision encoder + linear projection + frozen LLM, fine-tuned on each dataset
- Image size: 120³ voxels, patch size: 10³
- Single-stage training with concatenation alignment
- Instruction-tuned on GPT-4-generated visual conversations
- **Performance expectation**: Simpler architecture, potentially more robust

---

## Modality Alignment: BLIP-2 vs LLaVA

### BLIP-2: Cross-Attention Alignment

BLIP-2 employs a two-stage training paradigm:

**Stage 1: Q-Former Pre-training**
- Learns a set of query tokens that extract visual features through cross-attention
- Three objectives: image-text matching, image-text contrastive learning, image-grounded text generation
- Vision encoder and LLM remain frozen; only Q-Former trains
- **Purpose**: Learn a bottleneck representation that captures task-relevant visual information

**Stage 2: LLM Instruction Tuning**
- Connects trained Q-Former to frozen LLM decoder
- Trains on instruction-following datasets (question-answer pairs, image descriptions)
- Q-Former continues fine-tuning while LLM stays frozen
- **Purpose**: Adapt visual representations for language generation tasks

**Advantages**:
- Learned compression of visual information through query bottleneck
- Explicit separation of alignment (stage 1) and instruction following (stage 2)
- Lower computational cost (LLM never trains)

**Challenges**:
- Two-stage training adds complexity
- Requires large-scale stage 1 dataset for effective Q-Former training
- Limited flexibility if stage 1 training insufficient

### LLaVA: Concatenation Alignment

LLaVA simplifies the architecture:

**Single-Stage Training**:
- Linear projection layer maps vision encoder outputs to LLM embedding space
- Vision tokens concatenated with text tokens as input to LLM
- Vision encoder frozen, projection layer + LLM trained jointly
- **Purpose**: Direct alignment through gradient flow from language modeling loss

**Advantages**:
- Simpler architecture (no Q-Former complexity)
- Single-stage training easier to implement and debug
- Full LLM capacity available for multi-modal reasoning

**Challenges**:
- Higher computational cost (LLM trains)
- Longer input sequences (no compression bottleneck)
- Potentially more sensitive to hyperparameters

### Comparative Hypothesis

The study hypothesizes that **both alignment approaches should succeed for neuroimaging within individual datasets** provided the vision encoder learns meaningful brain features. The choice between cross-attention and concatenation may matter less than:
1. Quality of vision encoder pre-training
2. Appropriate prompt engineering for brain imaging
3. Sufficient training data scale within each dataset

---

## Prompt Engineering: The Critical Factor

UMBRELLA's text generation framework requires careful prompt design. The study explores multiple prompt strategies:

### Strategy 1: Question-Answer (QnA) Format

**Training**:
```
Question: You are a neurologist and now you are analyzing T1-weighted MRI Images.
Estimate the sex of subject from this image.
Answer: male
```

**Inference**:
```
Question: You are a neurologist and now you are analyzing T1-weighted MRI Images.
Estimate the sex of subject from this image.
Answer: male
```

**Rationale**: Instruction-following format common in LLM fine-tuning. Provides clear task specification.

### Strategy 2: Description → QnA (Single Label)

**Training**:
```
Caption: You are a neurologist analyzing T1-weighted MRI Images.
Answer: The brain shows male characteristics.
```

**Inference**:
```
Question: You are a neurologist analyzing T1-weighted MRI Images.
Estimate the sex of subject from this image.
Answer: male
```

**Rationale**: Tests format flexibility—training on descriptions, inferring from questions.

### Strategy 3: Description → QnA (Multi-Label)

**Training**:
```
Caption: You are a neurologist analyzing T1-weighted MRI Images.
Considering these features: overall brain volume, gray/white matter distribution,
ventricular size, cortical thickness pattern.
Answer: male
```

**Inference**:
```
Question: You are a neurologist analyzing T1-weighted MRI Images.
- Overall brain volume relative to skull
- Gray/white matter distribution patterns
- Ventricular size and shape
- Cortical thickness pattern
Estimate sex of subject from this image.
Answer: male
```

**Rationale**: Richer training signal from anatomical feature descriptions. Tests whether explicit feature guidance improves learning.

### Strategy 4: Chain-of-Thought (CoT)

**Training**:
```
Question: First, analyze key anatomical markers in the T1-weighted MRI, such as skull
robusticity, brain volume, and sinus size. Based on this analysis, determine the
subject's biological sex.
Answer: male
```

**Inference**: Same question format with reasoning prompt.

**Rationale**: Encourages step-by-step reasoning. Tests whether explicit reasoning improves or impairs performance.

### Prompt Complexity: Simple vs Complex Answers

The study also varies answer complexity:

**Simple Answer**: `Answer: male`

**Complex Answer**:
```
Answer: The brain shows typical male characteristics including larger overall brain
volume, lower gray-to-white matter ratio, increased ventricular size, and lower
cortical thickness.
```

**Hypothesis**: Simple answers may train faster; complex answers may provide richer learning signal but risk overfitting or model confusion.

---

## Parameter-Efficient Fine-Tuning Strategies

### Frozen Encoder + Trainable Projection

**Configuration**:
- Vision encoder (CLIP-ViT): Frozen
- Projection layer: Trainable (1-2 layers, ~1.2M parameters)
- Language model: Frozen (for BLIP-2) or trainable (for LLaVA)

**Rationale**: Preserves pre-trained visual understanding from CLIP while learning domain-specific alignment for brain MRI within each dataset.

### Frozen Encoder + Trainable Adapter Layers

**Configuration**:
- Vision encoder: Frozen
- Adapter layers: Transformer blocks inserted after projection (additional 2-4 layers)
- Language model: Frozen or trainable

**Rationale**: Increases model capacity for brain-specific feature learning while maintaining parameter efficiency.

**Experimental question**: Do additional adapter layers improve performance when training data is abundant within a single dataset?

---

## Experimental Variables and Ablations

### Image Resolution

**Standard configuration**: 96³ voxels (ViT variants), 120³ voxels (BLIP-2/LLaVA)
**Ablation**: 128³ voxels to test whether increased resolution improves age regression

**Hypothesis**: Higher resolution may capture finer anatomical details relevant for age-related atrophy patterns.

### Patch Size

**Standard**: 16³ (ViT), 10³ (BLIP-2/LLaVA)
**Trade-off**: Larger patches = fewer tokens (faster), smaller patches = finer detail (potentially better performance)

### Training Data Scale (Within-Dataset)

**ABCD only**: 11,316 samples (train/test split from ABCD)
**UKB only**: 42,794 samples (train/test split from UKB)
**ABCD + UKB combined**: 54,110 samples (combined training, but separate evaluation on each dataset's test set)

**Hypothesis**: Data scaling within datasets should narrow performance gap between CNN and ViT. Natural image pre-trained models may improve more with scale than CNNs when trained on individual datasets.

---

## Evaluation Metrics

### Classification Tasks (Sex, MCI vs HC)
- **Accuracy (ACC)**: Overall correct prediction rate on held-out test sets from the same dataset
- **AUROC (Area Under ROC Curve)**: Threshold-independent performance
- **Target**: ACC > 0.80, AUROC > 0.85 for viability within each dataset

### Regression Tasks (Age, BMI)
- **R² (Coefficient of Determination)**: Proportion of variance explained on test data from the same dataset
- **Mean Absolute Error (MAE)**: Average prediction error in years/kg
- **Target**: R² > 0.50 for age, R² > 0.30 for BMI (established benchmarks)

### Evaluation Protocol
- **Train/test splits**: Each dataset divided into training and test sets
- **No cross-dataset evaluation**: Models trained on ABCD are tested on ABCD test set only; models trained on UKB are tested on UKB test set only
- **Modality-specific evaluation**: sMRI models tested on sMRI data; fMRI models tested on fMRI data
- **Purpose**: Establish proof-of-concept that models can learn within individual domains before attempting cross-domain transfer

---

## Implementation Details

### Training Configuration

**Optimization**:
- Optimizer: AdamW with weight decay 0.01
- Learning rate: 1e-4 to 5e-5 (cosine decay)
- Batch size: 8-16 (limited by GPU memory for 3D volumes)
- Epochs: 10-50 depending on dataset size

**Hardware**:
- NVIDIA A100 GPUs (40GB or 80GB VRAM)
- Multi-GPU distributed training for large datasets
- Mixed precision (FP16) for memory efficiency

**Data Augmentation**:
- Random rotation: ±10 degrees
- Random intensity scaling: 0.9-1.1x
- Random Gaussian noise: σ = 0.02

---

## Hypotheses and Predictions

The feasibility study tests several key hypotheses:

**H1: Transfer Viability Within Datasets**: Natural image pre-trained vision encoders (CLIP-ViT) will achieve competitive performance (within 5% of CNN) on brain MRI classification tasks when training and testing on the same dataset.

**H2: Data Scaling Within Datasets**: Performance gap between ViT and CNN will narrow as dataset size increases from 10K to 40K+ samples within individual datasets.

**H3: Alignment Equivalence**: BLIP-2 and LLaVA will achieve similar performance on brain imaging within each dataset, with differences <3% accuracy.

**H4: Prompt Simplicity**: Simple, direct prompts will outperform complex chain-of-thought prompts for initial alignment within datasets.

**H5: Regression Challenge**: Text generation framework will struggle with continuous regression (age, BMI) compared to classification within datasets, requiring architectural refinement.

**H6: Proof-of-Concept Validation**: Models can learn meaningful representations from individual brain imaging datasets, establishing that vision-language architectures are viable for neuroimaging (but not yet demonstrating cross-dataset or cross-modality transfer).

These hypotheses guide the experimental design and interpretation of results, which are presented comprehensively in Manuscript 04.

---

**Next**: Manuscript 04 presents the complete experimental results, validates feasibility hypotheses, discusses findings, and outlines future research directions for UMBRELLA's development—including the critical need for true cross-dataset and cross-modality transfer learning experiments.
