# Project Setup & Management Guide

**Date Created**: October 23, 2025
**Status**: ✅ Active Multi-Project Management System

---

## Overview

This guide explains how the neuro-ai-research-system manages multiple independent research projects with separate documentation, vector databases, and workspaces.

## Projects Managed

### 1. SwiFT_v2 (fMRI Foundation Model)

| Property | Details |
|----------|---------|
| **Type** | Efficient 4D Swin Transformer for foundation model pretraining |
| **Code Location** | `/Users/apple/Desktop/SwiFT_v2_perlmutter` |
| **Docs Location** | `projects/SwiFT_v2/docs/` |
| **Database** | `projects/SwiFT_v2/vectordb/memory/research_vectordb.db` |
| **Documents** | 16 research files (~206 KB total) |
| **Status** | ✅ Research Phase |

**Key Documents**:
- `SwiFT_v2_Introduction_Critical_Review_and_Revision.md` - Publication-ready introduction
- `fMRI_Foundation_Models_Comparative_Analysis.md` - Competitive analysis vs BrainLM & Brain-JEPA
- `RESEARCH_SYNTHESIS_fMRI_Foundation_Models.md` - 9-point research roadmap

### 2. BrainVLM (Vision-Language Model)

| Property | Details |
|----------|---------|
| **Type** | Multimodal vision-language model for brain MRI report generation |
| **Code Location** | `/Users/apple/Desktop/BLIP_MRI` |
| **Docs Location** | `projects/BrainVLM/docs/` |
| **Database** | `projects/BrainVLM/vectordb/memory/research_vectordb.db` |
| **Documents** | 2 documentation files (~12 KB total) |
| **Status** | 🔬 Active Development |

**Key Documents**:
- `BrainVLM_Project_Overview.md` - Complete technical documentation
- `BrainVLM_Quick_Reference.md` - Quick start and configuration guide

---

## Directory Structure

```
neuro-ai-research-system/
│
├── projects/                                    ← CENTRAL PROJECT HUB
│   │
│   ├── SwiFT_v2/
│   │   ├── docs/
│   │   │   ├── SwiFT_v2_Introduction_Critical_Review_and_Revision.md
│   │   │   ├── fMRI_Foundation_Models_Comparative_Analysis.md
│   │   │   ├── RESEARCH_SYNTHESIS_fMRI_Foundation_Models.md
│   │   │   ├── SwiFT_v2_Project_Familiarization.md
│   │   │   ├── EXECUTIVE_SUMMARY.md
│   │   │   ├── COMPLETION_REPORT.md
│   │   │   └── [10 more reference documents]
│   │   │
│   │   ├── vectordb/
│   │   │   └── memory/
│   │   │       ├── research_vectordb.db        (284 KB, 16 documents indexed)
│   │   │       ├── research_documents_backup.json
│   │   │       └── VECTORDB_MANIFEST.json
│   │   │
│   │   └── workspace/                           ← Experiments, analysis, results
│   │
│   ├── BrainVLM/
│   │   ├── docs/
│   │   │   ├── BrainVLM_Project_Overview.md
│   │   │   └── BrainVLM_Quick_Reference.md
│   │   │
│   │   ├── vectordb/
│   │   │   └── memory/
│   │   │       └── research_vectordb.db        (44 KB, 2 documents indexed)
│   │   │
│   │   └── workspace/                           ← Experiments, analysis, results
│   │
│   └── PROJECT_SETUP_GUIDE.md                   ← THIS FILE
│
├── PROJECTS_MANAGEMENT.md                       ← Central project overview
├── simple_vectordb.py                           ← Vector database implementation
├── save_to_sqlite_vectordb.py                   ← SwiFT_v2 database populator
├── populate_brainvlm_vectordb.py                ← BrainVLM database populator
├── test_project_databases.py                    ← Test separate databases
│
└── [other root files and configurations]
```

---

## Working with SwiFT_v2

### Accessing SwiFT_v2 Documentation

**Method 1: Direct File Access**
```bash
cat projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md
cat projects/SwiFT_v2/docs/fMRI_Foundation_Models_Comparative_Analysis.md
```

