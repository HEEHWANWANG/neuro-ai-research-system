# Benchmark Models - Project Organization

**Purpose**: Manage Brain-JEPA and BrainLM as separate tracked projects for SwiFT_v2 evaluation
**Date**: October 23, 2025
**Status**: Setup Configuration

---

## Project Structure

### Three-Project Ecosystem

```
neuro-ai-research-system/          # Main project (SwiFT_v2)
├── .claude/benchmarks/             # Benchmark management (THIS LOCATION)
│   ├── BENCHMARKS_INDEX.md         # Navigation and quick reference
│   ├── BRAIN_JEPA_ANALYSIS.md      # Brain-JEPA technical analysis
│   ├── BRAINLM_ANALYSIS.md         # BrainLM technical analysis
│   ├── BENCHMARK_COMPARISON_FRAMEWORK.md  # Evaluation protocol
│   ├── PROJECT_ORGANIZATION.md     # This file
│   ├── results/                    # Benchmark evaluation results
│   ├── embeddings/                 # Extracted embeddings
│   └── comparison_metrics.csv      # Aggregated comparison results
│
├── Brain-JEPA/                     # External linked project (embedding extraction)
│   ├── EMBEDDING_EXTRACTION_GUIDE.md    # Extraction protocol
│   ├── downstream_embedding_extraction.py
│   ├── pretrained_models/          # Checkpoint directory
│   └── [original project structure]
│
└── BrainLM/                        # External linked project (embedding extraction)
    ├── README.md                   # Setup and usage
    ├── brainlm_tutorial.ipynb      # Data preprocessing
    ├── inference_*.ipynb           # Downstream tasks
    ├── pretrained_models/          # HuggingFace models
    └── [original project structure]
```

---

## Project Linking Strategy

### Why Separate Projects?

1. **Code Isolation**: Each project has its own dependencies, configs, Git history
2. **Reproducibility**: Maintain original project structures with minimal modification
3. **Comparison Clarity**: Easy to run both models on same data in parallel
4. **Manuscript Organization**: Clear separation for "benchmark models" section in paper

### External Project References

The two benchmark models are maintained as **external projects** linked via:

1. **Symbolic Links** (Development)
   ```bash
   ln -s /Users/apple/Desktop/Brain-JEPA ./Brain-JEPA
   ln -s /Users/apple/Desktop/BrainLM ./BrainLM
   ```

2. **Git Submodules** (If version control needed)
   ```bash
   git submodule add /Users/apple/Desktop/Brain-JEPA Brain-JEPA
   git submodule add /Users/apple/Desktop/BrainLM BrainLM
   ```

3. **Documentation Cross-References** (Current approach)
   - Links in BENCHMARKS_INDEX.md to external locations
   - Documented paths in analysis documents
   - Relative path examples in framework

---

## Organization Layers

### Layer 1: Documentation & Analysis (`.claude/benchmarks/`)

**Purpose**: Central knowledge base for benchmark model understanding and comparison

**Contents**:
- `BENCHMARKS_INDEX.md` - Master navigation and quick reference
- `BRAIN_JEPA_ANALYSIS.md` - 12-section technical deep-dive
- `BRAINLM_ANALYSIS.md` - 15-section technical deep-dive
- `BENCHMARK_COMPARISON_FRAMEWORK.md` - 10-section evaluation protocol
- `PROJECT_ORGANIZATION.md` - This file, project structure and workflow

**Access Pattern**:
```
Research Question → BENCHMARKS_INDEX (quick lookup)
                 → Specific Analysis Doc (detailed understanding)
                 → Comparison Framework (evaluation design)
```

### Layer 2: Code Repositories (External)

**Brain-JEPA Location**: `/Users/apple/Desktop/Brain-JEPA`
**BrainLM Location**: `/Users/apple/Desktop/BrainLM`

**Purpose**: Production code for embedding extraction and model inference

