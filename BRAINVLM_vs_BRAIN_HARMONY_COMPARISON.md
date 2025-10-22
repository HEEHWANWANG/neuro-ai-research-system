# BrainVLM vs Brain Harmony: Comparative Analysis

**Date**: October 23, 2025
**Paper**: Brain Harmony: A Multimodal Foundation Model Unifying Morphology and Function into 1D Tokens
**ArXiv**: https://arxiv.org/abs/2509.24693

---

## Executive Summary

Brain Harmony (2509.24693) and BrainVLM represent two distinct but complementary approaches to multimodal neuroimaging AI:

| Aspect | Brain Harmony | BrainVLM (LLaVa Track) |
|--------|---------------|----------------------|
| **Primary Goal** | Foundation model for structure-function integration | Clinical reasoning via question-answering |
| **Core Innovation** | 1D tokenization + brain hub fusion | LLaVa multimodal instruction tuning |
| **Data Modalities** | sMRI (T1) + fMRI joint representation | sMRI (T1) + fMRI separate/joint encoding |
| **Scale** | 14M T1 images + 70K fMRI (massive pretraining) | ABCD + UKB datasets (medium scale) |
| **Output Type** | Foundation representations for downstream tasks | Clinical text reports/classifications |
| **Architecture** | Vision Transformers (ViT-B) + Harmonizer | LLaVa 1.5-7B (CLIP vision + 7B LLM) |
| **Training Stage** | Unsupervised foundation pretraining | Supervised task-specific instruction tuning |

**Key Insight**: Brain Harmony is a **foundation model** (like SwiFT_v2) designed for feature extraction. BrainVLM is an **application-focused model** optimized for clinical interpretation tasks through natural language interfaces.

---

## 1. Architecture Comparison

### Brain Harmony Architecture

```
┌─────────────────────────────────────────────────────────┐
│         BRAIN HARMONY MULTIMODAL FUSION                 │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Structural MRI (T1)          Functional MRI (fMRI)     │
│  ┌──────────────────┐         ┌──────────────────┐      │
│  │  ViT-B (3D MAE)  │         │  Temporal Adaptive│      │
│  │  Token Encoder   │         │  Patch Embedding │      │
│  │  Z_S latents     │         │  (TAPE)           │      │
│  │  (hierarchical)  │         │  Z_F latents     │      │
│  └────────┬─────────┘         └────────┬─────────┘      │
│           │                           │                  │
│           └──────────┬────────────────┘                  │
│                      │                                   │
│           ┌──────────▼──────────┐                       │
│           │  Brain Hub Tokens   │                       │
│           │  (learnable 1D)     │                       │
│           └──────────┬──────────┘                       │
│                      │                                   │
│           ┌──────────▼──────────┐                       │
│           │  Harmonizer (Xfmr)  │                       │
│           │  Cross-modal fusion │                       │
│           └──────────┬──────────┘                       │
│                      │                                   │
│        ┌─────────────┴─────────────┐                    │
│        │                           │                    │
│   ┌────▼─────┐             ┌──────▼─────┐             │
│   │Decoder_S │             │Decoder_F   │             │
│   │Reconstruct            │Reconstruct  │             │
│   │T1 latents│             │fMRI latents│             │
│   └──────────┘             └────────────┘             │
│                                                           │
│  OUTPUT: Unified 1D token representation space          │
└─────────────────────────────────────────────────────────┘
```

**Key Components**:
1. **Unimodal Encoders** (separate): Vision Transformer for T1, temporal encoder for fMRI
2. **Brain Hub Tokens**: Learnable 1D vectors acting as representational bottleneck
3. **Harmonizer**: Transformer-based multimodal fusion via self-attention
4. **Dual Decoders**: Reconstruct original modality latents from hub tokens
5. **Training Objective**: Cross-reconstruction loss minimizes information loss in fusion

### BrainVLM (LLaVa) Architecture

