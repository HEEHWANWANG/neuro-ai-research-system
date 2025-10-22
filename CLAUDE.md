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

**The Forge Pod** 🔬
- 5 specialized agents  
- Implements hypotheses as code
- Runs experiments and analysis
- Output: Experimental results

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

## Best Practices

- Always start through @supervisor for complex workflows
- Let evolution loops complete (3 iterations recommended)
- Review `.claude/workspace/hypotheses/research_overview.md` before implementation
- Archive completed work by date
- Use "think hard" for complex research planning

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

## Notes

- This system uses Claude Code's subagent feature
- Each agent has specialized system prompts
- Agents communicate via filesystem (prevents information loss)
- Parallel execution maximizes test-time compute
- Extended thinking ("think hard") used for complex planning

---

For detailed documentation, see README.md
