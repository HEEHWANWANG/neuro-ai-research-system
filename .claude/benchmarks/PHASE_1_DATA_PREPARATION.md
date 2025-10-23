# Phase 1: Benchmark Data Preparation

**Purpose**: Establish standardized dataset structure and metadata for benchmark model evaluation
**Timeline**: 1-2 days
**Status**: Ready for Implementation

---

## Overview

Phase 1 is the critical foundation for all subsequent benchmark evaluation. It involves:

1. Creating standardized dataset directory structure
2. Preparing ADNI dataset (primary evaluation dataset)
3. Preparing HCP-Aging dataset (secondary evaluation dataset)
4. Creating fixed train/val/test splits with documented random seed
5. Collecting and organizing metadata (demographics, clinical labels)
6. Validating data integrity and consistency

**Outcome**: Ready-to-use dataset structure for embedding extraction and downstream task evaluation

---

## Directory Structure

### Target Structure

```
.claude/benchmarks/
├── datasets/                           # NEW: Benchmark datasets
│   ├── ADNI/                          # Primary evaluation dataset
│   │   ├── raw/                       # Original NIfTI files
│   │   │   ├── SUBJECT_001/
│   │   │   │   ├── fMRI.nii.gz
│   │   │   │   └── T1.nii.gz
│   │   │   └── ... (more subjects)
│   │   ├── brain-jepa/                # Brain-JEPA extracted embeddings
│   │   │   ├── SUBJECT_001/
│   │   │   │   └── frame0.pt
│   │   │   └── ... (more subjects)
│   │   ├── brainlm-111m/              # BrainLM 111M extracted embeddings
│   │   ├── brainlm-650m/              # BrainLM 650M extracted embeddings
│   │   ├── swift-v2/                  # SwiFT_v2 extracted embeddings
│   │   ├── metadata/                  # Supporting data files
│   │   │   ├── demographics.csv       # Subject demographics
│   │   │   ├── clinical_labels.csv    # Disease labels (NC/MCI/AD)
│   │   │   ├── split_info.csv         # Train/val/test assignments
│   │   │   └── preprocessing_log.txt  # Data prep documentation
│   │   └── downstream_results/        # Evaluation results
│   │       ├── linear_probing.csv
│   │       ├── fine_tuning.csv
│   │       └── representation_analysis.csv
│   │
│   └── HCP_Aging/                     # Secondary evaluation dataset
│       ├── raw/                       # Original NIfTI files
│       ├── [same structure as ADNI]
│       └── ...
│
├── results/                            # Aggregated benchmark results
├── embeddings/                         # Central embedding storage
└── [other documentation files]
```

### Creation Commands

```bash
# Navigate to project
cd /Users/apple/Desktop/neuro-ai-research-system

# Create dataset directories
mkdir -p .claude/benchmarks/datasets/ADNI/{raw,metadata,downstream_results}
mkdir -p .claude/benchmarks/datasets/ADNI/{brain-jepa,brainlm-111m,brainlm-650m,swift-v2}
mkdir -p .claude/benchmarks/datasets/HCP_Aging/{raw,metadata,downstream_results}
mkdir -p .claude/benchmarks/datasets/HCP_Aging/{brain-jepa,brainlm-111m,brainlm-650m,swift-v2}

# Create results directories
mkdir -p .claude/benchmarks/results/visualizations
mkdir -p .claude/benchmarks/results/statistical_tests

# Verify structure
tree .claude/benchmarks/datasets/
```

---

## Dataset 1: ADNI (Primary Evaluation)

### Dataset Overview

**Purpose**: Alzheimer's Disease classification - primary benchmark evaluation task

