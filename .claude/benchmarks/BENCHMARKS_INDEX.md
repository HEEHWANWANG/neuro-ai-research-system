# SwiFT_v2 Benchmark Models - Master Index

**Purpose**: Central reference for benchmark models and comparison framework
**Date**: October 23, 2025
**Status**: ✅ Complete - Ready for Evaluation

---

## Overview

SwiFT_v2 will be evaluated against two state-of-the-art brain foundation models:

1. **Brain-JEPA** - Joint-Embedding Predictive Architecture for brain dynamics
2. **BrainLM** - Masked Autoencoder for brain activity recordings

This index provides quick navigation to all benchmark-related documentation and code.

---

## Quick Reference

### Brain-JEPA
- **Paper**: Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking
- **Venue**: NeurIPS 2024 (Spotlight)
- **ArXiv**: https://arxiv.org/abs/2409.19407
- **Architecture**: Vision Transformer + JEPA (Non-contrastive learning)
- **Key Innovation**: Gradient-based positioning + Spatiotemporal masking
- **ROIs**: 450 (400 Schaefer cortical + 50 Tian subcortical)
- **Embedding Dim**: 768-1024
- **Pretraining Data**: UK Biobank
- **Evaluated On**: UKB, HCP-Aging, ADNI, MACC

### BrainLM
- **Paper**: BrainLM: A Foundation Model for Brain Activity Recordings
- **Venue**: OpenReview
- **GitHub**: https://github.com/vandijklab/BrainLM
- **Architecture**: Vision Transformer + MAE (Masked Autoencoder)
- **Key Innovation**: Scalable masked prediction, transfer learning
- **Model Variants**: 111M parameters (efficient), 650M parameters (high-capacity)
- **Pretraining Data**: UK Biobank
- **Evaluated On**: UKB, ADNI, EMBARC, YooAttn, ToPS

### SwiFT_v2
- **Status**: [Under Evaluation]
- **Architecture**: [To be compared]
- **Parameters**: [To be measured]
- **Embedding Dim**: [To be measured]
- **Pretraining Data**: [Document]

---

## Documentation Structure

### Analysis Documents
1. **`BRAIN_JEPA_ANALYSIS.md`** (12 sections, comprehensive)
   - Technical contributions
   - Data specifications
   - Model architecture details
   - Training methodology
   - Code structure and embedding extraction
   - Strengths and limitations
   - Relevance for SwiFT_v2

2. **`BRAINLM_ANALYSIS.md`** (15 sections, comprehensive)
   - Technical contributions
   - Data and datasets
   - Model architecture
   - Training methodology
   - Downstream capabilities
   - Code structure
   - Model variants and usage
   - Strengths and limitations
   - Relevance for SwiFT_v2

3. **`BENCHMARK_COMPARISON_FRAMEWORK.md`** (10 sections, operational)
   - Comparison dimensions
   - Evaluation protocols
   - Benchmark datasets
   - Metrics summary
   - Experimental protocols
   - Implementation checklist
   - Output deliverables
   - Manuscript integration
   - Timeline and success criteria

4. **`DATASETS_FOR_EVALUATION.md`** (📋 Dataset specifications)
   - ADNI dataset (primary evaluation dataset)
   - HCP-Aging dataset (secondary evaluation dataset)
   - Paper-derived dataset information
   - Data access and preprocessing guidelines
   - Quality control standards
   - Integration with benchmark framework

5. **`DOWNSTREAM_EVALUATION_TASKS.md`** (📋 NEW - Task definitions)
   - Task 1: MCI-to-AD Conversion Prediction (neurodegenerative domain)
   - Task 2: Antidepressant Response Prediction (psychiatric domain)
   - Task 3: Pain-Evoked Brain State Classification (functional domain)
   - Clinical significance and evaluation protocols
   - Implementation workflow and expected outcomes
   - Unified benchmark suite specifications

---

## Key Comparison Dimensions

### Architecture
| Aspect | Brain-JEPA | BrainLM |
|--------|-----------|---------|
| Base | JEPA | MAE |
| Masking | Spatiotemporal (structured) | Random patches |
| Positional Encoding | Gradient-based | Standard |
| Output Layer | Global pooling | CLS token |
| Parameter Count | [Estimate] | 111M / 650M |

### Training
| Aspect | Brain-JEPA | BrainLM |
|--------|-----------|---------|
| Objective | Prediction loss | Reconstruction loss |
| Pretraining Data | UK Biobank | UK Biobank |
| Hardware | 4x A100 (40GB) | Flexible |
| Loss Type | Non-contrastive | Contrastive/Masked |

