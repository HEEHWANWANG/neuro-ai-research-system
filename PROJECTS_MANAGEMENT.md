# Research Projects Management System

**Central Hub for Managing Multiple AI+Neuroscience Research Projects**

---

## 📋 Projects Overview

This research system manages multiple independent but related projects:

### Project 1: SwiFT v2 (fMRI Foundation Model)

**Description**: Efficient 4D Swin Transformer for foundation model pretraining on fMRI data

| Property | Value |
|----------|-------|
| **Status** | ✅ Active Research |
| **Primary Focus** | Self-supervised fMRI representation learning |
| **Architecture** | 4D Swin Transformer with temporal-spatial asymmetry |
| **Key Datasets** | 100K+ subjects from UKB, ABCD, HCP |
| **Code Location** | `/Users/apple/Desktop/SwiFT_v2_perlmutter` |
| **Project Folder** | `projects/SwiFT_v2/` |
| **Repository** | https://github.com/HEEHWANWANG/neuro-ai-research-system |

**Key Deliverables**:
- Publication-ready introduction (27.8 KB)
- Competitive analysis vs BrainLM & Brain-JEPA
- Strategic roadmap with 9 research directions
- SQLite vector database (16 documents, 206 KB)

**Contact**: hwang@snu.ac.kr | Paper: https://arxiv.org/pdf/2307.05916

---

### Project 2: BrainVLM (Vision Language Model)

**Description**: Multimodal vision-language model for medical report generation from brain MRI

| Property | Value |
|----------|-------|
| **Status** | 🔬 Active Development |
| **Primary Focus** | Medical report generation from T1/rsfMRI |
| **Architecture** | BLIP-2 + T5 encoder for 3D brain imaging |
| **Key Datasets** | ABCD, UK Biobank |
| **Code Location** | `/Users/apple/Desktop/BLIP_MRI` |
| **Project Folder** | `projects/BrainVLM/` |
| **Code Size** | ~1,256 lines Python |

**Key Features**:
- Multi-modal learning (T1-weighted + rsfMRI)
- Multi-dataset training (ABCD + UKB)
- Vision-language medical report generation
- Scalable training with DeepSpeed

**Contact**: hwang@snu.ac.kr

---

## 📁 Project Folder Structure

```
neuro-ai-research-system/
│
├── projects/                          ← CENTRAL PROJECT MANAGEMENT
│   │
│   ├── SwiFT_v2/                      ← Project 1: fMRI Foundation Model
│   │   ├── docs/                      ← All SwiFT_v2 documentation
│   │   │   ├── COMPLETION_REPORT.md
│   │   │   ├── EXECUTIVE_SUMMARY.md
│   │   │   ├── SwiFT_Paper_Summary.md
│   │   │   ├── fMRI_Foundation_Models_Comparative_Analysis.md
│   │   │   ├── RESEARCH_SYNTHESIS_fMRI_Foundation_Models.md
│   │   │   └── [11 more documents]
│   │   │
│   │   ├── vectordb/                  ← SwiFT_v2 Vector Database
│   │   │   ├── memory/
│   │   │   │   ├── research_vectordb.db           (284 KB)
│   │   │   │   ├── research_documents_backup.json (221 KB)
│   │   │   │   └── VECTORDB_MANIFEST.json
│   │   │   └── [other metadata files]
│   │   │
│   │   └── workspace/                 ← SwiFT_v2 Workspace
│   │       └── [experiments, analysis, results]
│   │
│   └── BrainVLM/                      ← Project 2: Vision Language Model
│       ├── docs/                      ← All BrainVLM documentation
│       │   ├── BrainVLM_Project_Overview.md
│       │   ├── BrainVLM_Quick_Reference.md
│       │   ├── BrainVLM_Architecture.md
│       │   └── [more documentation]
│       │
│       ├── vectordb/                  ← BrainVLM Vector Database
│       │   ├── memory/
│       │   │   ├── research_vectordb.db
│       │   │   └── [manifest files]
│       │   └── [metadata]
│       │
│       └── workspace/                 ← BrainVLM Workspace
│           └── [experiments, analysis, results]
│
├── PROJECTS_MANAGEMENT.md             ← THIS FILE
├── PROJECT_SELECTOR.md                ← Quick project selection guide
│
└── [other root files]
```

---

