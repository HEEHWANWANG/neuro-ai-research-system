# BrainVLM - Quick Reference Guide

## Project Summary

**Vision Language Model for Brain MRI** - Multi-modal approach to learning from structural (T1) and functional (rsfMRI) brain images using BLIP-2 + T5 architecture.

---

## Quick Start

### Clone & Setup
```bash
cd /Users/apple/Desktop/BLIP_MRI
conda env create -f environment.yaml
conda activate brain_vlm
```

### Run Training
```bash
# T1-weighted training
python project/main_Bblip_t5_hf_joint.py

# LLaVa variant
python project/main_BLLaVa_hf_joint.py

# Sequential training
python project/main_Bblip_t5_hf_sequential.py
```

### Configuration
**Edit config**: `project/config/Brain_blip_t5_train_DeepSpeed.yaml`

Key settings:
```yaml
dataset:
    T1:
        img_size: [128, 128, 128]  # T1 volume size
        study_sample: ["ABCD"]      # Dataset source
        img_dir: "/path/to/images"
trainer:
    max_epochs: 50
    learning_rate: 0.00005
    per_device_batch_size: 32
```

---

## Project Structure

```
BLIP_MRI/
├── project/
│   ├── main_Bblip_t5_hf_joint.py        ← T5 training
│   ├── main_BLLaVa_hf_joint.py          ← LLaVa training
│   ├── main_Bblip_t5_hf_sequential.py   ← Sequential training
│   ├── main_Bblip_t5_hf_resume.py       ← Resume training
│   ├── main_Bblip_t5_hf_inference.py    ← Inference
│   │
│   ├── model/
│   │   ├── modeling_blip_2.py           ← Core BLIP-2 model
│   │   ├── Bblip_t5.py                  ← T5 wrapper
│   │   └── Bblip_t5_tmp.py
│   │
│   ├── dataset/
│   │   ├── dataset_T1.py                ← T1 MRI loader
│   │   ├── dataset_T1_LLaVa.py          ← LLaVa-compatible
│   │   ├── dataset_rsfMRI.py            ← rsfMRI loader
│   │   └── datamodule_rsfMRI.py         ← PyTorch Lightning
│   │
│   ├── utils/
│   │   ├── Trainer.py                   ← Custom trainer
│   │   ├── utils.py                     ← Helpers
│   │   └── data.py                      ← Data utils
│   │
│   └── config/
│       ├── Brain_blip_t5_train_DeepSpeed.yaml
│       ├── Brain_LLaVa_train_DeepSpeed_joint_T1.yaml
│       └── deepspeed/
│           ├── hf_deepspeed_zero3.json
│           ├── hf_deepspeed_zero2.json
│           └── hf_deepspeed_zero3_offload.json
│
├── sample_scripts/
├── environment.yaml                     ← Dependencies
└── overview.pptx                        ← Project slides
```

---

## Models

| Model | Input | Purpose |
|-------|-------|---------|
| **BLIP-2** | Images | Vision encoder |
| **T5-XL** | Text | Text decoder |
| **LLaVa-1.5-7B** | Images + Text | Alternative vision-language |

---

## Datasets

| Dataset | Modality | Size | Purpose |
|---------|----------|------|---------|
| **ABCD** | T1-weighted sMRI | 10K+ subjects | Adolescent neuroimaging |
| **UKB** | T1-weighted sMRI | 45K+ subjects | Population-based |
| **rsfMRI** | 4D resting-state fMRI | Subset | Functional connectivity |

---

## Key Configurations

### Input Sizes
- **T1**: 128×128×128 voxels
- **rsfMRI**: 96×96×96×20 (space × time)

### Patch Sizes
- **T1**: 18×18×18 voxels per patch
- **rsfMRI**: 16×16×16×5 per patch

### Training
- **Batch Size**: 32 per GPU
- **Learning Rate**: 5e-5
- **Gradient Accumulation**: 1
- **Max Epochs**: 50
- **Warmup**: 500 steps

### Optimization
- **Optimizer**: AdamW
- **Weight Decay**: 0.01
- **Mixed Precision**: Yes
- **Gradient Checkpointing**: Yes
- **DeepSpeed**: ZeRO-3

---

## Common Tasks

### 1. Change Dataset
Edit `project/config/Brain_blip_t5_train_DeepSpeed.yaml`:
```yaml
dataset:
    T1:
        study_sample: ["ABCD", "UKB"]  # Use both
        img_dir: ["/path/ABCD", "/path/UKB"]
```

### 2. Adjust Batch Size
```yaml
trainer:
    per_device_batch_size: 64  # Increase for more memory
```

### 3. Resume Training
```bash
python project/main_Bblip_t5_hf_resume.py
# Loads checkpoint from: trainer.ckpt_dir
```

### 4. Run Inference
```bash
python project/main_Bblip_t5_hf_inference.py
# Generate predictions on test data
```

### 5. Monitor Training
Uses Weights & Biases (wandb):
- Project: `BLIP_sMRI`
- Auto-logs: loss, metrics, checkpoints

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Out of memory | Reduce `per_device_batch_size` or increase `gradient_accumulation_steps` |
| Slow training | Use `gradient_checkpointing: True` |
| Missing data | Check paths in config match your setup |
| CUDA errors | Verify DeepSpeed installation |

---

## Important Files

| File | Purpose |
|------|---------|
| `environment.yaml` | Conda dependencies |
| `project/config/*.yaml` | Training configs |
| `project/model/modeling_blip_2.py` | BLIP-2 implementation |
| `project/dataset/*.py` | Data loaders |

---

## Output Locations

- **Checkpoints**: `./hf_results/{hash_key}/last.ckpt`
- **Logs**: wandb dashboard
- **Predictions**: Saved per experiment

---

## Useful Commands

```bash
# Check environment
conda list | grep torch

# GPU memory usage
nvidia-smi

# Check data loading
python -c "from project.dataset.dataset_T1 import ABCD_T1; print(ABCD_T1.__doc__)"

# List available configs
ls project/config/*.yaml
```

---

## Next Steps for Development

1. **Test rsfMRI loading** - Complete 4D dataset integration
2. **Benchmark models** - Compare BLIP-2 vs LLaVa performance
3. **Ablation studies** - Test architecture components
4. **Clinical validation** - Evaluate on test sets
5. **Report quality** - Improve generated medical text

---

**Status**: 🔬 Active Development
**Architecture**: Vision-Language Multi-Modal
**Framework**: PyTorch + HuggingFace + DeepSpeed
