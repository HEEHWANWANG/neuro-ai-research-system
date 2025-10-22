# SwiFT v2 Project Familiarization Report

**Date**: October 22, 2025
**Project**: SwiFT_v2_perlmutter
**Status**: Ready for AI+Neuroscience Research Development

---

## Executive Summary

SwiFT v2 is an advanced transformer-based architecture for analyzing 4D fMRI (functional magnetic resonance imaging) data. It represents an evolution of the original SwiFT paper (arxiv.org/pdf/2307.05916) and implements:

- **Shifted-window Swin Transformer architecture** adapted for 4D fMRI data (spatial + temporal)
- **SimMIM pretraining** with masked image modeling for self-supervised learning
- **Multi-dataset training** across UKB, ABCD, HCP, and other large-scale neuroimaging datasets
- **Scalable distributed training** on NERSC Perlmutter supercomputer
- **Comprehensive downstream evaluation** on classification and regression tasks

---

## Project Architecture Overview

### 🏗️ Directory Structure

```
SwiFT_v2_perlmutter/
├── project/
│   ├── module/
│   │   ├── models/              # Neural network architectures
│   │   │   ├── swin4d_transformer_ver11.py    # Latest Swin4D
│   │   │   ├── simmim_swin4d_transformer_ver11.py  # SimMIM variant
│   │   │   └── [other model variants v7-v9]
│   │   ├── utils/               # Data, metrics, losses
│   │   │   ├── data_module.py   # Data loading
│   │   │   ├── metrics.py       # Evaluation metrics
│   │   │   └── losses.py        # Custom loss functions
│   │   ├── pl_classifier.py     # PyTorch Lightning module
│   │   └── main_embedding_extraction.py  # Feature extraction
│   ├── main.py                  # Main training entry point
│   └── debug.py                 # Debugging utilities
├── downstream_optuna/           # Downstream task optimization
│   ├── main.py                  # Downstream training script
│   ├── trainer.py               # Training loop
│   ├── dataloaders.py           # Data loading
│   ├── models.py                # Classification heads
│   └── bash_scripts/            # Task-specific scripts
├── sample_scripts/              # Example training scripts
│   ├── pretraining/             # Pretraining examples
│   ├── downstream/              # Downstream task examples
│   └── scalability/             # Scale testing
├── data/splits/                 # Data splits
│   ├── UKB_v1-v6/
│   ├── ABCD/
│   ├── S1200/
│   └── [other datasets]
└── notebooks/                   # Jupyter notebooks
```

### 🧠 Core Concepts

#### 1. **Swin4D Transformer Architecture**
- Extends 2D Swin Transformer to 4D (spatial: D×H×W, temporal: T)
- Uses shifted-window attention for efficiency
- Patch embedding reduces 4D volumes to sequence of tokens
- Hierarchical architecture with multiple stages

**Key files**:
- `project/module/models/swin4d_transformer_ver11.py` - Main architecture
- `project/module/models/patchembedding.py` - Patch embedding layer

#### 2. **SimMIM Pretraining**
- Self-supervised learning using masked image modeling
- Masks random patches of input and predicts them
- Enables learning from unlabeled data
- Better generalization to downstream tasks

**Key file**: `project/module/models/simmim_swin4d_transformer_ver11.py`

#### 3. **Data Pipeline**
- Multi-dataset integration (UKB, ABCD, HCP, ABIDE, EMBARC)
- Custom PyTorch Lightning DataModule
- Handles 4D fMRI volumes with temporal sequences
- Data preprocessing and normalization

**Key files**:
- `project/module/utils/data_module.py` - Data module
- `project/module/utils/data_preprocess_and_load/` - Preprocessing

#### 4. **Training Framework**
- PyTorch Lightning for clean, modular training
- Distributed training via DDP (DistributedDataParallel)
- DeepSpeed integration for large-scale training
- Neptune logging for experiment tracking

**Key file**: `project/module/pl_classifier.py` - LitClassifier module

---

## Training Pipeline

### Phase 1: Pretraining (Self-Supervised)
```
Unlabeled fMRI data → SimMIM masking → Swin4D encoder
↓
Predict masked patches → Pretraining loss → Pretrained weights
```

**What happens**:
1. Load large unlabeled datasets (UKB, ABCD)
2. Randomly mask patches (configurable ratio: 0.2, 0.4, 0.6, 0.8)
3. Train model to predict masked patches
4. Learn general fMRI representations
5. Save pretrained weights for downstream tasks

**Scripts**: `sample_scripts/pretraining/masking*/`