```
┌──────────────────────────────────────────────────────────┐
│           BRAINVLM (LLaVA) MULTIMODAL PIPELINE           │
├──────────────────────────────────────────────────────────┤
│                                                            │
│  Structural MRI (T1)          Functional MRI (rsfMRI)    │
│  ┌──────────────────┐         ┌──────────────────┐       │
│  │ 120×120×120      │         │ 96×96×96×24      │       │
│  │ patches: 10³     │         │ patches: 16³×3   │       │
│  │ (3D volumetric)  │         │ (4D spatiotempo) │       │
│  └────────┬─────────┘         └────────┬─────────┘       │
│           │                           │                   │
│           └──────────┬────────────────┘                   │
│                      │                                    │
│           ┌──────────▼──────────┐                        │
│           │  CLIP Vision Encoder │                        │
│           │  (from LLaVa 1.5-7B) │                        │
│           │  Image embeddings    │                        │
│           └──────────┬──────────┘                        │
│                      │                                    │
│                      ├─ <image> token placeholder        │
│                      │                                    │
│           ┌──────────▼──────────────────────┐            │
│           │  Question-Answer Template       │            │
│           │  "USER: <image>                 │            │
│           │   You are a neurologist         │            │
│           │   analyzing T1-weighted MRI...  │            │
│           │   ASSISTANT: [response]"        │            │
│           └──────────┬──────────────────────┘            │
│                      │                                    │
│           ┌──────────▼──────────┐                        │
│           │  7B Language Model   │                        │
│           │  Instruction tuning  │                        │
│           │  Clinical reasoning  │                        │
│           └──────────┬──────────┘                        │
│                      │                                    │
│           ┌──────────▼──────────┐                        │
│           │   Clinical Output    │                        │
│           │  - Sex classification │                        │
│           │  - Cognitive pred.   │                        │
│           │  - Diagnostic report │                        │
│           └──────────────────────┘                        │
│                                                            │
│  OUTPUT: Task-specific clinical predictions/reports     │
└──────────────────────────────────────────────────────────┘
```

**Key Components**:
1. **Vision Encoder**: CLIP-based from LLaVa (shared with language model)
2. **Patch Embedding**: 3D patches for T1, 4D patches for rsfMRI
3. **Question-Answer Template**: Clinical domain-specific prompting
4. **Language Model**: 7B parameter LLM for instruction following
5. **Training**: Supervised instruction tuning on labeled brain imaging tasks
6. **Output**: Structured clinical predictions or narrative reports

---

## 2. Technical Approach Comparison

### Data Handling & Modality Integration

| Aspect | Brain Harmony | BrainVLM (LLaVa) |
|--------|---------------|-----------------|
| **T1 Processing** | 3D MAE with random masking, ViT-B encoder | 3D patch embedding (10×10×10), CLIP vision |
| **fMRI Processing** | Schaefer-400 ROI parcellation, TAPE (adaptive) | 4D patch embedding (16×16×16×3), temporal sequences |
| **Heterogeneity Handling** | **Dynamic TAPE**: resizes embeddings by TR | Fixed patch size across TRs; uses data augmentation |
| **Fusion Strategy** | **Late fusion**: Hub tokens + cross-modal attention | **Early fusion**: Joint instruction template with vision |
| **Pretraining Data** | 14M T1s + 70K fMRI (massive unsupervised) | ABCD + UKB (medium supervised) |
| **Training Paradigm** | Unsupervised foundation pretraining | Supervised instruction tuning |

### Key Technical Innovations

**Brain Harmony**:
1. **Temporal Adaptive Patch Embedding (TAPE)**: Novel solution to varying TR problem
   - Dynamically adjusts patch size: k = round(τ/s)
   - Uses pseudoinverse weight resizing: ω = ((B^k*_k)^T)† · ω*
   - Enables first fMRI data augmentation by temporal downsampling

2. **Geometric Pre-alignment**: Embeds structural constraints into functional representations
   - Uses Laplace-Beltrami operator on population cortical mesh
   - Natural vibration patterns guide fMRI encoding
   - Achieves +3-5% improvement over unaligned baseline

3. **Brain Hub Tokens**: Learnable bottleneck for structure-function relationships
   - Enables cross-modal information flow via self-attention
   - Compact yet expressive representation space
   - Enables efficient linear probing (0.0015M parameters)

**BrainVLM (LLaVa)**:
1. **Question-Answer Framework**: Clinical domain-specific prompting
   - "You are a neurologist analyzing T1-weighted MRI images..."
   - Natural language interface for clinical workflows
   - Enables zero-shot task transfer via instruction tuning

