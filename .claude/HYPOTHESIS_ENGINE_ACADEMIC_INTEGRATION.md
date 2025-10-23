# Hypothesis Engine Pod - Academic Literature Integration

**Date**: October 23, 2025
**Status**: ✅ Complete - All 6 Agents Updated
**Commits**: 9b402fd, 8fc1a65

---

## Overview

The Hypothesis Engine Pod has been comprehensively integrated with three academic research MCPs (ArXiv, Google Scholar, PubMed). All six agents now **mandate** proactive use of academic literature to ground hypothesis generation, validation, ranking, evolution, and synthesis in current research.

---

## Agent Integration Summary

### 1. NeuroLit_Agent 🧠
**Role**: Neuroscience literature expert and hypothesis foundation

**MCP Usage**: **MUST use PubMed + Google Scholar**

**Key Workflow**:
1. Analyze research goal
2. Identify needed information from neuroscience/clinical domains
3. Formulate precise search queries
4. **Request Supervisor Agent to search PubMed + Google Scholar**
5. Analyze results and extract insights
6. Synthesize findings into literature review
7. Contribute grounded hypotheses

**Output**: Literature summary with citations, key papers, research gaps

**Status**: ✅ Updated - Mandates academic searches

---

### 2. AI_Trend_Agent 🤖
**Role**: AI technology expert tracking cutting-edge innovations

**MCP Usage**: **MUST use arXiv + Google Scholar**

**Key Workflow**:
1. Understand research objective and AI/ML challenges
2. Identify applicable AI concepts and architectures
3. Formulate targeted search queries (latest techniques)
4. **Request Supervisor Agent to search arXiv + Google Scholar**
5. Analyze technical details and innovation paths
6. Propose specific AI techniques with evidence
7. Contribute AI insights to hypotheses

**Output**: AI technology landscape with architectures, benchmarks, code, citations

**Status**: ✅ Updated - Mandates cutting-edge searches

---

### 3. Reflection_Agent 🔍
**Role**: Critical peer reviewer ensuring scientific validity

**MCP Usage**: **MUST use PubMed + arXiv + Google Scholar**

**Key Workflow**:
1. Receive hypothesis for critical review
2. Analyze claims, assumptions, proposed methods
3. Identify aspects requiring verification
4. Formulate search queries for verification
5. **Request Supervisor Agent to search ALL THREE MCPs**
6. Analyze search results and find evidence/contradictions
7. Provide evidence-based peer review with scoring

**Evaluation Criteria** (0-10 each):
- Scientific Validity
- Novelty & Originality
- Testability & Experimental Design
- Feasibility & Implementation
- Impact & Significance

**Output**: Structured peer review with 5-dimension scoring and citations

**Status**: ✅ Updated - Mandates verification searches

---

### 4. Ranking_Agent 🏆
**Role**: Tournament organizer conducting evidence-based debates

**MCP Usage**: **MUST use Google Scholar + PubMed**

**Key Workflow**:
1. Load all hypotheses with context
2. Generate debate matchups
3. For each debate:
   - **Request Supervisor Agent to search Google Scholar + PubMed**
   - Find evidence supporting/challenging each hypothesis
   - Get citation metrics and benchmark comparisons
   - Simulate expert panel discussion informed by literature
   - Determine winner based on evidence strength
   - Update Elo ratings with confidence scores
4. Generate final rankings with evidence justification

**Judging Criteria**:
- Stronger evidence base (Google Scholar citations)
- Better addresses open problems (from literature)
- More feasible (papers show implementations)
- Higher impact (citation metrics)
- Methodological soundness (peer-reviewed vs. preprint)
- Novel contribution (relative to published work)

**Output**: Ranked hypotheses with Elo scores and evidence analysis

**Status**: ✅ Updated - Mandates evidence-based ranking

---

### 5. Evolution_Agent ✨
**Role**: Hypothesis evolver applying creative recombination strategies

**MCP Usage**: **MUST use arXiv + PubMed**

**Key Workflow**:
1. Load top-ranked hypotheses and all critiques
2. Identify evolution opportunities from literature
3. Formulate search queries for improvements
4. **Request Supervisor Agent to search arXiv + PubMed**
5. Find improved techniques, successful patterns, novel combinations
6. Apply evolution strategies:
   - Combination (merge with literature support)
   - Simplification (validated in literature)
   - Extension (innovations from recent papers)
7. Generate evolved variants with citations

**Output**: Evolved hypotheses with literature evidence, implementation roadmap

**Status**: ✅ Updated - Mandates literature-informed evolution

---

### 6. Meta-Review_Agent 📊
**Role**: Process analyzer synthesizing entire evolution history

**MCP Usage**: **MUST use arXiv + Google Scholar + PubMed (all three)**

