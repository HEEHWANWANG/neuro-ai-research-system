#!/usr/bin/env python3
"""
Populate BrainVLM Vector Database
Saves all BrainVLM markdown documentation to a project-specific vector database
"""

import sys
import hashlib
from pathlib import Path

# Add the root directory to the path so we can import simple_vectordb
sys.path.insert(0, str(Path(__file__).parent))

from simple_vectordb import SimpleVectorDB

def populate_brainvlm_database():
    """Populate the BrainVLM vector database with all documentation."""

    # Initialize database for BrainVLM
    db_path = Path("/Users/apple/Desktop/neuro-ai-research-system/projects/BrainVLM/vectordb/memory/research_vectordb.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)

    db = SimpleVectorDB(str(db_path))

    # Define the collection
    collection_name = "brainvlm_documentation"

    # Create collection
    db.create_collection(collection_name)

    print(f"📚 Populating BrainVLM Vector Database")
    print(f"   Database: {db_path}")
    print(f"   Collection: {collection_name}\n")

    # Define BrainVLM documentation files
    docs_dir = Path("/Users/apple/Desktop/neuro-ai-research-system/projects/BrainVLM/docs")
    markdown_files = sorted(docs_dir.glob("*.md"))

    if not markdown_files:
        print("❌ No markdown files found in BrainVLM docs directory!")
        return

    total_size = 0
    documents_saved = 0

    for md_file in markdown_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            file_size = len(content.encode('utf-8'))
            total_size += file_size

            # Extract title from first heading
            title = md_file.stem.replace('_', ' ')
            for line in content.split('\n'):
                if line.startswith('#'):
                    title = line.replace('#', '').strip()
                    break

            # Generate doc ID from file name
            doc_id = hashlib.md5(md_file.name.encode()).hexdigest()[:16]

            # Add to database
            success = db.add_document(
                collection_name=collection_name,
                doc_id=doc_id,
                content=content,
                metadata={
                    'source': 'BrainVLM Documentation',
                    'file': md_file.name,
                    'title': title,
                    'type': 'markdown',
                    'size_kb': round(file_size / 1024, 2)
                }
            )

            print(f"✅ {md_file.name}")
            print(f"   Size: {round(file_size/1024, 2)} KB | ID: {doc_id}")
            documents_saved += 1

        except Exception as e:
            print(f"❌ Error processing {md_file.name}: {e}")

    # Get collection stats
    stats = db.get_collection_stats(collection_name)

    print(f"\n📊 Database Summary")
    print(f"   Documents Saved: {documents_saved}")
    print(f"   Total Size: {round(total_size/1024, 2)} KB")
    print(f"   Collection Stats: {stats}")

    # Test search functionality
    print(f"\n🔍 Testing Search Functionality")
    test_queries = [
        "vision language model",
        "BLIP-2 T5",
        "training configuration"
    ]

    for query in test_queries:
        results = db.search(query, collection_name=collection_name, limit=2)
        print(f"   Query: '{query}' → {len(results)} results found")

    print(f"\n✨ BrainVLM Vector Database successfully populated!")
    print(f"   Location: {db_path}")
    print(f"   Access: SimpleVectorDB('{db_path}')")

    return db

if __name__ == "__main__":
    populate_brainvlm_database()
