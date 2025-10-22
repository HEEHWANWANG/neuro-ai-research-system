# Usage Examples for AI+Neuroscience Multi-Agent Research System

## Table of Contents
1. [Quick Start](#quick-start)
2. [Example Workflows](#example-workflows)
3. [Advanced Usage](#advanced-usage)
4. [Troubleshooting](#troubleshooting)

## Quick Start

### Initial Setup

```bash
# Navigate to project directory
cd /path/to/neuro-ai-research-system

# Copy environment template
cp .env.template .env

# Edit .env with your API keys
nano .env

# Start Claude Code
claude
```

### Your First Research Project

```
@supervisor

I want to develop a novel graph neural network architecture for 
modeling functional brain connectivity from fMRI data. The goal is 
to predict cognitive states better than existing methods.
```

**What happens:**
1. Supervisor analyzes your goal
2. Invokes Hypothesis Engine (parallel literature review)
3. Generates 7 initial hypotheses
4. Runs 3 evolution loops (debates + improvements)
5. Presents top 3 evolved hypotheses
6. Awaits your selection for implementation

---

## Example Workflows

### Workflow 1: New Research from Scratch

#### Step 1: Hypothesis Generation
```
@supervisor

Research Goal: Develop attention mechanisms that capture temporal 
dynamics in fMRI time-series better than sliding window approaches.

Requirements:
- Novel architecture (not just incremental improvement)
- Computationally efficient for clinical use
- Interpretable attention weights
```

**Expected Output** (after ~30-60 min):
- Literature review (neuroscience + AI)
- 3 evolved hypotheses with evidence
- Comparative analysis
- Implementation roadmap

#### Step 2: Select and Implement

```
@supervisor

I want to implement Hypothesis #2 (the temporal attention mechanism 
with learnable time lags). Please coordinate with the Forge Pod to:
1. Create preprocessing pipeline for HCP fMRI data
2. Implement the model in PyTorch
3. Set up hyperparameter tuning with Optuna
```

**Expected Output** (after ~1-2 hours):
- Preprocessing code (`preprocessing/pipeline.py`)
- Model implementation (`models/temporal_attention_model.py`)
- Training script with logging
- Hyperparameter tuning configuration

#### Step 3: Run Experiments

```
@supervisor

Run experiments comparing our model against:
1. Standard GNN baseline
2. Sliding window attention
3. Reproduce the method from Li et al. 2023 paper

Use 5-fold cross-validation on HCP dataset.
```

**Expected Output**:
- Baseline implementations
- Training logs
- Statistical analysis
- Visualization of results

#### Step 4: Write Paper

```
@supervisor

Draft a manuscript for submission to MICCAI:
- Target length: 8 pages
- Emphasize novelty of temporal attention mechanism
- Include all experimental results
- Prepare for blind review
```

**Expected Output**:
- `papers/draft_manuscript.tex`
- `papers/references.bib`
- Figures and tables ready for submission

#### Step 5: Create Presentation

```
@supervisor

Create a 15-minute conference talk for MICCAI 2025:
- Audience: Medical imaging + ML researchers
- Focus on intuition behind temporal attention
- Show key experimental results
```

**Expected Output**:
- `presentations/slides.tex` (Beamer)
- `presentations/speaking_script.md`
- `presentations/qna_prep.md`

---

### Workflow 2: Iterative Hypothesis Refinement

Sometimes initial hypotheses need refinement based on experimental feedback.

#### Initial Experiment
```
@supervisor

Quick feasibility test: Can we predict task vs rest states from 
fMRI using a simple GNN? Use 10% of HCP data for rapid prototyping.
```

#### Analysis
```
@supervisor

Results show 75% accuracy (baseline: 60%). However, the model 
struggles with transition periods. Invoke Hypothesis Engine to 
generate ideas for handling state transitions.
```

**Hypothesis Engine will:**
1. Reflect on experimental findings
2. Search literature on transition modeling
3. Generate hypotheses specifically for this problem
4. Evolve through debate
5. Propose solutions

#### Re-implementation
```
@supervisor

Implement the top hypothesis (hierarchical temporal modeling) and 
re-run experiments with full dataset.
```

---

### Workflow 3: Literature Review & Gap Analysis

```
@hypothesis-coordinator

Conduct comprehensive literature review on:
- Transformer applications to neuroimaging (last 3 years)
- Graph neural networks for brain connectivity
- Interpretability methods in neuroscience ML

Identify research gaps and propose 5 novel research directions.
```

**Output:**
- Comprehensive literature review
- Gap analysis
- 5 novel hypotheses
- Feasibility assessment for each

---

### Workflow 4: Baseline Reproduction

```
@forge-coordinator

Reproduce the experiments from:
"Deep Graph Convolutional Networks for Predicting Brain Connectivity"
by Zhang et al., NeuroImage 2022

Tasks:
1. Find and set up their code
2. Prepare data in their format
3. Run their experiments
4. Document any differences from paper

Purpose: Establish fair comparison baseline for our new method.
```

---

### Workflow 5: Paper Revision

```
@scribe-coordinator

Revise our manuscript based on reviewer comments:

Reviewer 1:
- "Methods section lacks detail on GNN architecture"
- "Statistical tests not clearly described"

Reviewer 2:
- "Need ablation study on attention components"
- "Discussion should address limitation X"

Please update the manuscript and highlight changes.
```

---

## Advanced Usage

### Parallel Hypothesis Exploration

For exploring multiple research directions simultaneously:

```
@supervisor

I want to explore THREE parallel research directions:

Direction A: Vision Transformers for fMRI
Direction B: Graph Attention Networks for brain connectivity  
Direction C: Self-supervised learning on unlabeled neuroimaging

For each direction:
1. Run separate hypothesis generation
2. Create parallel implementations
3. Compare results after 2 weeks

Use git worktrees for true parallelization.
```

**Implementation:**
```bash
# Create separate worktrees
git worktree add ../direction-a feature/vit-fmri
git worktree add ../direction-b feature/gat-connectivity
git worktree add ../direction-c feature/ssl-neuro

# Launch separate Claude instances
# Terminal 1:
cd ../direction-a && claude
# Work on Direction A

# Terminal 2:
cd ../direction-b && claude
# Work on Direction B

# Terminal 3:
cd ../direction-c && claude
# Work on Direction C
```

### Extended Thinking for Complex Planning

```
@supervisor

ultrathink: Design a comprehensive research program for the next 
6 months combining:
- Novel architecture development
- Large-scale dataset collection
- Multi-site validation study
- Clinical translation pathway

Provide detailed timeline, resource requirements, and risk mitigation.
```

### Meta-Analysis Across Projects

```
@hypothesis-coordinator

Analyze patterns across our last 5 research projects:
- What types of hypotheses led to successful publications?
- Which evolution strategies were most effective?
- Are there recurring critiques we should address upfront?

Use this meta-knowledge to improve future hypothesis generation.
```

---

## Troubleshooting

### Issue: Hypothesis Engine produces similar hypotheses

**Solution:**
```
@hypothesis-coordinator

The last generation produced too similar hypotheses. Please:
1. Increase diversity in initial generation (use different search terms)
2. Apply stronger mutation in evolution phase
3. Penalize similarity in ranking algorithm
```

### Issue: Forge generates non-working code

**Solution:**
```
@forge-coordinator

The generated model code has bugs. Please:
1. Review the code with @pytorch-dev-agent
2. Run unit tests on each component
3. Fix errors iteratively
4. Add error handling and validation
```

### Issue: Need to access previous project's insights

**Solution:**
```
@supervisor

Load insights from archived project "gnn-connectivity-2024":
1. Search memory/vector_db for relevant code snippets
2. Retrieve successful hypothesis patterns
3. Apply learnings to current project
```

### Issue: Experiments taking too long

**Solution:**
```
@supervisor

Experiments are slow. Optimize by:
1. Use smaller dataset for initial tests (10% sample)
2. Reduce hyperparameter search space
3. Use early stopping
4. Profile code to find bottlenecks
5. Consider using faster model (Haiku instead of Sonnet)
```

---

## Tips for Effective Use

### 1. Be Specific in Goals
❌ "Study brain networks"
✓ "Predict Alzheimer's disease progression from longitudinal fMRI connectivity patterns"

### 2. Provide Context
Always mention:
- Target dataset
- Computational constraints
- Timeline
- Specific challenges

### 3. Review Intermediate Outputs
Don't wait until the end:
- Check `research_overview.md` after hypothesis generation
- Review code structure before full training
- Read draft sections as they're written

### 4. Use Checkpoints
```
@supervisor

Before implementing the full pipeline, create checkpoints:
1. Prototype with toy data
2. Validate preprocessing on 1 subject
3. Train model on 10% data
4. Full-scale training only after validation
```

### 5. Maintain Clean Workspace
```bash
# Check project status
python system_manager.py status

# Generate report
python system_manager.py report

# Archive completed work
python system_manager.py archive --project "gnn-fmri-2025"

# Clean for new project
python system_manager.py clean --keep-memory
```

---

## Getting Help

### View Available Agents
```bash
python system_manager.py list
python system_manager.py list --pod hypothesis-engine
```

### Check System Status
```bash
python system_manager.py status
```

### Review Agent Prompts
```bash
# Read agent's system prompt
cat .claude/agents/pods/hypothesis-engine/neurolit-agent.md
```

### Enable Debug Logging
Edit `.env`:
```
LOG_LEVEL=DEBUG
```

---

## Next Steps

1. Try the "Workflow 1" example end-to-end
2. Adapt examples to your specific research question
3. Experiment with different agent combinations
4. Share successful patterns with the research community

Happy researching! 🧠🤖
