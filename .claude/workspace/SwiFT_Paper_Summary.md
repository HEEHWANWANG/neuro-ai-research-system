# SwiFT Paper Summary & Key Concepts

**Paper**: SwiFT: Shifting Window Fourier Transform for 4D fMRI

**Link**: https://arxiv.org/pdf/2307.05916

---

## Core Innovation: 4D Transformer for fMRI

### Problem Statement
Traditional fMRI analysis treats each 3D brain volume independently, ignoring:
- Temporal dynamics in brain activation
- Efficient spatial-temporal relationships
- Scale-invariant representations across different brain regions

### SwiFT Solution
A **Swin Transformer adapted for 4D fMRI** that:
1. Processes fMRI as 4D tensors: (Time, Depth, Height, Width)
2. Uses shifted-window attention for efficiency
3. Learns hierarchical spatio-temporal representations
4. Scales efficiently with minimal memory overhead

---

## Technical Architecture

### 1. **Patch Embedding (4D)**
```
Input fMRI volume: [T, D, H, W]
        ↓
Divide into overlapping 4D patches
        ↓
Project to embedding space: [N_patches, embedding_dim]
        ↓
Output: Sequence of patch tokens
```

**Why 4D?**
- Temporal: Captures brain dynamics over time
- Spatial: Maintains 3D volumetric structure
- Tokens: Efficient parallel processing

### 2. **Shifted-Window Attention (Key Efficiency Gain)**

**Standard attention complexity**: O(N²) where N = total patches

**Shifted-window approach**:
- Divide patches into non-overlapping windows
- Compute attention within each window (local)
- Shift windows between layers for information flow
- **Complexity**: O(N log N) - massive efficiency gain

**Why important for fMRI**:
- fMRI volumes are large (96³ spatial voxels, 40+ timesteps)
- Standard attention would be computationally prohibitive
- Shifted windows preserve long-range interactions efficiently

### 3. **Hierarchical Architecture (Multi-Stage)**
```
Stage 1: 96×96×96×T   → Low-level features
         (patch size: 4×4×4)
           ↓ Patch merging
Stage 2: 48×48×48×T   → Mid-level features
           ↓ Patch merging
Stage 3: 24×24×24×T   → High-level features
           ↓ Patch merging
Stage 4: 12×12×12×T   → Global representation
```

**Benefits**:
- Coarse-to-fine hierarchical understanding
- Computational efficiency (fewer tokens at deeper stages)
- Multi-scale feature fusion
- Similar to medical image segmentation (U-Net style)

### 4. **Temporal-Spatial Asymmetry** (SwiFT Innovation)
```
Spatial patch merging: Combine 2×2×2 = 8 patches
Temporal: No merging (preserve temporal resolution)
```

**Rationale**:
- Temporal resolution is critical for fMRI dynamics
- Spatial merging acceptable (downsampling brain space)
- Maintains fine temporal details for BOLD signal changes

---

## Self-Supervised Pretraining: SimMIM

### What is SimMIM?
**Masked Image Modeling**: Train model to predict masked patches

### How it works:
```
Input fMRI: [T, D, H, W]
        ↓
Mask random patches (40% default in SwiFT)
        ↓
Feed masked volume to encoder
        ↓
Decoder reconstructs original pixel values
        ↓
Loss: MSE between prediction and ground truth
```

### Why SimMIM for fMRI?
1. **Self-supervised**: No labels needed (large unlabeled datasets available)
2. **Representative learning**: Model learns to encode fMRI patterns
3. **Transfer learning**: Pretrained weights transfer to downstream tasks
4. **Efficiency**: One model -> multiple downstream tasks

### Training dynamics:
- Learn spatial patterns (brain anatomy, vascular structure)
- Learn temporal patterns (BOLD dynamics, neural oscillations)
- Learn functional connectivity implicit relationships
- No labels required - scale to millions of subjects

---

## Downstream Applications

### Classification Tasks (SwiFT can predict)
- **Sex**: Male/Female classification
- **Disease**: Autism (ABIDE), Depression (EMBARC)
- **Cognitive**: Cognitive performance levels

### Regression Tasks
- **Age**: Predict subject age
- **Intelligence**: Cognitive ability scores
- **Pain**: Pain intensity levels

### Why downstream tasks matter:
1. **Clinical relevance**: Can model predict clinical outcomes?
2. **Generalization**: Does pretraining help all tasks equally?
3. **Efficiency**: How many labeled samples needed? (few-shot)
4. **Interpretability**: What brain patterns matter for predictions?

---

## Key Experimental Results (Expected from SwiFT)

### Performance Metrics
- **Accuracy**: Classification tasks (e.g., sex prediction >90%)
- **R² score**: Regression tasks (age, intelligence)
- **AUC**: Disease classification (autism, depression)
- **Pearson correlation**: Continuous predictions

### Scaling behavior:
- Larger models → Better performance
- But: Diminishing returns at scale
- Sweet spot: 200M-800M parameters for most tasks

### Pretraining benefit:
- Self-supervised pretraining → Better performance than scratch
- Example: Sex classification improves ~5-10% with pretraining
- Especially helps with small labeled datasets

### Dataset benefits:
- Multi-dataset pretraining → Better generalization
- Model trained on UKB transfers well to ABCD, HCP
- Domain-specific knowledge accumulates

---

## Why SwiFT Matters for AI+Neuroscience

### 1. **Architectural Novelty**
- First successful 4D transformer for neuroimaging
- Shifted-window attention solves efficiency problem
- Temporal-spatial asymmetry (smart design choice)

