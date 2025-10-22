#!/usr/bin/env python3
"""
Save all workspace documents to SQLite vector database
No external dependencies required - uses Python standard library only
"""

import sys
from pathlib import Path
from datetime import datetime
import json

# Import our simple vector database
from simple_vectordb import SimpleVectorDB


def main():
    # Initialize Vector DB
    db_path = ".claude/workspace/memory/research_vectordb.db"
    print(f"Initializing SQLite Vector Database at: {db_path}")
    print("=" * 70)

    db = SimpleVectorDB(db_path=db_path)

    # Find all markdown documents
    workspace_dir = Path(".claude/workspace")
    md_files = sorted(workspace_dir.rglob("*.md"))

    print(f"\nFound {len(md_files)} markdown documents to save")
    print("=" * 70)

    # Create collection
    db.create_collection(
        "research_documents",
        metadata={
            "description": "SwiFT v2 research documents and analysis",
            "created_at": datetime.now().isoformat(),
            "document_count": len(md_files)
        }
    )

    # Process and save documents
    documents_by_type = {
        "research_analysis": [],
        "introductions": [],
        "summaries": [],
        "reference": []
    }

    saved_count = 0
    total_size_kb = 0

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

            # Calculate file size
            file_size_kb = len(content) / 1024

            # Create metadata
            try:
                rel_path = str(md_file.relative_to(Path.cwd()))
            except ValueError:
                rel_path = str(md_file)

            metadata = {
                "source_file": rel_path,
                "document_type": doc_type,
                "file_size_kb": round(file_size_kb, 2),
                "saved_at": datetime.now().isoformat(),
                "filename": md_file.name
            }

            # Create document ID
            doc_id = f"{doc_type}_{md_file.stem}_{i}"

            # Save to database
            if db.add_document("research_documents", doc_id, content, metadata):
                documents_by_type[doc_type].append({
                    "file": md_file.name,
                    "size_kb": round(file_size_kb, 2),
                    "id": doc_id
                })
                saved_count += 1
                total_size_kb += file_size_kb

                print(f"✓ [{i:2d}/{len(md_files)}] {md_file.name:50s} | {doc_type:15s} | {round(file_size_kb, 1):6.1f} KB")
            else:
                print(f"✗ [{i:2d}/{len(md_files)}] Error saving {md_file.name}")

        except Exception as e:
            print(f"✗ [{i:2d}/{len(md_files)}] Error processing {md_file.name}: {e}")

    # Display results
    print("\n" + "=" * 70)
    print(f"Successfully saved: {saved_count}/{len(md_files)} documents")
    print(f"Total size: {round(total_size_kb, 2)} KB")

    print("\nDocument breakdown by type:")
    for doc_type, docs in documents_by_type.items():
        if docs:
            size = sum(d["size_kb"] for d in docs)
            print(f"  • {doc_type:20s}: {len(docs):3d} documents ({size:8.2f} KB)")

    # Get and display collection stats
    stats = db.get_collection_stats("research_documents")
    print("\nCollection Statistics:")
    print(f"  • Collection name: {stats['name']}")
    print(f"  • Total documents: {stats['document_count']}")
    print(f"  • Database path: {stats['db_path']}")

    # Create manifest
    manifest = {
        "saved_at": datetime.now().isoformat(),
        "total_documents": saved_count,
        "total_size_kb": round(total_size_kb, 2),
        "documents_by_type": {
            doc_type: len(docs) for doc_type, docs in documents_by_type.items() if docs
        },
        "db_type": "SQLite Vector Database",
        "db_path": db_path,
        "document_list": [
            doc for docs in documents_by_type.values() for doc in docs
        ]
    }

    manifest_path = Path(".claude/workspace/memory/VECTORDB_MANIFEST.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    try:
        rel_manifest = str(manifest_path.relative_to(Path.cwd()))
    except ValueError:
        rel_manifest = str(manifest_path)
    print(f"\n✓ Manifest saved to: {rel_manifest}")

    # Export collection to JSON backup
    export_path = ".claude/workspace/memory/research_documents_backup.json"
    db.export_collection("research_documents", export_path)

    print("\n" + "=" * 70)
    print("✓ SUCCESS: All documents saved to SQLite vector database")
    print("=" * 70)
    print(f"\nVector database location: {db_path}")
    print(f"You can now query documents from Python:")
    print(f"  from simple_vectordb import SimpleVectorDB")
    print(f"  db = SimpleVectorDB('{db_path}')")
    print(f"  results = db.search('foundation models')")

    db.close()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
