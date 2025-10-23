# Benchmark Models for SwiFT_v2 Evaluation

**Purpose**: Comprehensive framework for evaluating SwiFT_v2 against state-of-the-art brain foundation models
**Status**: ✅ Documentation Complete - Ready for Benchmark Implementation
**Created**: October 23, 2025

---

## Quick Navigation

### 📚 Documentation Files

| Document | Purpose | Audience |
|----------|---------|----------|
| **README.md** | This file - Overview and navigation | Everyone starting here |
| **BENCHMARKS_INDEX.md** | Master index with quick reference | Quick lookup and navigation |
| **BRAIN_JEPA_ANALYSIS.md** | Detailed Brain-JEPA technical analysis | Implementation and writing |
| **BRAINLM_ANALYSIS.md** | Detailed BrainLM technical analysis | Implementation and writing |
| **BENCHMARK_COMPARISON_FRAMEWORK.md** | Evaluation protocol and metrics | Researchers and analysts |
| **PROJECT_ORGANIZATION.md** | Project structure and workflow | Project managers and coordinators |
| **PHASE_1_DATA_PREPARATION.md** | Dataset preparation guide | Data engineers |

### 🎯 Find What You Need

```
I want to...

→ Understand what these benchmark models are?
  Start: BENCHMARKS_INDEX.md → QUICK REFERENCE

→ Set up the benchmark evaluation workflow?
  Start: PROJECT_ORGANIZATION.md → WORKFLOW INTEGRATION

→ Prepare datasets for evaluation?
  Start: PHASE_1_DATA_PREPARATION.md

→ Extract embeddings from Brain-JEPA?
  Start: BRAIN_JEPA_ANALYSIS.md (Section 7) → Brain-JEPA/EMBEDDING_EXTRACTION_GUIDE.md

→ Extract embeddings from BrainLM?
  Start: BRAINLM_ANALYSIS.md (Section 7) → BrainLM/brainlm_tutorial.ipynb

→ Implement the evaluation protocol?
  Start: BENCHMARK_COMPARISON_FRAMEWORK.md (Section 3 & 5)

→ Write the benchmark section for the paper?
  Start: BENCHMARK_COMPARISON_FRAMEWORK.md (Section 8)
```

---

## The Benchmark Models

### 🧠 Brain-JEPA
**Paper**: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking
**Venue**: NeurIPS 2024 (Spotlight)
**Architecture**: JEPA-based with brain gradient positional encoding
**Innovation**: Spatiotemporal masking + gradient-based positioning
**Key Stats**: 450 ROI parcellation, 768-1024 embedding dimension

**Quick Facts**:
- ✅ Non-contrastive learning (efficient, no collapse)
- ✅ Neuroscience-specific positional encoding
- ✅ Multi-scale temporal and spatial masking
- ⚠️ High computational cost (4x A100)
- ⚠️ Dataset-specific (UK Biobank pretraining)

**Best For**: Models prioritizing brain structure preservation and interpretability

### 🧬 BrainLM
**Paper**: A Foundation Model for Brain Activity Recordings
**Venue**: OpenReview
**Architecture**: MAE-based with scalable variants
**Innovation**: Masked autoencoder adapted for fMRI sequences
**Key Stats**: 111M and 650M parameter variants, flexible architecture

**Quick Facts**:
- ✅ Scalable variants (111M lightweight, 650M high-capacity)
- ✅ HuggingFace integration (easy loading)
- ✅ Multiple downstream task examples
- ✅ Tested on diverse datasets
- ⚠️ Flash Attention complexity for 650M
- ⚠️ Fine-tuned models not yet released

**Best For**: Models balancing performance and computational efficiency

### 🚀 SwiFT_v2
**Status**: Under Evaluation
**Role**: Candidate model to benchmark against state-of-the-art

---

## Evaluation Framework

### 📊 The Three Datasets