**Key Files**:
- Brain-JEPA: `downstream_embedding_extraction.py` (main entry point)
- BrainLM: `brainlm_tutorial.ipynb` + inference notebooks (entry points)

**Access Pattern**:
```
Need Embeddings → EMBEDDING_EXTRACTION_GUIDE (Brain-JEPA)
              or → brainlm_tutorial.ipynb (BrainLM)
              → Run extraction script on datasets
              → Store embeddings in .claude/benchmarks/embeddings/
```

### Layer 3: Results & Artifacts (`.claude/benchmarks/`)

**Purpose**: Centralized storage for benchmark evaluation outputs

**Subdirectories**:
```
results/
├── adni_comparison.csv             # ADNI disease classification results
├── hcp_aging_comparison.csv        # HCP-Aging sex classification results
├── efficiency_metrics.csv          # Model efficiency comparison
├── visualizations/                 # Plots and figures
│   ├── performance_comparison.png
│   ├── efficiency_tradeoff.png
│   ├── representation_analysis.png
│   └── correlation_matrices.png
└── statistical_tests/              # Statistical analysis results
    ├── significance_tests.csv
    └── effect_sizes.csv

embeddings/
├── brain-jepa/                     # Brain-JEPA extracted embeddings
│   ├── adni/
│   │   ├── SUBJECT_001_embedding.pt
│   │   ├── SUBJECT_002_embedding.pt
│   │   └── ...
│   └── hcp_aging/
├── brainlm-111m/                   # BrainLM 111M variant embeddings
│   ├── adni/
│   └── hcp_aging/
├── brainlm-650m/                   # BrainLM 650M variant embeddings
│   ├── adni/
│   └── hcp_aging/
└── swift-v2/                       # SwiFT_v2 embeddings (when ready)
    ├── adni/
    └── hcp_aging/
```

---

## Workflow Integration

### Phase 1: Setup & Data Preparation (1-2 days)

**Action Items**:
1. Create benchmark dataset directory structure
2. Download/link ADNI data (clinical labels, subject info)
3. Prepare HCP-Aging data (sex labels, demographics)
4. Create standardized train/val/test splits (fixed random seed)
5. Document data preprocessing applied

**Checklist**:
- [ ] Dataset directories created
- [ ] Metadata files collected (demographics, clinical scores)
- [ ] Labels and split assignments prepared
- [ ] Data validation completed

---

### Phase 2: Brain-JEPA Evaluation (2-3 days)

**Entry Point**: `/Users/apple/Desktop/Brain-JEPA/downstream_embedding_extraction.py`

**Steps**:
1. Load pretrained Brain-JEPA checkpoint
2. Extract embeddings on ADNI and HCP-Aging
3. Save to `.claude/benchmarks/embeddings/brain-jepa/`
4. Run linear probing on both datasets
5. Run fine-tuning evaluation
6. Compute representation metrics
7. Save results to `.claude/benchmarks/results/`

**Command Template**:
```bash
cd /Users/apple/Desktop/Brain-JEPA

python downstream_embedding_extraction.py \
    --data_make_fn external_dataset \
    --dataset_name ADNI \
    --output_root /Users/apple/Desktop/neuro-ai-research-system/.claude/benchmarks \
    --load_path ./pretrained_models/checkpoint.pth \
    --batch_size 4 \
    --downsample \
    --crop_size 450,160 \
    --patch_size 16
```

**Checklist**:
- [ ] Checkpoint downloaded and verified
- [ ] ADNI embeddings extracted
- [ ] HCP-Aging embeddings extracted
- [ ] Linear probing completed
- [ ] Fine-tuning completed
- [ ] Results saved to benchmarks/results/

---

### Phase 3: BrainLM Evaluation (2-3 days)

**Entry Points**:
- Data prep: `/Users/apple/Desktop/BrainLM/brainlm_tutorial.ipynb`
- Evaluation: `/Users/apple/Desktop/BrainLM/inference_*.ipynb`

