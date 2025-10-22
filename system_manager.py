#!/usr/bin/env python3
"""
System Management Utilities for AI+Neuroscience Multi-Agent Research System
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

WORKSPACE = Path(".claude/workspace")
AGENTS_DIR = Path(".claude/agents")

class ResearchSystemManager:
    """Manage the multi-agent research system"""
    
    def __init__(self):
        self.workspace = WORKSPACE
        self.vector_db_path = Path(os.getenv('VECTOR_DB_PATH', '.claude/workspace/memory/vector_db'))
        self.ensure_workspace()
    
    def ensure_workspace(self):
        """Create workspace directories if they don't exist"""
        dirs = [
            self.workspace / "hypotheses",
            self.workspace / "experiments",
            self.workspace / "papers",
            self.workspace / "presentations",
            self.workspace / "memory" / "vector_db",
            self.workspace / "memory" / "backups",
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
        
        # Ensure Vector DB is initialized
        if not (self.vector_db_path / "chroma.sqlite3").exists():
            print(f"ℹ️  Initializing Vector DB at {self.vector_db_path}")
            self._init_vector_db()
    
    def _init_vector_db(self):
        """Initialize Vector DB if not exists"""
        try:
            from vector_db_manager import VectorDBManager
            db_manager = VectorDBManager(str(self.vector_db_path))
            print(f"✓ Vector DB initialized at {self.vector_db_path}")
        except ImportError:
            print("⚠️  chromadb not installed. Install with: pip install chromadb")
        except Exception as e:
            print(f"⚠️  Vector DB initialization warning: {e}")
    
    def check_vector_db_status(self) -> Dict:
        """Check Vector DB status and collections"""
        try:
            from vector_db_manager import VectorDBManager
            db_manager = VectorDBManager(str(self.vector_db_path))
            collections = db_manager.list_collections()
            
            status = {
                "initialized": True,
                "path": str(self.vector_db_path.absolute()),
                "collections": len(collections),
                "collection_names": collections
            }
            
            # Get size of database
            if self.vector_db_path.exists():
                total_size = sum(
                    f.stat().st_size for f in self.vector_db_path.rglob('*') if f.is_file()
                )
                status["size_mb"] = round(total_size / (1024 * 1024), 2)
            
            return status
        except Exception as e:
            return {
                "initialized": False,
                "error": str(e)
            }
    
    def list_agents(self, pod: Optional[str] = None) -> Dict[str, List[str]]:
        """List all available agents, optionally filtered by pod"""
        agents = {}
        
        if pod:
            pod_dir = AGENTS_DIR / "pods" / pod
            if pod_dir.exists():
                agents[pod] = [
                    f.stem for f in pod_dir.glob("*.md")
                    if not f.name.endswith("-coordinator.md")
                ]
        else:
            # List all pods
            for pod_dir in (AGENTS_DIR / "pods").iterdir():
                if pod_dir.is_dir():
                    agents[pod_dir.name] = [
                        f.stem for f in pod_dir.glob("*.md")
                    ]
        
        return agents
    
    def archive_project(self, project_name: str):
        """Archive a completed research project"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        archive_dir = self.workspace / "archive" / f"{timestamp}_{project_name}"
        archive_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy all workspace directories
        for subdir in ["hypotheses", "experiments", "papers", "presentations"]:
            src = self.workspace / subdir
            dst = archive_dir / subdir
            if src.exists():
                shutil.copytree(src, dst)
        
        print(f"✓ Project archived to: {archive_dir}")
        return archive_dir
    
    def clean_workspace(self, keep_memory: bool = True):
        """Clean workspace (keep memory by default)"""
        for subdir in ["hypotheses", "experiments", "papers", "presentations"]:
            path = self.workspace / subdir
            if path.exists():
                shutil.rmtree(path)
                path.mkdir()
        
        if not keep_memory:
            memory_path = self.workspace / "memory"
            if memory_path.exists():
                shutil.rmtree(memory_path)
                memory_path.mkdir()
        
        print("✓ Workspace cleaned")
    
    def get_project_status(self) -> Dict:
        """Get current project status"""
        status = {
            "timestamp": datetime.now().isoformat(),
            "hypotheses": self._count_files("hypotheses"),
            "experiments": self._count_files("experiments"),
            "papers": self._count_files("papers"),
            "presentations": self._count_files("presentations"),
        }
        
        # Check for research overview
        overview = self.workspace / "hypotheses" / "research_overview.md"
        status["has_research_overview"] = overview.exists()
        
        # Check for experiment results
        results = self.workspace / "experiments" / "results"
        status["has_results"] = results.exists() and any(results.iterdir())
        
        return status
    
    def _count_files(self, subdir: str) -> int:
        """Count files in a workspace subdirectory"""
        path = self.workspace / subdir
        if not path.exists():
            return 0
        return len([f for f in path.rglob("*") if f.is_file()])
    
    def generate_project_report(self, output_file: Optional[Path] = None) -> str:
        """Generate a summary report of the current project"""
        status = self.get_project_status()
        
        report = f"""# Project Status Report
Generated: {status['timestamp']}

## Workspace Contents

### Hypotheses
- Files: {status['hypotheses']}
- Research Overview: {'✓' if status['has_research_overview'] else '✗'}

### Experiments
- Files: {status['experiments']}
- Results Available: {'✓' if status['has_results'] else '✗'}

### Papers
- Files: {status['papers']}

### Presentations
- Files: {status['presentations']}

## Next Steps

"""
        
        if not status['has_research_overview']:
            report += "1. Run Hypothesis Engine to generate research overview\n"
        elif not status['has_results']:
            report += "1. Run experiments via Forge Pod\n"
        elif status['papers'] == 0:
            report += "1. Draft manuscript via Scribe Pod\n"
        elif status['presentations'] == 0:
            report += "1. Create presentation via Podium Pod\n"
        else:
            report += "1. Review and finalize all outputs\n"
            report += "2. Consider archiving this project\n"
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report)
        
        return report


def main():
    """CLI for system management"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="AI+Neuroscience Multi-Agent Research System Manager"
    )
    parser.add_argument(
        "command",
        choices=["list", "status", "archive", "clean", "report", "vectordb"],
        help="Management command"
    )
    parser.add_argument(
        "--pod",
        help="Filter agents by pod (for 'list' command)"
    )
    parser.add_argument(
        "--project",
        help="Project name (for 'archive' command)"
    )
    parser.add_argument(
        "--keep-memory",
        action="store_true",
        help="Keep memory when cleaning (for 'clean' command)"
    )
    
    args = parser.parse_args()
    manager = ResearchSystemManager()
    
    if args.command == "list":
        agents = manager.list_agents(args.pod)
        for pod, agent_list in agents.items():
            print(f"\n{pod.upper()} Pod:")
            for agent in agent_list:
                print(f"  - @{agent}")
    
    elif args.command == "status":
        status = manager.get_project_status()
        print(json.dumps(status, indent=2))
    
    elif args.command == "archive":
        if not args.project:
            print("Error: --project name required")
            return
        manager.archive_project(args.project)
    
    elif args.command == "clean":
        confirm = input("Clean workspace? (y/N): ")
        if confirm.lower() == 'y':
            manager.clean_workspace(keep_memory=args.keep_memory)
    
    elif args.command == "report":
        report = manager.generate_project_report()
        print(report)
    
    elif args.command == "vectordb":
        db_status = manager.check_vector_db_status()
        print("\n📊 Vector Database Status:")
        print(json.dumps(db_status, indent=2))


if __name__ == "__main__":
    main()
