# Multi-Project Research System - Quick Start

**Status**: ✅ All projects operational with separate management
**Last Updated**: October 23, 2025

---

## Quick Access

### 📖 Read These First

1. **[PROJECTS_MANAGEMENT.md](./PROJECTS_MANAGEMENT.md)** - Central hub for all projects
   - Project overview and comparison
   - How to switch between projects
   - Quick links to resources

2. **[PROJECT_SETUP_GUIDE.md](./projects/PROJECT_SETUP_GUIDE.md)** - Comprehensive setup guide
   - Detailed directory structure
   - Working with each project
   - Vector database API reference
   - Best practices and examples

3. **[MULTI_PROJECT_SETUP_COMPLETE.md](./MULTI_PROJECT_SETUP_COMPLETE.md)** - Completion report
   - All deliverables
   - Key statistics
   - Verification checklist

---

## Project Links

### SwiFT_v2 (fMRI Foundation Model)

**Code**: `/Users/apple/Desktop/SwiFT_v2_perlmutter`

**Documentation**:
- Executive Summary: `projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md`
- Competitive Analysis: `projects/SwiFT_v2/docs/fMRI_Foundation_Models_Comparative_Analysis.md`
- Research Roadmap: `projects/SwiFT_v2/docs/RESEARCH_SYNTHESIS_fMRI_Foundation_Models.md`
- Quick Reference: `projects/SwiFT_v2/docs/SwiFT_v2_Development_Quick_Reference.md`

**Vector Database**:
```
Location: projects/SwiFT_v2/vectordb/memory/research_vectordb.db
Size: 284 KB
Documents: 16
Collection: "research_documents"
```

**Search Example**:
```bash
python3 -c "
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/SwiFT_v2/vectordb/memory/research_vectordb.db')
results = db.search('foundation models', collection_name='research_documents')
for r in results:
    print(f'{r[\"metadata\"][\"file\"]}: {r[\"content\"][:200]}...')
"
```

---

### BrainVLM (Vision-Language Model)

**Code**: `/Users/apple/Desktop/BLIP_MRI`

**Documentation**:
- Project Overview: `projects/BrainVLM/docs/BrainVLM_Project_Overview.md`
- Quick Reference: `projects/BrainVLM/docs/BrainVLM_Quick_Reference.md`

**Vector Database**:
```
Location: projects/BrainVLM/vectordb/memory/research_vectordb.db
Size: 44 KB
Documents: 2
Collection: "brainvlm_documentation"
```

**Search Example**:
```bash
python3 -c "
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/BrainVLM/vectordb/memory/research_vectordb.db')
results = db.search('BLIP-2 training', collection_name='brainvlm_documentation')
for r in results:
    print(f'{r[\"metadata\"][\"file\"]}: {r[\"content\"][:200]}...')
"
```

---

## Key Files

### Project Management
```
├── PROJECTS_MANAGEMENT.md          ← Central hub for both projects
├── PROJECT_SETUP_GUIDE.md          ← Comprehensive setup & usage guide
├── MULTI_PROJECT_SETUP_COMPLETE.md ← Completion report with statistics
└── README_MULTI_PROJECT.md         ← This file
```

### Utility Scripts
```
├── simple_vectordb.py              ← Core vector database implementation
├── populate_brainvlm_vectordb.py   ← BrainVLM database populator
├── save_to_sqlite_vectordb.py      ← SwiFT_v2 database populator
└── test_project_databases.py       ← Validation & testing script
```

### Project Directories
```
projects/
├── SwiFT_v2/
│   ├── docs/                       ← 12 markdown documentation files
│   ├── vectordb/memory/            ← 284 KB SQLite database
│   └── workspace/                  ← Experiments & analysis
│
├── BrainVLM/
│   ├── docs/                       ← 2 markdown documentation files
│   ├── vectordb/memory/            ← 44 KB SQLite database
│   └── workspace/                  ← Experiments & analysis
│
└── PROJECT_SETUP_GUIDE.md          ← Comprehensive usage guide
```

---

## Common Tasks

### 1. Search SwiFT_v2 Documentation

```bash
python3 -c "
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/SwiFT_v2/vectordb/memory/research_vectordb.db')
results = db.search('Brain-JEPA', collection_name='research_documents', limit=5)
print(f'Found {len(results)} results for \"Brain-JEPA\"')
"
```

### 2. Search BrainVLM Documentation

```bash
python3 -c "
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/BrainVLM/vectordb/memory/research_vectordb.db')
results = db.search('training', collection_name='brainvlm_documentation', limit=5)
print(f'Found {len(results)} results for \"training\"')
"
```

### 3. View Project Status

```bash
# SwiFT_v2
cat projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md

# BrainVLM
cat projects/BrainVLM/docs/BrainVLM_Project_Overview.md
```

