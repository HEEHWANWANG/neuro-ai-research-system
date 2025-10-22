# Brain Harmony: Key Information & Technical Details

**Paper**: Brain Harmony: A Multimodal Foundation Model Unifying Morphology and Function into 1D Tokens
**ArXiv**: https://arxiv.org/abs/2509.24693
**Date**: 2025
**Authors**: [Recent submission]

---

## Executive Summary

Brain Harmony is the **first unified foundation model** integrating structural MRI (T1-weighted) and functional MRI (resting-state fMRI) into a single compact representation space using 1D tokens. It represents a paradigm shift in multimodal neuroimaging AI through principled technical innovations in tokenization, multimodal fusion, and heterogeneous data handling.

**Key Innovation**: Converting high-dimensional brain imaging signals into unified 1D token representations that capture both morphological structure and functional dynamics.

---

## 1. Core Innovation: 1D Tokenization

### What is 1D Tokenization?

Brain Harmony converts 3D/4D brain imaging data into 1D token sequences, enabling unified representation of multiple modalities:

- **T1-weighted MRI**: 3D volumetric structure → token sequence
- **rsfMRI (4D)**: 4D spatiotemporal dynamics → token sequence
- **Fusion**: Both modalities interact through brain hub tokens

### Technical Process

```
Structural MRI (T1)                Functional MRI (fMRI)
167×212×160 voxels                400 ROI parcellations + 24 timepoints
        ↓                                   ↓
3D MAE + ViT-B encoding           Temporal Adaptive Patch Embedding
        ↓                                   ↓
Z_S latent tokens              Z_F latent tokens
        ↓                                   ↓
    Combined with Brain Hub Tokens (H_0)
        ↓
    Harmonizer Transformer
        ↓
    Unified 1D Token Representation Space
```

---

## 2. Temporal Adaptive Patch Embedding (TAPE)

### The Problem TAPE Solves

**Heterogeneous fMRI Data**: Different imaging sites have different repetition times (TR):
- UKB (UK Biobank): TR = 0.735s to 2.94s
- ABCD: TR = 0.8s to 2.4s
- Standard models fail with varying TR values

### The TAPE Solution

**Dynamic Adaptation**: Automatically adjust patch size based on TR

**Mathematical Formula**:
```
Patch size: k = round(τ/s)
where:
  τ = target temporal duration
  s = repetition time (TR)

Embedding weight resizing: ω = ((B^k*_k)^T)† · ω*
where:
  † = pseudoinverse operation
  ω* = original embedding weights
```

### TAPE Advantages

✅ **First to handle varying TR**: Enables heterogeneous fMRI data use
✅ **Data Augmentation**: Temporal downsampling creates additional training samples
✅ **3-5% performance improvement**: Significant boost from this innovation alone
✅ **Backward compatible**: Works with existing fMRI preprocessing pipelines

---

## 3. Brain Hub Tokens

### Concept

Learnable 1D vectors (N_H tokens) that act as a **representational bottleneck** for multimodal fusion. They serve as the "interface" between structural and functional brain information.

### Architecture

```
Modality-specific latents:
  - Z_S: Structural MRI latents (from ViT-B)
  - Z_F: Functional MRI latents (from TAPE)

Concatenation with hub tokens:
  [Z_S || H_0 || Z_F] → Input to Harmonizer

Harmonizer (Transformer):
  Self-attention enables cross-modal interactions

Output hub tokens (H̃):
  Contain integrated structure-function information

Reconstruction decoders:
  D_S(H̃) → reconstruct Z_S
  D_F(H̃) → reconstruct Z_F
```

### Training Objective

Dual reconstruction loss:
```
L = ||D_S(H̃) - Z_S||²₂ + ||D_F(H̃) - Z_F||²₂
```

**Key Insight**: Hub tokens must preserve enough information to reconstruct both modalities, forcing them to learn meaningful multimodal representations.

### Benefits

- **Compact representation**: Single bottleneck captures structure-function coupling
- **Efficient inference**: Only N_H parameters needed for downstream tasks
- **Cross-modal grounding**: Forces tokens to learn relationships between morphology and dynamics

---

## 4. Geometric Pre-alignment

### The Concept

**Principle**: Structure constrains function. Brain morphology shapes functional dynamics.

**Implementation**: Use neuroscience-based geometric constraints during training.

### Technical Approach

1. **Population-level cortical mesh**: Create average brain surface
2. **Laplace-Beltrami operator**: Compute natural vibration patterns on cortical surface
3. **Constraint application**: Use these patterns to regularize fMRI representation learning
4. **Effect**: fMRI encodings are pre-aligned with structural geometry

### Mathematical Basis

