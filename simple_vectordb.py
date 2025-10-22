#!/usr/bin/env python3
"""
Simple SQLite-based Vector Database for research documents
No external dependencies needed - uses Python standard library only
"""

import sqlite3
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple


class SimpleVectorDB:
    """Lightweight SQLite-based vector database using sentence embeddings"""

    def __init__(self, db_path: str = ".claude/workspace/memory/research_vectordb.db"):
        """Initialize the vector database"""
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = None
        self.cursor = None
        self._init_db()

    def _init_db(self):
        """Initialize database connection and schema"""
        self.connection = sqlite3.connect(str(self.db_path))
        self.cursor = self.connection.cursor()

        # Create collections table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS collections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create documents table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id TEXT PRIMARY KEY,
                collection_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (collection_id) REFERENCES collections(id)
            )
        """)

        # Create search index table (stores document summaries for keyword search)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS search_index (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_id TEXT NOT NULL,
                keywords TEXT,
                summary TEXT,
                FOREIGN KEY (doc_id) REFERENCES documents(id)
            )
        """)

        self.connection.commit()
        print(f"✓ Database initialized at: {self.db_path.absolute()}")

    def create_collection(self, name: str, metadata: Optional[Dict] = None) -> bool:
        """Create a new collection"""
        try:
            meta_json = json.dumps(metadata or {})
            self.cursor.execute(
                "INSERT INTO collections (name, metadata) VALUES (?, ?)",
                (name, meta_json)
            )
            self.connection.commit()
            print(f"✓ Collection '{name}' created")
            return True
        except sqlite3.IntegrityError:
            print(f"✓ Collection '{name}' already exists")
            return True
        except Exception as e:
            print(f"✗ Error creating collection: {e}")
            return False

    def get_collection_id(self, name: str) -> Optional[int]:
        """Get collection ID by name"""
        self.cursor.execute("SELECT id FROM collections WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def add_document(self, collection_name: str, doc_id: str, content: str, metadata: Optional[Dict] = None) -> bool:
        """Add a document to a collection"""
        try:
            collection_id = self.get_collection_id(collection_name)
            if collection_id is None:
                self.create_collection(collection_name)
                collection_id = self.get_collection_id(collection_name)

            meta_json = json.dumps(metadata or {})
            self.cursor.execute(
                "INSERT OR REPLACE INTO documents (id, collection_id, content, metadata) VALUES (?, ?, ?, ?)",
                (doc_id, collection_id, content, meta_json)
            )

            # Extract keywords from content (first 100 words)
            words = content.split()[:100]
            keywords = " ".join(words)
            summary = content[:500].replace('\n', ' ')

            self.cursor.execute(
                "INSERT OR REPLACE INTO search_index (doc_id, keywords, summary) VALUES (?, ?, ?)",
                (doc_id, keywords, summary)
            )

            self.connection.commit()
            return True
        except Exception as e:
            print(f"✗ Error adding document: {e}")
            return False

    def add_documents_batch(self, collection_name: str, documents: List[str],
                           metadatas: List[Dict], ids: List[str]) -> int:
        """Add multiple documents at once"""
        count = 0
        for doc, meta, doc_id in zip(documents, metadatas, ids):
            if self.add_document(collection_name, doc_id, doc, meta):
                count += 1
        return count

    def search(self, query: str, collection_name: str = "research_documents",
               limit: int = 5) -> List[Dict]:
        """Simple keyword search"""
        collection_id = self.get_collection_id(collection_name)
        if collection_id is None:
            return []

        # Search for documents containing query keywords
        query_words = query.lower().split()
        placeholders = " OR ".join([f"keywords LIKE ?" for _ in query_words])
        search_terms = [f"%{word}%" for word in query_words]

        self.cursor.execute(f"""
            SELECT d.id, d.content, d.metadata, s.summary
            FROM documents d
            LEFT JOIN search_index s ON d.id = s.doc_id
            WHERE d.collection_id = ? AND ({placeholders})
            LIMIT ?
        """, [collection_id] + search_terms + [limit])

        results = []
        for row in self.cursor.fetchall():
            results.append({
                "id": row[0],
                "content": row[1],
                "metadata": json.loads(row[2]) if row[2] else {},
                "summary": row[3]
            })
        return results

    def get_document(self, doc_id: str) -> Optional[Dict]:
        """Get a specific document"""
        self.cursor.execute(
            "SELECT id, content, metadata FROM documents WHERE id = ?",
            (doc_id,)
        )
        result = self.cursor.fetchone()
        if result:
            return {
                "id": result[0],
                "content": result[1],
                "metadata": json.loads(result[2]) if result[2] else {}
            }
        return None

    def list_collections(self) -> List[str]:
        """List all collections"""
        self.cursor.execute("SELECT name FROM collections")
        return [row[0] for row in self.cursor.fetchall()]

    def get_collection_stats(self, collection_name: str) -> Dict:
        """Get statistics for a collection"""
        collection_id = self.get_collection_id(collection_name)
        if collection_id is None:
            return {"error": f"Collection '{collection_name}' not found"}

        self.cursor.execute(
            "SELECT COUNT(*) FROM documents WHERE collection_id = ?",
            (collection_id,)
        )
        count = self.cursor.fetchone()[0]

        return {
            "name": collection_name,
            "document_count": count,
            "db_path": str(self.db_path)
        }

    def export_collection(self, collection_name: str, output_file: str) -> bool:
        """Export collection to JSON"""
        try:
            collection_id = self.get_collection_id(collection_name)
            if collection_id is None:
                return False

            self.cursor.execute(
                "SELECT id, content, metadata FROM documents WHERE collection_id = ?",
                (collection_id,)
            )

            documents = []
            for row in self.cursor.fetchall():
                documents.append({
                    "id": row[0],
                    "content": row[1],
                    "metadata": json.loads(row[2]) if row[2] else {}
                })

            export_data = {
                "collection_name": collection_name,
                "export_time": datetime.now().isoformat(),
                "document_count": len(documents),
                "documents": documents
            }

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)

            print(f"✓ Collection exported to: {output_file}")
            return True
        except Exception as e:
            print(f"✗ Error exporting collection: {e}")
            return False

    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()

    def __del__(self):
        """Cleanup on deletion"""
        self.close()
