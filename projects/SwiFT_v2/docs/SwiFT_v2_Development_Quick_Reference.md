# SwiFT v2 Development Quick Reference

**Quick lookup for developers working on SwiFT v2 codebase**

---

## 🚀 Quick Start Commands

### Test Setup (Interactive, Small Scale)
```bash
cd /Users/apple/Desktop/SwiFT_v2_perlmutter

# Test data loading
python project/debug.py

# Small pretraining test
bash sample_scripts/v2_simmim_multiDS_script_perlmutter_interactive.sh

# Test downstream task
bash sample_scripts/downstream/UKB/sex/sub10_unfreeze_0.2.sh
```

### Full Pretraining
```bash
# Multi-node pretraining on Perlmutter
bash sample_scripts/v2_simmim_multiDS_script_perlmutter.sh

# With DeepSpeed
bash sample_scripts/v2_simmim_multiDS_script_perlmutter.sh
```

### Downstream Fine-tuning
```bash
# Sex prediction (UKB, 100 samples, unfreeze with 0.2 weight decay)
bash sample_scripts/downstream/UKB/sex/sub100_unfreeze_0.2.sh

# Age prediction (similar structure)
bash sample_scripts/downstream/UKB/age/sub100_unfreeze_0.2.sh

# With Optuna hyperparameter optimization
cd downstream_optuna
python main.py --dataset_name UKB --downstream_task sex --limit_batches 100
```

---

## 📁 Key Directory Map

```
project/                              # Main training code
├── main.py                           # Entry: pretraining & fine-tuning
├── debug.py                          # Debug mode
├── main_embedding_extraction.py      # Extract features
└── module/
    ├── pl_classifier.py              # PyTorch Lightning module
    ├── models/
    │   ├── swin4d_transformer_ver11.py          # ⭐ Main architecture
    │   ├── simmim_swin4d_transformer_ver11.py   # SimMIM variant
    │   ├── patchembedding.py                    # 4D patch embedding
    │   ├── load_model.py                        # Model loading utilities
    │   └── utils.py                             # Model utilities
    └── utils/
        ├── data_module.py            # Data loading (⭐ PyTorch Lightning)
        ├── data_utils.py             # Data utilities
        ├── metrics.py                # Evaluation metrics
        ├── losses.py                 # Loss functions
        ├── lr_scheduler.py           # Learning rate schedulers
        └── data_preprocess_and_load/
            ├── preprocessing.py      # fMRI preprocessing
            └── datasets.py           # Dataset classes

downstream_optuna/                   # Downstream task optimization
├── main.py                           # Downstream training entry
├── trainer.py                        # Training loop
├── models.py                         # Classification/regression heads
├── dataloaders.py                    # Data loading for downstream
└── bash_scripts/
    ├── 5M/                          # Scripts for 5M model
    ├── 202M/                        # Scripts for 202M model
    └── 806M/                        # Scripts for 806M model

sample_scripts/
├── pretraining/masking*/            # Different masking ratios
├── downstream/DATASET/TASK/         # Task-specific scripts
└── scalability/                     # Scale testing

data/splits/                         # Data split files
├── UKB_v1-v6/pretraining/
├── ABCD/pretraining/
├── S1200/downstream/
└── ...
```

---

## 🧬 Core Architecture Quick Reference

### Swin4D Transformer Flow
```
Input: [B, T, D, H, W] where B=batch, T=time, D,H,W=spatial
  ↓
Patch Embedding: [B, N, C] where N=num_patches, C=channels
  ↓
Stage 1: Window attention (Shifted windows)
  ↓ Patch Merging (spatial only)
  ↓
Stage 2: Window attention
  ↓ Patch Merging
  ↓
Stage 3: Window attention
  ↓ Patch Merging
  ↓
Stage 4: Window attention
  ↓
Output: Global features [B, C_final]
```

### PyTorch Lightning Module (LitClassifier)
```python
class LitClassifier(pl.LightningModule):
    def __init__(self, args):
        super().__init__()
        self.model = load_model(args.model_name, args)  # Swin4D
        self.head = MLPClassifier(...)  # Task-specific head
        self.loss_fn = define_loss(args.loss_type)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self.model(x)
        logits = self.head(logits)
        loss = self.loss_fn(logits, y)
        return loss

    def validation_step(self, batch, batch_idx):
        # Compute validation metrics
        pass
```

---

## 📊 Common Arguments & Configurations

