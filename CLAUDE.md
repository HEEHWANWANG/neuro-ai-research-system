# AI+Neuroscience Multi-Agent Research System
# Claude Code Project Configuration

## Project Overview

This is a hierarchical multi-agent research system designed for AI+Neuroscience research. It follows the "Generate-Debate-Evolve" paradigm to accelerate scientific discovery.

## Architecture

**Supervisor Agent** (MCP Server)
- Orchestrates all pods and agents
- Manages task queues and parallelization
- Mediates external tool communications
- User's primary interface

**Hypothesis Engine Pod** 💡
- 6 specialized agents
- Generates and evolves research hypotheses
- Runs simulated scientific debates
- Output: Top 3 evolved hypotheses

**The Forge Pod** 🔬 ⚡ [SuperClaude Framework Integrated]
- 5 specialized agents
- Implements hypotheses as code via SuperClaude `/sc:` commands
- Runs experiments and analysis with test-driven development
- Output: Production-ready code + Experimental results
- **Integration**: Uses SuperClaude's `/sc:design`, `/sc:implement`, `/sc:test`, `/sc:analyze`, `/sc:improve` commands

**The Scribe Pod** ✍️
- 3 specialized agents
- Drafts scientific manuscripts
- Manages citations and references
- Output: Publication-ready papers

**The Podium Pod** 🎤
- 4 specialized agents
- Creates presentation materials
- Tailors content to audiences
- Output: Conference-ready talks

## Usage

### Quick Start
```
@supervisor
I want to [your research goal]
```

### Direct Pod Access
```
@hypothesis-coordinator  # For hypothesis generation
@forge-coordinator       # For implementation
@scribe-coordinator      # For writing
@podium-coordinator      # For presentations
```

## Workflow Patterns

1. **New Research**: Supervisor → Hypothesis Engine → Forge → Scribe → Podium
2. **Iteration**: Forge → Hypothesis Engine (reflection) → Forge → Analysis
3. **Publication**: Gather results → Scribe → Podium

## SuperClaude Framework Integration (Forge Pod)

The **Forge Pod** is now fully integrated with SuperClaude's `/sc:` command system for production-quality code development:

### Available SuperClaude Commands for Forge Pod

| Command | Purpose | Forge Use Case |
|---------|---------|---|
| **`/sc:design`** | Architecture & API design | Design data pipelines and model architectures before implementation |
| **`/sc:implement`** | Feature implementation | Implement PyTorch models, data processors, analysis scripts |
| **`/sc:test`** | Comprehensive testing | Test-driven development - unit, integration, and E2E tests |
| **`/sc:analyze`** | Code quality & performance analysis | Identify bottlenecks, verify code correctness, security analysis |
| **`/sc:improve`** | Refactoring & optimization | Optimize performance, improve readability, reduce technical debt |
| **`/sc:troubleshoot`** | Debugging | Systematic root cause analysis of failures and errors |
| **`/sc:explain`** | Code explanation | Explain algorithms, model architectures, implementation details |
| **`/sc:document`** | Documentation | Generate API docs, function docstrings, README files |
| **`/sc:build`** | Build & deployment | Package code, manage dependencies, create deployment artifacts |
| **`/sc:cleanup`** | Code cleanup | Remove dead code, organize project structure, maintain hygiene |

### Forge Pod Development Workflow

```
Hypothesis Input (from Hypothesis Engine)
        ↓
/sc:design → Define architecture and APIs
        ↓
/sc:implement → Write production-ready code
        ↓
/sc:test → Comprehensive test coverage
        ↓
/sc:analyze → Verify quality and performance
        ↓
/sc:improve → Optimize and refactor
        ↓
/sc:document → Generate documentation
        ↓
Output: Ready for Scribe/Podium pods
```

### Key Benefits of SuperClaude Integration

1. **Quality Assurance**: Every code step includes design, implementation, testing, and analysis
2. **Reproducibility**: Test-driven development ensures results are reproducible
3. **Documentation**: Automatic documentation generation for all code
4. **Optimization**: Performance analysis and improvement built-in
5. **Debugging**: Systematic troubleshooting for issues
6. **Scalability**: Organized, maintainable code structure

## Best Practices

- Always start through @supervisor for complex workflows
- Let evolution loops complete (3 iterations recommended)
- **For Forge Pod**: Use `/sc:` commands throughout entire development cycle (not ad-hoc coding)
- Review `.claude/workspace/hypotheses/research_overview.md` before implementation
- Archive completed work by date
- Use "think hard" for complex research planning
- Ensure all Forge code includes tests (`/sc:test`), analysis (`/sc:analyze`), and documentation (`/sc:document`)

## External Dependencies

- Python 3.8+ (for data processing and ML)
- PyTorch (for neural network models)
- LaTeX (for document generation)
- Git (for version control)

## Workspace

All outputs stored in `.claude/workspace/`:
- `hypotheses/` - Generated hypotheses and debates
- `experiments/` - Code, data, and results
- `papers/` - Manuscripts and references
- `presentations/` - Slides and scripts
- `memory/` - Vector database and context

## Configuration

Copy `.env.template` to `.env` and configure:
- API keys for LLM services
- Academic database access
- Vector DB settings
- System parameters

## Academic Research Integration

The **Hypothesis Engine Pod** has access to three academic research MCP servers:

### ArXiv MCP Server
- **Access**: 1.2M+ papers from arXiv.org
- **Best For**: Latest AI/ML techniques, preprints, computer science papers
- **Tools**: `search_arxiv`, `get_arxiv_paper`, `deep_paper_analysis`
- **Install**: `npx -y @smithery/cli install arxiv-mcp-server --client claude`

### Google Scholar MCP Server
- **Access**: Broad academic search with citation counts and author profiles
- **Best For**: Citation impact, author networks, publication discovery
- **Tools**: `search_google_scholar_keywords`, `get_author_profile`
- **Install**: `npx -y @smithery/cli install google-scholar-mcp-server --client claude`

### PubMed MCP Server
- **Access**: 30M+ biomedical articles from PubMed/NIH
- **Best For**: Clinical evidence, disease-specific literature, biomedical research
- **Tools**: `search_pubmed_keywords`, `search_pubmed_advanced`, `download_pubmed_pdf`
- **Install**: `npx -y @smithery/cli install @JackKuo666/pubmed-mcp-server --client claude`

### Usage Example
```
@neurolit-agent
"Search literature on Vision Transformers for brain imaging:
- ArXiv: Latest techniques
- Google Scholar: Citation impact
- PubMed: Clinical validation"
```

See `.claude/MCP_ACADEMIC_SEARCH_INTEGRATION.md` for detailed configuration and usage.

## Notes

- This system uses Claude Code's subagent feature
- Each agent has specialized system prompts
- Agents communicate via filesystem (prevents information loss)
- Parallel execution maximizes test-time compute
- Extended thinking ("think hard") used for complex planning
- Academic search MCPs enable literature-driven hypothesis generation
- Forge Pod uses SuperClaude framework for production-quality code

---

For detailed documentation:
- **Forge Pod Integration**: See `.claude/FORGE_POD_SUPERCLAUADE_INTEGRATION.md`
- **Academic Search MCPs**: See `.claude/MCP_ACADEMIC_SEARCH_INTEGRATION.md`
- **Project Overview**: See README.md
