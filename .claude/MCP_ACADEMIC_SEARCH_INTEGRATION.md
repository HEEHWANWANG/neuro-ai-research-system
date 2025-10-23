# 📚 Academic Research MCP Integration Guide

**Date**: October 23, 2025
**Purpose**: Enable Hypothesis Engine Pod to search and analyze academic papers from ArXiv, Google Scholar, and PubMed
**Status**: Integration Planning & Implementation

---

## Overview

Your AI+Neuroscience research system includes a **Hypothesis Engine Pod** that generates and validates research hypotheses. This Pod needs access to academic literature to:
1. Survey existing work
2. Identify research gaps
3. Generate informed hypotheses
4. Validate against existing approaches

Three MCP servers provide this capability:

| MCP Server | Primary Source | Best For |
|-----------|---|---|
| **ArXiv MCP** | arXiv.org | Preprints, CS/ML/Physics papers, latest research |
| **Google Scholar MCP** | Google Scholar | Broad academic search, citation counts, author profiles |
| **PubMed MCP** | PubMed/NIH | Biomedical literature, clinical studies, neuroscience papers |

---

## 1. ArXiv MCP Server

### What It Does
Provides programmatic access to arXiv repository (1.2M+ physics, CS, math, biology papers)

### Core Tools
1. **`search_arxiv`** - Search papers by query, subject category, date range
2. **`get_arxiv_paper`** - Download full paper by arXiv ID
3. **`list_arxiv_papers`** - List all locally cached papers
4. **`read_arxiv_paper`** - Read cached paper content
5. **`deep_paper_analysis`** - Systematic paper evaluation

### Installation

**Method 1: Via Smithery (Recommended)**
```bash
npx -y @smithery/cli install arxiv-mcp-server --client claude
```

**Method 2: Via UV**
```bash
uv tool install arxiv-mcp-server
```

**Method 3: Development Setup**
```bash
git clone https://github.com/blazickjp/arxiv-mcp-server.git
cd arxiv-mcp-server
uv pip install -e ".[test]"
```

### Claude Configuration

Add to `.claude/mcp_config.json`:
```json
{
  "mcpServers": {
    "arxiv": {
      "command": "uv",
      "args": ["tool", "run", "arxiv-mcp-server", "--storage-path", "/Users/apple/Desktop/neuro-ai-research-system/.claude/workspace/papers/arxiv"]
    }
  }
}
```

### Example Usage in Hypothesis Engine

```
@neurolit-agent
"Search arXiv for recent papers on Vision Transformers for medical imaging.
Command: search_arxiv(query='Vision Transformer medical imaging',
                     subject_category='eess.IV',
                     start_date='2023-01-01')"
```

### Use Cases for Your System

- **Literature Review**: `@neurolit-agent` searches for foundation models in neuroimaging
- **Trend Analysis**: `@ai-trend-agent` identifies latest AI techniques applicable to brain imaging
- **Baseline Identification**: `@reflection-agent` finds comparable work for hypothesis validation
- **Paper Deep Dive**: `@meta-review-agent` analyzes top papers from search results

---

## 2. Google Scholar MCP Server

### What It Does
Enables search of Google Scholar (broader than arXiv, includes journals, conferences, theses)

### Core Tools
1. **`search_google_scholar_keywords`** - Search by keywords with result limits
2. **`search_google_scholar_advanced`** - Advanced search with author, year, journal filters
3. **`get_author_profile`** - Retrieve researcher profile and publications
4. **`get_paper_metadata`** - Extract structured paper information

### Installation

**Method 1: Via Smithery**
```bash
npx -y @smithery/cli install google-scholar-mcp-server --client claude
```

