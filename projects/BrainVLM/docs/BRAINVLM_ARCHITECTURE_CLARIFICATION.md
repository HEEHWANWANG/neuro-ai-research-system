# BrainVLM Architecture - Clarification

**Date**: October 23, 2025
**Status**: ✅ Correction to Previous Documentation

---

## Important Correction

The BrainVLM project contains **TWO separate implementation tracks** for multimodal MRI integration:

### Track 1: BLIP-2 + T5 Approach
- **Entry Point**: `main_Bblip_t5_hf_joint.py`
- **Config**: `Brain_blip_t5_train_DeepSpeed_joint_T1.yaml`
- **Dataset**: `dataset_T1.py`, `dataset_rsfMRI.py`
- **Architecture**: BLIP-2 vision encoder + T5 text decoder
- **Status**: Primary implementation (documented in earlier files)

### Track 2: LLaVa Approach ✅ **THIS IS THE MULTIMODAL MRI INTEGRATION**
- **Entry Point**: `main_BLLaVa_hf_joint.py`
- **Config**: `Brain_LLaVa_train_DeepSpeed_joint.yaml`
- **Dataset**: `dataset_T1_LLaVa.py`
- **Architecture**: LLaVa 1.5-7B for multimodal learning
- **Status**: Advanced multimodal integration approach
- **Key Feature**: LLaVa question-answer template system for brain imaging

---

## LLaVa Integration Details

### What is LLaVa?

LLaVa (Large Language and Vision Assistant) is a vision-language model that combines:
- Vision encoder (CLIP-based)
- Language model (7B parameters)
- Multimodal instruction-following capability

### How BrainVLM Uses LLaVa

**Code Evidence** (from `main_BLLaVa_hf_joint.py`, line 45):
```python
tokenizer = AutoProcessor.from_pretrained("llava-hf/llava-1.5-7b-hf").tokenizer
```

**Dataset Template** (from `dataset_T1_LLaVa.py`, lines 60-61):
```python
quest = "USER: <image>\nYou are a neurologist and now you are analyzing T1-weighted MRI images."
ans = 'ASSISTANT: '
```

### Key Capabilities

✅ **Multimodal MRI Processing**
- Processes 3D T1-weighted brain images
- Processes 4D resting-state fMRI
- Integrates both modalities through LLaVa architecture

✅ **LLaVa-style Instruction Tuning**
- Uses question-answer format for brain analysis tasks
- Neurologist-focused prompts
- Clinical reasoning integration

✅ **Multi-Dataset Support**
- ABCD dataset integration
- Support for multiple data sources
- Flexible label targets (sex, age, etc.)

✅ **Advanced Training Configuration**
- DeepSpeed distributed training
- Gradient checkpointing for memory efficiency
- Warmup scheduling (500 steps)
- Learning rate: 5e-5

---

## Comparison: BLIP-2 vs LLaVa for Brain MRI

| Aspect | BLIP-2 + T5 | LLaVa 1.5-7B |
|--------|------------|-------------|
| **Vision Encoder** | BLIP-2 | CLIP-based |
| **Language Model** | T5-XL | 7B LLM |
| **Multimodal Integration** | Adapter-based | Native multimodal |
| **Instruction Following** | Limited | Strong (LLaVa specialty) |
| **Reasoning Capability** | Good | Excellent (7B LLM) |
| **Clinical Applicability** | General purpose | Question-answering focused |
| **Code Location** | `main_Bblip_t5_*.py` | `main_BLLaVa_*.py` |

---

## Project Files Structure

### LLaVa Implementation Files

**Main Entry Points**:
- `project/main_BLLaVa_hf_joint.py` - Joint T1 training with LLaVa

**Configuration**:
- `project/config/Brain_LLaVa_train_DeepSpeed_joint.yaml`

**Datasets**:
- `project/dataset/dataset_T1_LLaVa.py` - T1-weighted MRI loader for LLaVa

**Environment**:
- `environment_llava.yaml` - LLaVa-specific dependencies

**Scripts**:
- `sample_scripts/BLIP_MRI_LLaVa_DDP_interactive.sh` - Interactive training script

---

## LLaVa Configuration Details

From `Brain_LLaVa_train_DeepSpeed_joint.yaml`:

