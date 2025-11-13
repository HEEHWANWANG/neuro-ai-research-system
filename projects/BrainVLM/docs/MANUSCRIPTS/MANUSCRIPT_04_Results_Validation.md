# Manuscript 04: Results and Validation - Proof-of-Concept for Single-Domain Learning

**Slides Covered**: Pages 23-42 (Results, Summary, Discussion, Appendix)
**Word Count**: ~2200 words
**Date**: November 12, 2025

---

## Executive Summary of Findings

UMBRELLA's feasibility study provides strong empirical evidence that vision-language model architectures can adapt to neuroimaging data, but reveals the experiments test **single-domain, single-modality learning** rather than cross-dataset or cross-modality transfer. Across multiple datasets (ABCD, UKB, HCP, GARD) and modalities (sMRI, fMRI, dMRI), with each evaluated independently, the results consistently demonstrate:

1. **Vision-language architectures work for neuroimaging**: Models can learn discriminative features when training and testing on the same dataset
2. **Natural image pre-training provides modest benefits**: CLIP-ViT achieves competitive parameter efficiency but CNN baselines remain superior
3. **Data scaling improves performance within datasets**: Larger datasets narrow the gap between transformers and CNNs
4. **Alignment approaches succeed**: Both BLIP-2 and LLaVA are viable for brain imaging
5. **Prompt simplicity matters**: Clear, direct prompts outperform complex chain-of-thought reasoning
6. **Regression remains challenging**: Text generation framework requires refinement for continuous prediction
7. **Cross-domain transfer NOT demonstrated**: All experiments train and test on the same dataset—future work must validate true transfer learning

---

## Classification Results: Sex Prediction Across Datasets

### ABCD Dataset (N=11,316, Adolescents) - Within-Dataset Evaluation

**Performance hierarchy (all models trained and tested on ABCD)**:
- CNN: 0.92 ACC, 0.93 AUROC (baseline)
- CLIP-ViT (no LLM): 0.802 ACC, 0.878 AUROC
- ViT from scratch: 0.805 ACC, 0.881 AUROC
- BLIP-2 (VLM): 0.779 ACC
- LLaVA (VLM): 0.787 ACC

**Key observation**: CNN outperforms all ViT variants by 10-14% accuracy. This reflects data limitations—with only 11K samples, CNN's inductive biases for 3D medical imaging provide advantages over transformers' quadratic parameter scaling.

**Critical finding**: CLIP-ViT (1.2M trainable parameters) performs nearly identically to ViT from scratch (1B parameters), demonstrating that pre-trained natural image encoders transfer effectively within ABCD dataset despite 800× fewer trainable parameters. However, the 10-14% gap with CNN suggests domain-specific features are more efficiently learned by specialized architectures.

### UKB Dataset (N=42,794, Middle-Aged to Elderly) - Within-Dataset Evaluation

**Performance hierarchy (all models trained and tested on UKB)**:
- CNN: 0.98 ACC, 0.98 AUROC
- CLIP-ViT (no LLM): 0.94 ACC, 0.985 AUROC
- ViT from scratch: 0.93 ACC, 0.984 AUROC
- BLIP-2 (VLM): 0.95 ACC

**Key observation**: Performance gap between CNN and ViT narrows dramatically with scale. At 43K samples, ViT approaches CNN performance (2% gap vs 10% gap with ABCD). CLIP-ViT achieves 0.985 AUROC, demonstrating excellent discrimination within UKB.

**Data scaling validation**: Comparing ABCD (11K) to UKB (43K), CLIP-ViT improves from 0.878 to 0.985 AUROC (+10.7 percentage points), while CNN improves from 0.93 to 0.98 AUROC (+5 percentage points). This differential scaling confirms that transformers benefit more from data scale than CNNs within individual datasets.

### Combined ABCD + UKB (N=54,110, Age 9-82) - Multi-Dataset Training

**BLIP-2 performance**:
- UKB test set: 0.980 ACC (trained on ABCD+UKB, tested on UKB)
- ABCD test set: 0.787 ACC (trained on ABCD+UKB, tested on ABCD)

**Key observation**: Training on combined datasets enables strong performance when testing on either dataset's held-out test samples. The model learns age-invariant sex features that generalize across developmental stages within the combined training distribution.

