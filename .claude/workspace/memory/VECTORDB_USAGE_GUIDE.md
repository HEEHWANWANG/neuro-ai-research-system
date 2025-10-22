# Vector Database Usage Guide

## Overview

All research documents have been successfully saved to a **SQLite-based vector database** for persistent storage and searchable access across sessions.

**Database Location**: `.claude/workspace/memory/research_vectordb.db`

**Database Type**: SQLite (no external dependencies required)

**Total Documents Saved**: 16 research documents (206.15 KB)

---

## Quick Start

### Basic Usage in Python

```python
from simple_vectordb import SimpleVectorDB

# Initialize the database
db = SimpleVectorDB(".claude/workspace/memory/research_vectordb.db")

# Search for documents
results = db.search("foundation models", limit=5)

# View results
for doc in results:
    print(f"Document: {doc['metadata']['filename']}")
    print(f"Type: {doc['metadata']['document_type']}")
    print(f"Preview: {doc['summary'][:200]}...")

db.close()
```

---

## Database Contents

### Documents by Type

| Type | Count | Total Size |
|------|-------|-----------|
| Research Analysis | 1 | 18.71 KB |
| Introductions | 2 | 42.79 KB |
| Summaries | 3 | 31.26 KB |
| Reference | 10 | 113.37 KB |
| **TOTAL** | **16** | **206.15 KB** |

### Document List

1. **COMPLETION_REPORT.md** (14.2 KB) - Project completion summary
2. **EXECUTIVE_SUMMARY.md** (10.9 KB) - Key findings and recommendations
3. **FAMILIARIZATION_COMPLETE.md** (10.9 KB) - Project familiarization status
4. **README_Research_Documentation.md** (13.3 KB) - Documentation navigation guide
5. **RESEARCH_SYNTHESIS_fMRI_Foundation_Models.md** (15.0 KB) - Research synthesis and strategy
6. **SESSION_SUMMARY_Oct22_2025.md** (9.8 KB) - Previous session summary
7. **SwiFT_Paper_Summary.md** (10.6 KB) - SwiFT paper theoretical foundations
8. **SwiFT_v2_Development_Quick_Reference.md** (13.5 KB) - Development quick reference
9. **SwiFT_v2_Draft_Introduction.md** (15.0 KB) - Initial introduction draft
10. **SwiFT_v2_Introduction_Critical_Review_and_Revision.md** (27.8 KB) ⭐ **KEY DOCUMENT** - Publication-ready introduction
11. **SwiFT_v2_Project_Familiarization.md** (12.5 KB) - Project overview
12. **fMRI_Foundation_Models_Comparative_Analysis.md** (18.7 KB) - Competitive analysis
13. **MANIFEST.md** (9.9 KB) - Document manifest
14. **QUICK_REFERENCE.md** (7.9 KB) - Quick reference guide
15. **RESEARCH_VECTOR_DB_INDEX.md** (11.5 KB) - Research index
16. **START_HERE.md** (4.8 KB) - Getting started guide

---

## Available Methods

### Search Documents

```python
# Simple keyword search
results = db.search(
    query="foundation models",
    collection_name="research_documents",
    limit=5
)
```

**Parameters:**
- `query` (str): Search term(s)
- `collection_name` (str): Collection to search (default: "research_documents")
- `limit` (int): Maximum results (default: 5)

**Returns:** List of dictionaries with:
- `id`: Document ID
- `content`: Full document text
- `metadata`: Document metadata
- `summary`: First 500 characters of content

---

### Get Specific Document

```python
# Retrieve a specific document by ID
doc = db.get_document("research_analysis_fMRI_Foundation_Models_Comparative_Analysis_12")

if doc:
    print(f"Document: {doc['metadata']['filename']}")
    print(f"Content: {doc['content'][:500]}...")
```

---

### List Collections

```python
# See all collections
collections = db.list_collections()
print(f"Collections: {collections}")
# Output: ['research_documents']
```

---

### Get Collection Stats

```python
# Get collection information
stats = db.get_collection_stats("research_documents")

print(f"Collection: {stats['name']}")
print(f"Documents: {stats['document_count']}")
print(f"Database: {stats['db_path']}")
```

---

### Export Collection

```python
# Export collection to JSON
db.export_collection(
    "research_documents",
    "exported_research.json"
)
```

---

## Search Examples

### Find Introduction Documents
```python
results = db.search("introduction SwiFT paper", limit=2)
```

### Find Comparative Analysis
```python
results = db.search("BrainLM Brain-JEPA comparison", limit=5)
```