### Main Training Arguments
```bash
# Model architecture
--model_name "swin4d_v11"           # Model variant
--input_size 96                      # Spatial size (96×96×96)
--in_channels 1                      # Input channels (fMRI is 1)
--patch_size 4                       # Patch size for embedding
--embed_dim 96                       # Embedding dimension
--depths "2,2,6,2"                   # Blocks per stage
--num_heads "3,6,12,24"             # Attention heads per stage

# Pretraining (SimMIM)
--mask_ratio 0.4                     # Masking ratio (0.2-0.8)
--model_patch_size 4                 # Patch size for masking
--mask_patch_size 16                 # Masked patch size

# Training
--batch_size 4                       # Batch per GPU
--num_epochs 100                     # Total epochs
--lr 1e-4                            # Learning rate
--weight_decay 0.05                  # L2 regularization
--strategy ddp                       # Distributed strategy

# Data
--dataset_name "UKB"                 # Which dataset
--data_path /path/to/data            # Data location
--num_workers 4                      # Data loading workers

# Downstream
--downstream_task "sex"              # Task name
--downstream_task_type "default"     # Classification/regression
--freeze_feature_extractor           # Freeze backbone
--finetune_last_block                # Fine-tune only last block
```

### Neptune Logging
```bash
--loggername "neptune"               # Use Neptune
--project_name "workspace/project"   # Neptune project
--neptune_tags ["tag1", "tag2"]      # Tags for tracking
```

---

## 🔑 Key Classes & Functions

### Model Loading
```python
from project.module.models.load_model import load_model

model = load_model(
    model_name="swin4d_v11",
    args=args  # Contains model config
)
```

### Data Module (PyTorch Lightning)
```python
from project.module.utils.data_module import fMRIDataModule

data_module = fMRIDataModule(
    dataset_name="UKB",
    batch_size=4,
    num_workers=4,
    split_file="data/splits/UKB_v3/pretraining/split_fixed_1.txt"
)

# In trainer
trainer.fit(model, datamodule=data_module)
```

### Metrics
```python
from project.module.utils.metrics import (
    compute_r2_score,
    compute_pearson_correlation
)

r2 = compute_r2_score(predictions, targets)
pearson = compute_pearson_correlation(predictions, targets)
```

### Loss Functions
```python
from project.module.utils.losses import (
    MSELoss,          # For regression/reconstruction
    CrossEntropyLoss  # For classification
)
```

---

## 🧪 Testing & Debugging

### Data Loading Test
```bash
python project/debug.py \
    --dataset_name UKB \
    --batch_size 2 \
    --num_workers 0 \
    --limit_batches 10
```

### Model Output Test
```python
import torch
from project.module.models import load_model

model = load_model("swin4d_v11", args)
x = torch.randn(1, 36, 96, 96, 96)  # [B, T, D, H, W]
out = model(x)
print(out.shape)  # [1, 4096] or appropriate output size
```

### Checkpoint Inspection
```python
import torch
checkpoint = torch.load("path/to/checkpoint.pth")
print(checkpoint.keys())  # ['state_dict', 'hparams', ...]
model.load_state_dict(checkpoint['state_dict'])
```

---

## 📈 Common Development Tasks

### Task 1: Modify Model Architecture
```python
# File: project/module/models/swin4d_transformer_ver12.py
# (Create new version)

class Swin4DTransformerV12(nn.Module):
    """My improved version"""
    def __init__(self, args):
        super().__init__()
        # Your modifications here

    def forward(self, x):
        # [B, T, D, H, W] -> [B, embed_dim]
        pass

# Register in: project/module/models/__init__.py
# Update: project/module/models/load_model.py
```

### Task 2: Add New Loss Function
```python
# File: project/module/utils/losses.py

class ContrastiveLoss(nn.Module):
    def __init__(self, temperature=0.07):
        super().__init__()
        self.temperature = temperature

    def forward(self, z1, z2, labels):
        # Your loss implementation
        return loss

# Use in pl_classifier.py:
# if args.loss_type == "contrastive":
#     self.loss_fn = ContrastiveLoss()
```

### Task 3: New Downstream Task
```python
# 1. Create bash script in sample_scripts/downstream/DATASET/TASK/
# 2. Update downstream_optuna/dataloaders.py for label loading
# 3. Update downstream_optuna/models.py for task-specific head
# 4. Update downstream_optuna/main.py for loss function
# 5. Test with: python downstream_optuna/main.py --downstream_task NEW_TASK
```

### Task 4: Modify Data Preprocessing
```python
# File: project/module/utils/data_preprocess_and_load/preprocessing.py
# or project/module/utils/data_utils.py

# Add custom preprocessing:
def custom_preprocessing(fmri_volume):
    """Your preprocessing"""
    # Normalization, registration, etc.
    return processed_volume

# Update data_module.py to use it
```

