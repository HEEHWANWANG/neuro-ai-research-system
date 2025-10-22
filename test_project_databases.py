#!/usr/bin/env python3
"""
Test script to demonstrate separate vector databases for SwiFT_v2 and BrainVLM
Shows how to search each project's documentation independently
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from simple_vectordb import SimpleVectorDB

def test_databases():
    """Test both project databases independently."""

    print("=" * 70)
    print("🔬 AI+Neuroscience Research System - Project Database Test")
    print("=" * 70)

    # Test SwiFT_v2 database
    print("\n📦 SwiFT_v2 Project Database")
    print("-" * 70)

    swift_db_path = "/Users/apple/Desktop/neuro-ai-research-system/projects/SwiFT_v2/vectordb/memory/research_vectordb.db"
    swift_db = SimpleVectorDB(swift_db_path)

    swift_stats = swift_db.get_collection_stats("research_documents")
    print(f"✓ Database Location: {swift_db_path}")
    print(f"✓ Collection: research_documents")
    print(f"✓ Documents: {swift_stats['document_count']}")

    # Test SwiFT_v2 searches
    swift_queries = [
        "Swin Transformer fMRI",
        "self-supervised learning",
        "Brain-JEPA competitive analysis"
    ]

    print(f"\n🔍 SwiFT_v2 Sample Searches:")
    for query in swift_queries:
        results = swift_db.search(query, collection_name="research_documents", limit=2)
        print(f"   '{query}' → {len(results)} results")
        if results:
            print(f"      Top result: {results[0].get('metadata', {}).get('file', 'Unknown')}")

    # Test BrainVLM database
    print("\n\n📦 BrainVLM Project Database")
    print("-" * 70)

    brainvlm_db_path = "/Users/apple/Desktop/neuro-ai-research-system/projects/BrainVLM/vectordb/memory/research_vectordb.db"
    brainvlm_db = SimpleVectorDB(brainvlm_db_path)

    brainvlm_stats = brainvlm_db.get_collection_stats("brainvlm_documentation")
    print(f"✓ Database Location: {brainvlm_db_path}")
    print(f"✓ Collection: brainvlm_documentation")
    print(f"✓ Documents: {brainvlm_stats['document_count']}")

    # Test BrainVLM searches
    brainvlm_queries = [
        "vision language model",
        "BLIP-2 T5 training",
        "medical report generation"
    ]

    print(f"\n🔍 BrainVLM Sample Searches:")
    for query in brainvlm_queries:
        results = brainvlm_db.search(query, collection_name="brainvlm_documentation", limit=2)
        print(f"   '{query}' → {len(results)} results")
        if results:
            print(f"      Top result: {results[0].get('metadata', {}).get('file', 'Unknown')}")

    # Summary
    print("\n\n" + "=" * 70)
    print("✨ Project Database Separation Summary")
    print("=" * 70)
    print(f"""
📁 Separate Project Structure Established:
   ├── projects/SwiFT_v2/
   │   ├── docs/              (13 markdown files)
   │   ├── vectordb/          (44 KB database with 16 documents)
   │   └── workspace/         (experiments & analysis)
   │
   └── projects/BrainVLM/
       ├── docs/              (2 markdown files)
       ├── vectordb/          (44 KB database with 2 documents)
       └── workspace/         (experiments & analysis)

✅ Benefits of Separate Databases:
   • Independent document indexing per project
   • Faster searches within project scope
   • Clear separation of concerns
   • Easy to scale each project independently
   • Simple per-project archive and backup

🔍 Usage Examples:
   # Load SwiFT_v2 docs
   from simple_vectordb import SimpleVectorDB
   swift_db = SimpleVectorDB("projects/SwiFT_v2/vectordb/memory/research_vectordb.db")
   results = swift_db.search("foundation models", collection_name="research_documents")

   # Load BrainVLM docs
   brainvlm_db = SimpleVectorDB("projects/BrainVLM/vectordb/memory/research_vectordb.db")
   results = brainvlm_db.search("vision language", collection_name="brainvlm_documentation")
""")

if __name__ == "__main__":
    test_databases()
