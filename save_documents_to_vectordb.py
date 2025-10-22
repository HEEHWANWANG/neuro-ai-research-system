#!/usr/bin/env python3
"""
Script to save all workspace documents to ChromaDB vector database
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import json

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from vector_db_manager import VectorDBManager


def extract_text_preview(text: str, max_chars: int = 500) -> str:
    """Extract first N characters as preview"""
    return text[:max_chars].replace('\n', ' ')


def main():
    # Initialize Vector DB Manager
    db_path = ".claude/workspace/memory/vector_db"
    print(f"Initializing ChromaDB at: {db_path}")

    try:
        manager = VectorDBManager(db_path=db_path)
    except ImportError as e:
        print(f"Error: {e}")
        print("Installing chromadb...")
        os.system("pip install chromadb")
        manager = VectorDBManager(db_path=db_path)

    # Find all markdown documents
    workspace_dir = Path(".claude/workspace")
    md_files = list(workspace_dir.rglob("*.md"))

    print(f"\nFound {len(md_files)} markdown documents")
    print("=" * 60)

    # Organize documents by type
    documents_by_type = {
        "research_analysis": [],
        "introductions": [],
        "summaries": [],
        "reference": []
    }

    all_documents = []
    all_metadatas = []
    all_ids = []

    for i, md_file in enumerate(md_files, 1):
        try:
            # Read document
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Determine document type
            filename = md_file.name.lower()
            if "introduction" in filename or "intro" in filename:
                doc_type = "introductions"
            elif "summary" in filename or "executive" in filename:
                doc_type = "summaries"
            elif "analysis" in filename or "comparative" in filename:
                doc_type = "research_analysis"
            else:
                doc_type = "reference"

            # Create metadata
            metadata = {
                "source_file": str(md_file.relative_to(Path.cwd())),
                "document_type": doc_type,
                "file_size_kb": round(len(content) / 1024, 2),
                "saved_at": datetime.now().isoformat(),
                "filename": md_file.name
            }

            # Create document ID
            doc_id = f"{doc_type}_{md_file.stem}_{i}"

            # Store in appropriate category
            documents_by_type[doc_type].append({
                "file": md_file.name,
                "size_kb": metadata["file_size_kb"]
            })

            # Add to batch
            all_documents.append(content)
            all_metadatas.append(metadata)
            all_ids.append(doc_id)

            print(f"✓ [{i:2d}] {md_file.name:50s} | Type: {doc_type:15s} | Size: {metadata['file_size_kb']:6.1f} KB")

        except Exception as e:
            print(f"✗ [{i:2d}] Error reading {md_file.name}: {e}")

    print("\n" + "=" * 60)
    print(f"Total documents to save: {len(all_documents)}")
    print("\nDocument breakdown:")
    for doc_type, docs in documents_by_type.items():
        if docs:
            print(f"  • {doc_type:20s}: {len(docs):3d} documents")

    # Create ChromaDB collection and add all documents
    print("\n" + "=" * 60)
    print("Saving to ChromaDB...")

    try:
        # Create main research collection
        manager.add_documents(
            collection_name="research_documents",
            documents=all_documents,
            metadatas=all_metadatas,
            ids=all_ids
        )

        print(f"✓ Successfully saved {len(all_documents)} documents to 'research_documents' collection")

        # Get and display collection stats
        stats = manager.get_collection_stats("research_documents")
        print(f"\nCollection Statistics:")
        print(f"  • Collection name: {stats['name']}")
        print(f"  • Total documents: {stats['count']}")
        print(f"  • Metadata: {stats.get('metadata', {})}")

        # Create a manifest file
        manifest = {
            "saved_at": datetime.now().isoformat(),
            "total_documents": len(all_documents),
            "total_size_kb": sum(m["file_size_kb"] for m in all_metadatas),
            "documents_by_type": {
                doc_type: len(docs) for doc_type, docs in documents_by_type.items() if docs
            },
            "db_path": db_path,
            "document_list": [
                {
                    "id": all_ids[i],
                    "filename": all_metadatas[i]["filename"],
                    "type": all_metadatas[i]["document_type"],
                    "size_kb": all_metadatas[i]["file_size_kb"]
                }
                for i in range(len(all_documents))
            ]
        }

        manifest_path = Path(".claude/workspace/memory/VECTORDB_MANIFEST.json")
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)

        print(f"\n✓ Manifest saved to: {manifest_path.relative_to(Path.cwd())}")

        # Create backup
        print("\nCreating database backup...")
        backup_path = manager.backup_database()
        print(f"✓ Backup created at: {backup_path.relative_to(Path.cwd())}")

        print("\n" + "=" * 60)
        print("✓ SUCCESS: All documents saved to ChromaDB vector database")
        print("=" * 60)

        return 0

    except Exception as e:
        print(f"✗ Error saving documents: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
