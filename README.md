# AI+Neuroscience Multi-Agent Research System

## Overview

This system implements a hierarchical multi-agent architecture for AI+Neuroscience research, following the "Generate-Debate-Evolve" paradigm from AI co-scientist research.

**New Features:**
- ✨ **Persistent Vector DB**: ChromaDB with local SQLite storage
- 🔀 **Version Control Agent**: Automated Git/GitHub management
- 📦 **Complete Package**: Ready-to-use with all dependencies

## Architecture

```
User
  ↓
Supervisor Agent (MCP Server)
  ↓
  ├── Hypothesis Engine Pod (6 agents)
  │   - Generate → Debate → Evolve loop
  │
  ├── The Forge Pod (6 agents)
  │   - Code generation & experimentation
  │   - Git version control
  │
  ├── The Scribe Pod (3 agents)
  │   - Scientific writing & documentation
  │
  └── The Podium Pod (4 agents)
      - Presentation materials
```

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.template .env
# Edit .env with your API keys and settings
```

### 3. Initialize System
```bash
# Initialize workspace and vector database
python system_manager.py status

# Check vector database
python system_manager.py vectordb
```

### 4. Start Research
```bash
cd /path/to/neuro-ai-research-system
claude
```

Then interact with:
```
@supervisor
"I want to develop a novel ViT architecture for fMRI analysis"
```

The Supervisor will automatically:
- Invoke Hypothesis Engine for ideation
- Run evolution loops
- Coordinate implementation via Forge
- Generate documentation via Scribe
- Create presentations via Podium

## Pod Details

### Hypothesis Engine 💡
**Purpose**: Generate and evolve research hypotheses

**Process**:
1. Literature review (neuroscience + AI)
2. Generate initial hypotheses
3. Critical reflection
4. Tournament ranking
5. Evolution through combination/simplification
6. Iterate until convergence

**Output**: Top 3 evolved hypotheses with evidence

### The Forge 🔬
**Purpose**: Implement and validate hypotheses

**Capabilities**:
- Neuroimaging data preprocessing
- PyTorch model development
- Hyperparameter tuning
- Statistical analysis
- Baseline reproduction
- **Git version control** (NEW)

**Output**: Working code, experimental results, version-controlled repository

### The Scribe ✍️
**Purpose**: Document research for publication

**Capabilities**:
- Manuscript drafting (LaTeX)
- Bibliography management
- Language polishing

**Output**: Publication-ready papers

### The Podium 🎤
**Purpose**: Communicate research effectively

**Capabilities**:
- Audience analysis
- Narrative crafting
- Slide design
- Speaking scripts
- Q&A preparation

**Output**: Conference-ready presentations

## Workspace Organization

```
.claude/workspace/
├── hypotheses/
│   ├── literature_review.md
│   ├── generation_1/
│   ├── evolved/
│   └── research_overview.md
│
├── experiments/
│   ├── preprocessing/
│   ├── models/
│   ├── results/
│   └── baselines/
│
├── papers/
│   ├── draft_manuscript.tex
│   └── references.bib
│
├── presentations/
│   ├── audience_profile.md
│   ├── slides.tex
│   └── speaking_script.md
│
└── memory/
    └── vector_db/
```

## External Tools Integration

The Supervisor mediates all external tool calls:

- **LLM APIs**: Claude, Gemini
- **Academic APIs**: arXiv, PubMed, Semantic Scholar
- **Vector DBs**: ChromaDB (local persistent storage)
- **PDF Parsers**: Grobid, Nougat
- **Web Search**: Tavily, Google Search
- **Version Control**: Git, GitHub API
- **Specialized**: AlphaFold, neuroscience databases

## Best Practices

1. **Start with Supervisor**: Always communicate through @supervisor
2. **Trust the Process**: Let evolution loops run (typically 3 generations)
3. **Review Checkpoints**: Check research_overview.md before implementation
4. **Iterate Experiments**: Use Forge → Hypothesis Engine feedback loops
5. **Archive Work**: Move completed projects to dated subdirectories

## Example Workflows

### New Project
```
User: "Investigate graph neural networks for brain connectivity"

→ Supervisor invokes Hypothesis Engine
→ 3 evolution loops (1 hour)
→ Top 3 hypotheses presented
→ User selects hypothesis
→ Forge implements & experiments
→ Results analyzed
→ Scribe drafts paper
→ Podium creates talk
```

### Paper Revision
```
User: "Revise methods section based on reviewer comments"

→ Supervisor invokes Scribe
→ Manuscript Agent updates methods
→ Clarity Agent polishes
→ Biblio Agent checks citations
→ Revised draft delivered
```

## Tips

- Use "think hard" for complex research planning
- Request intermediate checkpoints for long processes
- Archive successful hypotheses for future inspiration
- Maintain clean workspace (use filesystem-manager)

## System Requirements

- Claude Code environment
- Python 3.8+
- Git (for version control)
- LaTeX (for document generation)

## Documentation

- 📖 [README.md](README.md) - This file
- 🗂️ [SUMMARY.md](SUMMARY.md) - Complete system summary
- 📚 [EXAMPLES.md](EXAMPLES.md) - Usage examples
- 💾 [VECTOR_DB_GUIDE.md](VECTOR_DB_GUIDE.md) - Vector database setup
- 🔀 [VERSION_CONTROL_GUIDE.md](VERSION_CONTROL_GUIDE.md) - Git/GitHub guide

## Support

For issues or questions, review:
1. Agent system prompts in `.claude/agents/`
2. Workspace outputs for debugging
3. Error logs in `.claude/workspace/errors.log`
4. Setup guides for Vector DB and Version Control

---

*Built for accelerating AI+Neuroscience discovery through intelligent automation*
