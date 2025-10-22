# BrainVLM Project Overview

## Project Information

**Project Name**: BrainVLM (Vision Language Model for Brain MRI)
**Code Location**: `/Users/apple/Desktop/BLIP_MRI`
**Primary Architecture**: BLIP-2 with T5 encoder for multimodal brain imaging
**Code Size**: ~1,256 lines of Python
**Main Entry Points**:
- `main_Bblip_t5_hf_joint.py` - Joint T1 training
- `main_BLLaVa_hf_joint.py` - LLaVa-based T1 training

---

## Project Architecture

### Important: Dual Implementation Approach

**BrainVLM contains TWO separate multimodal approaches:**

1. **BLIP-2 + T5** (`main_Bblip_t5_*.py`): Adapter-based multimodal learning
2. **LLaVa 1.5-7B** (`main_BLLaVa_*.py`): **Native multimodal vision-language integration** ⭐

The **LLaVa approach** is the primary implementation for multimodal MRI integration with superior clinical reasoning capabilities.

### Core Components

#### 1. **Models** (`project/model/`)
- **modeling_blip_2.py** (81 KB) - BLIP-2 model implementation
- **Bblip_t5.py** (5.1 KB) - BLIP T5 wrapper for brain imaging
- **Bblip_t5_tmp.py** (4.6 KB) - Temporary T5 variant for testing

**Key Features**:
- Vision-language model using BLIP-2 as base
- T5 text encoder for medical report generation
- Support for 3D brain MRI inputs (T1-weighted and rsfMRI)

#### 2. **Datasets** (`project/dataset/`)
- **dataset_T1.py** (19.1 KB) - T1-weighted structural MRI loader
- **dataset_T1_LLaVa.py** (19.1 KB) - LLaVa-compatible T1 dataset
- **dataset_rsfMRI.py** (17.0 KB) - Resting-state fMRI loader
- **datamodule_rsfMRI.py** (23.3 KB) - PyTorch Lightning datamodule

**Dataset Support**:
- **ABCD Study**: Adolescent Brain Cognitive Development
- **UKB (UK Biobank)**: Large population cohort
- **Modalities**: T1-weighted sMRI, rsfMRI (4D)

#### 3. **Utilities** (`project/utils/`)
- **Trainer.py** (Custom training loops)
- **utils.py** (Helper functions)
- **data.py** (Data loading utilities)
- **CustomDataCollatorWithPadding** - Padding for variable-length inputs
- **InterleaveDataset** - Multi-modality dataset interleaving

#### 4. **Configuration** (`project/config/`)
**Key Config Files**:
- `Brain_blip_t5_train_DeepSpeed.yaml` - Main T5 training config
- `Brain_blip_t5_train_DeepSpeed_joint_T1.yaml` - Joint T1 training
- `Brain_LLaVa_train_DeepSpeed_joint_T1.yaml` - LLaVa variant
- `deepspeed/` - DeepSpeed distributed training configs

---

## Technical Architecture

### Input/Output Flow

```
Raw MRI Data (3D/4D)
        ↓
Dataset Loaders (T1/rsfMRI)
        ↓
Patch Embedding (3D patches)
        ↓
BLIP-2 Vision Encoder
        ↓
T5 Text Decoder
        ↓
Medical Report / Prediction
```

### Key Parameters

| Component | T1-weighted | rsfMRI |
|-----------|-----------|---------|
| **Image Size** | 128×128×128 | 96×96×96×20 |
| **Patch Size** | 18×18×18 | 16×16×16×5 |
| **Base Model** | BLIP-2 + T5 | BLIP-2 + T5 |
| **Datasets** | ABCD, UKB | ABCD |

### Training Configuration

**Default Settings**:
- **Max Epochs**: 50
- **Learning Rate**: 5e-5
- **Batch Size**: 32 (per device)
- **Optimizer**: AdamW with weight decay (0.01)
- **Warmup Steps**: 500
- **Gradient Accumulation**: 1 step
- **Precision**: DeepSpeed ZeRO-3

**Hardware Requirements**:
- Multi-GPU setup (uses DeepSpeed)
- Estimated: 4x A100 or equivalent
- Mixed precision training enabled