**Important limitation**: This is NOT cross-dataset transfer learning (e.g., train on UKB, test on ABCD). Both ABCD and UKB data are present in the training set. The model learns from both distributions simultaneously, then generalizes to held-out samples from each.

### HCP Dataset (N=1,200+, Functional MRI) - Within-Dataset Evaluation

**Performance hierarchy (all models trained and tested on HCP fMRI)**:
- SwiFT (specialized fMRI model): 0.929 ACC
- CLIP-ViT (no LLM): 0.81 ACC
- BLIP-2 (VLM): 0.86 ACC

**Key observation**: BLIP-2 outperforms CLIP-ViT alone by 5%, suggesting that language model integration provides benefits even without instruction tuning. SwiFT's superior performance reflects specialized pre-training on fMRI data. CLIP-ViT achieves respectable 0.81 ACC despite training exclusively on natural images, demonstrating that vision-language architectures can learn from functional connectivity patterns within a single dataset.

**Implication**: Natural image encoders can adapt to fMRI when trained on HCP data, but domain-specific pre-training (SwiFT) provides substantial advantages. This 12% gap motivates UMBRELLA's brain-specific tokenization approach for future multi-dataset pre-training.

---

## Regression Results: Age and BMI Prediction

### Age Prediction on UKB (N=42,794) - Within-Dataset Evaluation

**Performance hierarchy (all models trained and tested on UKB)**:
- ViT from scratch: R² = 0.55
- CLIP-ViT with adapter layers: R² = 0.58
- BLIP-2 (VLM): R² = 0.52
- CLIP-ViT (no LLM): R² = 0.44

**Key observation**: Text generation framework shows reduced performance on regression compared to classification. R² = 0.52-0.58 represents moderate age prediction within UKB, explaining 52-58% of variance.

**Adapter layer benefit**: Adding 2-4 transformer blocks after the frozen CLIP encoder improves R² from 0.44 to 0.58 (+14 percentage points) when training on UKB. This suggests that brain-specific feature learning benefits from increased model capacity when data is abundant within a single dataset.

**Image resolution experiment**: Increasing image size from 96³ to 128³ voxels improves CLIP-ViT performance from R² = 0.44 to 0.45 (marginal gain). This modest improvement suggests that resolution alone does not solve regression challenges—architectural refinements (adapter layers) prove more effective for learning age-related features within UKB.

### BMI Prediction on ABCD (N=11,316) - Within-Dataset Evaluation

**Performance hierarchy (all models trained and tested on ABCD)**:
- CNN: R² = 0.43
- CLIP-ViT (no LLM): R² = 0.312
- ViT from scratch: R² = 0.304
- BLIP-2 (VLM): R² = 0.21

**Key observation**: BMI prediction proves challenging for all models within ABCD. The reduction in BLIP-2 performance (R² = 0.21) compared to CLIP-ViT (R² = 0.312) suggests that text generation loss may not provide sufficient gradient signal for continuous regression with limited data.

**Interpretation**: BMI correlates weakly with brain structure in adolescents. The task difficulty exceeds classification (sex) due to: (1) weaker neurobiological signal, (2) higher label noise, (3) text generation framework limitations for continuous values, (4) limited training data (11K samples).

---

## Alignment Approach Comparison: BLIP-2 vs LLaVA

### Architectural Equivalence on ABCD Sex Classification

**BLIP-2**: 0.779 ACC (trained and tested on ABCD)
**LLaVA**: 0.787 ACC (trained and tested on ABCD)
**Difference**: 0.8 percentage points (not statistically significant)

**Conclusion**: Cross-attention (BLIP-2) and concatenation (LLaVA) alignment strategies achieve essentially identical performance on brain imaging within the ABCD dataset. This validates the hypothesis that **alignment architecture matters less than vision encoder quality** when the encoder learns meaningful features from a single dataset.

**Implication for UMBRELLA**: Either alignment approach can be adopted. LLaVA's simpler single-stage training may provide practical advantages for rapid iteration during domain-specific training phases.

---

## Prompt Engineering Results: Simplicity Wins

### QnA vs Description Formats

**BLIP-2 with QnA → QnA**: 0.779 ACC
**BLIP-2 with Description → QnA**: NaN (training failed)
**LLaVA with Description → QnA (simple)**: 0.741 ACC
**LLaVA with Description → QnA (complex)**: 0.64 ACC