2. **Instruction Tuning**: Leverages LLaVa's multimodal training
   - Jointly trains vision (CLIP) and language (7B LLM) components
   - Clinical-specific instruction data for neuroimaging tasks
   - Superior reasoning capability vs adapter-based approaches

3. **Dual Modality Support**: Processes T1 and rsfMRI independently or jointly
   - Can handle single or paired modality inputs
   - Flexible for different clinical scenarios
   - Integrable with different label targets (sex, age, cognition)

---

## 3. Scale & Computational Resources

### Brain Harmony Scale

| Metric | Value |
|--------|-------|
| **Structural data** | 64,594 T1 images (UKB + ABCD) |
| **Functional data** | 252,961 fMRI samples with TR augmentation |
| **Paired T1-fMRI** | 69,360 paired samples |
| **Total pretraining scale** | ~14 million T1s + 70K fMRI globally |
| **Hardware** | 8× NVIDIA H100 GPUs (80GB each) |
| **Training time** | ~10 hours for multimodal fusion stage |
| **Model parameters** | Not explicitly stated (foundation model) |

### BrainVLM Scale

| Metric | Value |
|--------|-------|
| **Datasets** | ABCD + UKB for T1 and rsfMRI |
| **Datasets per modality** | 80% train, 10% val, 10% test split |
| **T1 resolution** | 120×120×120 voxels (smaller than Brain Harmony's 167×212×160) |
| **rsfMRI temporal** | 96×96×96×24 (24 time points), configurable |
| **Hardware** | DeepSpeed ZeRO-3 on multi-GPU setup (4× A100 estimated) |
| **Training time** | 50 epochs with 500 warmup steps (typical 2-4 hours per epoch) |
| **Model parameters** | 7B language model + CLIP vision encoder (multimodal) |

**Scale Assessment**:
- **Brain Harmony** is fundamentally larger pretraining (14M vs hundreds of thousands)
- **BrainVLM** is optimized for supervised fine-tuning on specific tasks
- Different scaling philosophies: foundation (BH) vs application (BV)

---

## 4. Downstream Task Performance

### Brain Harmony Results

**Neurodevelopmental Disorders** (Table 1 - Classification):
- **ABIDE-I**: 63.13% ACC, 72.63% F1 (BrainMass baseline: 65.64% ACC, 69.07% F1)
- **ABIDE-II**: 66.67% ACC, 74.88% F1 (BrainMass baseline: 59.35% ACC, 71.86% F1)
- **ADHD-200**: 70.09% F1 (BrainMass baseline: 65.99% F1)

**Neurodegenerative Disorders** (Table 2 - Classification):
- **PPMI (Parkinson's)**: 64.34% ACC (Brain-JEPA baseline: 60.36%)
- **ADNI (Alzheimer's)**: 64.65% ACC (Brain-JEPA baseline: 59.60%)

**Cognitive Prediction** (HCP-A):
- **Correlation for cognition**: 0.42 (Brain-JEPA baseline: 0.26)
- **62% improvement** over prior foundation model

**Key Finding**: Only 0.0015M trainable parameters in linear probing, demonstrating representation quality far exceeds parameter count.

### BrainVLM Expected Performance

**Targets (based on code configuration)**:
- **Sex classification** (T1 + rsfMRI): Expected >85% accuracy
- **Cognitive prediction**: Expected moderate correlation (TBD)
- **Age prediction**: Feasible downstream task
- **Disease classification**: Not yet demonstrated (future work)

**Advantages over Brain Harmony for specific tasks**:
1. Direct clinical language output (not just embeddings)
2. Interpretable reasoning through question-answer framework
3. Can be applied zero-shot to new questions without retraining
4. Better suited for clinical report generation

---

## 5. Complementary Strengths & Positioning

### Brain Harmony Strengths ✅

1. **Principled Foundation Model**
   - Large-scale unsupervised pretraining (14M images)
   - Generalizes excellently to diverse downstream tasks
   - Theoretical grounding in structure-function relationships

2. **Elegant Multimodal Integration**
   - Hub tokens elegantly encode structure-function interactions
   - Geometric pre-alignment embeds neuroscience principles
   - Superior representation quality (0.0015M params sufficient)

3. **Handles Data Heterogeneity**
   - TAPE solves the fundamental TR variation problem
   - Data augmentation strategy (temporal downsampling)
   - First solution to varying temporal resolution fMRI

4. **Scalability**
   - Foundation for many downstream applications
   - Proven on diverse clinical tasks
   - +3-10% improvement over single-modality baselines

### BrainVLM Strengths ✅

1. **Clinical Interpretability**
   - Natural language outputs (reports, classifications)
   - Neurologist-focused question templates
   - Explainable reasoning through language

2. **Instruction Tuning Flexibility**
   - Can handle diverse clinical questions zero-shot
   - No retraining needed for new tasks
   - Leverages LLaVa's instruction-following capability

3. **Practical Clinical Deployment**
   - Question-answer interface matches clinical workflows
   - Can integrate with clinical decision support systems
   - Natural interaction for medical professionals

4. **Dual Modality Handling**
   - Processes both T1 and rsfMRI in unified framework
   - Flexible single or paired modality inputs
   - Supports multiple label targets in single architecture

### Complementary Positioning

**Brain Harmony = Foundation Model Layer**
- Pretraining stage creating reusable neuroimaging representations
- Like ImageNet for brain MRI
- Enables downstream task scaling

**BrainVLM = Application Layer**
- Fine-tuned for clinical interpretation tasks
- Like CLIP + GPT-4 for neuroimaging
- Direct clinical utility through language interface

**Potential Integration**:
```
Brain Harmony Foundation
        ↓
[14M T1 pretraining + 70K fMRI]
        ↓
Extract rich representations
        ↓
BrainVLM Fine-tuning
        ↓
[Clinical instruction tuning]
        ↓
Clinical Question-Answering System
```

---

## 6. Innovation Analysis

### Brain Harmony's Key Innovations

| Innovation | Impact | Novelty |
|-----------|--------|---------|
| **TAPE (Temporal Adaptive Patch Embedding)** | Solves varying TR heterogeneity | ⭐⭐⭐⭐⭐ High |
| **Brain Hub Tokens** | Elegant structure-function fusion bottleneck | ⭐⭐⭐⭐ High |
| **Geometric Pre-alignment** | Embeds neuroscience principles into learning | ⭐⭐⭐⭐ High |
| **1D Tokenization** | First unified representation space | ⭐⭐⭐⭐⭐ High |
| **Large-scale Pretraining** | 14M images enables generalization | ⭐⭐⭐ Moderate |

### BrainVLM's Key Innovations

| Innovation | Impact | Novelty |
|-----------|--------|---------|
| **LLaVa for Neuroimaging** | First instruction-tuned VLM for brain MRI | ⭐⭐⭐⭐ High |
| **Question-Answer Template** | Clinical domain-specific prompting | ⭐⭐⭐ Moderate |
| **4D fMRI Patch Embedding** | Handles temporal dimension explicitly | ⭐⭐⭐ Moderate |
| **Multimodal Instruction Tuning** | Clinical reasoning via natural language | ⭐⭐⭐⭐ High |
| **Zero-shot Clinical Tasks** | Transfer learning without task-specific training | ⭐⭐⭐ Moderate |

---

## 7. Technical Comparison Table

| Technical Aspect | Brain Harmony | BrainVLM (LLaVa) |
|-----------------|---------------|-----------------|
| **Vision Backbone** | ViT-B (3D MAE) | CLIP (from LLaVa 1.5-7B) |
| **T1 Tokenization** | Random masking + reconstruction | 3D patch embedding |
| **fMRI Tokenization** | ROI parcellation + TAPE | 4D patch embedding |
| **Fusion Mechanism** | Hub tokens + self-attention | Joint instruction template |
| **Training Loss** | Reconstruction L2 loss | Instruction tuning cross-entropy |
| **Hyperparameters** | Learning rate, mask ratio, hub token count | Learning rate: 5e-5, warmup: 500 steps |
| **Batch Size** | Not specified | Per device: 2 (gradient accumulation: 1) |
| **Temporal Handling** | **TAPE (dynamic)** | Fixed patch size (static) |
| **Modality Coupling** | Late fusion (after encoding) | Early fusion (in template) |
| **Inference Speed** | Fast (simple linear probing) | Slower (LLM generation) |
| **Output Type** | Embeddings | Text/classifications |

---

## 8. Potential Synergies

### How BrainVLM Could Leverage Brain Harmony Insights

1. **Adopt TAPE for fMRI**: Replace fixed patch embedding with adaptive temporal encoding
   - Would handle varying TR in ABCD/UKB datasets
   - Better alignment with functional brain dynamics
   - Could improve cognitive prediction accuracy

2. **Incorporate Geometric Pre-alignment**: Constrain fMRI representation learning
   - Use Laplace-Beltrami operator on cortical surface
   - Better structure-function coupling
   - Potentially improve clinical predictions

3. **Hub Token Bottleneck**: Implement compact fusion layer
   - Replace direct concatenation with learnable hub tokens
   - More efficient multimodal representation
   - Better generalization to unseen tasks

### How Brain Harmony Could Leverage BrainVLM Insights

1. **Add Language Interface**: Make representations clinically interpretable
   - Fine-tune LLaVa on top of Brain Harmony embeddings
   - Create question-answering system for brain representations
   - Enable clinical report generation from representations

2. **Instruction Tuning**: Enable zero-shot task transfer
   - Use instruction tuning paradigm on Brain Harmony features
   - Broader applicability without task-specific training
   - Better generalization to novel clinical questions

3. **Clinical Validation**: Downstream application focus
   - Demonstrate clinical utility in real hospital workflows
   - Patient-level validation vs benchmark-only evaluation
   - Clinical interpretability requirements

---

## 9. Research Directions & Future Work

### For BrainVLM Project

**Short-term (Next 3 months)**:
1. Implement TAPE for fMRI temporal adaptivity
2. Add geometric pre-alignment for structure-function coupling
3. Benchmark against Brain Harmony embeddings on HCP cognitive prediction
4. Create comprehensive clinical task evaluation (not just ABCD/UKB)

**Medium-term (3-6 months)**:
1. Integrate Brain Harmony foundation model as feature extractor
2. Fine-tune LLaVa on Brain Harmony embeddings
3. Develop clinical report generation capability
4. Evaluate on real clinical datasets (Siemens scanner data, clinical phenotypes)

**Long-term (6-12 months)**:
1. Multi-scale architecture: Brain Harmony (foundation) → BrainVLM (application)
2. Clinical deployment pipeline with model interpretability
3. Comparison with radiologist performance on diagnostic tasks
4. Publication of unified neuroimaging foundation + application framework

### For Field Integration

1. **Foundation + Application Layer**: Combine Brain Harmony's robust features with BrainVLM's clinical interface
2. **Benchmark Creation**: Standardized evaluation for brain VLMs on neuroimaging tasks
3. **Clinical Validation**: Real-world hospital deployment studies
4. **Theoretical Integration**: Formal connection between structure-function representations and clinical reasoning

---

## 10. Conclusion

**Brain Harmony** and **BrainVLM** represent two essential but distinct layers of the neuroimaging AI stack:

| Layer | Brain Harmony | BrainVLM |
|-------|---------------|----------|
| **Role** | Foundation Model | Application Model |
| **Input** | Raw MRI data | Raw MRI + Clinical context |
| **Output** | Rich representations | Clinical predictions/reports |
| **Use Case** | Transfer learning baseline | Clinical decision support |
| **Scaling** | Foundation (14M images) | Application (specific tasks) |

### Strategic Positioning

**Brain Harmony** solves the fundamental problem of unified neuroimaging representation with principled techniques (TAPE, hub tokens, geometric alignment). It's ready for broad adoption as a foundation model.

**BrainVLM** solves the clinical interpretation problem, making neuroimaging AI accessible through natural language interfaces. It's ready for task-specific clinical deployment.

### Recommended Approach

For maximum impact, BrainVLM should:

1. **Short-term**: Adopt Brain Harmony's technical innovations (TAPE, pre-alignment)
2. **Medium-term**: Use Brain Harmony as foundation + add LLaVa for clinical interpretation
3. **Long-term**: Establish as the clinical application layer of neuroimaging AI ecosystem

This positions BrainVLM not as a competitor to Brain Harmony, but as a **complementary application framework** that brings foundation models to clinical reality.

---

**Document Created**: October 23, 2025
**Source Paper**: arXiv:2509.24693
**Related Project**: BrainVLM (LLaVa track - `/Users/apple/Desktop/BLIP_MRI`)