### 4. Add New Documentation to SwiFT_v2

```bash
# 1. Create document
cat > projects/SwiFT_v2/docs/New_Document.md << 'EOF'
# Your Document Title
Content here...
EOF

# 2. Update database
python3 save_to_sqlite_vectordb.py

# 3. Verify
python3 test_project_databases.py
```

### 4. Add New Documentation to BrainVLM

```bash
# 1. Create document
cat > projects/BrainVLM/docs/New_Document.md << 'EOF'
# Your Document Title
Content here...
EOF

# 2. Update database
python3 populate_brainvlm_vectordb.py

# 3. Verify
python3 test_project_databases.py
```

### 5. Run Validation Tests

```bash
python3 test_project_databases.py
```

This will:
- Verify both databases are functional
- Test search on sample queries
- Display statistics for each project
- Provide usage examples

---

## Project Comparison

| Feature | SwiFT_v2 | BrainVLM |
|---------|----------|----------|
| **Type** | Foundation Model | Vision-Language Model |
| **Input** | fMRI (4D) | MRI (3D+4D) |
| **Architecture** | 4D Swin Transformer | BLIP-2 + T5 |
| **Status** | 🔬 Research | 🔬 Development |
| **Docs** | 12 files, 192 KB | 2 files, 16 KB |
| **Database** | 284 KB, 16 docs | 44 KB, 2 docs |
| **Code Dir** | `SwiFT_v2_perlmutter` | `BLIP_MRI` |

---

## Getting Help

### For SwiFT_v2
1. Start with: `projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md`
2. Deep dive: `projects/SwiFT_v2/docs/SwiFT_v2_Project_Familiarization.md`
3. Search: Use vector database for specific queries
4. Code: `/Users/apple/Desktop/SwiFT_v2_perlmutter`

### For BrainVLM
1. Start with: `projects/BrainVLM/docs/BrainVLM_Project_Overview.md`
2. Quick ref: `projects/BrainVLM/docs/BrainVLM_Quick_Reference.md`
3. Search: Use vector database for specific queries
4. Code: `/Users/apple/Desktop/BLIP_MRI`

### For System Questions
1. Central hub: `PROJECTS_MANAGEMENT.md`
2. Setup guide: `PROJECT_SETUP_GUIDE.md`
3. Completion: `MULTI_PROJECT_SETUP_COMPLETE.md`

---

## System Architecture

### Database Technology
- **SQLite 3** for persistence (no external dependencies)
- **Full-text keyword search** for fast retrieval
- **JSON metadata** for document tracking
- **Automatic backup** to JSON format

### Project Organization
- **Independent databases**: Each project has separate SQLite database
- **Isolated workspaces**: Each project has `workspace/` folder
- **Clear separation**: No cross-project dependencies
- **Scalable design**: Easy to add new projects

### Key Features
✅ Separate documentation folders per project
✅ Project-specific vector databases
✅ Full-text search capability
✅ Zero external dependencies
✅ Easy to backup and restore
✅ Simple Python API for searching
✅ Comprehensive documentation
✅ Validation and testing scripts

---

## Quick Statistics

**Total Documentation**: 14 files, 208 KB
- SwiFT_v2: 12 files (192 KB)
- BrainVLM: 2 files (16 KB)

**Vector Databases**: 328 KB total
- SwiFT_v2: 284 KB (16 documents)
- BrainVLM: 44 KB (2 documents)

**Documentation Files**:
- Main guides: 3 files
- SwiFT_v2: 12 files
- BrainVLM: 2 files

**Utility Scripts**: 3 Python scripts
- Database implementation
- BrainVLM populator
- Validation & testing

---

## Next Steps

### Immediate
- [ ] Review `PROJECTS_MANAGEMENT.md` for project overview
- [ ] Read `PROJECT_SETUP_GUIDE.md` for detailed instructions
- [ ] Run `test_project_databases.py` to verify setup

### Short-term
- [ ] Create BrainVLM GitHub repository
- [ ] Add more BrainVLM documentation as experiments run
- [ ] Create documentation indexes for both projects

### Medium-term
- [ ] Establish experiment tracking system
- [ ] Create collaborative workflows
- [ ] Set up backup and archival procedures

### Long-term
- [ ] Expand to additional projects (Brain-JEPA, etc.)
- [ ] Create multi-project comparison dashboards
- [ ] Develop advanced analysis tools

---

## Support & Contact

**Project Lead**: hwang@snu.ac.kr

**System Status**: ✅ **READY FOR PRODUCTION**

All components have been tested and verified working correctly.

---

**Created**: October 23, 2025
**Last Updated**: October 23, 2025
**Version**: 1.0