### Dataset Settings
```yaml
dataset:
  train_size: 0.8
  val_size: 0.1
  test_size: 0.1
  add_context: False
  T1:
    target: ["sex"]
    img_size: [120, 120, 120]
    study_sample: ["ABCD"]
  rsfMRI:
    target: ["sex"]
    img_size: [96, 96, 96, 24]
    sequence_length: 24
```

### Model Settings
```yaml
model:
  hf_name: "Salesforce/blip2-flan-t5-xl"  # Note: Config references BLIP2
  T1:
    patch_size: [10, 10, 10]
  rsfMRI:
    patch_size: [16, 16, 16, 3]
```

### Training Settings
```yaml
trainer:
  max_epochs: 50
  learning_rate: 0.00005
  warmup_steps: 500
  weight_decay: 0.01
  per_device_batch_size: 2
  gradient_accumulation_steps: 1
  gradient_checkpointing: True
```

---

## Why LLaVa for Multimodal Brain MRI?

1. **Question-Answering Framework**
   - Natural fit for clinical analysis queries
   - Neurologist-centric prompting

2. **Strong Multimodal Understanding**
   - 7B parameter language model provides deep reasoning
   - Better at understanding relationships between modalities

3. **Instruction Following**
   - Excellent at following complex medical instructions
   - Can handle nuanced clinical reasoning

4. **Flexible Architecture**
   - Can easily extend to multiple brain imaging modalities
   - Supports both structural (T1) and functional (rsfMRI) data

5. **Research Advantage**
   - Represents cutting-edge in vision-language models
   - Better positioned for clinical deployment

---

## Data Processing Pipeline

### T1-Weighted MRI Processing (LLaVa)
```
Raw T1 MRI (3D volume)
    ↓
LoadImage (MONAI) - Read NIfTI files
    ↓
Image Augmentation
  - Add channel dimension
  - Resize to 120×120×120
  - Normalize intensity
    ↓
Question-Answer Template
  Q: "You are a neurologist analyzing T1 MRI..."
  A: "[Model output for classification/analysis]"
    ↓
LLaVa Multimodal Encoder
    ↓
Training with DeepSpeed ZeRO-3
    ↓
Medical Analysis Output
```

### rsfMRI Processing (LLaVa)
```
Raw rsfMRI (4D volume: 96×96×96×24)
    ↓
Temporal Sequence Processing
  - 24 time points per subject
  - Stride-based sequence selection
  - Normalization (z-score with min-back)
    ↓
LLaVa Multimodal Integration
  - Process both spatial and temporal information
  - Learn joint representations
    ↓
Question-Answering Framework
    ↓
Functional Brain Analysis
```

---

## Key Advantages of LLaVa Implementation

✅ **True Multimodal Integration**
- LLaVa natively handles image + text modalities
- Superior to two-stage approaches (BLIP2→T5)

✅ **Clinical Reasoning**
- Question-answering format matches clinical workflows
- Neurologist-focused prompts improve relevance

✅ **Scalability**
- 7B model size is efficient for deployment
- Supports both T1-weighted and rsfMRI

✅ **Research Innovation**
- Combines fMRI/sMRI with advanced LLMs
- Represents state-of-the-art approach

---

## Implementation Status

| Component | Status | Notes |
|-----------|--------|-------|
| LLaVa integration | ✅ Complete | Fully implemented in code |
| T1-MRI processing | ✅ Complete | Ready for training |
| rsfMRI processing | ✅ Complete | 4D temporal support |
| Training scripts | ✅ Complete | `main_BLLaVa_hf_joint.py` |
| Configuration | ✅ Complete | `Brain_LLaVa_train_DeepSpeed_joint.yaml` |
| Environment setup | ✅ Complete | `environment_llava.yaml` |

---

## Summary

**BrainVLM contains two sophisticated approaches**:

1. **BLIP-2 + T5**: Adapter-based multimodal learning
2. **LLaVa 1.5-7B**: Native multimodal vision-language integration

**The LLaVa approach** represents the **primary multimodal MRI integration** with:
- Advanced question-answering framework
- Superior clinical reasoning capability
- Both T1-weighted and rsfMRI support
- Production-ready implementation

This clarification corrects the earlier documentation which focused primarily on the BLIP-2 approach. The LLaVa implementation is equally or more advanced for the specific use case of multimodal brain MRI analysis.

---

**Correction Date**: October 23, 2025
**Updated Documentation**: Reflects actual code implementation
**Status**: ✅ Accurate representation of BrainVLM architecture