**Key observation**: BLIP-2 requires consistent prompt formats between training and inference due to its two-stage training design. Stage 1 pre-training on image-text pairs biases the Q-Former toward specific text structures. LLaVA's single-stage training provides greater format flexibility.

**Complexity penalty**: Complex answer formats ("The brain shows typical male characteristics including...") reduce performance by 10 percentage points compared to simple formats ("male"). This suggests that rich anatomical descriptions introduce learning difficulties or label noise that impairs convergence when training on limited data.

### Chain-of-Thought Results

**LLaVA with base prompt**: 0.787 ACC
**LLaVA with CoT prompt**: 0.732 ACC
**BLIP-2 with base prompt**: 0.779 ACC
**BLIP-2 with CoT prompt**: 0.752 ACC

**Key observation**: Chain-of-thought reasoning consistently reduces performance by 3-5 percentage points across both architectures when training on individual datasets. This counterintuitive finding suggests that explicit reasoning steps may:
1. Increase output sequence length, diluting gradient signal
2. Introduce intermediate reasoning that the model cannot validate against training data
3. Require more training data to learn reasoning chains than available in single datasets
4. Amplify learning difficulties by demanding higher-level semantic understanding

**Implication**: For initial alignment within datasets, direct question-answer formats prove more effective than reasoning-heavy prompts. CoT may become valuable after strong base alignment is established through large-scale multi-dataset brain imaging pre-training.

### Optimal Prompt Strategy

**Winner**: Simple, direct question-answer format
```
Question: You are a neurologist analyzing T1-weighted MRI Images.
Estimate the sex of subject from this image.
Answer: male
```

**Rationale**: Provides clear task specification without unnecessary complexity. Enables efficient learning with limited data within individual datasets.

---

## GARD Dataset Results: Single-Domain Clinical Validation

### Experimental Context: What GARD Actually Tests

**Critical clarification**: GARD results do NOT demonstrate transfer learning from other datasets. All GARD experiments use standard train/test splits **within the GARD dataset only**.

**GARD dataset characteristics**:
- N=4,328 subjects (balanced) for sex classification
- N=2,506 subjects (balanced) for healthy control vs MCI classification
- Clinical population: elderly with cognitive impairment (age 60+)
- **Experimental design**: Train on GARD training set, test on GARD test set (no other datasets involved)

**What GARD tests**:
1. **Clinical applicability**: Can models trained on clinical data (GARD only) perform well on clinical tasks?
2. **Small dataset performance**: How do models perform with limited clinical data (2.5-4K training samples)?
3. **Disease classification difficulty**: Can models handle subtle MCI classification when trained on GARD alone?

### Sex Classification on GARD (N=4,328, Balanced)

**Performance (all models trained and tested on GARD only)**:
- CNN: 0.982 AUROC (baseline)
- ViT from scratch: 0.887 ACC, 0.95 AUROC
- CLIP-ViT (natural image pre-trained): 0.873 ACC, 0.953 AUROC

**Correct interpretation**:
- **CNN dominates**: 0.982 AUROC represents a 3% advantage over CLIP-ViT (0.953 AUROC) when all models train only on GARD
- **Natural image pre-training provides minimal benefit**: CLIP-ViT performs similarly to ViT from scratch (0.953 vs 0.95 AUROC)
- **Domain-specific architectures win on small data**: With only 4K training samples from GARD, CNN's 3D medical imaging inductive biases outperform transformer approaches

**What this reveals**: When training on small clinical datasets (GARD only, 4K samples), domain-specific CNNs outperform vision transformers by 3% even when transformers use natural image pre-training. The limited training data makes CNN inductive biases more valuable than transformer capacity.

### MCI vs Healthy Control Classification (N=2,506, Balanced)

**Performance (all models trained and tested on GARD only)**:
- CNN: 0.648 AUROC (challenging baseline)
- ViT from scratch: 0.50 ACC, **0.486 AUROC** (random chance—complete failure)
- CLIP-ViT (natural image pre-trained): 0.544 ACC, 0.544 AUROC

**Critical findings**:

