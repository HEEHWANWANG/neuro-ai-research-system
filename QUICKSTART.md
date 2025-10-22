# 🚀 QUICK START GUIDE

## 1. Download the System

The complete multi-agent system has been created at:
```
/mnt/user-data/outputs/neuro-ai-research-system/
```

Download this entire folder to your local machine.

## 2. Verify Structure

After downloading, you should have:
```
neuro-ai-research-system/
├── README.md                 ← Read this first!
├── CLAUDE.md                 ← Claude Code configuration
├── EXAMPLES.md               ← Detailed examples
├── SUMMARY.md                ← Complete system summary
├── .env.template             ← Configuration template
├── generate_agents.py        ← Agent generator
├── system_manager.py         ← Management utilities
└── .claude/
    ├── agents/               ← 20 specialized agents
    │   ├── supervisor/       ← Master orchestrator
    │   ├── pods/            ← 4 functional pods
    │   └── shared/          ← Utilities
    └── workspace/           ← Output directories
```

## 3. Initial Setup

### A. Configure Environment
```bash
cd neuro-ai-research-system
cp .env.template .env
nano .env  # Add your API keys
```

### B. Start Claude Code
```bash
claude
```

## 4. First Research Session

Type in Claude Code:
```
@supervisor

I want to develop a novel attention mechanism for analyzing 
fMRI time-series data. The goal is to capture temporal dynamics 
better than sliding window approaches.
```

## 5. What Happens Next

The Supervisor will:
1. ✅ Analyze your research goal
2. ✅ Invoke Hypothesis Engine pod
3. ✅ Run parallel literature reviews (neuroscience + AI)
4. ✅ Generate 7 initial hypotheses
5. ✅ Execute 3 evolution loops:
   - Critical reflection
   - Tournament debates
   - Evolution of top ideas
6. ✅ Present top 3 evolved hypotheses

**Expected time**: 30-60 minutes

## 6. Continue the Workflow

After receiving hypotheses:
```
@supervisor

Implement Hypothesis #2 using the Forge Pod:
1. Create preprocessing pipeline for HCP fMRI data
2. Build PyTorch model
3. Set up hyperparameter tuning
```

Then proceed to experiments, paper writing, and presentations!

## 7. Key Commands

### System Management
```bash
# Check what agents are available
python system_manager.py list

# Check current project status
python system_manager.py status

# Generate progress report
python system_manager.py report
```

### Claude Code Agents
```
@supervisor                  ← Your main interface
@hypothesis-coordinator      ← Direct hypothesis work
@forge-coordinator          ← Direct implementation
@scribe-coordinator         ← Direct writing
@podium-coordinator         ← Direct presentations
```

## 8. Tips for Success

### DO:
✅ Start with clear, specific research goals
✅ Let evolution loops complete (don't interrupt)
✅ Review intermediate outputs in `.claude/workspace/`
✅ Use "think hard" for complex planning
✅ Archive completed projects

### DON'T:
❌ Skip the literature review phase
❌ Rush through hypothesis evolution
❌ Ignore intermediate checkpoints
❌ Forget to configure `.env` file

## 9. Read the Documentation

For detailed information:
- **README.md** - System architecture and overview
- **EXAMPLES.md** - Step-by-step workflows
- **SUMMARY.md** - Complete technical details
- **CLAUDE.md** - Claude Code configuration

## 10. Example Research Timeline

**Day 1 (2-3 hours)**
- Hypothesis generation and evolution
- Review top 3 evolved hypotheses
- Select one for implementation

**Day 2-3 (4-6 hours)**
- Implement via Forge Pod
- Run initial experiments
- Analyze results

**Day 4 (2-3 hours)**
- Iterate based on results
- Complete full experiments
- Statistical analysis

**Day 5 (2-3 hours)**
- Draft manuscript via Scribe Pod
- Create presentation via Podium Pod
- Final review

**Total**: ~10-15 hours for complete project!

---

## Need Help?

1. Check the EXAMPLES.md for detailed workflows
2. Review individual agent prompts in `.claude/agents/`
3. Run `python system_manager.py status` to debug
4. Check `.claude/workspace/` for outputs

---

## Ready? Let's Go! 🚀

```bash
cd neuro-ai-research-system
claude
```

Then:
```
@supervisor
[Your brilliant research idea]
```

**Happy Researching!** 🧠🤖