### Phase 2: Downstream Task Fine-tuning
```
Pretrained model + Labeled fMRI → Classification/Regression head
↓
Task labels (sex, age, disease) → Fine-tuning loss → Task-specific model
```

**Supported tasks**:
- **Classification**: Sex, ASD (autism), Depression
- **Regression**: Age, Intelligence, Pain levels
- **Behavioral**: Cognitive performance (MOT, VSTM, gradCPT)

**Scripts**:
- `downstream_optuna/main.py` - General fine-tuning
- `sample_scripts/downstream/` - Task-specific examples
- `downstream_optuna/bash_scripts/` - Optimized runs

### Phase 3: Evaluation
- Metrics: Accuracy, AUC, R² score, Pearson correlation
- Validation on held-out test sets
- Performance analysis across model scales

**Key file**: `project/module/utils/metrics.py`

---

## Model Variants & Scaling

The project explores multiple model sizes:

| Model | Parameters | Use Case |
|-------|-----------|----------|
| 5M | ~5 Million | Quick prototyping |
| 51M | ~51 Million | Mid-scale experiments |
| 202M | ~202 Million | Standard scale |
| 806M | ~806 Million | Large-scale |
| 837M_new | ~837 Million | Latest variant |
| 3.2B | ~3.2 Billion | Ultra-large scale |

**Observation**: Clear scaling trends tested systematically

---

## Key Training Features

### 1. **Distributed Training**
```bash
# Multi-GPU/Multi-node training
accelerate launch project/main.py \
  --num_nodes 4 \
  --devices 8 \
  --strategy deepspeed
```

### 2. **Hyperparameter Tuning**
- Optuna-based automated hyperparameter search
- Separate downstream optimization loop
- Task and dataset-specific configurations

**Entry point**: `downstream_optuna/main.py`

### 3. **Checkpoint Management**
- Regular checkpoint saving
- Resume from checkpoints
- Support for DeepSpeed checkpoints
- Save best model based on validation metrics

### 4. **Experiment Tracking**
- Neptune logger integration for cloud logging
- TensorBoard for local monitoring
- Custom metrics logging

### 5. **Data Augmentation**
- Spatial: Rotation, elastic deformation
- Temporal: Gaussian noise on temporal dimension
- Configurable augmentation strategies

---

## Datasets Overview

### UKB (UK Biobank)
- **Size**: ~45,000 subjects
- **Tasks**: Intelligence, sex, age prediction
- **Versions**: UKB_v1 through UKB_v6 (different preprocessing)
- **Type**: Population-based neuroimaging

### ABCD (Adolescent Brain Cognitive Development)
- **Size**: ~10,000+ participants
- **Tasks**: Depression, intelligence, sex
- **Type**: Longitudinal child development study

### HCP (Human Connectome Project)
- **Size**: ~1,200 subjects
- **Tasks**: Age prediction
- **Code**: S1200 release

### ABIDE (Autism Brain Imaging Data Exchange)
- **Size**: ~1,100+ subjects
- **Tasks**: ASD classification, sex prediction
- **Type**: Clinical neuroimaging (autism)

### EMBARC (Early Mood Treatment)
- **Size**: ~300+ subjects
- **Tasks**: Depression prediction
- **Type**: Clinical (depression)

### BrainLM Dataset
- **Tasks**: Cognitive/behavioral tests
- **Subtasks**: VSTM, gradCPT, MOT, pain (ToPS)

---

## Important Implementation Details

### 1. **Patch Embedding Strategy**
- Temporal patches: Stacking fMRI volumes over time
- Spatial patches: 3D volumetric patches
- Combined 4D tokenization for efficiency

**File**: `project/module/models/patchembedding.py`

### 2. **Attention Mechanism**
- Shifted-window attention (like vision transformers)
- 4D patch layout with efficient windowing
- Reduces complexity from O(N²) to O(N log N)

### 3. **Pretraining Strategies**
- **SimMIM**: Masked image modeling
- **Masking types**: Random masking, structured masking
- **Mask ratios**: 0.2, 0.4, 0.6, 0.8 for ablation

### 4. **Loss Functions**
- **Pretraining**: MSE loss for reconstruction
- **Classification**: Cross-entropy
- **Regression**: MSE loss
- **Custom metrics**: R² score, Pearson correlation

**File**: `project/module/utils/losses.py`

### 5. **Learning Rate Scheduling**
- Cosine annealing decay
- Warm-up period for stability
- Custom schedulers in `project/module/utils/lr_scheduler.py`