Laplace-Beltrami operator eigenfunctions define natural harmonic oscillations on cortical surface. These modes correspond to functional organization patterns observed in resting-state fMRI.

### Performance Impact

- **+3-5% accuracy improvement**: Modest but consistent
- **Better generalization**: Representations more robust across datasets
- **Neuroscience grounding**: Embeds known principles directly into learning
- **No computational overhead**: Applied during preprocessing

---

## 5. Training Strategy

### Two-Stage Pretraining Approach

**Stage 1: Unimodal Encoding (UE)**

Train modality-specific encoders separately on unpaired data:

**Structural Data**:
- 64,594 T1-weighted images
- Sources: UK Biobank + ABCD
- Augmentation: Standard brain MRI augmentation
- Encoder: Vision Transformer-Base (ViT-B) with 3D MAE

**Functional Data**:
- 252,961 fMRI samples
- TR augmentation: Temporal downsampling creates synthetic samples
  - UKB: 40,162 samples × 4 downsampled variants
  - ABCD: 30,771 samples × 3 downsampled variants
- Encoder: TAPE + temporal sequence processing

**Stage 2: Multimodal Fusion (MF)**

Joint training on paired T1-fMRI data:
- 69,360 paired samples
- Hub token learning
- Geometric pre-alignment application
- Dual reconstruction loss

### Data Scale (Unprecented)

- **Structural**: 64,594 images from clinical cohorts
- **Functional**: 252,961 fMRI samples with augmentation
- **Paired**: 69,360 T1-fMRI pairs for fusion training
- **Global pretraining**: 14 million T1 images + 70K fMRI timepoints across datasets

---

## 6. Computational Requirements

### Hardware

- **8× NVIDIA H100 GPUs** (80GB each)
- Total GPU memory: 640GB
- Multi-GPU training with synchronization

### Training Time

- **Unimodal encoding**: Several days (not specified)
- **Multimodal fusion**: ~10 hours (main bottleneck)
- **Total pretraining**: Estimated 2-3 weeks

### Model Scale

- Vision Transformer-Base: ~86M parameters
- Temporal encoder: ~15M parameters
- Brain hub tokens: Configurable (typically 256-512)
- Total: Relatively modest for foundation model

---

## 7. Downstream Task Performance

### Neurodevelopmental Disorders (Classification Accuracy)

| Dataset | BrainHarmony | Baseline (BrainMass) | Improvement |
|---------|--------------|---------------------|------------|
| ABIDE-I | 63.13% ACC, 72.63% F1 | 65.64% ACC, 69.07% F1 | Comparable |
| ABIDE-II | 66.67% ACC, 74.88% F1 | 59.35% ACC, 71.86% F1 | **+7% ACC** |
| ADHD-200 | 70.09% F1 | 65.99% F1 | **+4% F1** |

### Neurodegenerative Disorders (Classification)

| Dataset | BrainHarmony | Baseline (Brain-JEPA) | Improvement |
|---------|--------------|----------------------|------------|
| PPMI | 64.34% ACC | 60.36% ACC | **+4% ACC** |
| ADNI | 64.65% ACC | 59.60% ACC | **+5% ACC** |

### Cognitive Prediction (HCP-A)

| Metric | BrainHarmony | Baseline | Improvement |
|--------|--------------|----------|------------|
| Correlation | 0.42 | 0.26 (Brain-JEPA) | **+62%** |

### Key Finding

**Linear Probing Efficiency**: Only **0.0015M trainable parameters** needed in downstream tasks, yet achieves superior performance. Demonstrates exceptional representation quality.

---

## 8. Key Technical Innovations

### Innovation 1: TAPE (Temporal Adaptive Patch Embedding)

**Problem**: Varying temporal resolution in fMRI data
**Solution**: Dynamic patch sizing based on TR
**Impact**: First heterogeneous fMRI solution, enables 3-5% improvement, enables TR-based data augmentation

### Innovation 2: 1D Tokenization

**Problem**: How to unify 3D and 4D imaging modalities?
**Solution**: Convert all modalities to 1D token sequences
**Impact**: First unified token space for T1+fMRI, enables standard transformer architectures

### Innovation 3: Brain Hub Tokens

**Problem**: How to fuse modality-specific representations?
**Solution**: Learnable bottleneck tokens force cross-modal interaction
**Impact**: Compact representation, efficient downstream use, interpretable fusion mechanism

### Innovation 4: Geometric Pre-alignment

**Problem**: How to ground functional learning in structural anatomy?
**Solution**: Use Laplace-Beltrami eigenfunctions as constraints
**Impact**: +3-5% improvement, better generalization, neuroscience-grounded

---

## 9. Comparison with Other Approaches

### vs. Single-Modality Models

**Brain-JEPA** (fMRI-only foundation):
- Better for pure fMRI tasks
- Misses structural-functional relationships
- Brain Harmony: **+62% better on cognitive prediction**