1. **ViT from scratch completely fails**: 0.486 AUROC is random performance. Without domain-specific pre-training or massive data, ViT cannot learn discriminative features for subtle disease classification from 2.5K GARD training samples.

2. **CLIP-ViT barely exceeds chance**: 0.544 AUROC is only 4.4 percentage points above random. This suggests that natural image pre-training provides minimal transferable features for subtle neuroanatomical disease markers when training data is limited (2.5K GARD samples).

3. **CNN struggles but succeeds**: 0.648 AUROC is modest but represents genuine learning. Domain-specific architectural biases provide advantages even with 2.5K GARD samples.

**What this reveals about small dataset learning**:
- **Transformers need more data**: ViT from scratch fails completely on 2.5K samples; CLIP-ViT barely works
- **Natural image pre-training helps weakly**: CLIP's slight edge over random (0.544 vs 0.50) suggests some transferable low-level features
- **CNN inductive biases matter**: The 10-percentage-point gap between CNN and CLIP-ViT (0.648 vs 0.544) demonstrates that domain-specific architectures are essential for small clinical datasets

### GARD Results: Implications for UMBRELLA

**The GARD findings validate the need for data scale and domain-specific training**:

1. **Small dataset challenges revealed**
   - CLIP-ViT performs only marginally better than random on MCI classification (2.5K training samples)
   - CNN (domain-specific architecture) outperforms CLIP-ViT significantly on small datasets
   - Natural image pre-training provides insufficient inductive bias for small clinical datasets

2. **Data scale is critical**
   - Compare GARD (2.5-4K samples) vs UKB (43K samples):
     - GARD CLIP-ViT: 0.873 ACC (sex), 0.544 ACC (MCI)
     - UKB CLIP-ViT: 0.94 ACC (sex)
   - Transformers require substantially more training data than CNNs to achieve competitive performance

3. **UMBRELLA's strategy addresses these limitations**
   - **Large-scale brain data**: Train on 54K+ brain scans (ABCD+UKB combined), not 2.5K samples
   - **Brain-specific tokenization**: Create domain-appropriate visual features through brain imaging pre-training
   - **Multi-dataset pre-training**: Learn generalizable representations from diverse brain imaging datasets
   - **Transfer to clinical tasks**: Once pre-trained on large-scale brain data, UMBRELLA can transfer to small clinical datasets more effectively than models trained from scratch

**Correct conclusion from GARD**: These results demonstrate that (1) transformers need large training datasets, (2) natural image pre-training provides weak transfer to neuroimaging, and (3) UMBRELLA's approach of pre-training on large-scale brain imaging data (54K+ samples) before fine-tuning on small clinical datasets is justified.

**Future work needed**: True transfer learning experiments (e.g., pre-train on UKB 43K samples, then fine-tune and test on GARD 2.5K samples) will validate whether UMBRELLA's large-scale brain pre-training enables effective transfer to small clinical datasets.

---

## Multi-Agent System Validation: Consensus Achievement

An independent multi-agent system analyzed UMBRELLA's feasibility results, with agents spanning skeptical to optimistic perspectives. The agents evaluated:
- Format flexibility as evidence
- Caption engineering implications
- Projector unfreezing safety
- Clinical deployment readiness
- Neuroimaging understanding validation

**Unanimous conclusion**: All agents—from skeptical to optimistic—agreed that results provide **strong evidence supporting further development**, with important caveats about single-domain limitations.

**Key concurrence points**:
1. Format flexibility proven (LLaVA successfully trains across prompt variations within datasets)
2. Caption engineering feasible (simple prompts work within datasets)
3. Projector strategy validated (adapter layers improve performance with sufficient data)
4. Clinical potential implied (but single-domain experiments only)
5. Proof-of-concept established (architectures work for neuroimaging within individual datasets)

**Recommended next actions**:
1. Design cross-dataset transfer experiments (e.g., UKB → GARD)
2. Validate multi-modality transfer (e.g., sMRI → fMRI)
3. Schedule radiologist consultation for clinical feedback
4. Perform Grad-CAM analysis to validate feature learning
5. Create strategic roadmap for true universal framework validation

---

## Summary of Key Findings

### Model Performance Hierarchy (Within-Dataset Learning)