**Method 2: Manual Setup**
```bash
git clone https://github.com/JackKuo666/Google-Scholar-MCP-Server.git
cd Google-Scholar-MCP-Server
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

**Method 3: Docker**
```bash
docker pull jackuo666/google-scholar-mcp-server:latest
docker run -p 5000:5000 jackuo666/google-scholar-mcp-server:latest
```

### Claude Configuration

```json
{
  "mcpServers": {
    "google_scholar": {
      "command": "python",
      "args": ["/path/to/google_scholar_server.py"]
    }
  }
}
```

### Example Usage

```
@neurolit-agent
"Search Google Scholar for papers on fMRI analysis with deep learning.
Command: search_google_scholar_keywords(
  query='fMRI deep learning analysis',
  num_results=20
)"
```

### Key Advantages
- **Citation Counts**: See how many times papers are cited
- **Author Profiles**: Find leading researchers in your field
- **Broad Coverage**: Includes journals, conferences, theses
- **Relevance Ranking**: Results ranked by Google Scholar algorithm

### Use Cases for Your System

- **Author Discovery**: Find leading neuroscience AI researchers
- **Citation Network**: Understand influence and relationships between papers
- **Impact Assessment**: Compare citation counts of different approaches
- **Researcher Profiles**: Get publication history of key scientists

---

## 3. PubMed MCP Server

### What It Does
Provides access to PubMed/NIH biomedical literature database (30M+ articles)

### Core Tools
1. **`search_pubmed_keywords`** - Search by keywords
2. **`search_pubmed_advanced`** - Advanced search with MeSH terms, date range, etc.
3. **`get_pubmed_article_metadata`** - Fetch article details by PMID
4. **`download_pubmed_pdf`** - Download full-text PDFs (when available)
5. **`deep_paper_analysis`** - Comprehensive article evaluation

### Installation

**Method 1: Via Smithery (Recommended)**
```bash
npx -y @smithery/cli install @JackKuo666/pubmed-mcp-server --client claude
```

**Method 2: Manual Setup**
```bash
git clone https://github.com/JackKuo666/PubMed-MCP-Server.git
cd PubMed-MCP-Server
pip install -r requirements.txt
```

### Claude Configuration

```json
{
  "mcpServers": {
    "pubmed": {
      "command": "python",
      "args": ["-m", "pubmed-mcp-server"]
    }
  }
}
```

### Example Usage

```
@neurolit-agent
"Search PubMed for clinical neuroimaging studies on Alzheimer's disease.
Command: search_pubmed_advanced(
  query='Alzheimer neuroimaging deep learning',
  date_range='2022-2025',
  result_limit=50
)"
```

### Key Advantages
- **Clinical Focus**: Clinical trials, patient studies
- **Structured Data**: MeSH terms, PMID standard identifiers
- **Full-Text PDFs**: Many articles available as PDFs
- **Medical Authority**: NIH/NLM curated database

### Use Cases for Your System

- **Clinical Validation**: Find clinical studies relevant to BrainVLM applications
- **Disease Datasets**: Discover neuroimaging datasets for Alzheimer's, Parkinson's, etc.
- **Medical Terminology**: Understand medical context for brain imaging
- **Clinical Evidence**: Support hypothesis with clinical research evidence

---

## Integration Architecture

### How These MCPs Fit Into Your System

```
HYPOTHESIS ENGINE POD
        ↓
    Agents:
    ├─ @neurolit-agent
    │  └─ Uses: ArXiv MCP + Google Scholar MCP + PubMed MCP
    │     Task: Survey literature, identify gaps, propose hypotheses
    │
    ├─ @ai-trend-agent
    │  └─ Uses: ArXiv MCP + Google Scholar MCP
    │     Task: Track AI trends, latest techniques applicable to brain imaging
    │
    ├─ @reflection-agent
    │  └─ Uses: All three MCPs
    │     Task: Find comparable work, validate hypothesis feasibility
    │
    ├─ @ranking-agent
    │  └─ Uses: Google Scholar (citations) + PubMed (clinical evidence)
    │     Task: Rank hypotheses by evidence strength
    │
    └─ @evolution-agent
       └─ Uses: ArXiv MCP + PubMed MCP
          Task: Find papers with improved techniques to evolve hypothesis
```

### Data Flow

```
Research Goal
    ↓
@supervisor decomposes
    ↓
@neurolit-agent
├─ "Search for fMRI + Vision Transformer papers"
│  └─ ArXiv MCP: search_arxiv(query='Vision Transformer fMRI')
│     → Returns: [paper1, paper2, paper3, ...]
│
├─ "Find leading researchers in brain imaging AI"
│  └─ Google Scholar MCP: search_google_scholar_advanced(
│                            author='...', field='medical imaging')
│     → Returns: [author_profile1, author_profile2, ...]
│
└─ "Find clinical evidence for disease prediction"
   └─ PubMed MCP: search_pubmed_advanced(
                    query='neuroimaging disease prediction',
                    date_range='2022-2025')
      → Returns: [clinical_paper1, clinical_paper2, ...]

All results analyzed → Hypothesis Engine generates informed hypotheses
    ↓
