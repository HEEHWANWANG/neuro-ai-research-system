# 🔬 AI+Neuroscience Multi-Project Research System

**Welcome!** This is your central hub for managing multiple AI+Neuroscience research projects.

---

## 📍 You Are Here

You're in the main research system directory where all projects are organized and managed.

```
neuro-ai-research-system/          ← YOU ARE HERE
├── projects/                       ← All project folders
├── README_MULTI_PROJECT.md         ← Start with this! (Quick start guide)
├── PROJECTS_MANAGEMENT.md          ← Central project hub
├── PROJECT_SETUP_GUIDE.md          ← Comprehensive setup guide
└── ... (utilities and configs)
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Read the Quick Start Guide
```bash
cat README_MULTI_PROJECT.md
```
Takes 5 minutes. Gets you oriented with the system.

### Step 2: Check Your Projects
```bash
cat PROJECTS_MANAGEMENT.md
```
See what projects you have and their status.

### Step 3: Pick Your Project
Choose which project you want to work with:

**Option A: Work with SwiFT_v2** (fMRI Foundation Model)
```bash
cat projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md
```

**Option B: Work with BrainVLM** (Vision-Language Model)
```bash
cat projects/BrainVLM/docs/BrainVLM_Project_Overview.md
```

---

## 📂 Projects Overview

### SwiFT_v2 - fMRI Foundation Model
- **Status**: 🔬 Research Phase
- **Documentation**: 12 files, 192 KB
- **Database**: 284 KB (16 documents indexed)
- **Code Location**: `/Users/apple/Desktop/SwiFT_v2_perlmutter`
- **Key Doc**: `projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md`

### BrainVLM - Vision-Language Model  
- **Status**: 🔬 Active Development
- **Documentation**: 2 files, 16 KB
- **Database**: 44 KB (2 documents indexed)
- **Code Location**: `/Users/apple/Desktop/BLIP_MRI`
- **Key Doc**: `projects/BrainVLM/docs/BrainVLM_Project_Overview.md`

---

## 🔍 Search Documentation

### Search SwiFT_v2 (16 documents)
```bash
python3 << 'SEARCH'
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/SwiFT_v2/vectordb/memory/research_vectordb.db')
results = db.search('your search term', collection_name='research_documents', limit=5)
for r in results:
    print(f"📄 {r['metadata']['file']}")
    print(f"   {r['content'][:150]}...\n")
SEARCH
```

### Search BrainVLM (2 documents)
```bash
python3 << 'SEARCH'
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB('projects/BrainVLM/vectordb/memory/research_vectordb.db')
results = db.search('your search term', collection_name='brainvlm_documentation', limit=5)
for r in results:
    print(f"📄 {r['metadata']['file']}")
    print(f"   {r['content'][:150]}...\n")
SEARCH
```

---

## 📚 Documentation Files

### Main Guides (Start Here!)
1. **[README_MULTI_PROJECT.md](README_MULTI_PROJECT.md)** - Quick start & project links
2. **[PROJECTS_MANAGEMENT.md](PROJECTS_MANAGEMENT.md)** - Central project hub
3. **[PROJECT_SETUP_GUIDE.md](projects/PROJECT_SETUP_GUIDE.md)** - Complete setup guide

### Project Folders
```
projects/
├── SwiFT_v2/docs/                   ← 12 SwiFT_v2 documents
├── BrainVLM/docs/                   ← 2 BrainVLM documents  
└── PROJECT_SETUP_GUIDE.md           ← How to add new docs
```

### Reference
- **[MULTI_PROJECT_SETUP_COMPLETE.md](MULTI_PROJECT_SETUP_COMPLETE.md)** - Completion report

---

## ⚡ Common Tasks

### Add New Documentation to SwiFT_v2
```bash
# 1. Create your document
vim projects/SwiFT_v2/docs/Your_New_Doc.md

# 2. Update the database
python3 save_to_sqlite_vectordb.py