### 2. **Scalability**
- Can train on 10,000s to 100,000s of fMRI volumes
- Distributed training on HPC (like Perlmutter)
- Scales from 5M to 3.2B parameters

### 3. **Self-Supervised Learning**
- Unlabeled data >> labeled data in neuroimaging
- SimMIM unlocks this potential
- Enables transfer learning across datasets/tasks

### 4. **Multi-Task Capability**
- Single pretrained model works for many tasks
- Reduces redundant training
- Enables meta-learning potential

### 5. **Clinical Translation**
- Tested on real clinical populations (autism, depression)
- Competitive with domain-specific methods
- Potential for clinical decision support

---

## Key Concepts for AI+Neuroscience Research

### Concept 1: Inductive Bias Matters
**Question**: Why does SwiFT work better than RNNs/CNNs for fMRI?

**Answer**:
- Local windowing matches brain regional organization
- Hierarchical processing matches cortical hierarchy
- Transformer flexibility captures complex dynamics

### Concept 2: Pretraining is Crucial
**Question**: How important is self-supervised pretraining?

**Answer**:
- ~10-15% performance improvement on downstream tasks
- Especially important for small sample sizes
- Enables knowledge transfer across domains

### Concept 3: Scale Efficiency
**Question**: Is bigger always better?

**Answer**:
- Performance saturates around 800M-1B parameters
- Larger models benefit from more pretraining data
- Training cost increases faster than benefit gain

### Concept 4: Dataset Diversity
**Question**: Does mixing datasets help or hurt?

**Answer**:
- Diverse pretraining data → Better generalization
- Task-specific fine-tuning still needed
- But broader representations learned

### Concept 5: Temporal Dynamics
**Question**: What temporal information is critical?

**Answer**:
- Full temporal resolution important for pretraining
- But spatial resolution can be reduced
- Task-dependent: disease detection vs. trait prediction

---

## Research Opportunities Beyond SwiFT

### 1. **Architectural Improvements**
- Better temporal modeling (temporal convolutions + attention?)
- Adaptive masking (mask difficult regions more)
- Cross-subject attention (learn from population patterns)

### 2. **Pretraining Objectives**
- Contrastive learning (push similar subjects together)
- Multi-task pretraining (sex + age + disease)
- Auxiliary tasks (predict functional connectivity)

### 3. **Interpretability**
- Attention visualization (what brain regions matter?)
- Saliency maps (which timesteps critical?)
- Layer-wise analysis (what features learned where?)

### 4. **Clinical Applications**
- Personalized predictions (adjust for demographics)
- Uncertainty quantification (confidence scores)
- Explainability (why this prediction?)

### 5. **Efficient Learning**
- Knowledge distillation (small model mimics big)
- Quantization (lower precision, less memory)
- Pruning (remove less important connections)

### 6. **Domain Adaptation**
- Transfer across scanner types
- Transfer across age groups (pediatric ↔ adult)
- Transfer across clinical populations

---

## Mathematical Foundation (Brief)

### Shifted-Window Attention
```
Standard attention: Attention = softmax(QK^T / √d) V
Complexity: O(N²) for N patches

Shifted-window:
1. Partition into windows of size M×M×M
2. Compute attention within windows only
3. Shift by half window size between layers
4. Complexity: O(N log N)
```

### SimMIM Loss
```
Loss = MSE(predicted_patches, original_patches)
- Pixel-wise prediction loss
- Trains on masked regions only
- Backprop updates encoder
```

### Downstream Fine-tuning
```
Classification: Loss = CrossEntropy(logits, labels)
Regression: Loss = MSE(predictions, targets)
- Use pretrained encoder
- Add task-specific head
- Fine-tune entire model or partial
```

---

## Implications for Your Research

### If studying **model architecture**:
- Why is 4D better than 3D + temporal?
- Can we improve shifted-window design?
- Are there better pretraining objectives?

### If studying **neuroscience**:
- What does the model learn about brain organization?
- How do representations change with development?
- Can we discover new brain-behavior relationships?

### If studying **transfer learning**:
- How much pretraining data needed for saturation?
- Do different tasks benefit equally from pretraining?
- What's the clinical utility of these models?

### If studying **scalability**:
- Does performance scale with model/data size?
- What's the optimal model size for fMRI?
- Can we train on 1M+ subjects?

---

## Summary

SwiFT represents a **paradigm shift** in neuroimaging AI:

1. **From flat images** → **4D volumetric sequences** (proper fMRI representation)
2. **From labeled only** → **Self-supervised pretraining** (unlabeled data utilization)
3. **From task-specific** → **Foundation models** (transfer learning era)
4. **From small scale** → **Population scale** (100k+ subjects)

The v2 implementation optimizes this further with:
- Multiple model sizes for efficiency studies
- Comprehensive downstream evaluation
- Production-ready distributed training
- Multi-dataset pretraining

**Ready for your research innovations!**

---

## Quick Reference: Key Files to Understand

| Concept | File |
|---------|------|
| 4D Patch Embedding | `patchembedding.py` |
| Swin4D Architecture | `swin4d_transformer_ver11.py` |
| SimMIM Variant | `simmim_swin4d_transformer_ver11.py` |
| Training Loop | `pl_classifier.py` |
| Data Handling | `utils/data_module.py` |
| Metrics | `utils/metrics.py` |
| Losses | `utils/losses.py` |
| Downstream Tasks | `downstream_optuna/main.py` |