**Classification (large datasets: UKB 43K samples)**:
1. 3D CNN: Highest absolute performance (0.98 ACC)—domain-optimized
2. CLIP-ViT (pre-trained): Competitive, parameter-efficient (0.94 ACC)—efficient transfer
3. ViT from scratch: Competitive with sufficient data (0.93 ACC)—data-hungry

**Classification (small datasets: GARD 2.5K samples)**:
1. 3D CNN: Clear winner (0.648 AUROC for MCI)—domain-specific advantages critical
2. CLIP-ViT: Weak performance (0.544 AUROC for MCI)—natural image pre-training insufficient
3. ViT from scratch: Complete failure (0.486 AUROC for MCI = random)—cannot learn from small data

**Parameter Efficiency**:
1. CLIP-ViT: 1.2M trainable parameters (best efficiency)
2. 3D CNN: 12M trainable parameters (domain-optimized)
3. ViT from scratch: 1B trainable parameters (worst efficiency)

**Memory Usage**:
- ViT from scratch: Highest (full model gradient storage)
- CLIP-ViT: Lowest (frozen encoder, small projection layer)
- 3D CNN: Intermediate

### Data Scaling Effects Within Individual Datasets

**Small dataset (ABCD, 11K samples within-dataset training)**:
- CNN advantage: +10-14% accuracy over ViT
- Pre-training benefit: CLIP-ViT ≈ ViT from scratch (both limited by data)

**Large dataset (UKB, 43K samples within-dataset training)**:
- CNN advantage: +2-4% accuracy over ViT
- Pre-training benefit: CLIP-ViT slightly > ViT from scratch
- All approaches achieve high performance (>0.93 ACC)

**Small clinical dataset (GARD, 2.5K samples within-dataset training)**:
- CNN advantage: +10-20% accuracy over ViT variants
- Pre-training benefit: CLIP-ViT shows MINIMAL advantage (0.544 vs 0.50 random on MCI)
- Transformers fail without sufficient training data

**Implication**: Data scale is critical for transformers. UMBRELLA's strategy of pre-training on 54K+ brain scans addresses this limitation, but true transfer learning validation requires future cross-dataset experiments.

### Architecture Insights

**BLIP-2 vs LLaVA**:
- Comparable performance within datasets (no significant difference)
- BLIP-2 advantages: Lower computational cost, explicit alignment stage
- LLaVA advantages: Simpler architecture, greater format flexibility

**Adapter layers**:
- Improve performance when data is abundant (UKB: +14 percentage points R²)
- Minimal benefit when data is limited (GARD: marginal improvement)

**Image resolution**:
- Modest gains from 96³ to 128³ voxels (+1 percentage point R²)
- Suggests architectural improvements outweigh resolution increases

### Prompt Engineering Insights

**Effective strategies**:
- Simple, direct question-answer formats
- Clear task specification without unnecessary elaboration
- Consistent training/inference format for BLIP-2

**Ineffective strategies**:
- Complex anatomical descriptions in answers
- Chain-of-thought reasoning (reduces performance by 3-5%)
- Format mismatch between training and inference (BLIP-2)

### Text Generation Challenges

**Classification**: Strong performance (0.78-0.95 ACC across datasets within-dataset training)
**Regression**: Moderate performance (R² = 0.21-0.58, varies by task and data within datasets)