### Evaluation
| Task | Brain-JEPA | BrainLM |
|------|-----------|---------|
| Linear Probe | HCP-Aging (sex), ADNI (disease) | Multiple datasets |
| Fine-tuning | Yes | Yes |
| Zero-shot | Not reported | Tutorial provided |
| KNN Baseline | Not reported | Available |

---

## Project Code Locations

### Brain-JEPA
- **Project Root**: `/Users/apple/Desktop/Brain-JEPA`
- **Key Scripts**:
  - `downstream_embedding_extraction.py` - Extract embeddings from pretrained model
  - `src/datasets/external_dataset_parcellation.py` - Prepare external data
  - `src/models/vision_transformer.py` - ViT architecture
- **Documentation**: `EMBEDDING_EXTRACTION_GUIDE.md` (detailed extraction protocol)
- **Modified For**: Extracting embeddings from pretrained checkpoints

### BrainLM
- **Project Root**: `/Users/apple/Desktop/BrainLM`
- **Key Scripts**:
  - `brainlm_mae/modeling_brainlm.py` - Core model class
  - `brainlm_mae/configuration_brainlm.py` - Configuration
  - `continue_train_same_wandb.py` - Training script
- **Notebooks**:
  - `brainlm_tutorial.ipynb` - Data preprocessing
  - `inference_02_cls_token_knn_regressor.ipynb` - KNN evaluation
  - `inference_03_cls_token_mlp_classification.ipynb` - Classification
- **Model Hub**: https://huggingface.co/vandijklab/brainlm/
- **Modified For**: Embedding extraction pipeline

---

## Evaluation Datasets

### Primary: ADNI
- **Disease**: Alzheimer's (NC vs MCI vs AD)
- **Subjects**: [Number]
- **Task**: Disease classification
- **Relevance**: Both models evaluated here; primary comparison point
- **Status**: [To be prepared]

### Secondary: HCP-Aging
- **Task**: Sex classification
- **Subjects**: [Number]
- **Relevance**: Brain-JEPA evaluated here; out-of-distribution test
- **Status**: [To be prepared]

### Tertiary: SwiFT_v2 Internal Datasets
- **Status**: [To be documented]

---

## Experimental Workflow

```
Step 1: Setup
├─ Create benchmark dataset structure
├─ Download and prepare ADNI data
├─ Prepare train/val/test splits
└─ Compile metadata and labels

Step 2: Brain-JEPA Evaluation
├─ Load pretrained checkpoint
├─ Extract embeddings (ADNI)
├─ Linear probing
├─ Fine-tuning
├─ Representation analysis
└─ Save results and embeddings

Step 3: BrainLM Evaluation
├─ Load from HuggingFace (111M and 650M)
├─ Extract embeddings (ADNI)
├─ Linear probing
├─ Fine-tuning
├─ KNN-based evaluation
├─ Representation analysis
└─ Save results and embeddings

Step 4: SwiFT_v2 Evaluation
├─ Extract embeddings (same data)
├─ Run same downstream tasks
├─ Compute comparison metrics
└─ Save results and embeddings

Step 5: Analysis & Comparison
├─ Compile results table
├─ Perform statistical testing
├─ Generate visualizations
├─ Analyze representations
└─ Document findings

Step 6: Manuscript Integration
├─ Create benchmark section
├─ Write results and discussion
├─ Generate figures for paper
└─ Prepare supplementary materials
```

---

## Key Metrics to Compute

### Performance Metrics
- Linear probing accuracy
- Fine-tuning accuracy
- AUC-ROC
- Sensitivity/Specificity
- Data efficiency curves

### Efficiency Metrics
- Model parameters
- Embedding dimensions
- Inference time per subject
- Peak GPU memory
- Pretraining time

### Representation Metrics
- Embedding correlation
- Preserved brain structure
- Dimensionality (PCA)
- KNN classification quality
- Nearest neighbor overlap

---

## Analysis Summaries

### Brain-JEPA: Key Strengths
✅ Novel gradient-based positional encoding
✅ Structured spatiotemporal masking (multi-scale)
✅ Non-contrastive learning (efficient, no collapse)
✅ NeurIPS 2024 spotlight recognition
✅ Clear code and documentation
✅ Embedding extraction pipeline available

### Brain-JEPA: Key Limitations
⚠️ Designed for specific ROI atlas (Schaefer + Tian)
⚠️ High computational cost for pretraining (4x A100)
⚠️ Temporal downsampling (490 → 160 frames)
⚠️ UK Biobank-specific pretraining

### BrainLM: Key Strengths
✅ Scalable variants (111M and 650M)
✅ MAE approach (simple, interpretable)
✅ HuggingFace integration (easy loading)
✅ Multiple downstream task examples
✅ KNN-based no-training baseline
✅ Tested on diverse datasets (ADNI, EMBARC, YooAttn, ToPS)

