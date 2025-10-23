# Brain-JEPA: Analysis and Benchmark Documentation

**Paper**: Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking
**Venue**: NeurIPS 2024 (Spotlight)
**ArXiv**: https://arxiv.org/abs/2409.19407
**Citation**: Dong et al., 2024

---

## Executive Summary

Brain-JEPA is a state-of-the-art foundation model for brain dynamics that uses self-supervised learning via Joint-Embedding Predictive Architecture (JEPA). The model introduces novel techniques for positional encoding (brain gradient positioning) and masking (spatiotemporal masking) specifically designed for fMRI data structure.

---

## 1. Core Technical Contributions

### 1.1 Brain Gradient Positioning
- **Innovation**: Uses cortical/subcortical gradient information for ROI positional encoding
- **Method**: Brain gradient derived from UKB population-level data using Brainspace toolbox
- **Encoding**: Combines gradient-based spatial positioning with sine/cosine temporal functions
- **Advantage**: Incorporates neuroscientific knowledge of brain organization into positional encoding

### 1.2 Spatiotemporal Masking
- **Architecture**: Single observation block predicts target block representations
- **Masking Regions**:
  - **Cross-ROI**: Different ROIs, same time
  - **Cross-Time**: Same ROI, different times
  - **Double-Cross**: Different ROIs AND different times
- **Advantage**: Captures multi-scale dependencies in brain dynamics

### 1.3 JEPA Architecture
- **Backbone**: Based on I-JEPA (Facebook Research)
- **Key Components**:
  - Online network (updated by gradient descent)
  - Target network (exponential moving average)
  - Predictor module
- **Advantage**: Non-contrastive approach avoiding collapse, more efficient than contrastive methods

---

## 2. Data and Datasets

### 2.1 fMRI Data Specification
- **Parcellation**: 450 ROIs total
  - 400 cortical ROIs (Schaefer atlas)
  - 50 subcortical ROIs (Tian Scale III atlas)
- **Data Format**: Time series data extracted from NIfTI images
- **Preprocessing**: Follows standard fMRI pipelines (FSL-based)

### 2.2 Datasets Used

#### Pretraining
- **UKB (UK Biobank)**
  - Large population cohort
  - Source of population-level brain gradients
  - Direct download from Mansour et al. preprocessing

#### Evaluation
- **HCP-Aging (Human Connectome Project - Aging)**
  - Preprocessing: Wu et al. pipeline
  - Sex classification downstream task