Hypotheses sent to Forge Pod for implementation
```

---

## Configuration for Your Project

### Step 1: Create MCP Configuration File

Create `.claude/mcp_servers_config.json`:

```json
{
  "mcpServers": {
    "arxiv": {
      "command": "uv",
      "args": ["tool", "run", "arxiv-mcp-server", "--storage-path", ".claude/workspace/papers/arxiv"],
      "description": "ArXiv paper search and analysis",
      "category": "academic_research"
    },
    "google_scholar": {
      "command": "python",
      "args": ["-m", "google-scholar-mcp-server"],
      "description": "Google Scholar search for broad academic papers",
      "category": "academic_research"
    },
    "pubmed": {
      "command": "python",
      "args": ["-m", "pubmed-mcp-server"],
      "description": "PubMed biomedical literature search",
      "category": "academic_research"
    }
  }
}
```

### Step 2: Update Hypothesis Engine Configuration

Update `.claude/agents/hypothesis-engine-coordinator.md`:

```markdown
## Available MCP Tools

### Academic Paper Search
- **ArXiv MCP**: `search_arxiv`, `get_arxiv_paper`, `deep_paper_analysis`
  - Best for: Preprints, CS/ML papers, latest research

- **Google Scholar MCP**: `search_google_scholar_keywords`, `get_author_profile`
  - Best for: Citation counts, author profiles, broad search

- **PubMed MCP**: `search_pubmed_keywords`, `search_pubmed_advanced`, `download_pubmed_pdf`
  - Best for: Clinical studies, biomedical literature, disease-specific papers

### Recommended Search Strategy
1. Use ArXiv for cutting-edge AI/ML techniques
2. Use Google Scholar for citation impact and author networks
3. Use PubMed for clinical validation and disease-specific literature
```

### Step 3: Update Project CLAUDE.md

Add to `CLAUDE.md`:

```markdown
## Academic Search Integration

The Hypothesis Engine Pod can access academic literature via three MCP servers:

### ArXiv MCP
- Access: 1.2M+ papers from arXiv.org
- Use: Latest AI techniques, preprints
- Tools: search_arxiv, get_arxiv_paper, deep_paper_analysis

### Google Scholar MCP
- Access: Broad academic search with citation counts
- Use: Author profiles, publication networks, citation impact
- Tools: search_google_scholar_keywords, get_author_profile

### PubMed MCP
- Access: 30M+ biomedical articles
- Use: Clinical evidence, disease-specific literature
- Tools: search_pubmed_keywords, download_pubmed_pdf

### Usage in Hypothesis Engine
```
@neurolit-agent
"Search literature on [your topic]"
→ ArXiv MCP: Latest preprints
→ Google Scholar MCP: Citation impact
→ PubMed MCP: Clinical validation
```
```

---

## Installation Instructions for Your System

### Prerequisites
```bash
# Python 3.10+
python --version

# UV (for ArXiv MCP)
pip install uv

# Smithery (optional, but recommended)
npm install -g @smithery/cli
```

### Installation Steps

**Option 1: Via Smithery (Recommended)**

```bash
# Install ArXiv MCP
npx -y @smithery/cli install arxiv-mcp-server --client claude

# Install Google Scholar MCP
npx -y @smithery/cli install google-scholar-mcp-server --client claude

# Install PubMed MCP
npx -y @smithery/cli install @JackKuo666/pubmed-mcp-server --client claude
```

**Option 2: Manual Installation**

```bash
# Create MCP directory
mkdir -p ~/.claude/mcp_servers

# Install ArXiv MCP
uv tool install arxiv-mcp-server

# Install Google Scholar MCP
cd ~/.claude/mcp_servers
git clone https://github.com/JackKuo666/Google-Scholar-MCP-Server.git
cd Google-Scholar-MCP-Server
pip install -r requirements.txt

# Install PubMed MCP
cd ~/.claude/mcp_servers
git clone https://github.com/JackKuo666/PubMed-MCP-Server.git
cd PubMed-MCP-Server
pip install -r requirements.txt
```

---

## Example Workflows

### Workflow 1: Literature Survey for New Topic

```
@neurolit-agent
"I need to understand the state of Vision Transformers in medical imaging.
Please:
1. Search ArXiv for latest ViT papers
2. Find leading researchers via Google Scholar
3. Find clinical applications in PubMed"

Expected Flow:
├─ ArXiv: search_arxiv(query='Vision Transformer medical imaging',
                       subject_category='eess.IV',
                       start_date='2023-01-01')
├─ Google Scholar: search_google_scholar_keywords(query='Vision Transformer medical imaging')
├─ PubMed: search_pubmed_advanced(query='Vision Transformer clinical imaging')
└─ Result: Comprehensive literature overview
```

### Workflow 2: Hypothesis Validation

```
@reflection-agent
"Validate hypothesis: 'Brain Harmony embeddings improve BrainVLM performance'