### BrainLM: Key Limitations
⚠️ Flash Attention complexity for 650M model
⚠️ Preprocessing varies by dataset
⚠️ Fine-tuned models not yet released
⚠️ Less neuroscience-specific design

---

## Relevance for SwiFT_v2 Paper

### What These Benchmarks Establish
1. **State-of-the-art Baselines**: Current best performance on brain fMRI
2. **Architecture Diversity**: Two different approaches (JEPA vs MAE)
3. **Scale Range**: Covers 111M to 650M parameters
4. **Evaluation Best Practices**: Standardized downstream tasks

### SwiFT_v2 Positioning
- Compare to cutting-edge foundation models
- Demonstrate advantages/tradeoffs
- Position in landscape of brain foundation models
- Support claims with empirical evidence

### Expected Paper Sections
- **Introduction**: Brief overview of benchmarks
- **Methods**: How comparison conducted (datasets, metrics)
- **Results**: Performance tables, efficiency comparison
- **Discussion**: SwiFT_v2 advantages/disadvantages vs benchmarks
- **Supplementary**: Extended analysis, visualizations

---

## Next Steps

### Immediate (This Week)
1. ✅ Complete paper and code analysis (DONE)
2. ✅ Create benchmark documentation (DONE)
3. ⏳ Prepare datasets and directory structure
4. ⏳ Extract Brain-JEPA embeddings
5. ⏳ Extract BrainLM embeddings (111M and 650M)

### Short-term (Next 2 weeks)
1. ⏳ Extract SwiFT_v2 embeddings
2. ⏳ Run downstream task evaluations
3. ⏳ Compute comparison metrics
4. ⏳ Perform statistical analysis

### Medium-term (Next month)
1. ⏳ Analyze representations
2. ⏳ Generate comparison visualizations
3. ⏳ Write manuscript section
4. ⏳ Prepare final benchmark report

---

## Files in This Directory

```
benchmarks/
├── BENCHMARKS_INDEX.md                    # This file
├── BRAIN_JEPA_ANALYSIS.md                 # Brain-JEPA paper analysis
├── BRAINLM_ANALYSIS.md                    # BrainLM paper analysis
├── BENCHMARK_COMPARISON_FRAMEWORK.md      # Evaluation framework
├── results/                                # [Results directory - TBD]
│   ├── adni_comparison.csv                # [Results table]
│   ├── hcp_aging_comparison.csv           # [Results table]
│   └── visualizations/                    # [Plots and figures]
└── embeddings/                             # [Embeddings storage - TBD]
    ├── brain-jepa/
    ├── brainlm-111m/
    ├── brainlm-650m/
    └── swift-v2/
```

---

## Related Documentation

### In neuro-ai-research-system
- `.claude/HYPOTHESIS_ENGINE_ACADEMIC_INTEGRATION.md` - How benchmarks integrate with hypothesis engine
- `.claude/SYSTEM_INTEGRATION_STATUS.md` - Overall system architecture

### In project directories
- `/Users/apple/Desktop/Brain-JEPA/EMBEDDING_EXTRACTION_GUIDE.md` - Brain-JEPA embedding extraction
- `/Users/apple/Desktop/BrainLM/brainlm_tutorial.ipynb` - BrainLM usage tutorial

---

## Key Papers to Reference

1. **Brain-JEPA**: Dong et al. (2024)
   - Citation: @article{BrainJEPA, title={Brain-JEPA: Brain Dynamics Foundation Model...}, journal={NeurIPS 2024}, year={2024}}

2. **BrainLM**: Vandijk Lab (2024)
   - Citation: @article{BrainLM, title={BrainLM: A Foundation Model for Brain Activity Recordings}, journal={OpenReview}, year={2024}}

3. **I-JEPA**: Assran et al. (2023)
   - Foundation for Brain-JEPA's architecture

4. **MAE**: He et al. (2021)
   - Foundation for BrainLM's architecture

---

## Contact and Resources

### Brain-JEPA
- GitHub: Official repository with code
- Paper: https://arxiv.org/abs/2409.19407
- Model Checkpoints: Google Drive link in README

### BrainLM
- GitHub: https://github.com/vandijklab/BrainLM
- Model Hub: https://huggingface.co/vandijklab/brainlm/
- Lab: Vandijk Lab (Yale University)

---

**Master Index Version**: 1.0
**Created**: October 23, 2025
**Status**: ✅ Complete - Ready for Benchmark Implementation
**Next Review**: After Phase 1 setup completion
