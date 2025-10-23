# SwiFT_v2 Benchmark Comparison Framework

**Purpose**: Systematic evaluation of Brain-JEPA and BrainLM as benchmark models for SwiFT_v2
**Status**: Framework Design - Ready for Implementation
**Date**: October 23, 2025

---

## Overview

This document defines the framework for comprehensive benchmark comparison between SwiFT_v2 and two state-of-the-art brain foundation models:
1. **Brain-JEPA** (NeurIPS 2024): JEPA-based with gradient positioning and spatiotemporal masking
2. **BrainLM** (OpenReview 2024): MAE-based with scalable architecture (111M and 650M parameters)

---

## 1. Comparison Dimensions

### 1.1 Model Architecture
| Dimension | Brain-JEPA | BrainLM | SwiFT_v2 |
|-----------|-----------|---------|----------|
| Base Architecture | JEPA (I-JEPA) | MAE (Transformer) | [To be compared] |
| Positional Encoding | Gradient-based + Sinusoidal | Standard | [Compare] |
| Masking Strategy | Spatiotemporal (Cross-ROI, Cross-Time, Double-Cross) | Random patch masking | [Compare] |
| Backbone | Vision Transformer | Vision Transformer | [Compare] |
| Embedding Dimension | 768-1024 | Configurable | [Measure] |
| Parameters | [Estimate] | 111M or 650M | [Compare] |

### 1.2 Training Methodology
| Aspect | Brain-JEPA | BrainLM | SwiFT_v2 |
|--------|-----------|---------|----------|
| Objective | Non-contrastive prediction (JEPA) | Masked reconstruction (MAE) | [Compare] |
| Pretraining Data | UKB (UK Biobank) | UKB (UK Biobank) | [Document] |
| Loss Function | L2 prediction loss | L2 reconstruction loss | [Compare] |
| Hardware | 4x A100 (40GB) | Yale HPC (customizable) | [Document] |
| Training Duration | [Extract from paper] | [Extract from paper] | [Measure] |

### 1.3 Data Representation
| Property | Brain-JEPA | BrainLM | SwiFT_v2 |
|----------|-----------|---------|----------|
| Input Modality | fMRI (450 ROI parcellation) | fMRI (flexible) | [Document] |
| ROI Atlas | Schaefer (400) + Tian (50) | Flexible | [Document] |
| Temporal Resolution | 160 timepoints (downsampled) | Original | [Document] |
| Spatial Resolution | 450 ROIs | Variable | [Document] |
| Normalization | Robust scaling | Dataset-specific | [Compare] |

---

## 2. Evaluation Protocol

### 2.1 Downstream Task Evaluation

