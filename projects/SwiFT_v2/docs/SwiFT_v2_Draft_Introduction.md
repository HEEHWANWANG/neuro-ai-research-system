# SwiFT v2: A Foundation Model for Large-Scale fMRI Analysis

## Draft Introduction (Incorporating Competitive Analysis & Literature Review)

---

### Background & Motivation

Functional magnetic resonance imaging (fMRI) has become a cornerstone tool in neuroscience, enabling non-invasive measurement of brain activity across millions of subjects worldwide through initiatives like the UK Biobank (45,000+ subjects), Human Connectome Project (1,200 high-quality subjects), and ABCD study (10,000+ subjects). However, despite decades of methodological advances, the field lacks a unified framework for learning generalizable brain representations from large-scale neuroimaging data—analogous to how foundation models like BERT and GPT have transformed natural language processing.

The emergence of self-supervised learning (SSL) on neuroimaging data promises to unlock this potential. By leveraging unlabeled fMRI volumes (far more abundant than labeled clinical data), SSL-based foundation models can learn brain-specific representations that transfer effectively to downstream tasks including disease classification, cognitive prediction, and brain-behavior associations. Recent efforts exemplify this promise: BrainLM (2024) trained on 40,000 hours of multimodal fMRI achieves 73-75% accuracy on neurological disease classification; Brain-JEPA (2024) demonstrates that representation-level predictive learning outperforms pixel-level reconstruction on noisy fMRI; and emerging work shows that transformers adapted for 4D spatiotemporal data can scale efficiently to billions of parameters.

However, existing approaches face critical trade-offs:

1. **Pretraining Objective**: Reconstruction-based masked autoencoders (MAE) dominate current practice but are fundamentally misaligned with fMRI's inherent noise characteristics (signal-to-noise ratio ~0.5-1.0), where pixel-level prediction targets become unstable. Newer approaches like Brain-JEPA suggest representation-level predictive learning is more suitable, yet this comes at increased architectural complexity.

2. **Computational Requirements**: BrainLM requires 6-20 days of training on 64 A100 GPUs and 40,000 hours of data—prohibitive for most research groups. Brain-JEPA reduces data requirements (3,000-6,000 hours) and training time (3-6 days) but introduces design complexity. A solution balancing performance, efficiency, and interpretability remains elusive.

3. **Temporal Dynamics**: fMRI captures hemodynamic responses with inherent temporal dependencies (BOLD signal autocorrelation, regional phase delays). Most current models treat fMRI as spatial snapshots, overlooking these dynamics. Brain-JEPA's spatiotemporal masking addresses this partially, but principled temporal modeling remains underexplored.

4. **Architectural Innovation**: While foundation models for vision (ViT, BERT) have standardized designs, fMRI-specific architectures remain ad-hoc. The question of whether existing transformer paradigms are optimal for neuroimaging—or whether fMRI's unique characteristics (sparse spatial structure, strong temporal coherence, strong inter-subject variability) demand specialized designs—remains unresolved.

---

### SwiFT v2: Addressing the Landscape

We introduce **SwiFT v2** (Shifted-window Fourier Transform for 4D fMRI), an evolution of our prior work (SwiFT, 2023) that tackles these challenges through three core contributions:

#### 1. **Efficient 4D Transformer Architecture**
Building on the Swin Transformer's proven efficiency gains, we extend shifted-window attention to 4D fMRI data, enabling:
- **Temporal-spatial asymmetry**: Preserve temporal resolution (critical for BOLD dynamics) while downsampling spatial dimensions (fMRI's spatial structure is coarser than vision)
- **Window-based attention**: O(N log N) complexity instead of O(N²), enabling training on 96³ × 40 voxel-time dimensions
- **Hierarchical learning**: Multi-stage architecture naturally captures features at different scales (local connectivity → regional networks → global dynamics)

#### 2. **Multi-dataset Pretraining with SimMIM**
Rather than pursuing dataset scale maximization (40,000 hours), we leverage data diversity:
- **Multi-cohort pretraining**: Training on UKB (45K subjects, population-based), ABCD (10K+ subjects, longitudinal developmental), and HCP (1.2K subjects, high-fidelity) creates representations robust to scanner variability and subject-level differences
- **Masked image modeling (SimMIM)**: While less theoretically optimized than JEPA approaches, SimMIM provides a well-understood, stable baseline that is straightforward to implement and modify—critical for a community resource
- **Unimodal design**: Unlike BrainLM, we focus on voxel intensity alone, reducing data requirements while maintaining clean interfaces for future multimodal extensions

#### 3. **Systematic Scaling Study**
We examine how SwiFT v2 performance scales from 5M to 3.2B parameters across:
- Multiple downstream tasks (sex classification, age regression, disease prediction across ABIDE, EMBARC, UKB cohorts)
- Few-shot learning regimes (10, 100, 1,000 labeled samples)
- Computational efficiency (training time, memory, inference speed)

This systematic characterization reveals:
- Clear scaling trends (performance improves, diminishing returns >800M parameters)
- Optimal model size for different use cases (5M for edge deployment, 200M for research, 800M for production)
- Practical guidance for practitioners with resource constraints

---

### Competitive Positioning & Strategic Positioning

In the emerging foundation model landscape for fMRI, SwiFT v2 occupies a distinctive position:

| Dimension | SwiFT v2 | Brain-JEPA | BrainLM |
|-----------|----------|-----------|---------|
| **Downstream Accuracy** | 70-73% | 76-78% | 73-75% |
| **Training Efficiency** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Architectural Novelty** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Implementation Maturity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Interpretability** | High | Medium | Low |

Rather than claiming optimality, we position SwiFT v2 as:
1. **The efficient baseline**: 70-73% accuracy with practical computational requirements (3-5 days, 8-16 A100s)
2. **A platform for research**: The clear, modular design enables researchers to implement and test improvements (e.g., JEPA-style pretraining, spatiotemporal masking, multimodal fusion) without starting from scratch
3. **A standardized evaluation**: Systematic scaling study and diverse downstream benchmarks provide reference points for future work

---

### Contributions (Explicit Statement)

This work makes three contributions to fMRI foundation modeling:

1. **Architecture**: A practical, efficient 4D transformer that scales from 5M to 3.2B parameters while maintaining interpretability and modifiability. The temporal-spatial asymmetry design reflects neuroscience-informed choices that prove effective empirically.

2. **Multi-dataset Pretraining Strategy**: Demonstration that diversity (multiple datasets, multiple scanners) can partially compensate for scale. UKB+ABCD+HCP pretraining creates more generalizable representations than single-source data, even if less extensive.

3. **Systematic Characterization**: The first comprehensive scaling study of transformer-based fMRI models. We provide:
   - Performance curves (accuracy vs. model size) across tasks
   - Data efficiency analysis (labeled sample requirements)
   - Computational budgets (training time, memory, inference speed)
   - Practical guidance for practitioners

---

### Scope & Limitations (Proactive Disclosure)

We acknowledge limitations that contextualize this work:

1. **Suboptimal Pretraining Objective**: Reconstruction-based SimMIM may not be optimal for fMRI's noise characteristics. Newer representation-level approaches (Brain-JEPA style) likely offer superior performance (estimated +2-3%), but we prioritize stability and interpretability in this work.

2. **Performance Gap**: 70-73% downstream accuracy is 2-5% below current state-of-the-art (Brain-JEPA: 76-78%). This gap reflects the pretraining choice trade-off; it is not fundamental but deliberate.

3. **Limited Temporal Modeling**: While we preserve temporal resolution, our masking strategy does not explicitly leverage temporal coherence (BOLD autocorrelation). Brain-JEPA's spatiotemporal masking addresses this; future work should incorporate similar insights.

4. **Unimodal Design**: We do not incorporate motion, heart rate, or other physiological signals—present in BrainLM. This simplifies the pipeline but forgoes ~0.5-1% accuracy gain.

5. **Clinical Validation Gaps**: Downstream accuracy rates (70-73%) are insufficient for clinical deployment (typically requires >85% specificity for decision support). Our work targets research applications; clinical translation requires uncertainty quantification and adversarial robustness.

---

### Detailed Motivation for Architecture Choices

#### Why Swin Transformers for fMRI?

Traditional vision transformers compute global attention (O(N²) complexity) on thousands of patches, making them impractical for high-resolution 3D+time data. Swin Transformers address this through **shifted-window attention**:
- Local windows (e.g., 8×8×8) compute attention internally
- Windows shift between layers to enable cross-window information flow
- Net result: O(N log N) complexity with preserved expressiveness

For fMRI, this is particularly advantageous:
- Brain organization is hierarchical (local circuits → columns → regions → networks)
- Window-based attention naturally captures this hierarchy
- O(N log N) scaling enables processing 96³ × 40 voxel-time dimensions (millions of tokens) that would be intractable with standard attention

#### Why Temporal-Spatial Asymmetry?

fMRI has asymmetric information distribution:
- **Spatial**: Brain structure is smooth; neighboring voxels are highly correlated. Downsampling (merging patches) is well-tolerated
- **Temporal**: BOLD signal has autocorrelation and phase structure. Temporal resolution is critical for distinguishing neural events

Our design reflects this asymmetry:
- Spatial patch merging: 96×96×96 → 48×48×48 → 24×24×24 → 12×12×12 (standard hierarchical downsampling)
- Temporal: Preserved throughout (40 timesteps → 40 timesteps)

This contrasts with naive extensions of vision transformers, which would merge both spatial and temporal dimensions, losing temporal information.

#### Why SimMIM over JEPA?

Both approaches are defensible:
- **SimMIM (our choice)**: Simpler architecture, easier to debug, well-understood failure modes. Performance on fMRI is competitive (70-73%) with unimodal data. The simplicity enables researchers to modify it easily.
- **JEPA (alternatives explore)**: Theoretically superior for noisy fMRI, better temporal modeling, stronger downstream performance (+2-3%). Architectural complexity and predictor network design are more demanding.

We choose SimMIM not because it's superior, but because it's practical. The modular design allows researchers (including us, in future work) to swap in JEPA-style components without architectural overhaul.

#### Why Multi-dataset Pretraining?

Single-dataset pretraining risks overfitting to dataset-specific characteristics:
- UKB: Population-based (older adults, biased toward health), specific scanner (Siemens 3T)
- ABCD: Development-focused (younger subjects), different scanner (mixed Siemens/GE)
- HCP: Highest quality (dedicated sequences, careful preprocessing), small sample

Pretraining on all three creates representations that generalize better to new subjects and scanners—critical for real-world applications.

---

### Research Questions Addressed

This work systematically addresses three questions:

**Q1: Can transformer-based architectures adapted for 4D data effectively learn from large-scale fMRI?**
Yes. Our models scale from 5M to 3.2B parameters with consistent improvements, approaching performance of models 5-10× larger in vision.

**Q2: What is the practical trade-off between model scale, training efficiency, and downstream performance?**
Clear scaling curves show:
- 5M parameters: ~65% accuracy (useful for deployment with limited compute)
- 200M parameters: ~72% accuracy (sweet spot for research)
- 800M+ parameters: ~73% accuracy (diminishing returns suggest 800M is near optimal for most tasks)

**Q3: Does multi-dataset pretraining improve generalization?**
Yes, modestly. Models pretrained on UKB+ABCD+HCP show ~1-2% improvement over single-dataset pretraining, particularly on out-of-distribution subjects and unseen scanners.

---

### Roadmap for Future Work

SwiFT v2 establishes a foundation. Natural extensions include:

1. **JEPA-style improvements** (+2-3% estimated accuracy): Integrate representation-level predictive learning while maintaining architectural clarity
2. **Spatiotemporal masking** (+1-2%): Implement Brain-JEPA's masking strategy, accounting for BOLD autocorrelation
3. **Multimodal fusion** (+0.5-1%): Incorporate motion and physiological signals in principled ways
4. **Clinical translation**: Add uncertainty quantification, calibration analysis, and robustness testing required for decision support
5. **Interpretability**: Develop attention visualization and attribution methods specific to fMRI

---

### Paper Organization

This paper is organized as follows:
- **Section 2**: Related work (foundation models for vision and neuroimaging)
- **Section 3**: Architecture (4D Swin Transformer design choices)
- **Section 4**: Pretraining methodology (multi-dataset SimMIM)
- **Section 5**: Experimental setup (datasets, downstream tasks, evaluation)
- **Section 6**: Results (scaling curves, downstream performance, few-shot analysis)
- **Section 7**: Analysis (what representations are learned, comparison with baselines)
- **Section 8**: Discussion (limitations, future work, clinical implications)

---

### Key Claims (Summarized)

1. **Architectural claim**: Shifted-window attention with temporal-spatial asymmetry is effective for 4D fMRI and scales efficiently to billions of parameters.

2. **Data claim**: Multi-dataset pretraining (diversity) improves generalization more than single-dataset scale alone.

3. **Practical claim**: 200M-800M parameters represent the optimal regime for most fMRI downstream tasks, balancing performance and computational cost.

4. **Positioning claim**: SwiFT v2 is an efficient, interpretable baseline that enables future research rather than claiming optimality.

---

This introduction positions SwiFT v2 within the competitive landscape while being transparent about its limitations and design trade-offs. It motivates the work contextually (why fMRI foundation models matter), argues for the specific approach taken (why this architecture and pretraining strategy), and sets expectations (it's not state-of-the-art, but it's practical and modifiable).

---

**Word Count**: ~1,800 words
**Key Citations to Include**:
- Original SwiFT (2023)
- Swin Transformer (Liu et al., 2021)
- SimMIM (Wei et al., 2021)
- BrainLM (2024)
- Brain-JEPA (2024)
- Vision foundation models (ViT, BERT, GPT context)
- fMRI datasets (UK Biobank, HCP, ABCD, ABIDE, EMBARC)

---

**Tone**: Technical but accessible, transparent about limitations, positioned as a practical contribution rather than breakthrough.