Please search for:
1. Papers on foundation models for medical imaging (ArXiv)
2. Citation analysis of key papers (Google Scholar)
3. Clinical evidence for multimodal neuroimaging (PubMed)"

Expected Flow:
├─ ArXiv: deep_paper_analysis on top papers
├─ Google Scholar: Get citation counts and author influence
├─ PubMed: Find clinical validation studies
└─ Result: Evidence-based validation assessment
```

### Workflow 3: Find Baseline Methods

```
@evolution-agent
"Find papers with improved fMRI analysis techniques that we could
incorporate into our models.

Search:
1. ArXiv for novel deep learning approaches
2. Google Scholar for highly-cited methods
3. PubMed for validated clinical approaches"

Expected Flow:
├─ ArXiv: search recent papers on fMRI + deep learning
├─ Google Scholar: Filter by citation count (most influential)
├─ PubMed: Find clinically validated methods
└─ Result: Baseline methods to improve upon
```

---

## Best Practices

### 1. Search Strategy
- **ArXiv first** for cutting-edge techniques (preprints, recent)
- **Google Scholar second** for impact and influence (citations, author profiles)
- **PubMed third** for clinical validation and disease-specific literature

### 2. Query Formulation
```
Effective:
- "Vision Transformer fMRI analysis" (specific)
- "brain imaging deep learning 2023-2025" (dated)
- "Alzheimer neuroimaging classification" (disease-specific)

Less Effective:
- "brain" (too broad)
- "imaging" (too generic)
- Without date range (includes outdated papers)
```

### 3. Result Management
- Save important papers locally for reference
- Use deep_paper_analysis for systematic evaluation
- Document citation network for understanding field structure
- Archive results in `.claude/workspace/papers/`

### 4. Citation and Referencing
- Always record PMID for PubMed papers
- Always record arXiv ID for ArXiv papers
- Use Google Scholar to track citation impact
- Build bibliography as you search

---

## Troubleshooting

### ArXiv MCP Issues
- **"Storage path not found"**: Ensure `.claude/workspace/papers/arxiv` directory exists
- **"No results"**: Try broader keywords or different subject categories
- **"Rate limiting"**: ArXiv limits requests; wait before retrying

### Google Scholar MCP Issues
- **"Connection timeout"**: Google Scholar may detect automated access; retry later
- **"No results"**: Try simpler keywords without special characters
- **"Author not found"**: Full name required; try "firstname lastname"

### PubMed MCP Issues
- **"Invalid PMID"**: Verify PMID format (should be numeric)
- **"PDF not available"**: Not all PubMed papers have free full text
- **"Search timeout"**: Try narrower date range or specific MeSH terms

---

## Integration Roadmap

### Phase 1: Installation (Immediate)
- [ ] Install ArXiv MCP via Smithery
- [ ] Install Google Scholar MCP
- [ ] Install PubMed MCP
- [ ] Configure in MCP config
- [ ] Test each MCP independently

### Phase 2: Hypothesis Engine Integration (Week 1)
- [ ] Update @neurolit-agent with MCP capabilities
- [ ] Create search templates for common queries
- [ ] Test literature survey workflow
- [ ] Document best practices

### Phase 3: Optimization (Week 2)
- [ ] Implement caching strategy for papers
- [ ] Create paper organization system
- [ ] Build bibliography database
- [ ] Integrate with Scribe Pod for citation management

### Phase 4: Advanced Features (Month 1)
- [ ] Automated literature review generation
- [ ] Citation network visualization
- [ ] Author influence analysis
- [ ] Trend detection across papers

---

## Summary

Your Hypothesis Engine Pod can now access academic literature through three complementary MCP servers:

| Tool | Coverage | Use |
|------|----------|-----|
| **ArXiv MCP** | 1.2M+ preprints | Latest AI/ML techniques |
| **Google Scholar MCP** | Billions of papers | Citation impact, author profiles |
| **PubMed MCP** | 30M+ biomedical articles | Clinical validation, disease studies |

These integrate seamlessly into your research workflow:
1. **Literature Discovery** - Find relevant papers
2. **Hypothesis Generation** - Informed by existing work
3. **Validation** - Support hypotheses with evidence
4. **Publication** - Reference papers in manuscripts

Your AI+Neuroscience research system is now equipped for evidence-based hypothesis generation! 🔬📚