**Key Characteristics**:
- **Disease Classes**: NC (Cognitively Normal), MCI (Mild Cognitive Impairment), AD (Alzheimer's Disease)
- **Modality**: Resting-state fMRI
- **Subject Count**: ~800-1000 (varies by preprocessing pipeline)
- **Clinical Relevance**: Both Brain-JEPA and BrainLM evaluated on ADNI
- **Downstream Task**: 3-class disease classification (NC vs MCI vs AD)
- **Data Source**: https://adni.loni.usc.edu/

### Data Access Prerequisites

1. **ADNI Data Access**:
   - Register at https://adni.loni.usc.edu/
   - Request fMRI data access
   - Download preprocessed NIfTI files
   - Location: `/Users/apple/Desktop/neuro-ai-research-system/.claude/benchmarks/datasets/ADNI/raw/`

2. **Alternative: Use Existing Preprocessing**:
   - Brain-JEPA paper uses preprocessed ADNI from Kong et al. pipeline
   - BrainLM uses similar preprocessing
   - May already be available in research group shared storage

### Data Preparation Steps

#### Step 1: Organize Raw NIfTI Files

```bash
# Organize by subject ID (ADNI uses standard naming)
# Original: /path/to/ADNI_data/ADNI_001/...
# Target: .claude/benchmarks/datasets/ADNI/raw/SUBJECT_XXX/fMRI.nii.gz

cd .claude/benchmarks/datasets/ADNI/raw/

# Create subdirectories for each subject
for subject_id in SUBJECT_{001..500}; do
    mkdir -p "$subject_id"
    # Copy preprocessed fMRI (exact path depends on data source)
    # cp /source/path/$subject_id/fMRI.nii.gz "$subject_id/"
done
```

#### Step 2: Collect Subject Metadata

Create `metadata/demographics.csv`:

```csv
subject_id,age,sex,group,site
SUBJECT_001,75,M,NC,ADNI01
SUBJECT_002,68,F,MCI,ADNI02
SUBJECT_003,82,M,AD,ADNI03
...
```

**Required Columns**:
- `subject_id`: Unique subject identifier
- `age`: Subject age at scan
- `sex`: Biological sex (M/F)
- `group`: Clinical group (NC/MCI/AD)
- `site`: ADNI site/center
- `mmse`: Optional MMSE score (cognitive screening)
- `apo_e4`: Optional ApoE4 genotype (risk factor)

**Data Source**: ADNI downloads include demographic files (ADNIMERGE.csv typically)

#### Step 3: Collect Clinical Labels

Create `metadata/clinical_labels.csv`:

```csv
subject_id,diagnosis,diagnosis_confidence,cdr,mmse
SUBJECT_001,CN (Cognitive Normal),1.0,0.0,30
SUBJECT_002,MCI,0.95,0.5,26
SUBJECT_003,AD,0.98,1.0,18
...
```

**Label Definition**:
- NC: MMSE 24-30, no cognitive impairment
- MCI: MMSE 20-26, objective cognitive decline
- AD: MMSE <20, dementia diagnosis

**Data Validation**:
```python
import pandas as pd

labels = pd.read_csv('.claude/benchmarks/datasets/ADNI/metadata/clinical_labels.csv')

# Check label distribution
print(labels['diagnosis'].value_counts())
# Expected: NC ~300, MCI ~400, AD ~200 (approximate)

# Validate MMSE scores align with diagnoses
print(labels.groupby('diagnosis')['mmse'].describe())
```

#### Step 4: Create Train/Val/Test Splits

Create `metadata/split_info.csv`:

```csv
subject_id,split,fold
SUBJECT_001,train,1
SUBJECT_002,train,1
SUBJECT_003,val,1
SUBJECT_004,test,1
...
```

**Stratification Requirements**:
- Stratify by diagnosis (NC/MCI/AD)
- Stratify by site (ADNI center)
- Fixed random seed for reproducibility: `seed=42`
- Split ratio: 70% train / 15% val / 15% test

**Python Implementation**:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load demographics
demographics = pd.read_csv('.claude/benchmarks/datasets/ADNI/metadata/demographics.csv')
labels = pd.read_csv('.claude/benchmarks/datasets/ADNI/metadata/clinical_labels.csv')

# Merge
data = demographics.merge(labels, on='subject_id')

# Stratified split
# First: separate by diagnosis
stratify_col = data['diagnosis']

# Split: 70 train, 15 val, 15 test
train_data, temp_data = train_test_split(
    data, test_size=0.30, stratify=stratify_col, random_state=42
)

val_data, test_data = train_test_split(
    temp_data, test_size=0.50, stratify=temp_data['diagnosis'], random_state=42
)

# Create split info
train_data['split'] = 'train'
val_data['split'] = 'val'
test_data['split'] = 'test'

split_info = pd.concat([train_data, val_data, test_data])
split_info = split_info[['subject_id', 'split', 'diagnosis']]

# Add fold identifier for cross-validation (optional)
split_info['fold'] = 1

# Save
split_info.to_csv('.claude/benchmarks/datasets/ADNI/metadata/split_info.csv', index=False)

print("ADNI Split Summary:")
print(split_info['split'].value_counts())
# Expected: train ~600, val ~150, test ~150
```

**Documentation**:
Create `metadata/preprocessing_log.txt`:

```
ADNI Data Preparation Log
========================

Dataset: Alzheimer's Disease Neuroimaging Initiative (ADNI)
Preparation Date: 2025-10-23
Random Seed: 42

1. RAW DATA
   - Source: ADNI official downloads (Kong et al. preprocessing)
   - fMRI Modality: Resting-state fMRI
   - Total Subjects Initially: [X]
   - Subjects After QC: [Y]

2. PREPROCESSING APPLIED
   - fMRI Parcellation: Schaefer 400 (cortical) + Tian 50 (subcortical) = 450 ROIs
   - Temporal Resolution: Original timepoints
   - Normalization: Robust scaling (median/IQR based on training set)
   - Frame Count: Variable (range: 400-600 timepoints)

3. SPLIT STRATEGY
   - Train: 70% (N=~600)
   - Validation: 15% (N=~150)
   - Test: 15% (N=~150)
   - Stratification: By diagnosis (NC/MCI/AD) and site
   - Reproducibility: Fixed random seed (42)

4. CLASS DISTRIBUTION
   - NC (Cognitively Normal): ~300 subjects
   - MCI (Mild Cognitive Impairment): ~400 subjects
   - AD (Alzheimer's Disease): ~200 subjects
   - Total: ~900 subjects

5. VALIDATION CHECKS
   - ✓ All subjects have valid NIfTI files
   - ✓ All subjects have clinical labels
   - ✓ No overlapping subjects between splits
   - ✓ Balanced class distribution across splits
   - ✓ Site distribution balanced across splits
```

---

## Dataset 2: HCP-Aging (Secondary Evaluation)

### Dataset Overview

**Purpose**: Sex classification on healthy aging population - secondary evaluation task

**Key Characteristics**:
- **Task**: Binary sex classification (M/F)
- **Modality**: Resting-state fMRI
- **Subject Count**: ~1000+ healthy aging adults
- **Age Range**: 36-100 years
- **Clinical Relevance**: Out-of-distribution test (healthy population vs ADNI disease cohort)
- **Data Source**: Human Connectome Project - Lifespan

### Data Access

**Prerequisites**:
- HCP Lifespan Data Agreement
- Download from https://www.humanconnectome.org/study/hcp-lifespan-aging
- Use Wu et al. preprocessing (documented in paper)

### Data Preparation Steps

#### Step 1: Organize Raw Files

```bash
# Similar to ADNI structure
mkdir -p .claude/benchmarks/datasets/HCP_Aging/raw/SUBJECT_{001..1000}

# Copy preprocessed fMRI files
# cp /source/HCP_AGING/$subject_id/fMRI.nii.gz .claude/benchmarks/datasets/HCP_Aging/raw/SUBJECT_$subject_id/
```

#### Step 2: Collect Demographics

Create `metadata/demographics.csv`:

```csv
subject_id,age,sex,group
SUBJECT_001,42,M,healthy
SUBJECT_002,55,F,healthy
SUBJECT_003,78,M,healthy
...
```

**Required Columns**:
- `subject_id`: HCP subject ID
- `age`: Age at scan
- `sex`: Biological sex (M/F)
- `group`: Always "healthy" for this dataset

#### Step 3: Create Splits

Create `metadata/split_info.csv`:

```csv
subject_id,split
SUBJECT_001,train
SUBJECT_002,val
SUBJECT_003,test
...
```

**Split Strategy**:
- Same 70/15/15 ratio
- Stratify by sex (balance M/F in each split)
- Fixed random seed: `seed=42`

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Load HCP demographics
demographics = pd.read_csv('.claude/benchmarks/datasets/HCP_Aging/metadata/demographics.csv')

# Stratified split
train, temp = train_test_split(
    demographics, test_size=0.30, stratify=demographics['sex'], random_state=42
)
val, test = train_test_split(
    temp, test_size=0.50, stratify=temp['sex'], random_state=42
)

# Create split info
train['split'] = 'train'
val['split'] = 'val'
test['split'] = 'test'

split_info = pd.concat([train, val, test])
split_info = split_info[['subject_id', 'split']]

split_info.to_csv('.claude/benchmarks/datasets/HCP_Aging/metadata/split_info.csv', index=False)

print("HCP-Aging Split Summary:")
print(split_info['split'].value_counts())
```

---

## Step 5: Create Master Subject List

**File**: `.claude/benchmarks/metadata/all_subjects.csv`

**Purpose**: Unified reference for all subjects across both datasets

```csv
dataset,subject_id,age,sex,group,split,download_location
ADNI,SUBJECT_001,75,M,NC,train,/path/to/raw/SUBJECT_001/fMRI.nii.gz
ADNI,SUBJECT_002,68,F,MCI,train,/path/to/raw/SUBJECT_002/fMRI.nii.gz
HCP_Aging,SUBJECT_1001,42,M,healthy,val,/path/to/raw/SUBJECT_1001/fMRI.nii.gz
...
```

**Creation Script**:

```python
import pandas as pd

# Load ADNI splits
adni = pd.read_csv('.claude/benchmarks/datasets/ADNI/metadata/split_info.csv')
adni_demo = pd.read_csv('.claude/benchmarks/datasets/ADNI/metadata/demographics.csv')
adni_merged = adni.merge(adni_demo, on='subject_id')
adni_merged['dataset'] = 'ADNI'

# Load HCP-Aging splits
hcp = pd.read_csv('.claude/benchmarks/datasets/HCP_Aging/metadata/split_info.csv')
hcp_demo = pd.read_csv('.claude/benchmarks/datasets/HCP_Aging/metadata/demographics.csv')
hcp_merged = hcp.merge(hcp_demo, on='subject_id')
hcp_merged['dataset'] = 'HCP_Aging'

# Rename ADNI subject IDs to avoid conflicts
adni_merged['subject_id_full'] = 'ADNI_' + adni_merged['subject_id']
hcp_merged['subject_id_full'] = 'HCP_' + hcp_merged['subject_id']

# Combine
all_subjects = pd.concat([adni_merged, hcp_merged])
all_subjects = all_subjects[[
    'dataset', 'subject_id_full', 'age', 'sex', 'group', 'split'
]]

all_subjects.to_csv('.claude/benchmarks/metadata/all_subjects.csv', index=False)

print(f"Total subjects: {len(all_subjects)}")
print(all_subjects['dataset'].value_counts())
print(all_subjects['split'].value_counts())
```

---

## Validation Checklist

### Data Integrity

- [ ] All NIfTI files present and readable
- [ ] All subjects have demographics
- [ ] All subjects have clinical labels (ADNI) or sex labels (HCP)
- [ ] No duplicate subjects between splits
- [ ] No missing values in critical columns

### Split Balance

- [ ] Class distribution balanced across splits
  - ADNI: NC/MCI/AD similar proportions in train/val/test
  - HCP-Aging: M/F similar proportions in train/val/test
- [ ] Site distribution balanced (ADNI)
- [ ] Age distribution similar across splits
- [ ] Sex distribution similar across splits (ADNI)

### Documentation

- [ ] `demographics.csv` complete and validated
- [ ] `clinical_labels.csv` complete (ADNI)
- [ ] `split_info.csv` created with fixed seed documented
- [ ] `preprocessing_log.txt` documents all applied preprocessing
- [ ] `all_subjects.csv` master list created
- [ ] Random seed (42) documented in all files

### Python Validation Script

```python
import pandas as pd
import numpy as np

# Load all metadata
adni_demo = pd.read_csv('.claude/benchmarks/datasets/ADNI/metadata/demographics.csv')
adni_labels = pd.read_csv('.claude/benchmarks/datasets/ADNI/metadata/clinical_labels.csv')
adni_splits = pd.read_csv('.claude/benchmarks/datasets/ADNI/metadata/split_info.csv')

# Merge
adni = adni_demo.merge(adni_labels, on='subject_id').merge(adni_splits, on='subject_id')

print("=== ADNI VALIDATION ===")
print(f"Total subjects: {len(adni)}")
print(f"\nDiagnosis distribution:")
print(adni['diagnosis'].value_counts())
print(f"\nSplit distribution:")
print(adni['split'].value_counts())
print(f"\nClass balance in splits:")
for split in ['train', 'val', 'test']:
    subset = adni[adni['split'] == split]
    print(f"\n{split.upper()}:")
    print(subset['diagnosis'].value_counts(normalize=True))

# HCP-Aging validation
hcp_demo = pd.read_csv('.claude/benchmarks/datasets/HCP_Aging/metadata/demographics.csv')
hcp_splits = pd.read_csv('.claude/benchmarks/datasets/HCP_Aging/metadata/split_info.csv')
hcp = hcp_demo.merge(hcp_splits, on='subject_id')

print("\n=== HCP-AGING VALIDATION ===")
print(f"Total subjects: {len(hcp)}")
print(f"\nSex distribution:")
print(hcp['sex'].value_counts())
print(f"\nSplit distribution:")
print(hcp['split'].value_counts())
print(f"\nSex balance in splits:")
for split in ['train', 'val', 'test']:
    subset = hcp[hcp['split'] == split]
    print(f"\n{split.upper()}:")
    print(subset['sex'].value_counts(normalize=True))
```

---

## Next Steps

Upon completion of Phase 1, you will have:

1. **Organized Dataset Structure**: Ready for embedding extraction
2. **Standardized Metadata**: Demographics, labels, and splits documented
3. **Fixed Random Seed**: Reproducible splits (seed=42)
4. **Validated Data**: Integrity checks passed
5. **Documentation**: Complete preprocessing log

**Timeline**: Phase 1 should take 1-2 days depending on data access

**Proceed To**: Phase 2 - Brain-JEPA Embedding Extraction

---

**Document Version**: 1.0
**Created**: October 23, 2025
**Status**: Ready for Implementation
