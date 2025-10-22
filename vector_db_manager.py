#!/usr/bin/env python3
"""
Vector Database Manager for AI+Neuroscience Multi-Agent Research System
Manages ChromaDB local persistent storage
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import json

try:
    import chromadb
    from chromadb.config import Settings
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    print("Warning: chromadb not installed. Install with: pip install chromadb")


class VectorDBManager:
    """Manage ChromaDB local persistent storage"""
    
    def __init__(self, db_path: Optional[str] = None):
        """
        Initialize Vector DB Manager
        
        Args:
            db_path: Path to ChromaDB storage directory
                    If None, reads from environment variable VECTOR_DB_PATH
                    Default: .claude/workspace/memory/vector_db
        """
        if db_path is None:
            db_path = os.getenv('VECTOR_DB_PATH', '.claude/workspace/memory/vector_db')
        
        self.db_path = Path(db_path)
        self.db_path.mkdir(parents=True, exist_ok=True)
        
        if not CHROMADB_AVAILABLE:
            raise ImportError(
                "chromadb is not installed. Install with: pip install chromadb"
            )
        
        # Initialize ChromaDB with persistent storage
        self.client = chromadb.PersistentClient(
            path=str(self.db_path),
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        
        print(f"✓ ChromaDB initialized at: {self.db_path.absolute()}")
    
    def create_collection(
        self, 
        name: str, 
        metadata: Optional[Dict] = None,
        embedding_function: Optional[Any] = None
    ) -> Any:
        """
        Create a new collection or get existing one
        
        Args:
            name: Collection name
            metadata: Optional metadata for the collection
            embedding_function: Custom embedding function
        
        Returns:
            ChromaDB collection object
        """
        try:
            collection = self.client.get_or_create_collection(
                name=name,
                metadata=metadata or {},
                embedding_function=embedding_function
            )
            print(f"✓ Collection '{name}' ready")
            return collection
        except Exception as e:
            print(f"✗ Error creating collection '{name}': {e}")
            raise
    
    def list_collections(self) -> List[str]:
        """List all collections in the database"""
        collections = self.client.list_collections()
        return [col.name for col in collections]
    
    def get_collection(self, name: str) -> Any:
        """Get an existing collection"""
        try:
            return self.client.get_collection(name=name)
        except Exception as e:
            print(f"✗ Collection '{name}' not found: {e}")
            return None
    
    def delete_collection(self, name: str):
        """Delete a collection"""
        try:
            self.client.delete_collection(name=name)
            print(f"✓ Collection '{name}' deleted")
        except Exception as e:
            print(f"✗ Error deleting collection '{name}': {e}")
    
    def add_documents(
        self,
        collection_name: str,
        documents: List[str],
        metadatas: Optional[List[Dict]] = None,
        ids: Optional[List[str]] = None
    ):
        """
        Add documents to a collection
        
        Args:
            collection_name: Name of the collection
            documents: List of document texts
            metadatas: Optional list of metadata dicts
            ids: Optional list of document IDs
        """
        collection = self.get_collection(collection_name)
        if collection is None:
            collection = self.create_collection(collection_name)
        
        if ids is None:
            ids = [f"doc_{i}_{datetime.now().timestamp()}" for i in range(len(documents))]
        
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"✓ Added {len(documents)} documents to '{collection_name}'")
    
    def query_documents(
        self,
        collection_name: str,
        query_texts: List[str],
        n_results: int = 5,
        where: Optional[Dict] = None
    ) -> Dict:
        """
        Query documents from a collection
        
        Args:
            collection_name: Name of the collection
            query_texts: List of query texts
            n_results: Number of results to return
            where: Optional metadata filter
        
        Returns:
            Query results dictionary
        """
        collection = self.get_collection(collection_name)
        if collection is None:
            return {"error": f"Collection '{collection_name}' not found"}
        
        results = collection.query(
            query_texts=query_texts,
            n_results=n_results,
            where=where
        )
        return results
    
    def get_collection_stats(self, collection_name: str) -> Dict:
        """Get statistics about a collection"""
        collection = self.get_collection(collection_name)
        if collection is None:
            return {"error": f"Collection '{collection_name}' not found"}
        
        count = collection.count()
        return {
            "name": collection_name,
            "count": count,
            "metadata": collection.metadata
        }
    
    def backup_database(self, backup_path: Optional[str] = None) -> Path:
        """
        Create a backup of the entire database
        
        Args:
            backup_path: Path for backup directory
        
        Returns:
            Path to backup directory
        """
        if backup_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f".claude/workspace/memory/backups/vectordb_{timestamp}"
        
        backup_dir = Path(backup_path)
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy entire database directory
        shutil.copytree(
            self.db_path,
            backup_dir / "vector_db",
            dirs_exist_ok=True
        )
        
        # Save metadata
        metadata = {
            "backup_time": datetime.now().isoformat(),
            "collections": self.list_collections(),
            "db_path": str(self.db_path)
        }
        
        with open(backup_dir / "metadata.json", 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"✓ Database backed up to: {backup_dir.absolute()}")
        return backup_dir
    
    def restore_database(self, backup_path: str):
        """
        Restore database from backup
        
        Args:
            backup_path: Path to backup directory
        """
        backup_dir = Path(backup_path)
        if not backup_dir.exists():
            raise FileNotFoundError(f"Backup directory not found: {backup_path}")
        
        # Clear current database
        if self.db_path.exists():
            shutil.rmtree(self.db_path)
        
        # Restore from backup
        shutil.copytree(
            backup_dir / "vector_db",
            self.db_path
        )
        
        # Reinitialize client
        self.client = chromadb.PersistentClient(
            path=str(self.db_path),
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        
        print(f"✓ Database restored from: {backup_path}")
    
    def reset_database(self):
        """Reset the entire database (delete all collections)"""
        confirm = input(
            f"⚠️  This will delete all data in {self.db_path}. Continue? (yes/no): "
        )
        if confirm.lower() == 'yes':
            self.client.reset()
            print("✓ Database reset complete")
        else:
            print("✗ Reset cancelled")
    
    def export_collection(self, collection_name: str, output_file: str):
        """
        Export collection to JSON file
        
        Args:
            collection_name: Name of the collection
            output_file: Path to output JSON file
        """
        collection = self.get_collection(collection_name)
        if collection is None:
            return
        
        # Get all documents
        results = collection.get()
        
        export_data = {
            "collection_name": collection_name,
            "export_time": datetime.now().isoformat(),
            "count": len(results['ids']),
            "documents": results
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Collection '{collection_name}' exported to: {output_file}")
    
    def import_collection(self, input_file: str, collection_name: Optional[str] = None):
        """
        Import collection from JSON file
        
        Args:
            input_file: Path to input JSON file
            collection_name: Optional name for the collection (uses file name if not provided)
        """
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if collection_name is None:
            collection_name = data.get('collection_name', Path(input_file).stem)
        
        collection = self.create_collection(collection_name)
        
        # Add documents
        collection.add(
            ids=data['documents']['ids'],
            documents=data['documents']['documents'],
            metadatas=data['documents']['metadatas']
        )
        
        print(f"✓ Imported {data['count']} documents to '{collection_name}'")


def main():
    """CLI for Vector DB management"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="ChromaDB Vector Database Manager"
    )
    parser.add_argument(
        "command",
        choices=[
            "init", "list", "create", "delete", "stats", 
            "backup", "restore", "reset", "export", "import"
        ],
        help="Management command"
    )
    parser.add_argument("--name", help="Collection name")
    parser.add_argument("--path", help="Path (for backup/restore/export/import)")
    parser.add_argument("--db-path", help="Database directory path")
    
    args = parser.parse_args()
    
    try:
        manager = VectorDBManager(db_path=args.db_path)
        
        if args.command == "init":
            print(f"Database initialized at: {manager.db_path}")
        
        elif args.command == "list":
            collections = manager.list_collections()
            print(f"\nCollections ({len(collections)}):")
            for col in collections:
                stats = manager.get_collection_stats(col)
                print(f"  - {col}: {stats['count']} documents")
        
        elif args.command == "create":
            if not args.name:
                print("Error: --name required")
                return
            manager.create_collection(args.name)
        
        elif args.command == "delete":
            if not args.name:
                print("Error: --name required")
                return
            manager.delete_collection(args.name)
        
        elif args.command == "stats":
            if not args.name:
                print("Error: --name required")
                return
            stats = manager.get_collection_stats(args.name)
            print(json.dumps(stats, indent=2))
        
        elif args.command == "backup":
            backup_path = manager.backup_database(args.path)
            print(f"Backup created at: {backup_path}")
        
        elif args.command == "restore":
            if not args.path:
                print("Error: --path required")
                return
            manager.restore_database(args.path)
        
        elif args.command == "reset":
            manager.reset_database()
        
        elif args.command == "export":
            if not args.name or not args.path:
                print("Error: --name and --path required")
                return
            manager.export_collection(args.name, args.path)
        
        elif args.command == "import":
            if not args.path:
                print("Error: --path required")
                return
            manager.import_collection(args.path, args.name)
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