**Steps**:
1. Load BrainLM 111M from HuggingFace
2. Extract embeddings on ADNI and HCP-Aging
3. Save to `.claude/benchmarks/embeddings/brainlm-111m/`
4. Repeat for BrainLM 650M variant
5. Run all downstream tasks (linear probing, fine-tuning, KNN)
6. Compute representation metrics
7. Save results to `.claude/benchmarks/results/`

**Command Template**:
```python
from transformers import AutoModel

# Load BrainLM 111M
model_111m = AutoModel.from_pretrained("vandijklab/brainlm-111m")

# Load BrainLM 650M
model_650m = AutoModel.from_pretrained("vandijklab/brainlm-650m")

# Extract embeddings (use inference notebooks as template)
# Save to .claude/benchmarks/embeddings/
```

**Checklist**:
- [ ] BrainLM 111M loaded from HuggingFace
- [ ] BrainLM 650M loaded from HuggingFace
- [ ] ADNI embeddings extracted (both variants)
- [ ] HCP-Aging embeddings extracted (both variants)
- [ ] Linear probing completed
- [ ] Fine-tuning completed
- [ ] KNN evaluation completed
- [ ] Results saved to benchmarks/results/

---

### Phase 4: SwiFT_v2 Evaluation (1-2 days)

**When**: After SwiFT_v2 model is finalized

**Steps**:
1. Extract embeddings from SwiFT_v2 on same datasets
2. Save to `.claude/benchmarks/embeddings/swift-v2/`
3. Run identical downstream tasks
4. Compute same representation metrics

**Consistency Requirements**:
- Same data preprocessing as Brain-JEPA and BrainLM
- Same train/val/test splits
- Same hyperparameters for downstream tasks
- Same evaluation metrics

---

### Phase 5: Analysis & Comparison (2-3 days)

**Action Items**:
1. Load all embeddings (Brain-JEPA, BrainLM-111M, BrainLM-650M, SwiFT_v2)
2. Compile results into comparison table
3. Perform statistical significance testing
4. Generate visualization plots
5. Analyze computational efficiency
6. Analyze representation quality
7. Write comprehensive comparison section

**Outputs**:
- Comparison metrics table (CSV)
- Performance comparison plots (PNG)
- Efficiency tradeoff plots (PNG)
- Representation analysis plots (PNG)
- Statistical test results (CSV)
- Comprehensive results report (MD)

---

### Phase 6: Paper Integration (1-2 days)

**Action Items**:
1. Create benchmark results section for manuscript
2. Generate publication-quality figures
3. Write interpretation and discussion
4. Cite related work appropriately
5. Create supplementary materials

**Outputs**:
- Benchmark results section (manuscript-ready)
- Figure files (publication quality)
- Supplementary tables and analysis (PDF)
- Extended methods section (detailed)

---

## Access Patterns

### Quick Reference
```
How do I find [X]?

Architecture of Brain-JEPA?
→ BENCHMARKS_INDEX.md (Quick Reference) → BRAIN_JEPA_ANALYSIS.md (Section 3)

Embedding extraction protocol?
→ BENCHMARKS_INDEX.md (Project Code Locations) → Brain-JEPA/EMBEDDING_EXTRACTION_GUIDE.md

Evaluation framework?
→ BENCHMARK_COMPARISON_FRAMEWORK.md (Full framework)

Expected paper section structure?
→ BENCHMARK_COMPARISON_FRAMEWORK.md (Section 8: Manuscript Integration)

Where are results stored?
→ .claude/benchmarks/results/ (directory)

Where are embeddings stored?
→ .claude/benchmarks/embeddings/ (directory)
```

### Data Flow
```
Raw Data (ADNI, HCP-Aging)
  ↓
[Brain-JEPA Extraction] → embeddings/brain-jepa/
  ↓
[Downstream Evaluation] → results/
  ↓
[Analysis & Comparison] → results/ (updated)
  ↓
[Manuscript Generation] → Paper section
```