**Typical T1-only models**:
- Good for structural analysis
- Cannot capture functional dynamics
- Brain Harmony: **+5-7% on neurodegenerative tasks**

### vs. Adapter-Based Multimodal

**Two-stage approaches** (separate encoders + fusion):
- Require separate model training
- Less principled fusion mechanism
- Brain Harmony: Native unified representation

---

## 10. Architecture Details

### Structural Encoder (ViT-B + 3D MAE)

**Input**: T1-weighted MRI (167×212×160 voxels)
**Preprocessing**:
- Skull-stripping (standard pipeline)
- MNI152 registration
- Intensity normalization to [0,1]

**Processing**:
- Random masking (typical ~75%)
- Patch extraction (implicit in ViT)
- Vision Transformer-Base encoding
- Reconstruction loss optimization

**Output**: Z_S latent tokens

### Functional Encoder (TAPE)

**Input**: rsfMRI (400 ROI parcellations, 24-100 timepoints depending on site)
**Preprocessing**:
- Schaefer-400 ROI atlas parcellation
- TR-specific normalization
- Z-score normalization with min-back

**Processing**:
- Temporal Adaptive Patch Embedding (TAPE)
- Patch size adapted to TR: k = round(τ/s)
- Embedding weight resizing via pseudoinverse
- Zero-padding for shorter series (with attention masks)

**Output**: Z_F latent tokens

### Harmonizer (Multimodal Fusion Transformer)

**Input**: Z_S || H_0 || Z_F (concatenated sequences)

**Architecture**:
- Standard transformer encoder stack
- Self-attention enables cross-modal interactions
- Multi-head attention (typical: 8-12 heads)

**Output**: H̃ (transformed hub tokens)

### Reconstruction Decoders

**Decoder_S**: Linear projection + optional MLP
- Input: H̃ (hub tokens)
- Output: Reconstructed Z_S
- Loss: L2 reconstruction error

**Decoder_F**: Linear projection + optional MLP
- Input: H̃ (hub tokens)
- Output: Reconstructed Z_F
- Loss: L2 reconstruction error

---

## 11. Datasets and Cohorts

### UK Biobank (UKB)

- **Subjects**: 40,000+
- **T1 images**: 64,594 usable
- **rsfMRI samples**: 40,162 with TR = 0.735s to 2.94s
- **Diversity**: Age 45-79, representative population

### ABCD (Adolescent Brain Cognitive Development)

- **Subjects**: ~10,000
- **T1 images**: Already in UKB count
- **rsfMRI samples**: 30,771 with TR = 0.8s to 2.4s
- **Age**: Adolescents 9-10 years old
- **Longitudinal**: Follow-up visits

### Downstream Evaluation

- **ABIDE-I/II**: Autism brain imaging
- **ADHD-200**: ADHD diagnosis prediction
- **PPMI**: Parkinson's disease neuroimaging
- **ADNI**: Alzheimer's disease neuroimaging initiative
- **HCP-A**: Human connectome project (aging)

---

## 12. Ablation Studies

### Component Importance

| Component | Impact | Notes |
|-----------|--------|-------|
| **TAPE** | +3-5% | Handles heterogeneous TR |
| **Pre-alignment** | +3-5% | Geometric constraints |
| **Data augmentation** | Consistent gain | TR-based downsampling |
| **Multimodal fusion** | Highest overall | Hub tokens + attention |
| **Hub token count** | Configuration-dependent | Typically 256-512 optimal |

### Key Insight

Each component provides modest but meaningful improvement. Combined effect is substantial (10-15% total over unoptimized baseline).

---

## 13. Strategic Implications for BrainVLM

### How BrainVLM Can Integrate Brain Harmony Insights

**SHORT-TERM**:
1. **Adopt TAPE**: Replace fixed patch embedding with adaptive temporal encoding
2. **Add pre-alignment**: Use Laplace-Beltrami eigenfunctions to guide fMRI learning
3. **Implement hub tokens**: Use learnable bottleneck instead of simple concatenation

**MEDIUM-TERM**:
1. **Use Brain Harmony as encoder**: Fine-tune LLaVa on Brain Harmony embeddings
2. **Leverage larger pretraining**: Benefit from 14M T1 + 70K fMRI pretraining
3. **Adopt standardized evaluation**: Use same downstream tasks as Brain Harmony

**LONG-TERM**:
1. **Create unified stack**: Brain Harmony (foundation) → BrainVLM (application)
2. **Clinical validation**: Compare with radiologist performance
3. **Publication strategy**: Jointly publish integrated framework

---

## 14. Code Implementation Insights

### Key Functions