**Method 2: Vector Database Search**
```python
from simple_vectordb import SimpleVectorDB

# Load SwiFT_v2 database
db = SimpleVectorDB("projects/SwiFT_v2/vectordb/memory/research_vectordb.db")

# Search for relevant documents
results = db.search("Swin Transformer fMRI", collection_name="research_documents", limit=5)

for result in results:
    print(f"Match: {result['metadata']['file']}")
    print(f"Content snippet: {result['content'][:200]}...")
```

### Running SwiFT_v2 Code

```bash
# Navigate to SwiFT_v2 code directory
cd /Users/apple/Desktop/SwiFT_v2_perlmutter

# Check the quickstart guide
cat /Users/apple/Desktop/neuro-ai-research-system/projects/SwiFT_v2/docs/SwiFT_v2_Development_Quick_Reference.md
```

### Adding New SwiFT_v2 Documentation

```bash
# 1. Create documentation in SwiFT_v2 docs folder
vim projects/SwiFT_v2/docs/Your_New_Document.md

# 2. Repopulate the vector database
python3 save_to_sqlite_vectordb.py

# 3. Verify new documents are indexed
python3 test_project_databases.py
```

---

## Working with BrainVLM

### Accessing BrainVLM Documentation

**Method 1: Direct File Access**
```bash
cat projects/BrainVLM/docs/BrainVLM_Project_Overview.md
cat projects/BrainVLM/docs/BrainVLM_Quick_Reference.md
```

**Method 2: Vector Database Search**
```python
from simple_vectordb import SimpleVectorDB

# Load BrainVLM database
db = SimpleVectorDB("projects/BrainVLM/vectordb/memory/research_vectordb.db")

# Search for relevant documents
results = db.search("BLIP-2 T5 training", collection_name="brainvlm_documentation", limit=5)

for result in results:
    print(f"Match: {result['metadata']['file']}")
    print(f"Content snippet: {result['content'][:200]}...")
```

### Running BrainVLM Code

```bash
# Navigate to BrainVLM code directory
cd /Users/apple/Desktop/BLIP_MRI

# Quick start with T5 training
python project/main_Bblip_t5_hf_joint.py

# Check configuration
cat /Users/apple/Desktop/neuro-ai-research-system/projects/BrainVLM/docs/BrainVLM_Quick_Reference.md
```

### Adding New BrainVLM Documentation

```bash
# 1. Create documentation in BrainVLM docs folder
vim projects/BrainVLM/docs/Your_New_Document.md

# 2. Repopulate the vector database
python3 populate_brainvlm_vectordb.py

# 3. Verify new documents are indexed
python3 test_project_databases.py
```

---

## Switching Between Projects

### Quick Context Switch

**To SwiFT_v2:**
```bash
# Review project status
cat projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md

# Load project context via vector database
python3 -c "
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/SwiFT_v2/vectordb/memory/research_vectordb.db')
results = db.search('foundation models', collection_name='research_documents', limit=3)
print('Found:', len(results), 'relevant documents')
"
```

**To BrainVLM:**
```bash
# Review project status
cat projects/BrainVLM/docs/BrainVLM_Project_Overview.md

# Load project context via vector database
python3 -c "
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/BrainVLM/vectordb/memory/research_vectordb.db')
results = db.search('vision language', collection_name='brainvlm_documentation', limit=3)
print('Found:', len(results), 'relevant documents')
"
```

---

## Vector Database API Reference

### Creating a Database Instance

```python
from simple_vectordb import SimpleVectorDB

# SwiFT_v2 database
swift_db = SimpleVectorDB("projects/SwiFT_v2/vectordb/memory/research_vectordb.db")

# BrainVLM database
brainvlm_db = SimpleVectorDB("projects/BrainVLM/vectordb/memory/research_vectordb.db")
```

### Searching Documents

```python
# Search SwiFT_v2
results = swift_db.search(
    query="foundation models",
    collection_name="research_documents",
    limit=5
)

# Search BrainVLM
results = brainvlm_db.search(
    query="training optimization",
    collection_name="brainvlm_documentation",
    limit=5
)

# Process results
for result in results:
    print(f"Document: {result['metadata']['file']}")
    print(f"Type: {result['metadata']['type']}")
    print(f"Content: {result['content'][:500]}...")
```

### Adding New Documents