---

## Running the Code

### Quick Start (Pretraining)
```bash
cd /Users/apple/Desktop/SwiFT_v2_perlmutter

# Interactive run (small scale test)
bash sample_scripts/v2_simmim_multiDS_script_perlmutter_interactive.sh

# Full pretraining
bash sample_scripts/v2_simmim_multiDS_script_perlmutter.sh
```

### Downstream Task (Fine-tuning)
```bash
# Sex classification on UKB with 100 samples
bash sample_scripts/downstream/UKB/sex/sub100_unfreeze_0.2.sh

# Age regression
bash sample_scripts/downstream/UKB/age/sub100_unfreeze_0.2.sh

# With Optuna optimization
cd downstream_optuna
python main.py --dataset_name ABCD --downstream_task depression ...
```

### Extract Embeddings (Feature Extraction)
```bash
python project/main_embedding_extraction.py \
  --load_model_path /path/to/pretrained.pth \
  --output_path embeddings/
```

---

## Key Concepts for Development

### 1. **4D Tensor Operations**
- fMRI data: (Subjects, Time, Depth, Height, Width)
- Patch embedding: (Subjects, Time, #Patches) → tokens
- Attention: Window-based for efficiency
- Importance: Understanding 4D transformations for modifications

### 2. **Distributed Training Complexities**
- Gradient synchronization across GPUs
- DeepSpeed stage 2 (gradient partitioning)
- Checkpoint compatibility between DDP and DeepSpeed
- Data loading in distributed context

### 3. **Multi-Dataset Training**
- Mixing datasets with different characteristics
- Balancing dataset sizes
- Preventing dataset-specific overfitting

### 4. **Downstream Task Variability**
- Different task types (classification vs regression)
- Different label distributions
- Few-shot learning capability (small sample sets)
- Transfer learning efficiency

---

## Project Status & Next Steps

### ✅ Current Capabilities
- Full pretraining pipeline on Perlmutter
- Multiple downstream task implementations
- Comprehensive evaluation framework
- Scalable from 5M to 3.2B parameters
- Multi-dataset support

### 🚀 Potential Research Directions
1. **Architecture improvements**: Better temporal modeling, adaptive masking
2. **Pretraining objectives**: Contrastive learning, multi-task pretraining
3. **Downstream applications**: More clinical tasks, interpretability
4. **Efficiency**: Knowledge distillation, quantization, pruning
5. **Theoretical understanding**: Why 4D transformers work for fMRI

### 📊 Development Opportunities
- Visualization tools for embeddings
- Explainability methods for clinical predictions
- Cross-dataset generalization studies
- Few-shot learning protocols
- Domain adaptation techniques

---

## Tools & Dependencies

- **PyTorch**: Deep learning framework
- **PyTorch Lightning**: Training framework
- **DeepSpeed**: Distributed training optimization
- **MONAI**: Medical imaging tools (DropPath, trunc_normal_)
- **Optuna**: Hyperparameter optimization
- **Neptune**: Experiment tracking
- **TensorBoard**: Visualization
- **SLURM**: Job scheduling (Perlmutter)

---

## Important Notes for Development

1. **NERSC Perlmutter Specifics**
   - Uses DDP + DeepSpeed for large-scale training
   - GPU: NVIDIA A100s (80GB memory)
   - Environment setup via export_DDP_vars.sh

2. **Data Access**
   - Large-scale datasets (hundreds of GB to TB)
   - May require special access permissions
   - Efficient data loading critical for training speed

3. **Reproducibility**
   - Seed control in main.py (--seed argument)
   - Data splits stored in data/splits/
   - Fixed random seeds for deterministic results

4. **Checkpoint Management**
   - Regular saves during training
   - Best model selection based on validation metrics
   - Resume capability for long-running experiments

---

## Summary for AI+Neuroscience Integration

**SwiFT v2 is a production-ready pipeline for**:
1. Large-scale fMRI pretraining (self-supervised)
2. Downstream clinical/behavioral prediction
3. Scalable neuroimaging AI research
4. Multi-task and multi-dataset learning

**Perfect for research questions**:
- How do architectural choices affect neuroimaging model performance?
- What's the scaling behavior of transformers on fMRI?
- Can pretrained models improve clinical prediction?
- How to efficiently leverage unlabeled neuroimaging data?

The codebase is well-organized, extensively tested, and ready for methodological innovations in AI+neuroscience intersection.

---

**Status**: ✅ Project familiarization complete. Ready for supervised implementation of research hypotheses.