## 🎯 How to Switch Between Projects

### Quick Selection

```bash
# Select SwiFT_v2
cat projects/SwiFT_v2/docs/BrainVLM_Project_Overview.md

# Select BrainVLM
cat projects/BrainVLM/docs/BrainVLM_Quick_Reference.md
```

### Load Project Context

**For SwiFT_v2:**
```python
from simple_vectordb import SimpleVectorDB

# Load SwiFT_v2 vector database
db = SimpleVectorDB("projects/SwiFT_v2/vectordb/memory/research_vectordb.db")

# Search for research documents
results = db.search("foundation models")
```

**For BrainVLM:**
```python
# Load BrainVLM vector database (when created)
db = SimpleVectorDB("projects/BrainVLM/vectordb/memory/research_vectordb.db")

# Search project documentation
results = db.search("vision language model")
```

---

## 📊 Project Comparison

| Aspect | SwiFT_v2 | BrainVLM |
|--------|----------|----------|
| **Type** | Foundation Model | Vision-Language Model |
| **Primary Input** | fMRI (4D temporal-spatial) | MRI (3D + 4D) |
| **Learning Approach** | Self-supervised (SimMIM) | Supervised vision-language |
| **Base Architecture** | 4D Swin Transformer | BLIP-2 + T5 |
| **Key Datasets** | UKB, ABCD, HCP | ABCD, UKB |
| **Status** | Research (pre-training) | Development (training) |
| **Main Output** | Learned representations | Medical reports |
| **Compute** | 3-5 days (8-16 A100s) | Scaling (4x A100+) |
| **Documentation** | 16 documents (206 KB) | Expanding |

---

## 🔄 Workflow: Working with Multiple Projects

### Scenario 1: Switching Focus from SwiFT_v2 to BrainVLM

```bash
# 1. Review SwiFT_v2 state
cat projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md

# 2. Switch to BrainVLM
cd /Users/apple/Desktop/BLIP_MRI
cat projects/BrainVLM/docs/BrainVLM_Project_Overview.md

# 3. Load BrainVLM context
python -c "
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/BrainVLM/vectordb/memory/research_vectordb.db')
# ... search and access documentation
"
```

### Scenario 2: Comparing Approaches

```bash
# SwiFT_v2 approach (efficient, self-supervised)
cat projects/SwiFT_v2/docs/RESEARCH_SYNTHESIS_fMRI_Foundation_Models.md

# BrainVLM approach (multimodal, vision-language)
cat projects/BrainVLM/docs/BrainVLM_Project_Overview.md

# Comparison analysis (to be created)
cat projects/COMPARATIVE_ANALYSIS.md
```

### Scenario 3: Finding Documentation

**SwiFT_v2 Key Files**:
- `projects/SwiFT_v2/docs/SwiFT_Paper_Summary.md` - Theoretical foundations
- `projects/SwiFT_v2/docs/fMRI_Foundation_Models_Comparative_Analysis.md` - Competition
- `projects/SwiFT_v2/vectordb/memory/research_vectordb.db` - Full database

**BrainVLM Key Files**:
- `projects/BrainVLM/docs/BrainVLM_Project_Overview.md` - Complete overview
- `projects/BrainVLM/docs/BrainVLM_Quick_Reference.md` - Quick start
- `projects/BrainVLM/vectordb/memory/research_vectordb.db` - (to be created)

---

## 🗂️ Document Organization

### SwiFT_v2 Documents (16 total)

**Core Research** (3 documents):
- Comparative analysis
- Research synthesis & roadmap
- Introduction critical review

**Project Docs** (13 documents):
- Project familiarization
- Quick reference guides
- Completion reports
- Session summaries

**Vector Database**:
- Full-text searchable
- 206 KB of content
- 16 documents indexed

### BrainVLM Documents (2+ growing)

**Core Documentation** (2 documents):
- Project overview
- Quick reference

**To Create**:
- Architecture details
- Dataset documentation
- Training guides
- Experiment logs

**Vector Database** (to be created):
- Will contain all BrainVLM documentation
- Full-text searchable
- Per-project storage

---

## 📚 Documentation Best Practices

### When Adding Docs to SwiFT_v2
1. Save to: `projects/SwiFT_v2/docs/`
2. Update vector database: `projects/SwiFT_v2/vectordb/memory/research_vectordb.db`
3. Update index: `projects/SwiFT_v2/docs/INDEX.md`