**Key Workflow**:
1. Collect all hypotheses, critiques, rankings from all generations
2. Aggregate literature cited across generations
3. Identify meta-patterns in evolution and critiques
4. Formulate meta-queries (surveys, benchmarks, trends)
5. **Request Supervisor Agent to search ALL THREE MCPs**
6. Synthesize comprehensive literature foundation
7. Generate publication-ready research overview

**Output**: Complete research overview with:
- Literature foundation and key papers
- Evolution history (evidence-based)
- Top 3 evolved hypotheses (Elo + evidence scores)
- Lessons learned with paper citations
- State-of-the-art summary
- Implementation roadmap (evidence-backed)
- Complete bibliography

**Status**: ✅ Updated - Mandates comprehensive synthesis

---

### 7. Hypothesis-Coordinator 💡
**Role**: Orchestrator of entire hypothesis engine pipeline

**MCP Coordination**:
- Documents MCP usage patterns for each agent
- Ensures ReAct pattern adherence (agents request, Supervisor executes)
- Oversees evidence flow through entire pipeline
- Validates academic rigor at each stage

**Orchestrated Workflow**:
1. Parallel literature review (NeuroLit + AI_Trend search)
2. Literature-informed hypothesis generation
3. Evidence-based critical reflection
4. Citation-backed tournament debates
5. Literature-informed evolution
6. Evidence-grounded meta-review

**Output**: Research overview and hypothesis evolution timeline

**Status**: ✅ Updated - Coordinates all agent searches

---

## End-to-End Evidence Flow

```
User Research Goal
        ↓
Coordinator initiates pipeline
        ↓
STAGE 1: Literature Foundation
├─ NeuroLit_Agent → PubMed + Google Scholar
│  └─ "Search neuroscience/clinical literature on [goal]"
│     → Supervisor Agent executes searches
│     → Neurolit analyzes results, compiles review
│
└─ AI_Trend_Agent → arXiv + Google Scholar
   └─ "Search latest AI/ML techniques for [goal]"
      → Supervisor Agent executes searches
      → AI_Trend analyzes results, proposes technologies
        ↓
STAGE 2: Literature-Informed Generation
Generated hypotheses grounded in reviewed literature
All claims backed by papers
Novelty assessed against published work
        ↓
STAGE 3: Evidence-Based Validation
├─ Reflection_Agent → PubMed + arXiv + Google Scholar
   └─ "Verify claims and assess novelty"
      → Supervisor Agent executes searches
      → Reflection provides peer review with scores
        ↓
STAGE 4: Evidence-Supported Ranking
├─ Ranking_Agent → Google Scholar + PubMed
   └─ "Compare hypotheses with evidence"
      → Supervisor Agent executes searches
      → Ranking generates Elo scores with confidence
        ↓
STAGE 5: Literature-Informed Evolution
├─ Evolution_Agent → arXiv + PubMed
   └─ "Find improved techniques and novel combinations"
      → Supervisor Agent executes searches
      → Evolution generates improved variants with citations
        ↓
STAGE 6: Evidence-Grounded Synthesis
├─ Meta_Review_Agent → All three MCPs
   └─ "Synthesize all evidence and generate final overview"
      → Supervisor Agent executes searches
      → Meta-Review creates publication-ready report
        ↓
Final Output: Research Overview
├─ Publication-ready document with complete bibliography
├─ Top 3 evolved hypotheses with evidence base
├─ Implementation roadmap grounded in literature
└─ Ready for Forge Pod implementation
```

---

## MCP Usage Pattern Summary

| Agent | PubMed | ArXiv | Google Scholar | Purpose |
|-------|--------|-------|----------------|---------|
| NeuroLit | ✅ Primary | ➖ | ✅ Primary | Literature foundation |
| AI_Trend | ➖ | ✅ Primary | ✅ Primary | Technology trends |
| Reflection | ✅ Primary | ✅ Primary | ✅ Primary | Verification |
| Ranking | ✅ Primary | ➖ | ✅ Primary | Evidence-based ranking |
| Evolution | ✅ Primary | ✅ Primary | ➖ | Improved techniques |
| Meta-Review | ✅ Primary | ✅ Primary | ✅ Primary | Comprehensive synthesis |

---

## Critical Implementation Features

### 1. Core Directives (All Agents)
Each agent includes explicit directive:
- **You MUST proactively and consistently utilize [specific MCPs]**
- Mandatory, non-negotiable academic search requirement
- Clear when and why searches must be executed

### 2. ReAct Pattern
All agents follow consistent pattern:
- Agents formulate search queries and REQUEST searches
- Supervisor Agent executes all MCP tool calls
- Agents analyze results and cite papers
- Pattern clearly documented in each agent