- **ADNI (Alzheimer's Disease Neuroimaging Initiative)**
  - Preprocessing: Kong et al. pipeline
  - Disease classification (NC/MCI) downstream task

- **MACC (Memory, Ageing and Cognition Centre)**
  - In-house dataset
  - Clinical classification tasks

---

## 3. Model Architecture

### 3.1 Vision Transformer Backbone
- **Architecture**: ViT-Base variant adapted for fMRI
- **Input**: Tokenized fMRI patches
  - Patch size: 16 timepoints
  - ROI groups: Varies (typically 450 ROIs → multiple patches)
- **Output**:
  - Feature dimension: 768-1024 (depends on variant)
  - CLS token: Global representation
  - Patch tokens: Spatial-temporal local representations

### 3.2 Predictor Network
- **Type**: Deep transformer
- **Depth**: 12 layers
- **Embedding dimension**: 384
- **Attention**: Normal/masked attention modes
- **Purpose**: Predicts target representations from observation block

### 3.3 Training Components
- **Online Encoder**: Updated via gradient descent
- **Target Encoder**: EMA update (exponential moving average)
- **Predictor**: Transforms online representations
- **Loss**: L2 loss between predicted and target representations

---

## 4. Training Methodology

### 4.1 Self-Supervised Objective
- **Task**: Predict masked target block from observation block
- **Loss**: L2 distance between predictor output and target encoder representation
- **Advantage**: Non-contrastive, avoids representational collapse

### 4.2 Training Setup
- **Pretraining Hardware**: 4x A100 (40GB) GPUs
- **Optimization**: Standard gradient descent with momentum
- **Data Processing**:
  - Batch-level sampling of observation/target blocks
  - Random masking following spatiotemporal patterns
  - Normalization using training set statistics

### 4.3 Temporal and Spatial Sampling
- **Temporal**: Sine/cosine positional encoding for time dimension
- **Spatial**: Gradient-based positional encoding for ROI locations
- **Masking**: Structured to learn multi-scale dependencies

---

## 5. Downstream Evaluation

### 5.1 Linear Probing
- **Approach**: Freeze pretrained encoder, train linear classifier
- **Tasks**:
  - Sex classification (HCP-Aging)
  - Disease classification (ADNI: NC vs MCI)
- **Metrics**: Accuracy, AUC, ROC curves

### 5.2 Fine-tuning
- **Approach**: Full network optimization on downstream task
- **Adaptation**: Task-specific heads with appropriate loss functions
- **Typical Performance**: 5-15% improvement over linear probing

### 5.3 Representation Analysis
- **Quality**: Evaluated through downstream task performance
- **Interpretability**: Brain spatial organization preserved in embeddings
- **Efficiency**: Enables efficient transfer learning

---

## 6. Code Structure and Implementation

### 6.1 Directory Organization
```
Brain-JEPA/
├── configs/              # YAML config files for experiments
├── src/
│   ├── models/          # Model definitions (ViT, predictor)
│   ├── datasets/        # Data loaders and dataset classes
│   ├── masks/           # Masking utilities and collators
│   ├── utils/           # Helper functions
│   └── train.py         # Pretraining script
├── downstream_tasks/    # Downstream task implementations
│   ├── main_finetune.py
│   ├── main_linearprobe.py
│   └── models_vit.py
├── downstream_embedding_extraction.py  # Custom script for embedding extraction
├── main.py              # Entry point for pretraining
└── scripts/             # Shell scripts for running tasks
```

### 6.2 Key Files for Embedding Extraction
- **`downstream_embedding_extraction.py`**: Main entry point
  - Loads pretrained checkpoints
  - Processes external datasets
  - Extracts embeddings at global pooling layer
  - Saves per-subject embeddings as `.pt` files

- **`src/datasets/external_dataset_parcellation.py`**:
  - Converts NIfTI to parcellated CSV format
  - Applies Schaefer and Tian atlases
  - Handles multiple datasets (ADNI, EMBARC, YooAttn, ToPS)

- **`downstream_tasks/engine_embedding_extraction.py`**:
  - Core extraction logic
  - Batch processing with GPU support
  - Subject-specific output saving

### 6.3 Configuration Parameters
- **Model**: `vit_base` (Vision Transformer Base)
- **Crop size**: 450 ROIs × 160 timepoints (after downsampling)
- **Patch size**: 16 timepoints
- **Embedding dim**: 768-1024
- **Batch size**: 4 (adjustable based on GPU memory)

---

## 7. Embedding Extraction for SwiFT_v2

### 7.1 Extraction Pipeline
1. **Data Preparation**: Parcellate raw fMRI to CSV format
2. **Model Loading**: Load pretrained Brain-JEPA checkpoint
3. **Processing**:
   - Tokenize into patches
   - Forward through ViT encoder
   - Extract representations at global pooling
4. **Output**: Per-subject embeddings (n_frames × embedding_dim)

### 7.2 Output Specifications
- **Format**: PyTorch tensor (.pt file)
- **Shape**: (n_frames, embedding_dim)
  - n_frames: Number of timepoints in fMRI sequence
  - embedding_dim: 768-1024 depending on model variant
- **Location**: Subject-specific directories under `embeddings/`

### 7.3 Preprocessing Applied
- **Temporal downsampling**: 490 → 160 frames
- **Normalization**: Robust scaling using training set statistics
- **Standardization**: Applied per-dataset (maintains dataset-specific characteristics)

---

## 8. Strengths for Benchmark Comparison

### 8.1 Technical Strengths
1. **Novel Positional Encoding**: Incorporates neuroscientific priors (brain gradients)
2. **Multi-scale Masking**: Captures both local and global dependencies
3. **Non-contrastive Learning**: Avoids representational collapse, more efficient
4. **Large-scale Pretraining**: Foundation model trained on UKB population

### 8.2 Practical Strengths
1. **Embedding Extraction**: Clean interface for getting representations
2. **External Dataset Support**: Can process multiple datasets (ADNI, EMBARC, etc.)
3. **Code Availability**: Official PyTorch implementation
4. **Flexibility**: Adjustable model size and computational requirements

### 8.3 Evaluation Strengths
1. **Multiple Datasets**: Evaluated on HCP-Aging, ADNI, MACC
2. **Multiple Tasks**: Classification, prediction, representation quality
3. **Clinical Relevance**: Disease classification (Alzheimer's) tasks included
4. **Downstream Performance**: Strong results on downstream tasks

---

## 9. Limitations and Considerations

### 9.1 Technical Limitations
1. **Data-specific Training**: Pretrained on UKB; may need adaptation for other populations
2. **Resolution Trade-off**: Downsampling from 490 to 160 frames (temporal compression)
3. **Computational Cost**: Requires 4x A100 GPUs for pretraining
4. **Atlas Dependency**: Fixed to Schaefer (400) + Tian (50) ROI atlas

### 9.2 Practical Considerations
1. **Preprocessing Requirements**: Specific fMRI preprocessing pipeline needed
2. **Dataset Format**: Requires CSV format after parcellation
3. **Batch Size Constraints**: May need reduction for smaller GPU memory
4. **Checkpoint Availability**: Depends on authors' checkpoint release

---

## 10. Relevance for SwiFT_v2 Evaluation

### 10.1 Why Brain-JEPA as Benchmark?
1. **State-of-the-art Foundation Model**: NeurIPS 2024 Spotlight paper
2. **Brain-specific Innovations**: Gradient positioning designed for brain structure
3. **Multi-scale Representations**: Spatiotemporal masking captures hierarchy
4. **Production-ready Code**: Well-documented embedding extraction pipeline

### 10.2 Comparison Potential
- **Representation Quality**: Compare SwiFT_v2 embeddings with Brain-JEPA
- **Downstream Performance**: Evaluate both on same downstream tasks
- **Efficiency**: Compare embedding dimension vs. performance trade-offs
- **Interpretability**: Analyze preserved brain structure in embeddings

### 10.3 Integration with SwiFT_v2
- **Feature Extraction**: Use Brain-JEPA embeddings as input features
- **Ensemble Approaches**: Combine Brain-JEPA and SwiFT_v2 representations
- **Transfer Learning**: Fine-tune SwiFT_v2 on Brain-JEPA embeddings
- **Comparative Analysis**: Detailed benchmark comparison section in paper

---

## 11. References and Related Work

### 11.1 Foundation Papers
- **I-JEPA** (Assran et al., 2023): Joint-Embedding Predictive Architecture
- **MAE** (He et al., 2021): Masked Autoencoders in Vision Transformers
- **ViT** (Dosovitskiy et al., 2020): Vision Transformers for image classification

### 11.2 Brain Gradient Literature
- **Brainspace** (Vos de Wael et al., 2020): Brain gradient computation toolbox
- **Margulies et al., 2016**: Original brain gradients concept for connectivity

### 11.3 fMRI Foundation Models
- **BrainLM** (2024): Parallel foundation model for brain dynamics
- **Other Vision Transformer adaptations**: CoAtNet, Swin Transformer variants

---

## 12. Citation

```bibtex
@article{BrainJEPA,
  title={Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking},
  author={Zijian Dong and Ruilin Li and Yilei Wu and Thuan Tinh Nguyen and Joanna Su Xian Chong and Fang Ji and Nathanael Ren Jie Tong and Christopher Li Hsian Chen and Juan Helen Zhou},
  journal={NeurIPS 2024},
  year={2024}
}
```

---

**Document Version**: 1.0
**Last Updated**: October 23, 2025
**Status**: Analysis Complete - Ready for SwiFT_v2 Benchmark Comparison