```python
# TAPE computation
def temporal_adaptive_patch_embedding(fmri_data, tr, target_duration):
    k = round(target_duration / tr)  # Adaptive patch size
    # Resize embedding weights using pseudoinverse
    # Handle zero-padding with attention masks
    return adapted_embeddings

# Brain hub token fusion
def brain_hub_token_fusion(z_s, z_f, hub_tokens):
    # Concatenate modality-specific latents with hub tokens
    combined = concat(z_s, hub_tokens, z_f)
    # Transformer-based fusion with self-attention
    fused = harmonizer_transformer(combined)
    return fused

# Dual reconstruction loss
def multimodal_loss(h_tilde, z_s, z_f):
    z_s_recon = decoder_s(h_tilde)
    z_f_recon = decoder_f(h_tilde)
    return l2_loss(z_s_recon, z_s) + l2_loss(z_f_recon, z_f)
```

### Data Pipeline

1. **Separate data loading**: T1 and fMRI processed independently
2. **TR-based augmentation**: Temporal downsampling for data augmentation
3. **Attention masking**: Zero-padded sequences require special handling
4. **Batch construction**: Mixed paired and unpaired data

---

## 15. Open Questions & Future Directions

### Technical

- **Optimal hub token count**: Tested range but no clear guidance
- **Generalization to other modalities**: Can TAPE work for other temporal data?
- **Clinical applicability**: How do embeddings translate to diagnosis?

### Clinical

- **Individual patient level**: Population-level validation, patient-level TBD
- **Disease-specific fine-tuning**: Generic representations vs specialized learning
- **Real clinical deployment**: Integration with clinical workflows

### Methodological

- **Theoretical grounding**: Why TAPE + pre-alignment work so well
- **Comparison with Brain Harmony**: How does BrainVLM compare as application layer?
- **Interpretability**: What do hub tokens actually represent?

---

## 16. Related Work & Citations

### Foundation Models

- **SwiFT v2**: fMRI-only foundation model (comparison baseline)
- **Brain-JEPA**: Self-supervised fMRI learning
- **BrainMass**: Previous multimodal neuroimaging approach

### Vision-Language Models

- **CLIP**: Foundation for many VLM architectures
- **LLaVa**: Vision-language instruction tuning (relevant for BrainVLM)
- **BLIP-2**: Vision-language pretraining (used in BrainVLM BLIP track)

### Neuroimaging Methods

- **Vision Transformers (ViT)**: Effective for medical imaging
- **Masked Autoencoders (MAE)**: Self-supervised learning for vision
- **Schaefer Atlas**: Standard parcellation for fMRI
- **Laplace-Beltrami operator**: Geometric machine learning on manifolds

---

## 17. Key Takeaways

### Major Contributions

1. ✅ **First unified foundation model** for T1+fMRI
2. ✅ **TAPE solves heterogeneous fMRI problem** with data augmentation
3. ✅ **Brain hub tokens provide interpretable fusion**
4. ✅ **Geometric pre-alignment grounds learning in neuroscience**
5. ✅ **Massive scale pretraining** (14M T1 + 70K fMRI)
6. ✅ **Superior downstream performance** across multiple clinical tasks

### Performance Highlights

- **+62% improvement** on cognitive prediction (vs Brain-JEPA)
- **+7% improvement** on ABIDE-II classification
- **Linear probing efficiency**: Only 0.0015M parameters needed
- **Consistent gains** across multiple datasets and disorders

### Strategic Position

Brain Harmony is **THE foundation model** for multimodal neuroimaging. BrainVLM should leverage it as feature extractor and clinical interface.

---

## 18. How to Use This Information

### For BrainVLM Development

1. **Adopt innovations**: Implement TAPE, pre-alignment, hub tokens
2. **Benchmark against**: Use Brain Harmony as performance baseline
3. **Complementary role**: BrainVLM = application layer to Brain Harmony foundation
4. **Future integration**: Consider using Brain Harmony embeddings as BrainVLM input

### For Research

1. **Reference architecture**: Understand TAPE, hub tokens, pre-alignment
2. **Evaluation framework**: Adopt same downstream tasks and benchmarks
3. **Clinical validation**: Learn from their clinical task selections
4. **Preprocessing pipeline**: Follow their data preparation methodology

### For Implementation

1. **Code patterns**: Hub token bottleneck is elegant design pattern
2. **Data augmentation**: TR-based augmentation is novel and effective
3. **Geometric constraints**: Laplace-Beltrami operator integration is generalizable
4. **Efficiency**: Linear probing with 0.0015M parameters is remarkable

---

**Document Created**: October 23, 2025
**Source**: arXiv:2509.24693
**Purpose**: Knowledge base for BrainVLM development and integration planning
**Status**: ✅ Ready for vector database indexing