**Hypothesis**: Text generation loss provides clear gradient signal for discrete categories but struggles with continuous values. Potential solutions:
1. Binned regression (convert continuous → ordinal categories)
2. Auxiliary regression head alongside text generation
3. Larger brain imaging dataset scale (UMBRELLA's 54K+ samples)
4. Specialized prompting for continuous prediction

---

## Discussion: Implications and Future Directions

### Feasibility Validated with Critical Limitations

The comprehensive experimental results provide strong evidence that **vision-language model architectures can adapt to neuroimaging data**, with important caveats:

1. **Architectures work within individual datasets**: Models successfully learn from ABCD, UKB, HCP, and GARD when training and testing on the same dataset
2. **Natural image pre-training provides modest benefits**: CLIP-ViT achieves parameter efficiency but CNNs remain superior, especially on small datasets
3. **Text generation framework viable**: Both BLIP-2 and LLaVA successfully generate predictions as text
4. **Simple prompts effective**: Direct question-answer formats enable efficient learning
5. **Data scale critical**: Transformers require 40K+ samples to match CNN performance; fail on small datasets (2.5K samples)
6. **Cross-domain transfer NOT demonstrated**: All experiments are single-domain; future work must validate true transfer learning

### What the Results Actually Demonstrate

**Demonstrated (proof-of-concept)**:
- Vision-language architectures can learn discriminative features from brain imaging when training and testing on the same dataset
- Natural image pre-training (CLIP) provides parameter efficiency for large datasets
- Both BLIP-2 and LLaVA alignment approaches work for neuroimaging
- Simple prompts are more effective than complex reasoning prompts
- Data scaling improves transformer performance within datasets

**NOT demonstrated (requires future validation)**:
- Cross-dataset transfer learning (e.g., train on UKB, test on GARD)
- Cross-modality transfer learning (e.g., train on sMRI, test on fMRI)
- Unified representation learning across multiple modalities simultaneously
- True "universal" framework capabilities
- Effective few-shot learning on clinical tasks after large-scale pre-training

### The Case for UMBRELLA's Approach

**GARD results reveal the need for large-scale brain pre-training**:
- Small dataset experiments (GARD 2.5K samples) show transformers fail without pre-training
- Natural image pre-training (CLIP) provides minimal help on small clinical datasets
- Domain-specific CNNs outperform transformers on small data by 10-20%

**UMBRELLA's innovation addresses this limitation**:

1. **Large-scale brain imaging pre-training**: 54K+ brain scans provide sufficient data for transformers to learn domain-appropriate representations
   - Avoids small dataset failures observed in GARD single-domain experiments
   - Enables learning of brain-specific inductive biases
   - Supports effective transfer to clinical datasets (future validation needed)

2. **Brain-specific tokenization**: Instead of relying solely on natural image features, UMBRELLA trains vision encoders on brain imaging data
   - Creates domain-appropriate visual representations
   - Learns features relevant to neuroanatomical patterns
   - Addresses weak transfer from natural image pre-training

3. **Unified language generation**: Single text generation objective eliminates explicit loss weighting
   - Simplifies multi-task learning
   - Enables seamless task addition
   - Supports integration with agentic AI systems

**Future validation critical**: While GARD single-domain results show transformers need large-scale training data, true validation of UMBRELLA requires cross-dataset transfer experiments (e.g., pre-train on UKB+ABCD 54K samples, then fine-tune and test on GARD 2.5K samples). This will demonstrate whether large-scale brain pre-training enables effective transfer to small clinical datasets.

### Limitations and Refinements

**Single-domain experiments only**: All results are within-dataset training and testing. Solutions:
1. **Cross-dataset transfer experiments** (pre-train on UKB, test on GARD)
2. Validate multi-modality transfer (sMRI pre-training, fMRI fine-tuning)
3. Test zero-shot and few-shot generalization after large-scale pre-training
4. Demonstrate truly "universal" framework capabilities

**Regression performance**: Text generation requires architectural refinement for continuous prediction. Solutions:
1. Train auxiliary regression heads alongside text generation
2. Increase model scale to improve gradient signal
3. Explore binned regression (ordinal categories)
4. Use specialized prompting for continuous values

**Small dataset challenges**: Transformers fail on 2.5K samples even with natural image pre-training. Solutions:
1. Large-scale brain pre-training (UMBRELLA's 54K+ samples)
2. Few-shot learning capabilities after pre-training
3. Transfer learning from large to small datasets
4. Domain-specific architectural improvements

**Limited clinical validation**: GARD experiments show proof-of-concept but not transfer. Broader clinical datasets (ADNI, different diseases) needed with cross-dataset evaluation protocols.

### Future Work Priorities

**Phase 1: True Transfer Learning Validation (CRITICAL)**
- Pre-train on UKB+ABCD (54K samples)
- Fine-tune and test on GARD (demonstrate transfer)
- Compare transfer performance vs training from scratch on GARD only
- Validate that large-scale pre-training enables effective clinical transfer

**Phase 2: Multi-Modality Transfer**
- Pre-train on sMRI datasets (ABCD+UKB)
- Fine-tune and test on fMRI (HCP)
- Demonstrate cross-modality generalization
- Validate unified representation learning

**Phase 3: Clinical Deployment Preparation**
- Expand to additional disease categories with transfer learning protocols
- Implement uncertainty quantification
- Develop explainability interfaces (Grad-CAM validation)
- Test demographic robustness across datasets

**Phase 4: Scale and Optimization**
- Train on larger combined datasets (100K+ subjects)
- Increase model scale (larger vision encoders, larger LLMs)
- Implement efficient inference
- Develop GPT-4-generated captions for complex reasoning

### Strategic Positioning: The Path to True Universality

UMBRELLA's unified language generation paradigm distinguishes it from traditional multi-task learning, but the feasibility study reveals the path forward:

**Current status (proof-of-concept)**:
- Vision-language architectures work for neuroimaging within individual datasets
- Natural image pre-training provides weak transfer to brain imaging
- Large-scale training data (54K+ samples) available through ABCD+UKB combination
- Both BLIP-2 and LLaVA alignment approaches viable

**Required validation (future work)**:
- Cross-dataset transfer learning (UKB → GARD)
- Cross-modality transfer learning (sMRI → fMRI)
- Zero-shot and few-shot clinical task adaptation
- Truly unified representation learning across modalities

**Competitive advantages (once validated)**:
1. **Unified loss function**: Single text generation objective (no explicit weighting)
2. **Scalability**: Inherits language model scaling laws
3. **Extensibility**: Adding tasks requires no architectural changes
4. **Interpretability**: Text outputs inherently more interpretable
5. **Integration**: Immediate compatibility with agentic AI systems
6. **Domain-specificity**: Brain imaging pre-training (not just natural image features)

As language models improve, UMBRELLA automatically benefits—but only after demonstrating true cross-domain transfer capabilities that these feasibility experiments have not yet validated.

---

## Conclusion: Strong Proof-of-Concept with Clear Path Forward

UMBRELLA's feasibility study establishes that vision-language model architectures can successfully learn from brain imaging data within individual datasets. However, the experiments reveal a critical limitation: **all results are single-domain, single-modality**—true transfer learning has not been demonstrated.

**Key validated conclusions**:

1. **Vision-language architectures work for neuroimaging**: Models learn discriminative features when training and testing on the same dataset
2. **Natural image pre-training provides weak transfer**: CLIP-ViT achieves parameter efficiency on large datasets but CNNs remain superior, especially on small datasets
3. **Text generation framework viable**: Both BLIP-2 and LLaVA successfully generate predictions as text within datasets
4. **Data scale critical**: Transformers need 40K+ training samples; fail on small datasets (2.5K samples)
5. **Simple prompts effective**: Direct formats outperform complex reasoning prompts
6. **Cross-domain transfer NOT validated**: Future experiments must demonstrate transfer learning (e.g., pre-train on UKB, test on GARD)

**The path forward is clear**:

UMBRELLA's strategy—pre-training on large-scale brain imaging (54K+ samples) with text generation training—addresses the data scale limitations revealed by GARD single-domain experiments. However, true validation requires:

1. **Cross-dataset transfer experiments**: Pre-train on UKB+ABCD, transfer to GARD
2. **Cross-modality transfer experiments**: Pre-train on sMRI, transfer to fMRI
3. **Clinical task generalization**: Zero-shot and few-shot learning after large-scale pre-training
4. **Unified multi-modality learning**: Demonstrate true "universal" framework capabilities

The feasibility study provides strong proof-of-concept that vision-language architectures can adapt to neuroimaging, establishes that large-scale training data (54K+ samples) is available, and validates core architectural choices (alignment approaches, prompt strategies, parameter-efficient fine-tuning). With future experiments demonstrating true cross-domain transfer learning, UMBRELLA can evolve from a proof-of-concept to a genuinely universal framework for brain imaging analysis.

Most critically, these results reveal what remains to be done: the single-domain experiments establish architectural viability, but UMBRELLA's promise as a "universal" framework requires validation through cross-dataset and cross-modality transfer learning experiments. This is the essential next phase of research.

---

**Manuscript Series Complete**
**Total Word Count**: ~7,200 words across 4 manuscripts
**Coverage**: All 42 presentation slides explained with correct interpretation
**Critical Correction**: All manuscripts now accurately reflect single-domain, single-modality experimental design
**Next Phase**: Validate true transfer learning through cross-dataset and cross-modality experiments
