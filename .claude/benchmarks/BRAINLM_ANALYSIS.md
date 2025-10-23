# BrainLM: Analysis and Benchmark Documentation

**Paper**: BrainLM: A Foundation Model for Brain Activity Recordings
**Venue**: OpenReview (Under Review / ICLR/NeurIPS Track)
**Authors**: From Vandijk Lab
**Model Hub**: https://huggingface.co/vandijklab/brainlm/

---

## Executive Summary

BrainLM is a foundation model for brain dynamics that applies masked autoencoder (MAE) principles to fMRI data. The model demonstrates transfer learning across different brain datasets and provides both 111M and 650M parameter variants. BrainLM represents a scalable approach to learning general representations of brain dynamics through self-supervised masked prediction.

---

## 1. Core Technical Contributions

### 1.1 Foundation Model Architecture
- **Base**: Masked Autoencoder (MAE) applied to fMRI
- **Approach**: Masked prediction of hidden patches from visible patches
- **Innovation**: Adaptation of MAE (He et al., 2021) to sequential brain activity data
- **Advantage**: Simple, scalable, interpretable self-supervised learning

### 1.2 Transfer Learning Capabilities
- **Pretraining**: UK Biobank (population-level fMRI data)
- **Transfer**: Demonstrated transfer to multiple downstream datasets
  - Disease datasets (ADNI, clinical populations)
  - Task-based fMRI (attention, decision-making)
  - Different acquisition parameters
- **Advantage**: Learns generalizable brain dynamics representations

### 1.3 Model Scale Options
- **111M Parameters**: Lightweight, suitable for limited compute
- **650M Parameters**: Full-scale, higher representation capacity
- **Flash Attention**: Required for efficient 650M model inference
- **Advantage**: Flexibility for different computational budgets

---

## 2. Data and Datasets