| Dataset | Type | Task | Size | Key Advantage |
|---------|------|------|------|---------------|
| **ADNI** | Clinical (Alzheimer's) | 3-way disease classification (NC/MCI/AD) | ~900 subjects | Primary comparison point - both benchmarks evaluated here |
| **HCP-Aging** | Healthy aging | Binary sex classification | ~1000 subjects | Out-of-distribution test - transfers to healthy population |
| **SwiFT_v2 Internal** | Custom | Task-specific | Variable | Internal validation on specialized data |

### 📈 The Evaluation Protocol

```
Phase 1: Setup & Data Preparation (1-2 days)
├─ Organize dataset directories
├─ Collect demographics and labels
├─ Create fixed train/val/test splits (seed=42)
└─ Validate data integrity

Phase 2: Brain-JEPA Evaluation (2-3 days)
├─ Extract embeddings (ADNI + HCP-Aging)
├─ Linear probing evaluation
├─ Fine-tuning evaluation
├─ Representation analysis
└─ Save all results

Phase 3: BrainLM Evaluation (2-3 days)
├─ Extract embeddings (111M and 650M variants)
├─ Run all downstream tasks
├─ Compute efficiency metrics
└─ Save all results

Phase 4: SwiFT_v2 Evaluation (1-2 days)
├─ Extract embeddings (same data/protocol)
├─ Run identical downstream tasks
├─ Compute comparison metrics
└─ Save results in standardized format

Phase 5: Analysis & Comparison (2-3 days)
├─ Compile comparison table
├─ Perform statistical significance testing
├─ Generate visualization plots
├─ Analyze computational efficiency
└─ Write comprehensive comparison report

Phase 6: Manuscript Integration (1-2 days)
├─ Create benchmark results section
├─ Generate publication-quality figures
├─ Write interpretation and discussion
└─ Prepare supplementary materials
```

### 🎯 Evaluation Tasks

**Task 1: Linear Probing** (Frozen Encoder)
- Train linear classifier on frozen embeddings
- Measures representation quality without fine-tuning
- Fast baseline for model comparison

**Task 2: Fine-tuning** (Full Network)
- Optimize full model on downstream task
- Measures transfer learning capability
- Shows potential with task-specific adaptation

**Task 3: KNN Baseline** (No Training)
- k-Nearest Neighbor classification on embeddings
- Pure representation quality metric
- No training required (BrainLM provides examples)

**Task 4: Efficiency Analysis**
- Model parameters and memory usage
- Inference time per subject
- Training time comparisons
- Power and resource requirements

### 📊 Comparison Metrics

**Performance Metrics**:
- Linear probing accuracy
- Fine-tuning accuracy
- AUC-ROC
- Sensitivity/Specificity
- Data efficiency curves

**Efficiency Metrics**:
- Model parameters
- Embedding dimensions
- Inference time (ms/subject)
- Peak GPU memory
- Pretraining time

**Representation Metrics**:
- Embedding correlation across models
- Wasserstein distance
- Nearest neighbor overlap
- Brain structure preservation
- Dimensionality (PCA)

---

## Directory Structure

```
.claude/benchmarks/
│
├── README.md                                    # This file
├── BENCHMARKS_INDEX.md                          # Master reference
├── BRAIN_JEPA_ANALYSIS.md                       # Brain-JEPA technical details
├── BRAINLM_ANALYSIS.md                          # BrainLM technical details
├── BENCHMARK_COMPARISON_FRAMEWORK.md            # Evaluation protocol
├── PROJECT_ORGANIZATION.md                      # Project structure & workflow
├── PHASE_1_DATA_PREPARATION.md                  # Dataset preparation guide
│
├── datasets/                                    # Benchmark evaluation datasets
│   ├── ADNI/                                   # Primary dataset (Alzheimer's)
│   │   ├── raw/                                # Original NIfTI files
│   │   ├── brain-jepa/                         # Brain-JEPA embeddings
│   │   ├── brainlm-111m/                       # BrainLM 111M embeddings
│   │   ├── brainlm-650m/                       # BrainLM 650M embeddings
│   │   ├── swift-v2/                           # SwiFT_v2 embeddings
│   │   ├── metadata/                           # Demographics and labels
│   │   └── downstream_results/                 # Evaluation results
│   │
│   └── HCP_Aging/                              # Secondary dataset (healthy aging)
│       ├── raw/                                # Original NIfTI files
│       ├── [same structure as ADNI]
│       └── ...
│
├── embeddings/                                  # Central embedding storage
│   ├── brain-jepa/                             # Brain-JEPA extracted embeddings
│   │   ├── adni/
│   │   └── hcp_aging/
│   ├── brainlm-111m/                           # BrainLM 111M embeddings
│   ├── brainlm-650m/                           # BrainLM 650M embeddings
│   └── swift-v2/                               # SwiFT_v2 embeddings
│
├── results/                                     # Benchmark comparison results
│   ├── adni_comparison.csv                     # ADNI results table
│   ├── hcp_aging_comparison.csv                # HCP-Aging results table
│   ├── efficiency_metrics.csv                  # Computational efficiency
│   ├── comparison_metrics.csv                  # Unified metrics table
│   ├── visualizations/                         # Publication-quality plots
│   │   ├── performance_comparison.png
│   │   ├── efficiency_tradeoff.png
│   │   ├── representation_analysis.png
│   │   └── correlation_matrices.png
│   └── statistical_tests/                      # Statistical analysis
│       ├── significance_tests.csv
│       └── effect_sizes.csv
│
└── metadata/                                    # Cross-dataset metadata
    ├── all_subjects.csv                        # Unified subject list
    └── preprocessing_log.txt                   # Data preparation documentation
```

---

## Getting Started

### 1️⃣ Understand the Benchmark Models (15 minutes)

Read in this order:
1. **BENCHMARKS_INDEX.md** - Quick reference cards
2. **BRAIN_JEPA_ANALYSIS.md** (Sections 1-3) - What is Brain-JEPA?
3. **BRAINLM_ANALYSIS.md** (Sections 1-3) - What is BrainLM?

### 2️⃣ Understand the Evaluation Approach (30 minutes)

1. **BENCHMARK_COMPARISON_FRAMEWORK.md** (Sections 1-3) - Overview and protocol
2. **PROJECT_ORGANIZATION.md** (Sections 1-2) - Project structure
3. **BENCHMARKS_INDEX.md** (Evaluation Datasets, Key Metrics) - Quick reference

### 3️⃣ Prepare Datasets (1-2 days)

1. **PHASE_1_DATA_PREPARATION.md** - Detailed implementation guide
2. Organize ADNI dataset (raw NIfTI files)
3. Organize HCP-Aging dataset
4. Create metadata (demographics, labels, splits)
5. Validate data integrity

### 4️⃣ Extract Embeddings (4-6 days)

**Brain-JEPA**:
1. Read **BRAIN_JEPA_ANALYSIS.md** (Section 7 & 8)
2. Review `/Users/apple/Desktop/Brain-JEPA/EMBEDDING_EXTRACTION_GUIDE.md`
3. Run embedding extraction on both datasets
4. Store in `.claude/benchmarks/embeddings/brain-jepa/`

**BrainLM**:
1. Read **BRAINLM_ANALYSIS.md** (Section 8)
2. Review `/Users/apple/Desktop/BrainLM/brainlm_tutorial.ipynb`
3. Extract embeddings (111M and 650M variants)
4. Store in `.claude/benchmarks/embeddings/brainlm-*/`

### 5️⃣ Evaluate & Compare (2-3 days)

1. **BENCHMARK_COMPARISON_FRAMEWORK.md** (Section 5 & 6) - Evaluation protocol
2. Run downstream tasks (linear probing, fine-tuning, KNN)
3. Compute all comparison metrics
4. Generate comparison tables and plots

### 6️⃣ Write Manuscript Section (1-2 days)

1. **BENCHMARK_COMPARISON_FRAMEWORK.md** (Section 8) - Manuscript structure
2. Compile results into paper-quality tables and figures
3. Write interpretation and discussion
4. Integrate into SwiFT_v2 manuscript

---

## External Project References

### Brain-JEPA
- **Location**: `/Users/apple/Desktop/Brain-JEPA`
- **Key Guide**: `EMBEDDING_EXTRACTION_GUIDE.md` (detailed extraction protocol)
- **Main Script**: `downstream_embedding_extraction.py`
- **Status**: Modified for external dataset embedding extraction

### BrainLM
- **Location**: `/Users/apple/Desktop/BrainLM`
- **Key Tutorial**: `brainlm_tutorial.ipynb` (data preprocessing and usage)
- **Inference Examples**: `inference_*.ipynb` (downstream task notebooks)
- **Model Hub**: https://huggingface.co/vandijklab/brainlm/
- **Status**: Modified for embedding extraction

---

## Implementation Checklist

### Phase 1: Setup (1-2 days)
- [ ] Read PHASE_1_DATA_PREPARATION.md
- [ ] Create dataset directory structure
- [ ] Download/access ADNI raw fMRI data
- [ ] Download/access HCP-Aging raw fMRI data
- [ ] Collect demographics and clinical labels
- [ ] Create train/val/test splits (seed=42)
- [ ] Validate all data
- [ ] Document preprocessing applied

### Phase 2: Brain-JEPA (2-3 days)
- [ ] Review Brain-JEPA analysis and extraction guide
- [ ] Verify pretrained checkpoint available
- [ ] Extract embeddings on ADNI
- [ ] Extract embeddings on HCP-Aging
- [ ] Run linear probing evaluation
- [ ] Run fine-tuning evaluation
- [ ] Compute representation metrics
- [ ] Save all results to results/

### Phase 3: BrainLM (2-3 days)
- [ ] Review BrainLM analysis and tutorials
- [ ] Load BrainLM 111M from HuggingFace
- [ ] Load BrainLM 650M from HuggingFace
- [ ] Extract embeddings (111M variant)
- [ ] Extract embeddings (650M variant)
- [ ] Run all downstream tasks
- [ ] Compute efficiency metrics
- [ ] Save all results

### Phase 4: SwiFT_v2 (1-2 days)
- [ ] Extract embeddings (same data/protocol)
- [ ] Run identical downstream tasks
- [ ] Compute all metrics
- [ ] Save results in standardized format

### Phase 5: Analysis (2-3 days)
- [ ] Compile comparison metrics table
- [ ] Perform statistical significance testing
- [ ] Generate visualization plots
- [ ] Compute efficiency tradeoffs
- [ ] Analyze representation quality
- [ ] Write comprehensive report

### Phase 6: Manuscript (1-2 days)
- [ ] Write benchmark results section
- [ ] Create publication-quality figures
- [ ] Write interpretation and discussion
- [ ] Prepare supplementary materials
- [ ] Format citations and references

---

## Key Documents by Purpose

### For Quick Reference
- **BENCHMARKS_INDEX.md** - Quick lookup cards, model overview, code locations
- **README.md** (this file) - Navigation and getting started

### For Implementation
- **BRAIN_JEPA_ANALYSIS.md** - Technical details on architecture, training, code
- **BRAINLM_ANALYSIS.md** - Technical details on architecture, variants, usage
- **PHASE_1_DATA_PREPARATION.md** - Step-by-step dataset preparation

### For Project Management
- **PROJECT_ORGANIZATION.md** - Workflow structure, timeline, success criteria
- **BENCHMARK_COMPARISON_FRAMEWORK.md** - Evaluation protocol and metrics

### For Manuscript Writing
- **BENCHMARK_COMPARISON_FRAMEWORK.md** (Section 8) - Expected paper structure
- **Results CSVs** - Comparison metrics for tables and figures

---

## Common Questions

### Q: Where do I start?
**A**: Read BENCHMARKS_INDEX.md for quick overview, then follow "Getting Started" section above.

### Q: How long will the full evaluation take?
**A**: 9-15 days total:
- Phase 1 (Setup): 1-2 days
- Phase 2 (Brain-JEPA): 2-3 days
- Phase 3 (BrainLM): 2-3 days
- Phase 4 (SwiFT_v2): 1-2 days
- Phase 5 (Analysis): 2-3 days
- Phase 6 (Manuscript): 1-2 days

### Q: Can phases run in parallel?
**A**: Yes! Phase 2 (Brain-JEPA) and Phase 3 (BrainLM) can run simultaneously if you have multiple GPUs.

### Q: Where are the pretrained models?
**A**:
- Brain-JEPA: See EMBEDDING_EXTRACTION_GUIDE.md for checkpoint download
- BrainLM: HuggingFace Hub (vandijklab/brainlm-111m and vandijklab/brainlm-650m)

### Q: What's the random seed for reproducibility?
**A**: Seed=42 is used for all train/val/test splits. Documented in PHASE_1_DATA_PREPARATION.md

### Q: How should I organize results for the paper?
**A**: See BENCHMARK_COMPARISON_FRAMEWORK.md (Section 8) for expected manuscript structure and output format.

---

## Citation

When using these benchmark models in your paper, cite:

```bibtex
@article{BrainJEPA,
  title={Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking},
  author={Dong et al.},
  journal={NeurIPS 2024},
  year={2024}
}

@article{BrainLM,
  title={BrainLM: A Foundation Model for Brain Activity Recordings},
  journal={OpenReview},
  year={2024},
  note={Vandijk Lab}
}
```

---

## Status & Timeline

✅ **Documentation Complete** - All analysis and planning documents created
⏳ **Phase 1 Ready** - Dataset preparation guide complete, ready for implementation
🚀 **Estimated Full Evaluation**: 9-15 days from Phase 1 start

---

**Last Updated**: October 23, 2025
**Document Version**: 1.0
**Status**: Ready for Benchmark Implementation
**Next Step**: Start Phase 1 - Prepare benchmark datasets