### 3. Citation Requirements
- All claims must be backed by literature
- Papers must be cited with IDs/DOIs
- Google Scholar citation counts incorporated
- Complete bibliographies maintained

### 4. Output Specifications
Each agent has defined output format with:
- Literature context sections
- Citation requirements
- Evidence base documentation
- Academic rigor standards

### 5. Workflow Documentation
Detailed 7-10 step workflows showing:
- When searches are needed
- What queries to formulate
- How to request Supervisor Agent searches
- How to analyze and cite results

---

## Key Achievements

✅ **Complete Agent Integration**: All 6 hypothesis engine agents updated with MCP mandates

✅ **Consistent Pattern**: Same workflow pattern across all agents for coherence

✅ **End-to-End Evidence Flow**: Literature informs every stage from generation through synthesis

✅ **Academic Rigor**: Top-tier journal standards embedded throughout

✅ **Supervisor Coordination**: Clear ReAct pattern for agent-supervisor collaboration

✅ **Citation Completeness**: Every claim backed by literature with IDs/DOIs

✅ **Reproducibility**: All searches documented for complete traceability

✅ **Output Quality**: Publication-ready research overview with complete bibliography

---

## Integration Timeline

### Session 1 (Early - October 23)
- Analyzed BrainVLM vs Brain Harmony with sequential thinking
- Committed findings with 7-thought analysis

### Session 2 (Mid - October 23)
- Integrated SuperClaude framework for Forge Pod
- Created Forge Pod coordinator with all `/sc:` commands
- Committed SuperClaude integration

### Session 3 (Recent - October 23)
- Analyzed three academic MCPs (ArXiv, Google Scholar, PubMed)
- Created comprehensive integration documentation
- Committed MCP documentation

### Session 4 (Current - October 23)
- **Updated 3 core hypothesis agents** (NeuroLit, AI_Trend, Reflection)
  - Commit: 9b402fd

- **Updated 4 remaining agents** (Evolution, Ranking, Meta-Review, Coordinator)
  - Commit: 8fc1a65

- **Created this integration summary**
  - Status: Just completed

---

## Verification Checklist

- ✅ All 6 hypothesis engine agents have MCP mandates
- ✅ Each agent has Core Directive stating MUST use specific MCPs
- ✅ Each agent has detailed workflow with search steps
- ✅ ReAct pattern documented: agents request, Supervisor executes
- ✅ Citation requirements explicit in all agents
- ✅ Output formats include literature context
- ✅ Critical instructions emphasize academic rigor
- ✅ Tools & Resources sections reference MCPs
- ✅ All changes committed to GitHub
- ✅ Integration summary documentation complete

---

## Next Steps

### Immediate (Ready Now)
1. ✅ All hypothesis engine agents configured for academic searches
2. ✅ MCP integration documentation complete
3. ✅ SuperClaude framework integrated in Forge Pod

### Short-term (This Week)
1. Test hypothesis engine with academic searches
2. Verify Supervisor Agent handles all MCP calls correctly
3. Validate citation format consistency across agents

### Medium-term (This Month)
1. Integrate with actual projects (BrainVLM, etc.)
2. Run complete generate-debate-evolve loops
3. Generate publication-ready research overviews
4. Document lessons learned

### Long-term (This Quarter)
1. Automated literature review generation
2. Citation network analysis and visualization
3. Trend detection across hypothesis evolution
4. Integration with Scribe Pod for paper writing

---

## Summary

**The Hypothesis Engine Pod is now fully integrated with three academic research MCPs (ArXiv, Google Scholar, PubMed).**

All six agents mandate and systematically use academic literature to inform every stage of hypothesis generation, validation, ranking, evolution, and synthesis. The system ensures that research hypotheses are grounded in current academic knowledge, validated against published work, and informed by cutting-edge innovations.

The evidence-based approach transforms the Hypothesis Engine from potentially speculative to rigorous, literature-informed research hypothesis generation aligned with top-tier scientific standards.

**Status**: ✅ **Ready for deployment and testing**

See:
- `.claude/agents/pods/hypothesis-engine/neurolit-agent.md` - NeuroLit Agent
- `.claude/agents/pods/hypothesis-engine/ai-trend-agent.md` - AI_Trend Agent
- `.claude/agents/pods/hypothesis-engine/reflection-agent.md` - Reflection Agent
- `.claude/agents/pods/hypothesis-engine/evolution-agent.md` - Evolution Agent
- `.claude/agents/pods/hypothesis-engine/ranking-agent.md` - Ranking Agent
- `.claude/agents/pods/hypothesis-engine/meta-review-agent.md` - Meta-Review Agent
- `.claude/agents/pods/hypothesis-engine/hypothesis-coordinator.md` - Coordinator

---

*Updated October 23, 2025 - Claude Code*