### Task 5: Add Visualization
```python
# File: notebooks/custom_analysis.ipynb

import torch
import matplotlib.pyplot as plt
from project.module.models import load_model

# Load model and embeddings
model = load_model("swin4d_v11", args)
embeddings = extract_embeddings(model, data_loader)

# Visualize (t-SNE, PCA, etc.)
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2)
embedded = tsne.fit_transform(embeddings)
plt.scatter(embedded[:, 0], embedded[:, 1])
```

---

## 🔗 Important File Cross-References

| When you need to... | Check this file | Then see... |
|--------------------|-----------------|------------|
| Change model config | `project/main.py` | `add_model_specific_args()` in `pl_classifier.py` |
| Add new dataset | `utils/data_module.py` | `datasets.py` for dataset class |
| Modify training loop | `pl_classifier.py` | `training_step()`, `validation_step()` |
| Add new metric | `utils/metrics.py` | `compute_metrics()` in `pl_classifier.py` |
| Change loss | `utils/losses.py` | `_get_loss()` in `pl_classifier.py` |
| Visualize embeddings | `notebooks/` | `main_embedding_extraction.py` |
| Debug data loading | `project/debug.py` | `utils/data_module.py` |
| Deploy on Perlmutter | `sample_scripts/*.sh` | `export_DDP_vars.sh` |

---

## 🚨 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| CUDA out of memory | Reduce `batch_size`, or use gradient accumulation: `--gradient_accumulation_steps 2` |
| Data loading slow | Increase `num_workers`, check disk I/O |
| Model not converging | Check learning rate, try `--lr 5e-5`, check data normalization |
| DeepSpeed checkpoint issue | Use `--load_ds_ckpt_manually` flag |
| Resume training fails | Ensure checkpoint path matches `--resume_ckpt_path` |
| Validation metrics weird | Check dataset split, verify label encoding |

---

## 📝 Development Checklist

When implementing a new feature:

- [ ] Create feature branch: `git checkout -b feature/my-feature`
- [ ] Implement in appropriate file (don't create new modules unless necessary)
- [ ] Write small test script or notebook
- [ ] Update relevant `__init__.py` files for imports
- [ ] Test with small dataset first (`--limit_batches 10`)
- [ ] Test with downstream task
- [ ] Document changes in docstrings
- [ ] Run on full dataset if major change
- [ ] Commit with clear message
- [ ] Update CLAUDE.md with new capabilities if applicable

---

## 🎯 Research Workflow

### Hypothesis Generation Phase
1. Identify research question (architectural improvement, new loss, etc.)
2. Review relevant code sections
3. Design experiment
4. Create new model version or modify parameters

### Implementation Phase
1. Implement changes (follow code organization)
2. Test on small subset
3. Validate against baseline
4. Scale to full dataset

### Evaluation Phase
1. Compare metrics (accuracy, loss curves, etc.)
2. Analyze results
3. Test on multiple downstream tasks
4. Document findings

### Publishing Phase
1. Archive results in workspace
2. Write analysis notebook
3. Prepare figures and tables
4. Draft paper/report

---

## 🔬 Useful Python Snippets

### Quick Model Test
```python
import torch
from project.module.models.load_model import load_model

# Mock args
class Args:
    model_name = "swin4d_v11"
    input_size = 96
    in_channels = 1
    depths = "2,2,6,2"
    num_heads = "3,6,12,24"

args = Args()
model = load_model("swin4d_v11", args)
x = torch.randn(2, 36, 96, 96, 96)  # 2 samples, 36 timesteps, 96³ spatial
output = model(x)
print(f"Output shape: {output.shape}")
```

### Load Checkpoint
```python
import torch
from collections import OrderedDict

checkpoint_path = "output/project_name/checkpoints/last.ckpt"
checkpoint = torch.load(checkpoint_path)

# For PyTorch Lightning
if "state_dict" in checkpoint:
    state = checkpoint["state_dict"]
    # Remove 'model.' prefix if needed
    new_state = OrderedDict()
    for k, v in state.items():
        new_state[k.replace("model.", "")] = v
    model.load_state_dict(new_state)
```

### Extract Embeddings
```python
import torch
from torch.utils.data import DataLoader

@torch.no_grad()
def get_embeddings(model, dataloader):
    embeddings = []
    for batch in dataloader:
        x, _ = batch
        emb = model(x)  # [batch_size, embed_dim]
        embeddings.append(emb.cpu().numpy())
    return np.concatenate(embeddings, axis=0)
```

---

## 📚 Further Reading

- **Original SwiFT Paper**: https://arxiv.org/pdf/2307.05916
- **Swin Transformer**: https://arxiv.org/abs/2103.14030
- **SimMIM**: https://arxiv.org/abs/2111.06377
- **PyTorch Lightning**: https://lightning.ai/
- **DeepSpeed**: https://www.deepspeed.ai/

---

**Status**: Ready for active development!

Last updated: October 22, 2025
