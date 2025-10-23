# GitHub Upload Guide for Benchmark Models

**Date**: October 23, 2025
**Status**: Ready for Upload

---

## Current Status

✅ Both projects are now initialized as Git repositories with:
- Clean commit history (initial commit only)
- Proper `.gitignore` files (excludes large files, checkpoints, data)
- Git configuration set up
- Ready to push to GitHub

**Brain-JEPA Repository**:
- Location: `/Users/apple/Desktop/Brain-JEPA`
- Status: ✅ Git initialized, initial commit: `80e0f1b`
- Files: 34 files, 4,398 insertions

**BrainLM Repository**:
- Location: `/Users/apple/Desktop/BrainLM`
- Status: ✅ Git initialized, initial commit: `e8a544c`
- Files: 36+ files, ready for push

---

## Steps to Complete GitHub Upload

### Step 1: Create Remote Repositories on GitHub

1. **For Brain-JEPA**:
   - Go to https://github.com/new
   - Repository name: `Brain-JEPA` (or `brain-jepa`)
   - Description: "Brain-JEPA - NeurIPS 2024 Spotlight Model for fMRI Embedding Extraction"
   - Visibility: Public (recommended for research)
   - ✅ Create repository
   - Copy the repository URL (HTTPS or SSH format)

2. **For BrainLM**:
   - Go to https://github.com/new
   - Repository name: `BrainLM` (or `brainlm`)
   - Description: "BrainLM - Foundation Model for Brain Activity Recording Embeddings"
   - Visibility: Public (recommended for research)
   - ✅ Create repository
   - Copy the repository URL

### Step 2: Add Remote and Push (Brain-JEPA)

```bash
cd /Users/apple/Desktop/Brain-JEPA

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/Brain-JEPA.git

# Verify remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace** `YOUR_USERNAME` with your GitHub username.

### Step 3: Add Remote and Push (BrainLM)

```bash
cd /Users/apple/Desktop/BrainLM

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/BrainLM.git

# Verify remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace** `YOUR_USERNAME` with your GitHub username.

---

## Automated Upload Script

If you prefer, you can use this script to automate the process:

```bash
#!/bin/bash

# Set your GitHub username
GITHUB_USERNAME="your_username_here"

echo "Uploading Brain-JEPA..."
cd /Users/apple/Desktop/Brain-JEPA
git remote add origin https://github.com/${GITHUB_USERNAME}/Brain-JEPA.git
git branch -M main
git push -u origin main

echo "Uploading BrainLM..."
cd /Users/apple/Desktop/BrainLM
git remote add origin https://github.com/${GITHUB_USERNAME}/BrainLM.git
git branch -M main
git push -u origin main

echo "✅ Upload complete!"
```

Save as `upload_to_github.sh` and run:
```bash
chmod +x upload_to_github.sh
./upload_to_github.sh
```

---

## Verification

After upload, verify the repositories are on GitHub:

```bash
# Brain-JEPA
cd /Users/apple/Desktop/Brain-JEPA
git log --oneline -1
git remote -v

# BrainLM
cd /Users/apple/Desktop/BrainLM
git log --oneline -1
git remote -v
```

You should see:
- Remote origin pointing to your GitHub repositories
- Commit history available
- All files properly tracked

---

## Repository Structure on GitHub

After upload, your repositories will contain:

### Brain-JEPA
```
Brain-JEPA/
├── README.md                          # Project overview
├── EMBEDDING_EXTRACTION_GUIDE.md      # Usage guide
├── downstream_embedding_extraction.py # Main entry point
├── src/
│   ├── models/
│   ├── datasets/
│   └── utils/
├── configs/                           # Configuration files
├── downstream_tasks/                  # Downstream task implementations
└── .gitignore                         # Excludes large files
```

### BrainLM
```
BrainLM/
├── README.md                          # Project overview
├── brainlm_mae/                       # Core model implementation
├── brainlm_tutorial.ipynb             # Tutorial notebook
├── continue_train_same_wandb.py       # Training script
├── inference_*.ipynb                  # Inference notebooks
├── datasets/                          # Dataset utilities
└── .gitignore                         # Excludes large files
```

---

## What's Excluded (Not Pushed)

Due to `.gitignore`, the following are NOT uploaded:

- ✅ Large model checkpoints (`*.pth`, `*.pt`)
- ✅ Data files (`*.nii.gz`, `*.csv`)
- ✅ Jupyter notebook checkpoints
- ✅ Virtual environments
- ✅ Logs and temporary files
- ✅ IDE configuration files

This keeps repositories lightweight (~5-10 MB each) while preserving all code and documentation.

---

## GitHub URLs After Upload

After successful upload, your repositories will be available at:

- **Brain-JEPA**: `https://github.com/YOUR_USERNAME/Brain-JEPA`
- **BrainLM**: `https://github.com/YOUR_USERNAME/BrainLM`

You can share these URLs in:
- Paper supplementary materials
- Project documentation (.claude/benchmarks/)
- Research collaborations
- External citations

---

## Integration with Benchmark Documentation

After uploading, update the benchmark documentation:

In `.claude/benchmarks/BENCHMARKS_INDEX.md`, update:

```markdown
### Brain-JEPA
- **GitHub**: https://github.com/YOUR_USERNAME/Brain-JEPA
- **Documentation**: See repository README and EMBEDDING_EXTRACTION_GUIDE.md

### BrainLM
- **GitHub**: https://github.com/YOUR_USERNAME/BrainLM
- **HuggingFace Models**: https://huggingface.co/vandijklab/brainlm/
- **Documentation**: See repository README and brainlm_tutorial.ipynb
```

---

## Troubleshooting

### Issue: "fatal: 'origin' does not appear to be a git repository"

**Solution**: Make sure you're in the correct directory:
```bash
cd /Users/apple/Desktop/Brain-JEPA  # or BrainLM
```

### Issue: "Permission denied (publickey)"

**Solution**: Set up SSH key for GitHub:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# Follow prompts, then add public key to GitHub Settings > SSH Keys
```

Alternatively, use HTTPS (requires personal access token for pushing):
```bash
git remote set-url origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/Brain-JEPA.git
```

### Issue: "Could not resolve host: github.com"

**Solution**: Check internet connection and GitHub status at https://www.githubstatus.com/

---

## Summary

✅ **Pre-Upload Checklist**:
- [x] Both projects initialized as Git repositories
- [x] `.gitignore` files created (excludes large files)
- [x] Initial commits created
- [ ] GitHub repositories created (user action)
- [ ] Remote URLs added (user action)
- [ ] Code pushed to GitHub (user action)

**Next Step**: Follow the steps above to create GitHub repositories and push the code.

**Estimated Time**: 5-10 minutes

---

**Document Version**: 1.0
**Created**: October 23, 2025
**Status**: Ready for GitHub Upload