### When Adding Docs to BrainVLM
1. Save to: `projects/BrainVLM/docs/`
2. Update vector database: `projects/BrainVLM/vectordb/memory/research_vectordb.db`
3. Update index: `projects/BrainVLM/docs/INDEX.md`

### File Naming Convention
```
projects/{PROJECT}/docs/{TOPIC}_{DESCRIPTION}.md
```

Examples:
- `projects/SwiFT_v2/docs/fMRI_Foundation_Models_Comparative_Analysis.md`
- `projects/BrainVLM/docs/BrainVLM_Project_Overview.md`

---

## 🔍 Finding Information Across Projects

### Method 1: Direct File Access
```bash
# SwiFT_v2 research
ls projects/SwiFT_v2/docs/ | grep -i "synthesis\|analysis"

# BrainVLM architecture
ls projects/BrainVLM/docs/ | grep -i "architecture\|overview"
```

### Method 2: Vector Database Search

**SwiFT_v2**:
```python
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB("projects/SwiFT_v2/vectordb/memory/research_vectordb.db")
results = db.search("foundation models Brain-JEPA")
```

**BrainVLM** (when ready):
```python
db = SimpleVectorDB("projects/BrainVLM/vectordb/memory/research_vectordb.db")
results = db.search("vision language BLIP T5")
```

### Method 3: Project-Specific Indexes
```bash
cat projects/SwiFT_v2/docs/INDEX.md     # SwiFT_v2 doc index
cat projects/BrainVLM/docs/INDEX.md     # BrainVLM doc index
```

---

## 🚀 Future Projects

### Planned Integration
- **Brain-JEPA** (Self-supervised representation learning)
- **Other Neuroimaging Models** (as needed)

### Multi-Project Workflows
1. **Comparative Analysis** - Compare all projects
2. **Ensemble Approaches** - Combine strengths
3. **Meta-Learning** - Learn across projects
4. **Cross-Modal Learning** - Link different modalities

---

## 📋 Project Management Checklist

### SwiFT_v2
- ✅ Project familiarization completed
- ✅ Competitive analysis done
- ✅ Publication-ready introduction created
- ✅ Vector database populated (16 docs)
- ✅ GitHub repository created
- ⏳ Implementation of improvements (JEPA pretraining)
- ⏳ Experimental results validation

### BrainVLM
- ✅ Project familiarization started
- ✅ Initial documentation created
- ⏳ Vector database setup
- ⏳ Code review and refactoring
- ⏳ GitHub repository creation
- ⏳ Training documentation
- ⏳ Experiment tracking setup

---

## 🔗 Quick Links

### SwiFT_v2
- **Code**: `/Users/apple/Desktop/SwiFT_v2_perlmutter`
- **Docs**: `projects/SwiFT_v2/docs/`
- **Database**: `projects/SwiFT_v2/vectordb/memory/research_vectordb.db`
- **GitHub**: https://github.com/HEEHWANWANG/neuro-ai-research-system

### BrainVLM
- **Code**: `/Users/apple/Desktop/BLIP_MRI`
- **Docs**: `projects/BrainVLM/docs/`
- **Database**: `projects/BrainVLM/vectordb/memory/research_vectordb.db` (TBD)
- **GitHub**: TBD

---

## 📞 Getting Help

### For SwiFT_v2
1. Check: `projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md`
2. Search: Vector database
3. Ask: claude with "SwiFT_v2" context

### For BrainVLM
1. Check: `projects/BrainVLM/docs/BrainVLM_Project_Overview.md`
2. Read: `projects/BrainVLM/docs/BrainVLM_Quick_Reference.md`
3. Ask: claude with "BrainVLM" context

---

## 📈 Status Dashboard

| Project | Status | Progress | Last Updated |
|---------|--------|----------|--------------|
| SwiFT_v2 | ✅ Research | 60% | Oct 23, 2025 |
| BrainVLM | 🔬 Dev | 20% | Oct 23, 2025 |
| Brain-JEPA | 📋 Planning | 0% | - |

---

**Central Management Hub Created**: October 23, 2025
**Projects Managed**: 2 (SwiFT_v2, BrainVLM)
**Status**: ✅ Ready for Multi-Project Management