### 2.1 Brain Activity Modality
- **Type**: Resting-state fMRI
- **Processing**: Time series extraction, temporal alignment
- **Format**: Handled through preprocessing pipeline
- **Key Datasets**:
  - UK Biobank (pretraining)
  - ADNI (Alzheimer's Disease)
  - EMBARC (Depression/Antidepressant response)
  - YooAttn (Attention network)
  - ToPS (Obsessive-Compulsive Scale)

### 2.2 Data Preprocessing
- **Pipeline**: Custom preprocessing scripts provided
- **Tools**: Includes conversion and transformation utilities
- **Format**: Converts to standard tensor format for model input
- **Details**:
  - Scripts: `data_preprocessing.py`, dataset-specific movers
  - Tutorial: `brainlm_tutorial.ipynb` for preprocessing walkthrough
  - Note: Some datasets may need matrix transposition adjustments

### 2.3 Data Format Specifications
- **Input**: Standardized fMRI time series
- **Temporal dimension**: Preserved from original data
- **Spatial**: Channel/ROI representation (varies by dataset)
- **Note**: Flexible to different atlas definitions and data layouts

---

## 3. Model Architecture

### 3.1 Vision Transformer Adaptation
- **Base**: Vision Transformer (ViT) adapted for sequential data
- **Architecture**: Transformer encoder for temporal/spatial modeling
- **Key Components**:
  - Embedding layer: Token projection
  - Transformer blocks: Self-attention over time/space
  - Configuration: Variable depth and width (see config files)

### 3.2 Masked Autoencoder (MAE) Framework
- **Masking Strategy**: Random masking of input patches
- **Encoder**: Processes visible tokens only (efficient)
- **Decoder**: Reconstructs from encoder output + masked tokens
- **Loss**: L2 reconstruction loss on masked regions
- **Advantage**: Computationally efficient (doesn't process masked tokens)

### 3.3 Model Configuration Files
- **Main Config**: `configuration_brainlm.py`
  - Model hyperparameters
  - Architecture specifications
  - Training parameters
- **ViT Config**: `vit_image_finetune_config.py`
  - Depth, width, attention heads
  - Embedding dimensions
  - MLP dimensions

### 3.4 Finetuning Variants
- **Base**: `vit_image_finetune_config.py`
- **MLP Head**: `vit_image_finetuning_mlp_pred_head.py`
  - Multi-layer perceptron prediction head
  - Task-specific adaptation
- **Purpose**: Enables different downstream configurations

---

## 4. Training Methodology

### 4.1 Self-Supervised Objective
- **Task**: Masked prediction (MAE-style)
- **Masking Ratio**: Random masking of patches
- **Loss**: L2 reconstruction error on masked patches
- **Advantage**: Learns implicit structure of brain dynamics

### 4.2 Pretraining Setup
- **Dataset**: UK Biobank (large population cohort)
- **Scale**: Population-level representation learning
- **Duration**: Multiple epochs until convergence
- **Hardware**: Note in README mentions Yale HPC setup

### 4.3 Training Script
- **Location**: `scripts/train_brainlm_mae.sh`
- **Usage**: HPC job submission script
- **Configuration**: Modifiable for different hardware setups
- **Note**: Requires proper environment with PyTorch, Hugging Face, Flash Attention

---

## 5. Model Variants

### 5.1 Parameter Scale Variants
- **111M Parameters**:
  - Smaller, more efficient
  - Suitable for moderate GPU memory (16-24GB)
  - Faster inference
  - Good for downstream fine-tuning with limited compute

- **650M Parameters**:
  - Larger representation capacity
  - Better performance on complex tasks
  - Requires high-end GPUs (40GB+ like A100)
  - Recommended for production use

### 5.2 Architecture Variants
- **Configuration flexibility**:
  - Adjustable depth (number of transformer layers)
  - Variable embedding dimension
  - Different MLP head configurations
  - Supports different downstream task types

### 5.3 Model Access
- **Repository**: Hugging Face Model Hub
  - URL: https://huggingface.co/vandijklab/brainlm/
  - Both 111M and 650M weights available
  - Direct download via transformers library
- **Note**: Fine-tuned models still in preparation

---

## 6. Downstream Task Capabilities

### 6.1 Zero-Shot Prediction
- **Approach**: Use pretrained representations directly
- **Tutorial**: `brainlm_tutorial.ipynb`
- **Method**: Extract features, apply simple classifiers
- **Performance**: Surprisingly strong on unseen tasks

### 6.2 Linear Probing
- **Approach**: Freeze encoder, train linear classifier
- **Training**: Notebooks provided for setup
- **Applications**: Classification, regression tasks
- **Typical Improvement**: Moderate over zero-shot

### 6.3 Fine-tuning
- **Approach**: Full network optimization on downstream task
- **Script**: `continue_train_same_wandb.py` for resumable training
- **Tracking**: W&B integration for experiment tracking
- **Typical Improvement**: Significant (10-20%+ over linear probing)

### 6.4 Example Downstream Tasks
- **Classification**:
  - `inference_03_cls_token_mlp_classification.ipynb`
  - Task-specific MLP heads
  - Multi-class disease prediction

- **Regression**:
  - Continuous prediction tasks
  - Behavioral/clinical score prediction

- **KNN-based Methods**:
  - `inference_02_cls_token_knn_regressor.ipynb`
  - No training required, pure representation quality test

---

## 7. Code Structure and Implementation

### 7.1 Directory Organization
```
BrainLM/
├── brainlm_mae/              # Core model implementation
│   ├── modeling_brainlm.py   # Main model class
│   ├── configuration_brainlm.py
│   └── vit_image_*.py        # Variant configs
├── datasets/                 # Dataset utilities
├── data_preprocessing.py      # Preprocessing utilities
├── file_mover_*.py          # Dataset-specific movers
├── continue_train_same_wandb.py  # Training script
├── brainlm_tutorial.ipynb    # Preprocessing tutorial
├── pretrained_models/        # Model directory (auto-managed by HF)
├── training-runs/            # Training checkpoints
└── inference_*.ipynb         # Downstream task notebooks
```

### 7.2 Key Implementation Files

#### Core Model
- **`brainlm_mae/modeling_brainlm.py`**:
  - BrainLM main class
  - MAE encoder-decoder architecture
  - Masking and reconstruction logic
  - Integration with HuggingFace

- **`brainlm_mae/configuration_brainlm.py`**:
  - Configuration class
  - Hyperparameter specifications
  - Model initialization

#### Data Processing
- **`data_preprocessing.py`**:
  - General preprocessing utilities
  - Format conversion
  - Normalization and standardization

- **`file_mover_*.py`** (ADNI, EMBARC, ToPS, YooAttn):
  - Dataset-specific file organization
  - Directory structure management
  - Path handling for different datasets

#### Training
- **`continue_train_same_wandb.py`**:
  - Training loop
  - Checkpoint management
  - W&B experiment tracking
  - Resume training capability

#### Evaluation
- **`inference_01_cls_token_raw_data_plotting.ipynb`**:
  - Visualization of representations
  - Raw data analysis

- **`inference_02_cls_token_knn_regressor.ipynb`**:
  - KNN-based evaluation
  - No-training quality assessment

- **`inference_03_cls_token_mlp_classification.ipynb`**:
  - Full downstream classification
  - MLP head training
  - Performance evaluation

### 7.3 Integration with Hugging Face
- **Model Hub Integration**:
  - Weights directly downloadable
  - Automatic weight loading
  - Seamless with transformers library
- **Configuration**:
  ```python
  from transformers import AutoModel
  model = AutoModel.from_pretrained("vandijklab/brainlm-111m")
  ```

---

## 8. Model Loading and Usage

### 8.1 Basic Loading
```python
from transformers import AutoModel, AutoConfig

# Load configuration
config = AutoConfig.from_pretrained("vandijklab/brainlm-111m")

# Load model
model = AutoModel.from_pretrained("vandijklab/brainlm-111m")
```

### 8.2 Variant Selection
- **111M**: Smaller, faster, memory-efficient
  - Repository: `vandijklab/brainlm-111m`

- **650M**: Larger, higher capacity
  - Repository: `vandijklab/brainlm-650m`
  - Requires Flash Attention installation
  - Recommended for best performance

### 8.3 Custom Configuration
- Modify `configuration_brainlm.py` for custom architectures
- Different embedding dimensions, depths possible
- Supports multiple downstream task heads

---

## 9. Strengths for Benchmark Comparison

### 9.1 Architectural Strengths
1. **MAE Foundation**: Proven effective for self-supervised learning
2. **Scalability**: Both 111M and 650M variants available
3. **Flexibility**: Variable architecture configurations
4. **Efficiency**: Masked approach avoids processing masked tokens

### 9.2 Training Strengths
1. **Large-scale Pretraining**: UK Biobank population data
2. **Reproducibility**: Training scripts and configuration provided
3. **Transfer Capability**: Shows strong transfer across datasets
4. **Multi-dataset Validation**: Tested on ADNI, EMBARC, YooAttn, ToPS

### 9.3 Practical Strengths
1. **HuggingFace Integration**: Easy model access and loading
2. **Clear Documentation**: Tutorial notebooks provided
3. **Code Availability**: Full PyTorch implementation
4. **Flexible Hardware**: Works on different compute scales

### 9.4 Evaluation Strengths
1. **Multiple Downstream Tasks**: Classification, regression, KNN
2. **No-training Baseline**: KNN evaluation shows pure representation quality
3. **Clinical Datasets**: Disease prediction tasks included
4. **Diverse Benchmarks**: Multiple test sets reduce overfitting risk

---

## 10. Limitations and Considerations

### 10.1 Technical Limitations
1. **Preprocessing Variability**: Different datasets may need customized preprocessing
2. **Flash Attention Complexity**: 650M model requires special attention implementation
3. **UK Biobank Bias**: Pretrained on specific population, may need adaptation
4. **Fixed Architecture**: Limited to configurations in `configuration_brainlm.py`

### 10.2 Practical Considerations
1. **Data Access**: UK Biobank pretraining data not publicly available
2. **Environment Setup**: Requires careful dependency management (especially Flash Attention)
3. **Fine-tuned Models**: Not yet released (as of paper submission)
4. **Documentation**: Some preprocessing steps still in development

### 10.3 Implementation Notes
1. **Matrix Transposition**: Some datasets may require matrix shape adjustments
2. **Normalization**: Dataset-specific normalization may be needed
3. **Computational Cost**: 650M model requires high-end GPUs
4. **Training Curve**: Convergence depends on dataset size and task

---

## 11. Relevance for SwiFT_v2 Evaluation

### 11.1 Why BrainLM as Benchmark?
1. **Parallel Approach**: Different architecture (MAE vs. other methods)
2. **Scalable Design**: Multiple model sizes for different comparisons
3. **Transfer Learning Focus**: Directly relevant to SwiFT_v2 transfer
4. **Population-level Pretraining**: Large-scale foundation model

### 11.2 Comparison Opportunities
- **Architecture Comparison**: MAE vs. SwiFT_v2's approach
- **Scale Efficiency**: 111M vs. 650M vs. SwiFT_v2 parameter counts
- **Transfer Performance**: Comparative downstream task evaluation
- **Computational Efficiency**: Training/inference time comparisons

### 11.3 Integration Strategies
- **Feature Extraction**: Extract BrainLM embeddings for comparison
- **Ensemble Methods**: Combine BrainLM and SwiFT_v2 representations
- **Complementary Analysis**: Identify strengths/weaknesses of each
- **Benchmark Suite**: Create comprehensive evaluation framework

---

## 12. References and Related Work

### 12.1 Foundation Papers
- **MAE** (He et al., 2021): Masked Autoencoders in Vision Transformers
- **ViT** (Dosovitskiy et al., 2020): Vision Transformers
- **Flash Attention** (Dao et al., 2022): Efficient attention for large models

### 12.2 Related Work
- **Brain-JEPA** (2024): Parallel foundation model (different approach)
- **Other MAE Adaptations**: Various domain-specific MAE applications
- **Transfer Learning**: General transfer learning in neuroscience

### 12.3 Clinical Datasets
- **UK Biobank**: Population cohort for pretraining
- **ADNI**: Alzheimer's disease neuroimaging
- **EMBARC**: Depression and treatment response
- **YooAttn**: Attention and brain networks
- **ToPS**: Obsessive-compulsive disorder

---

## 13. Tutorial and Notebooks

### 13.1 Available Tutorials
- **Main Tutorial**: `brainlm_tutorial.ipynb`
  - Data preprocessing walkthrough
  - Model loading and inference
  - Zero-shot prediction examples

### 13.2 Downstream Task Notebooks
- **Plotting**: `inference_01_cls_token_raw_data_plotting.ipynb`
- **KNN Evaluation**: `inference_02_cls_token_knn_regressor.ipynb`
- **Classification**: `inference_03_cls_token_mlp_classification.ipynb`

### 13.3 Usage Pattern
1. Start with `brainlm_tutorial.ipynb` for setup
2. Choose downstream task notebook
3. Adapt for your dataset and task
4. Evaluate performance

---

## 14. Citation

```bibtex
@article{BrainLM,
  title={BrainLM: A Foundation Model for Brain Activity Recordings},
  journal={OpenReview},
  year={2024},
  note={Vandijk Lab}
}
```

---

## 15. Contact and Resources

- **GitHub**: https://github.com/vandijklab/BrainLM
- **Model Hub**: https://huggingface.co/vandijklab/brainlm/
- **Lab**: Vandijk Lab (Yale University)

---

**Document Version**: 1.0
**Last Updated**: October 23, 2025
**Status**: Analysis Complete - Ready for SwiFT_v2 Benchmark Comparison