# 3. Verify it worked
python3 test_project_databases.py
```

### Add New Documentation to BrainVLM
```bash
# 1. Create your document
vim projects/BrainVLM/docs/Your_New_Doc.md

# 2. Update the database
python3 populate_brainvlm_vectordb.py

# 3. Verify it worked
python3 test_project_databases.py
```

### View Project Code
```bash
# SwiFT_v2 code
cd /Users/apple/Desktop/SwiFT_v2_perlmutter

# BrainVLM code
cd /Users/apple/Desktop/BLIP_MRI
```

---

## 🎯 What's New?

✅ **Separate project folders** - Each project has its own `docs/`, `vectordb/`, and `workspace/`
✅ **Independent databases** - Fast searches within each project
✅ **Central management** - Easy comparison and switching between projects
✅ **Complete documentation** - Guides for setup, usage, and best practices
✅ **Validation scripts** - Verify both projects work correctly

---

## 📊 System Status

| Component | SwiFT_v2 | BrainVLM | Status |
|-----------|----------|----------|--------|
| Documentation | 12 files | 2 files | ✅ Active |
| Vector DB | 284 KB | 44 KB | ✅ Functional |
| Search | 16 docs | 2 docs | ✅ Working |
| Workspace | Ready | Ready | ✅ Available |

**Overall Status**: ✅ **READY FOR PRODUCTION**

---

## 🆘 Need Help?

### Quick Reference
- **Project Overview**: `PROJECTS_MANAGEMENT.md`
- **Setup Instructions**: `PROJECT_SETUP_GUIDE.md`
- **Quick Start**: `README_MULTI_PROJECT.md`

### Project-Specific Help
- **SwiFT_v2**: `projects/SwiFT_v2/docs/EXECUTIVE_SUMMARY.md`
- **BrainVLM**: `projects/BrainVLM/docs/BrainVLM_Project_Overview.md`

### Technical Questions
- **Vector Database**: `PROJECT_SETUP_GUIDE.md` → "Vector Database API Reference"
- **File Organization**: `PROJECT_SETUP_GUIDE.md` → "Best Practices"
- **Examples**: `test_project_databases.py` → Shows all features

---

## 🔗 Important Links

**Code Directories**:
- SwiFT_v2: `/Users/apple/Desktop/SwiFT_v2_perlmutter`
- BrainVLM: `/Users/apple/Desktop/BLIP_MRI`

**GitHub Repositories**:
- System: `https://github.com/HEEHWANWANG/neuro-ai-research-system`
- SwiFT_v2: ✅ Available
- BrainVLM: ⏳ To be created

**Contact**: hwang@snu.ac.kr

---

## 📋 Next Steps

1. ✅ **Read** `README_MULTI_PROJECT.md` for quick orientation
2. ✅ **Review** `PROJECTS_MANAGEMENT.md` for project details
3. ✅ **Choose** a project to work with (SwiFT_v2 or BrainVLM)
4. ⏳ **Explore** your project's documentation in `projects/{PROJECT}/docs/`
5. ⏳ **Search** project documentation using the vector database

---

**Last Updated**: October 23, 2025  
**System Version**: 1.0  
**Status**: ✅ Production Ready

---

## 📖 Document Reading Order

**For New Users** (First Time):
1. This file (START_HERE.md) ← You are here
2. README_MULTI_PROJECT.md (quick start)
3. PROJECTS_MANAGEMENT.md (project overview)
4. Your chosen project's README

**For Managing Projects**:
1. PROJECTS_MANAGEMENT.md (central hub)
2. PROJECT_SETUP_GUIDE.md (detailed guide)
3. Project-specific documentation

**For Technical Deep Dive**:
1. MULTI_PROJECT_SETUP_COMPLETE.md (architecture)
2. PROJECT_SETUP_GUIDE.md (API reference)
3. Source code comments

---

**🎉 Welcome to the AI+Neuroscience Research System!**

Start with reading `README_MULTI_PROJECT.md` → Click that link above or run:
```bash
cat README_MULTI_PROJECT.md
```