---

## Workflows

### 1. Training Workflows

#### Joint Training (T1)
```bash
python main_Bblip_t5_hf_joint.py
# Uses: Brain_blip_t5_train_DeepSpeed_joint_T1.yaml
```

#### LLaVa-based Training
```bash
python main_BLLaVa_hf_joint.py
# Uses: Brain_LLaVa_train_DeepSpeed_joint_T1.yaml
```

#### Sequential Training
```bash
python main_Bblip_t5_hf_sequential.py
# Progressive training on different modalities
```

#### Resume Training
```bash
python main_Bblip_t5_hf_resume.py
# Continues from saved checkpoint
```

#### Inference
```bash
python main_Bblip_t5_hf_inference.py
# Generate predictions on new data
```

### 2. Dataset Workflows

**Multi-Dataset Integration**:
1. Load ABCD T1-weighted structural MRI
2. Load UKB T1-weighted structural MRI
3. Optionally load rsfMRI data
4. Concatenate datasets with `InterleaveDataset`
5. Train jointly on all modalities

**Data Preprocessing**:
- Standardization and normalization
- 3D patch extraction
- Tokenization for text targets
- Data augmentation (optional)

---

## Key Features

✅ **Multimodal Learning**: Combines T1-weighted and rsfMRI data
✅ **Multi-Dataset**: ABCD + UKB for diverse demographics
✅ **Vision-Language**: Medical report generation from images
✅ **Scalable Training**: DeepSpeed for large models
✅ **Flexible Architecture**: Support for different base models (BLIP-2, LLaVa)
✅ **Custom Trainers**: Specialized training loops for medical imaging

---

## Data Format

### Input Format
- **T1 MRI**: 3D volumetric NIfTI files (128×128×128)
- **rsfMRI**: 4D volumetric NIfTI files (96×96×96×20)
- **Metadata**: CSV files with phenotype information

### Output Format
- **Predictions**: Medical text reports or classifications
- **Embeddings**: Image embeddings from BLIP-2
- **Logits**: Model outputs for downstream tasks

---

## Experiments Performed

**Current Status**: Active development

**Key Experiments**:
1. T1-weighted sMRI with BLIP-2 + T5
2. Joint T1 training across ABCD and UKB
3. LLaVa architecture comparison
4. Multi-modality fusion (T1 + rsfMRI)
5. Sequential vs. joint training strategies

---

## Dependencies

### Core Libraries
- `torch` - Deep learning framework
- `transformers` - Hugging Face models (BLIP-2, T5, LLaVa)
- `pytorch-lightning` - Training framework
- `deepspeed` - Distributed training optimization
- `wandb` - Experiment tracking

### Data Dependencies
- `nibabel` - NIfTI format support
- `numpy`, `pandas` - Data processing
- `PIL` - Image processing

### Environment Files
- `environment.yaml` - Main conda environment
- `environment_llava.yaml` - LLaVa-specific dependencies

---

## Next Development Steps

1. **Complete rsfMRI Integration**: Finalize 4D data loading
2. **Model Comparison**: Evaluate BLIP-2 vs LLaVa
3. **Cross-Modal Learning**: Learn joint representations
4. **Clinical Validation**: Evaluate on held-out test sets
5. **Report Generation**: Improve medical text quality
6. **Scalability**: Test on larger datasets
7. **Downstream Tasks**: Fine-tune for specific clinical predictions

---

## Related Work

**Inspiration & References**:
- BLIP-2 (Li et al., 2023) - Vision-Language pre-training
- LLaVa (Liu et al., 2023) - Multimodal instruction tuning
- Medical imaging + LLMs - Recent direction in medical AI

---

## Contact & Documentation

**Project Root**: `/Users/apple/Desktop/BLIP_MRI`
**Main Config**: `project/config/Brain_blip_t5_train_DeepSpeed.yaml`
**Primary Author**: hwang@snu.ac.kr

**Related Projects**:
- SwiFT v2 (fMRI foundation model)
- Brain-JEPA (Self-supervised learning)

---

**Status**: 🔬 Active Development
**Last Updated**: October 23, 2025