#### Task 1: Disease Classification
- **Datasets**:
  - ADNI (Alzheimer's): NC vs MCI vs AD
  - Clinical cohorts for other diseases
- **Metrics**:
  - Accuracy
  - AUC-ROC
  - Sensitivity/Specificity
  - F1 Score
- **Protocol**:
  - Linear probing (frozen encoder)
  - Fine-tuning (full network)
  - Compare performance across models

#### Task 2: Demographic Classification
- **Datasets**:
  - HCP-Aging (sex classification)
  - Age prediction (regression)
  - Other demographic features
- **Metrics**:
  - Accuracy (classification)
  - MAE/RMSE (regression)
  - Correlation coefficient
- **Protocol**:
  - Linear probe
  - Fine-tune
  - Cross-model comparison

#### Task 3: Representation Quality (No-Training Baseline)
- **Method**: KNN-based classification
  - Extract embeddings for all subjects
  - Use k-NN (k=5, 10, 20) for classification
  - No training required - pure representation quality
- **Advantage**: Training-free metric of representation quality
- **Implementation**: Use BrainLM's `inference_02_cls_token_knn_regressor.ipynb` as template

#### Task 4: Transfer Learning Efficiency
- **Protocol**:
  - Fine-tune on small subsets of data
  - Measure performance vs. training set size
  - Calculate data efficiency curves
- **Comparison**: Which model learns faster with limited data?

### 2.2 Representation Analysis

#### Analysis 1: Embedding Space Properties
- **Dimensionality**: Compare embedding dimensions
- **Correlation**: Compare embeddings for same subjects across models
- **Distance Metrics**: Intra-subject, inter-subject distances
- **Clustering**: Subject-based clustering quality

#### Analysis 2: Brain Structure Preservation
- **Connectivity**: Do embeddings preserve functional connectivity?
- **Regional Specialization**: Are brain regions distinguishable in embedding space?
- **Gradient Alignment**: How well do embeddings align with brain gradients?

#### Analysis 3: Interpretability
- **Feature Analysis**: Which embedding dimensions are most informative?
- **Attention Visualization**: Visualize what each model attends to
- **Brain Maps**: Project embeddings back to brain surface

### 2.3 Computational Efficiency

#### Metric 1: Model Size
- **Parameter Count**: Total parameters
- **Checkpoint Size**: MB on disk
- **Memory Usage**: Peak GPU memory during inference

#### Metric 2: Inference Speed
- **Throughput**: Subjects/second on standard GPU
- **Latency**: Per-subject inference time
- **Hardware Requirements**: GPU memory, CPU usage

#### Metric 3: Training Efficiency
- **Pretraining Time**: Hours on reference hardware
- **Convergence**: Epochs to convergence
- **Fine-tuning Time**: Hours to converge on downstream task

---

## 3. Benchmark Datasets

### 3.1 Datasets Already Supported

#### Brain-JEPA Tested Datasets
- UKB (UK Biobank) - Pretraining
- HCP-Aging (Human Connectome Project - Aging)
- ADNI (Alzheimer's Disease Neuroimaging Initiative)
- MACC (Memory, Ageing and Cognition Centre) - In-house

#### BrainLM Tested Datasets
- UK Biobank - Pretraining
- ADNI - Disease classification
- EMBARC - Depression, treatment response
- YooAttn - Attention networks
- ToPS - Obsessive-compulsive disorder

#### Intersection
- ADNI: Both models tested
- UKB: Both trained on it

### 3.2 Recommended Comparison Datasets
1. **ADNI** (Primary): Largest overlap, disease classification
2. **HCP-Aging** (Secondary): Sex classification, healthy aging
3. **Custom SwiFT_v2 Dataset** (Tertiary): If available

### 3.3 Dataset Preparation Protocol
```
Benchmark Data Structure:
benchmark_datasets/
├── ADNI/
│   ├── raw/                    # Original NIfTI files
│   ├── brain-jepa-embeddings/  # Brain-JEPA extracted embeddings
│   ├── brainlm-embeddings/     # BrainLM extracted embeddings
│   ├── swift-v2-embeddings/    # SwiFT_v2 extracted embeddings
│   ├── demographics.csv        # Subject metadata
│   └── labels.csv              # Disease labels, clinical scores
├── HCP-Aging/
│   └── [Similar structure]
└── custom-dataset/
    └── [Similar structure]
```

---

## 4. Comparison Metrics Summary

### 4.1 Performance Metrics
| Metric | Brain-JEPA | BrainLM | SwiFT_v2 | Notes |
|--------|-----------|---------|----------|-------|
| ADNI Disease Acc (Linear Probe) | [Measure] | [Measure] | [Measure] | Primary metric |
| ADNI Disease Acc (Fine-tune) | [Measure] | [Measure] | [Measure] | Secondary metric |
| HCP-Aging Sex Acc | [Measure] | [Measure] | [Measure] | Out-of-distribution test |
| KNN Classification (k=5) | [Measure] | [Measure] | [Measure] | No-training baseline |
| Data Efficiency (% of data) | [Curve] | [Curve] | [Curve] | Transfer learning |

### 4.2 Efficiency Metrics
| Metric | Brain-JEPA | BrainLM-111M | BrainLM-650M | SwiFT_v2 |
|--------|-----------|-------------|--------------|----------|
| Parameters (M) | [Estimate] | 111 | 650 | [Measure] |
| Embedding Dim | 768-1024 | [Measure] | [Measure] | [Measure] |
| Inference Time (ms/subject) | [Measure] | [Measure] | [Measure] | [Measure] |
| Peak GPU Memory (GB) | [Measure] | [Measure] | [Measure] | [Measure] |
| Pretraining Hours (4x A100) | [Extract] | [Extract] | [Extract] | [Measure] |

### 4.3 Representation Metrics
| Metric | Computation | Interpretation |
|--------|-----------|-----------------|
| Embedding Correlation | Pearson correlation of embeddings | How similar are representations? |
| Embedding Distance (Wasserstein) | Distribution distance | Different embedding distributions? |
| Nearest Neighbor Overlap | % of k-NN same across models | Consistent similarity structure? |
| Brain Structure Preservation | fMRI connectivity vs embedding space | Do embeddings preserve brain structure? |
| Dimensionality (PCA explained var) | PCA variance analysis | Effective dimensionality |

---

## 5. Experimental Protocol

### 5.1 Embedding Extraction Phase
1. **Brain-JEPA**:
   - Use modified extraction code from project
   - Output: Per-subject embeddings (n_frames × embedding_dim)
   - Save to: `benchmark_datasets/ADNI/brain-jepa-embeddings/`

2. **BrainLM**:
   - Use HuggingFace model loading
   - Extract at appropriate layer (typically CLS token)
   - Output: Per-subject embeddings
   - Save to: `benchmark_datasets/ADNI/brainlm-embeddings/`

3. **SwiFT_v2**:
   - Extract embeddings using same protocol
   - Match output format (n_frames × embedding_dim)
   - Save to: `benchmark_datasets/ADNI/swift-v2-embeddings/`

### 5.2 Evaluation Phase
1. **Setup**:
   - Prepare train/val/test splits (fixed seed)
   - Collect demographics and labels
   - Ensure balanced class representation

2. **Linear Probing**:
   - Freeze embeddings
   - Train logistic regression (sklearn)
   - Record accuracy, AUC, time to convergence

3. **Fine-tuning**:
   - Add task-specific head
   - Fine-tune on downstream task
   - Record best validation accuracy
   - Measure training time

4. **KNN Evaluation**:
   - No training required
   - Compute k-NN predictions (k=5, 10, 20)
   - Record accuracy

### 5.3 Analysis Phase
1. **Embedding Space Analysis**:
   - Compute correlations, distances
   - Visualize with t-SNE/UMAP
   - Analyze preservation of brain structure

2. **Statistical Comparison**:
   - Significance testing (t-tests, effect sizes)
   - Confidence intervals on metrics
   - Account for multiple comparisons

3. **Documentation**:
   - Create comparison tables
   - Generate visualization plots
   - Write interpretation section

---

## 6. Implementation Checklist

### Phase 1: Setup
- [ ] Create benchmark dataset directory structure
- [ ] Download ADNI data and prepare labels
- [ ] Extract demographics and prepare metadata
- [ ] Create standardized train/val/test splits

### Phase 2: Brain-JEPA Evaluation
- [ ] Load Brain-JEPA pretrained checkpoint
- [ ] Extract embeddings from ADNI
- [ ] Run linear probing evaluation
- [ ] Run fine-tuning evaluation
- [ ] Compute representation metrics
- [ ] Document results

### Phase 3: BrainLM Evaluation
- [ ] Load BrainLM models (111M and 650M)
- [ ] Extract embeddings from ADNI
- [ ] Run linear probing evaluation
- [ ] Run fine-tuning evaluation
- [ ] Compute representation metrics
- [ ] Document results

### Phase 4: SwiFT_v2 Evaluation
- [ ] Extract embeddings from ADNI
- [ ] Run linear probing evaluation
- [ ] Run fine-tuning evaluation
- [ ] Compute representation metrics
- [ ] Document results

### Phase 5: Comparison and Analysis
- [ ] Compile all metrics into comparison table
- [ ] Perform statistical significance testing
- [ ] Generate visualization plots
- [ ] Analyze computational efficiency
- [ ] Analyze representation quality
- [ ] Write comprehensive comparison section

### Phase 6: Paper Integration
- [ ] Create benchmark results section for manuscript
- [ ] Generate comparison figures
- [ ] Write interpretation and discussion
- [ ] Cite related work appropriately
- [ ] Create supplementary materials

---

## 7. Output and Deliverables

### 7.1 Comparison Table (Main Results)
```
Table: Performance Comparison on ADNI Disease Classification

Model               | Parameters | Linear Probe | Fine-tune | KNN-5 | Inference Time
                   |            | Accuracy     | Accuracy  | Acc   | (ms/subject)
Brain-JEPA         | [M]        | [%]          | [%]       | [%]   | [ms]
BrainLM-111M       | 111M       | [%]          | [%]       | [%]   | [ms]
BrainLM-650M       | 650M       | [%]          | [%]       | [%]   | [ms]
SwiFT_v2           | [M]        | [%]          | [%]       | [%]   | [ms]
Random Baseline    | -          | [%]          | [%]       | [%]   | [ms]
```

### 7.2 Visualization Outputs
1. **Performance Comparison**:
   - Bar plots (accuracy across models)
   - Error bars (confidence intervals)
   - Statistical significance markers

2. **Efficiency Comparison**:
   - Parameter count vs. performance
   - Inference time vs. performance
   - Memory usage vs. performance

3. **Representation Analysis**:
   - t-SNE/UMAP visualization of embeddings
   - Correlation matrices between models
   - Brain surface maps of learned representations

### 7.3 Detailed Results Document
- Methodology details
- Full results tables
- Statistical analysis
- Interpretation and discussion
- Limitations and future work

---

## 8. Manuscript Integration

### 8.1 Benchmark Section Structure
1. **Introduction**: Why these benchmarks, what they measure
2. **Methods**: Data, evaluation protocol, metrics
3. **Results**: Comparative performance tables and figures
4. **Discussion**: Interpretation, strengths/weaknesses
5. **Supplementary**: Extended tables, additional analyses

### 8.2 Key Points for Manuscript
- Position SwiFT_v2 relative to state-of-the-art
- Highlight specific advantages/disadvantages
- Support claims with empirical evidence
- Acknowledge limitations honestly
- Propose future research directions

---

## 9. Timeline Estimate

| Phase | Task | Estimated Time |
|-------|------|-----------------|
| 1 | Setup and data prep | 1-2 days |
| 2 | Brain-JEPA evaluation | 2-3 days |
| 3 | BrainLM evaluation | 2-3 days |
| 4 | SwiFT_v2 evaluation | 1-2 days |
| 5 | Analysis and comparison | 2-3 days |
| 6 | Paper integration | 1-2 days |
| **Total** | | **9-15 days** |

---

## 10. Success Criteria

### 10.1 Technical Success
- ✅ Extract embeddings from all models on same data
- ✅ Complete evaluation on all downstream tasks
- ✅ Compute all comparison metrics
- ✅ Statistical significance testing performed

### 10.2 Scientific Quality
- ✅ Fair comparison (same hyperparameters where possible)
- ✅ Multiple datasets tested
- ✅ Honest presentation of results (good and bad)
- ✅ Proper statistical rigor and error reporting

### 10.3 Publication Quality
- ✅ Clear, interpretable figures
- ✅ Comprehensive results tables
- ✅ Proper citations of benchmarked models
- ✅ Reproducible experimental details

---

## References

1. **Brain-JEPA**: Dong et al. (2024) - NeurIPS 2024 Spotlight
2. **BrainLM**: Vandijk Lab (2024) - OpenReview
3. **SwiFT_v2**: [Your reference]
4. **ADNI**: https://adni.loni.usc.edu/
5. **HCP-Aging**: https://www.humanconnectome.org/study/hcp-lifespan-aging

---

**Document Version**: 1.0
**Status**: Framework Ready for Implementation
**Next Step**: Begin Phase 1 (Setup and Data Preparation)