### Find Performance Metrics
```python
results = db.search("accuracy efficiency performance", limit=3)
```

### Find Clinical Applications
```python
results = db.search("clinical translation applications", limit=3)
```

---

## Data Files

### Primary Database
- **Name**: `research_vectordb.db`
- **Size**: 284 KB
- **Format**: SQLite 3
- **Features**: Full-text search, document storage, metadata indexing

### Backup Files
- **Manifest**: `VECTORDB_MANIFEST.json` - Complete document inventory
- **Backup**: `research_documents_backup.json` - JSON export of all documents

---

## Database Schema

### Collections Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Collection ID (primary key) |
| name | TEXT | Collection name |
| metadata | TEXT | JSON metadata |
| created_at | TIMESTAMP | Creation timestamp |

### Documents Table
| Column | Type | Description |
|--------|------|-------------|
| id | TEXT | Document ID (primary key) |
| collection_id | INTEGER | Reference to collection |
| content | TEXT | Full document text |
| metadata | TEXT | JSON metadata |
| created_at | TIMESTAMP | Creation timestamp |

### Search Index Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Index ID |
| doc_id | TEXT | Reference to document |
| keywords | TEXT | Extracted keywords |
| summary | TEXT | Document summary (first 500 chars) |

---

## Key Features

✅ **No External Dependencies** - Uses Python standard library only
✅ **Persistent Storage** - SQLite database survives sessions
✅ **Full-Text Search** - Keyword-based document search
✅ **Metadata Tracking** - Document type, size, source file
✅ **JSON Export** - Backup and portability
✅ **Session-Persistent** - Access across development sessions

---

## Advanced Usage

### Custom Queries with Metadata

```python
# Future enhancement: filter by document type
# Currently available via results filtering:

results = db.search("SwiFT architecture", limit=10)
introduction_docs = [r for r in results if 'introduction' in r['metadata']['filename'].lower()]
```

### Batch Document Addition

```python
# Add multiple new documents
new_docs = ["document 1 content", "document 2 content"]
new_metadata = [
    {"type": "analysis", "author": "User"},
    {"type": "notes", "author": "User"}
]
new_ids = ["custom_doc_1", "custom_doc_2"]

db.add_documents_batch(
    "research_documents",
    new_docs,
    new_metadata,
    new_ids
)
```

---

## Troubleshooting

### Database Not Found
```python
from pathlib import Path
db_path = Path(".claude/workspace/memory/research_vectordb.db")
if not db_path.exists():
    print("Database not found. Run save_to_sqlite_vectordb.py to create it.")
```

### Search Returns No Results
- Try shorter search terms
- Check document summaries to understand what keywords are indexed
- Export collection to JSON for manual inspection

### Database Corruption (Rare)
- Delete `research_vectordb.db`
- Restore from `research_documents_backup.json`
- Run `db.import_collection("research_documents_backup.json")`

---

## Session Resumption

When resuming work:

```python
# 1. Load the database
from simple_vectordb import SimpleVectorDB
db = SimpleVectorDB(".claude/workspace/memory/research_vectordb.db")

# 2. Search for relevant documents
results = db.search("your research topic")

# 3. Access full content
for doc in results:
    full_content = doc['content']
    metadata = doc['metadata']
    # Process as needed...

# 4. Close when done
db.close()
```

---

## Future Enhancements

Potential improvements for vector database:
1. **Embedding-based search** - Replace keyword search with semantic embeddings
2. **Advanced filtering** - Filter by document type, date range, file size
3. **Document relationships** - Link related documents
4. **Version control** - Track document revisions
5. **Full ChromaDB migration** - Upgrade to production ChromaDB when dependencies available

---

## File Locations

```
.claude/workspace/memory/
├── research_vectordb.db              ← Main database (284 KB)
├── VECTORDB_MANIFEST.json            ← Document inventory
├── research_documents_backup.json     ← JSON backup (221 KB)
├── VECTORDB_USAGE_GUIDE.md          ← This file
└── [other documentation files]
```

---

## Support Scripts

### Verify Database Health
```bash
python3 save_to_sqlite_vectordb.py  # Re-save documents (won't duplicate)
```

### Inspect Database
```python
import sqlite3
conn = sqlite3.connect(".claude/workspace/memory/research_vectordb.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM documents")
print(f"Total documents: {cursor.fetchone()[0]}")
conn.close()
```

---

**Last Updated**: 2025-10-23
**Documents Saved**: 16
**Total Size**: 206.15 KB
**Status**: ✅ Ready for use