---

## Key Decision Points

### 1. Embedding Storage Format
- **Decision**: PyTorch tensors (.pt files) per subject
- **Reason**: Same format as original extraction scripts, preserves temporal dimension
- **Alternative**: NumPy arrays (.npy) for language-agnostic access

### 2. Results Organization
- **Decision**: Separate CSV files per evaluation task
- **Reason**: Easy parsing, tabulation, and statistical analysis
- **Alternative**: Single HDF5 file with hierarchical structure

### 3. Evaluation Dataset Priority
- **Decision**: ADNI (primary) → HCP-Aging (secondary)
- **Reason**: Both models have evaluated on ADNI, allows direct comparison
- **Alternative**: Add custom SwiFT_v2 internal dataset as tertiary

### 4. External Project Linking
- **Decision**: Documentation-based cross-references
- **Reason**: Preserves original project independence, facilitates updates
- **Alternative**: Git submodules for version control integration

---

## Session Management

### Save Checkpoints
```
After each phase completion:
1. Save results to .claude/benchmarks/results/
2. Document progress in checkpoint file
3. Update TODO tracking in session memory
4. Commit progress to git
```

### Parallel Execution
```
Parallel opportunities:
- Brain-JEPA and BrainLM evaluations can run on different hardware
- Downstream task evaluation (linear probing, fine-tuning, KNN) can be parallelized
- Results collection and analysis can overlap with evaluation

Sequential requirements:
- Data preparation must complete before any model evaluation
- Embedding extraction must complete before downstream task evaluation
- All evaluations must complete before comparison analysis
```

---

## Success Criteria

### Phase 1: Setup ✅
- [x] Directory structure created
- [ ] ADNI data prepared and validated
- [ ] HCP-Aging data prepared and validated
- [ ] Train/val/test splits created (fixed seed documented)

### Phase 2: Brain-JEPA ✅
- [ ] Embeddings extracted from ADNI
- [ ] Embeddings extracted from HCP-Aging
- [ ] Linear probing results obtained
- [ ] Fine-tuning results obtained
- [ ] Representation analysis completed

### Phase 3: BrainLM ✅
- [ ] 111M embeddings extracted (ADNI + HCP-Aging)
- [ ] 650M embeddings extracted (ADNI + HCP-Aging)
- [ ] All downstream tasks evaluated
- [ ] Efficiency metrics computed

### Phase 4: SwiFT_v2 ✅
- [ ] Embeddings extracted (same data/protocol)
- [ ] All downstream tasks evaluated
- [ ] Results comparable with other models

### Phase 5: Analysis ✅
- [ ] Comparison metrics compiled
- [ ] Statistical testing performed
- [ ] Visualizations generated
- [ ] Analysis report written

### Phase 6: Paper Integration ✅
- [ ] Benchmark section written
- [ ] Results figures created
- [ ] Supplementary materials prepared
- [ ] Citations formatted

---

## References

### External Project Documentation
- Brain-JEPA Embedding Extraction Guide: `/Users/apple/Desktop/Brain-JEPA/EMBEDDING_EXTRACTION_GUIDE.md`
- BrainLM Tutorial: `/Users/apple/Desktop/BrainLM/brainlm_tutorial.ipynb`
- BrainLM Inference Examples: `/Users/apple/Desktop/BrainLM/inference_*.ipynb`

### Benchmark Documentation (This Project)
- BENCHMARKS_INDEX.md - Master navigation
- BRAIN_JEPA_ANALYSIS.md - Brain-JEPA deep-dive
- BRAINLM_ANALYSIS.md - BrainLM deep-dive
- BENCHMARK_COMPARISON_FRAMEWORK.md - Evaluation protocol

---

**Document Version**: 1.0
**Created**: October 23, 2025
**Status**: Setup Configuration Ready
**Next Action**: Proceed with Phase 1 (Data Preparation)