```python
# Add to SwiFT_v2
swift_db.add_document(
    collection_name="research_documents",
    doc_id="new_doc_001",
    content="Your document content here...",
    metadata={
        "file": "New_Document.md",
        "type": "markdown",
        "source": "SwiFT_v2 Research"
    }
)

# Add to BrainVLM
brainvlm_db.add_document(
    collection_name="brainvlm_documentation",
    doc_id="brainvlm_new_001",
    content="Your document content here...",
    metadata={
        "file": "BrainVLM_New_Document.md",
        "type": "markdown",
        "source": "BrainVLM Development"
    }
)
```

### Getting Collection Statistics

```python
# SwiFT_v2 stats
swift_stats = swift_db.get_collection_stats("research_documents")
print(f"Documents: {swift_stats['document_count']}")

# BrainVLM stats
brainvlm_stats = brainvlm_db.get_collection_stats("brainvlm_documentation")
print(f"Documents: {brainvlm_stats['document_count']}")
```

---

## Best Practices

### Document Organization

1. **Save location**: Always save project documents in `projects/{PROJECT}/docs/`
2. **Naming convention**: Use descriptive filenames with underscores
   - ✅ Good: `BrainVLM_Training_Configuration.md`
   - ❌ Bad: `doc1.md`, `notes.txt`
3. **File format**: Use Markdown (.md) for all documentation

### Vector Database Management

1. **Database location**: Keep databases in `projects/{PROJECT}/vectordb/memory/`
2. **Regular updates**: After adding documents, re-run population script
3. **Backups**: JSON backups are created automatically
4. **Collection names**: Use consistent collection names per project
   - SwiFT_v2: `"research_documents"`
   - BrainVLM: `"brainvlm_documentation"`

### Project Independence

1. **Separate workspaces**: Each project has its own `workspace/` folder
2. **Independent tracking**: Each project tracks its own progress
3. **No cross-project dependencies**: Keep projects modular and independent
4. **Clear separation**: Use `projects/` folder as the organizational hub

---

## Example: Complete Workflow

### Scenario: Reviewing BrainVLM Progress

```bash
# 1. Navigate to project management area
cd /Users/apple/Desktop/neuro-ai-research-system

# 2. Check project status
cat projects/BrainVLM/docs/BrainVLM_Project_Overview.md

# 3. Search for specific information
python3 -c "
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/BrainVLM/vectordb/memory/research_vectordb.db')

# Search for training details
results = db.search('training configuration', collection_name='brainvlm_documentation')
print(f'Found {len(results)} documents about training')

# Print relevant sections
for r in results:
    print(f'\\n=== {r[\"metadata\"][\"file\"]} ===')
    print(r['content'][:1000])
"

# 4. Navigate to code directory if needed
cd /Users/apple/Desktop/BLIP_MRI
ls project/config/*.yaml
```

### Scenario: Adding New Documentation

```bash
# 1. Create new document
cat > projects/BrainVLM/docs/BrainVLM_Experiment_Results.md << 'EOF'
# BrainVLM Experiment Results

## Experiment 1: Joint T1 Training
- Dataset: ABCD + UKB
- Results: ...

## Experiment 2: Sequential Training
- Method: ...
- Results: ...
EOF

# 2. Update database
python3 populate_brainvlm_vectordb.py

# 3. Verify
python3 test_project_databases.py
```

---

## FAQ

**Q: Can I have documents in the root level?**
A: No. Always store project documents in `projects/{PROJECT}/docs/` to maintain clean separation.

**Q: How do I backup my vector databases?**
A: Databases are automatically backed up to JSON format. Check `projects/{PROJECT}/vectordb/memory/` for backup files.

**Q: Can I search across both projects at once?**
A: No. Each project has its own database. You must search each database separately and combine results manually.

**Q: How do I delete a document from a project?**
A: Remove the document from `projects/{PROJECT}/docs/` and re-run the population script.

**Q: What if I want to merge projects?**
A: Move documents to a shared folder, create a combined vector database, and update references.

---

## Support

### For SwiFT_v2 Issues
1. Check: `projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md`
2. Search: Vector database for relevant documents
3. Code: `/Users/apple/Desktop/SwiFT_v2_perlmutter`

### For BrainVLM Issues
1. Check: `projects/BrainVLM/docs/BrainVLM_Project_Overview.md`
2. Search: Vector database for relevant documents
3. Code: `/Users/apple/Desktop/BLIP_MRI`

---

**Last Updated**: October 23, 2025
**System Status**: ✅ Ready for Multi-Project Management
