# SwiFT_v2 Downstream Evaluation Tasks

**Date**: October 24, 2025
**Status**: ✅ Task definitions finalized
**Purpose**: Define three clinical/scientific downstream tasks for comprehensive SwiFT_v2 evaluation

---

## Overview

SwiFT_v2 will be evaluated on three clinically-relevant downstream tasks that test different aspects of fMRI foundation model capabilities:

1. **Disease Progression Prediction** - Neurodegenerative disease (Alzheimer's)
2. **Treatment Response Prediction** - Psychiatric intervention (Depression)
3. **Functional State Classification** - Task-dependent brain states (Pain response)

These tasks span three major clinical neuroscience domains and enable comprehensive assessment of SwiFT_v2's learned representations.

---

## Task 1: MCI Conversion Prediction

### Formal Names:
- **Primary**: Mild Cognitive Impairment to Alzheimer's Disease Conversion Prediction
- **Abbreviation**: MCI-CP or MCI→AD
- **Informal**: AD Conversion Risk Prediction

### Task Definition:
**Objective**: Predict which patients with mild cognitive impairment (MCI) will progress to Alzheimer's disease dementia

**Input**: Resting-state fMRI from baseline visit
**Output**: Binary classification (Converter vs. Non-Converter)
**Clinical Significance**: Early identification of patients at high risk for cognitive decline to enable early intervention trials

### Dataset:
- **Source**: ADNI (Alzheimer's Disease Neuroimaging Initiative)
- **Sample**: MCI patients (N=262) at baseline
- **Follow-up**: Up to 10 years
- **Positive Class (Converter)**: N=57 (21.8% conversion rate)
- **Negative Class (Stable MCI)**: N=205 (78.2% remain stable)

### Data Characteristics:
- **Age**: Mean 73.5 years (range 55.6-93.3)
- **Sex**: 46.6% female, 53.4% male
- **Imaging**: 3T resting-state fMRI (140 volumes, 3000 ms TR)
- **Preprocessing**: fMRIPrep + FreeSurfer + ComBat harmonization
- **Parcellation**: 68-region Desikan-Killiany atlas

### Evaluation Metrics:
1. **Discrimination**: AUC-ROC (primary metric for conversion prediction)
2. **Classification Accuracy**: Balanced accuracy across converter/stable groups
3. **Sensitivity/Specificity**: Clinical utility for risk stratification
4. **Calibration**: Prediction confidence reflects true conversion likelihood

### Biomarkers Available for Control:
- MMSE (Mini-Mental State Examination) score
- APOE ε4 genotype status
- Hippocampal volume
- Cortical thickness
- Amyloid/tau biomarkers (if available)

### Clinical Context:
This task mirrors real-world clinical decision-making: identifying MCI patients who will progress to dementia to enable early intervention with disease-modifying therapies. Successful prediction from baseline fMRI would support using neuroimaging biomarkers for treatment planning.

---

## Task 2: Antidepressant Response Prediction

### Formal Names:
- **Primary**: Antidepressant Treatment Response Prediction from Resting-State fMRI
- **Abbreviation**: ARP or ATR-P
- **Informal**: Depression Treatment Response Prediction

### Task Definition:
**Objective**: Predict whether major depressive disorder (MDD) patients will respond favorably to pharmacotherapy

**Input**: Resting-state fMRI from baseline (pre-treatment) visit
**Output**: Binary classification (Responder vs. Non-Responder)
**Clinical Significance**: Personalize antidepressant selection to reduce trial-and-error medication cycling and improve treatment outcomes

### Dataset:
- **Source**: Nature Molecular Psychiatry (2025) - Multi-scanner multimodal neuroimaging
- **Sample Size**: [To be confirmed from paper]
- **Patient Population**: Major depressive disorder diagnosed patients
- **Response Definition**: Symptom reduction ≥50% on depression severity scale (standard clinical definition)

### Task Rationale:
- **Precision Psychiatry**: Pre-treatment neuroimaging biomarkers predict which patients benefit from specific antidepressants
- **Clinical Impact**: Reduces time to symptom improvement and medication side effect burden
- **Treatment Selection**: Identifies non-responders early for treatment switch to alternative therapy
- **Personalization**: Enables treatment optimization based on neural phenotype

### Data Characteristics:
- **Multi-scanner**: 6 different MRI scanners (tests cross-scanner generalization)
- **Multimodal**: fMRI + structural MRI + DTI (focus on fMRI embeddings)
- **Longitudinal**: Pre-treatment baseline → Post-treatment follow-up (typically 8-12 weeks)

### Evaluation Metrics:
1. **Discrimination**: AUC-ROC for treatment response prediction
2. **Classification Accuracy**: Sensitivity/specificity for responder classification
3. **Clinical Utility**: Positive/negative predictive value for clinical decision-making
4. **Cross-scanner Generalization**: Performance consistency across scanner types

### Related Biomarkers:
- Depression severity (Montgomery-Åsberg Depression Rating Scale, MADRS)
- Baseline cognitive/affective measures
- Genetic polymorphisms (SERT, BDNF)
- Inflammatory markers (if available)

### Clinical Context:
Only 30-40% of depression patients respond to first-line antidepressants. Predicting responders from baseline neuroimaging would enable:
- Faster medication selection for responders
- Earlier switch to combination therapy for non-responders
- Reduced burden of trial-and-error treatment cycling

---

## Task 3: Pain-Evoked Brain State Classification

### Formal Names:
- **Primary**: Pain-Evoked vs Resting-State Brain State Classification
- **Abbreviation**: PE-BSC or Pain-State
- **Informal**: Brain State Detection / Pain vs. Rest Classification

### Task Definition:
**Objective**: Classify whether resting-state fMRI was recorded during baseline resting state or during painful stimulus exposure

**Input**: fMRI time series (single or multiple runs)
**Output**: Binary classification (Resting vs. Pain-Evoked)
**Scientific Significance**: Test whether SwiFT_v2 embeddings are sensitive to task-dependent functional brain state changes, not just anatomical/static features

### Dataset:
- **Source**: Nature Molecular Psychiatry (2025) - Multi-scanner multimodal dataset
- **Paradigm**: Noxious heat stimulus with pain ratings during fMRI scanning
- **Resting Baseline**: Typical rest condition (no stimulus, "think of nothing")
- **Active Condition**: Calibrated noxious thermal stimulation to standardized temperature

### Task Rationale:
- **Functional Sensitivity**: Tests whether learned embeddings capture dynamic brain responses to stimuli
- **Task Generalization**: Evaluates model's ability to represent task-dependent, not just resting, brain states
- **Multi-scanner Validation**: Assesses robustness to scanner-induced variability in pain response fMRI
- **Clinical Relevance**: Pain processing is altered in multiple neuropsychiatric disorders (depression, anxiety, chronic pain)

### Data Characteristics:
- **Multiple Scanners**: 6 different MRI systems (tests cross-scanner robustness)
- **Repeated Scans**: Same subjects on different scanners (within-subject design)
- **Balanced Design**: Equal numbers of resting and pain-evoked runs
- **Standardized Stimulus**: Calibrated thermal pain protocol (reproducible across subjects/visits)
- **Pain Ratings**: Subjective pain intensity ratings during scanning (behavioral validation)

### Evaluation Metrics:
1. **Classification Accuracy**: Balanced accuracy for resting vs. pain classification
2. **AUC-ROC**: Discrimination between brain states
3. **Cross-scanner Generalization**: Train on Scanner A, test on Scanner B, etc.
4. **Sensitivity Analysis**: How much fMRI duration needed for reliable classification?
5. **Robustness**: Consistency across preprocessing variations

### Related Measures:
- Subjective pain intensity (Numerical Rating Scale)
- Skin conductance response (autonomic activation)
- Heart rate variability (autonomic response)
- Temperature of stimulus (quantified noxious input)

### Clinical Context:
Pain processing is a fundamental brain function affected by many clinical conditions:
- Chronic pain syndromes (altered pain-related brain responses)
- Depression and anxiety (comorbid with heightened pain sensitivity)
- Neuroinflammation conditions (altered nociceptive processing)

Successfully identifying pain-evoked states demonstrates that SwiFT_v2 captures both static anatomical structure AND dynamic functional changes—a requirement for a comprehensive foundation model.

---

## Comparison Summary

| Aspect | Task 1: AD Conversion | Task 2: Depression Response | Task 3: Pain State |
|--------|----------------------|----------------------------|--------------------|
| **Domain** | Neurodegenerative | Psychiatric | Functional neuroscience |
| **Clinical Application** | Disease progression prediction | Treatment selection | Pain/stimulus sensitivity |
| **Dataset** | ADNI (single-site harmonized) | Multi-site depression trial | Multi-scanner pain task |
| **Sample Size** | N=262 MCI | [TBD] | [TBD] |
| **Prediction Target** | Binary (Converter/Stable) | Binary (Responder/Non-responder) | Binary (Rest/Pain) |
| **Key Challenge** | Longitudinal prediction from static baseline | Treatment heterogeneity | Cross-scanner generalization |
| **Model Capability Tested** | Disease biomarker extraction | Clinical outcome prediction | Functional state sensitivity |
| **Timeline** | 10-year follow-up | 8-12 week post-treatment | Single session classification |
| **Success Metric** | AUC-ROC > 0.70+ (clinically useful) | AUC-ROC > 0.65+ (better than chance) | Accuracy > 75%+ across scanners |

---

## Unified Benchmark Suite

### "SwiFT Clinical Benchmark Suite" Components:

**1. Neurodegenerative Track** 🧠
- Task: MCI Conversion Prediction
- Dataset: ADNI (N=262)
- Duration: Longitudinal (up to 10 years)
- Challenge: Predicting rare events (21.8% conversion rate)

**2. Psychiatric Track** 🔗
- Task: Antidepressant Response Prediction
- Dataset: Depression treatment trial
- Duration: 8-12 week intervention period
- Challenge: Treatment heterogeneity (complex pharmacodynamics)

**3. Functional Neuroscience Track** ⚡
- Task: Pain-Evoked Brain State Classification
- Dataset: Multi-scanner pain paradigm
- Duration: Single session
- Challenge: Cross-scanner robustness and generalization

---

## Implementation Protocol

### Phase 2-4: Model Evaluation Workflow

For each downstream task, the standard workflow is:

1. **Embedding Extraction**
   - Extract learned representations from frozen encoder
   - Standardize embedding dimensions across models
   - Save embeddings for downstream task evaluation

2. **Linear Probing** (primary evaluation)
   - Train logistic regression on embeddings
   - 5-fold cross-validation
   - Metric: AUC-ROC, accuracy, sensitivity, specificity

3. **Fine-tuning** (secondary evaluation)
   - End-to-end fine-tune with task-specific head
   - Smaller learning rate, fewer epochs
   - Compare to frozen linear probing

4. **Baseline Comparisons**
   - KNN classifier (k=5, k=10)
   - Random forest on embeddings
   - Raw fMRI features (PCA + logistic regression)

### Reproducibility Parameters:
- **Random Seed**: 42 (all splits, model initialization)
- **Cross-validation**: 5-fold, stratified
- **Hyperparameters**: Grid search or Bayesian optimization
- **Multiple Runs**: Report mean ± std over 3-5 seeds

---

## Expected Outcomes

### Per-Task Deliverables:

**Task 1 Results Table**:
- Brain-JEPA: AUC, Accuracy, Sensitivity, Specificity
- BrainLM-111M: AUC, Accuracy, Sensitivity, Specificity
- BrainLM-650M: AUC, Accuracy, Sensitivity, Specificity
- SwiFT_v2: AUC, Accuracy, Sensitivity, Specificity
- Baselines: KNN, Random Forest, Raw Features

**Task 2 Results Table**:
- Same metrics as Task 1
- Additional: Cross-site generalization analysis
- Treatment effect size (Cohen's d)

**Task 3 Results Table**:
- Same metrics as Task 1
- Cross-scanner generalization matrix (train/test on each scanner pair)
- Robustness analysis: performance vs. fMRI sequence length

### Manuscript Section Integration:
- **Results**: Per-task performance tables and figures
- **Discussion**:
  - Comparative strengths of each model
  - Which tasks leverage which model capabilities?
  - Implications for clinical deployment

---

## Next Steps

1. **Finalize Dataset Access**
   - Confirm ADNI access and download timeline
   - Confirm Paper 2 (depression) dataset availability
   - Confirm Paper 3 (pain) dataset availability

2. **Prepare Task-Specific Protocols**
   - Define response criteria precisely for Tasks 2 & 3
   - Confirm sample sizes for power analysis
   - Establish train/val/test splits (seed=42)

3. **Implement Evaluation Pipeline**
   - Create standardized evaluation scripts
   - Test on Brain-JEPA and BrainLM first (validation)
   - Apply to SwiFT_v2 (inference)

4. **Generate Results**
   - Expected timeline: 2-3 weeks per model after data preparation
   - Generate comparison figures and statistical tests
   - Draft manuscript results sections

---

## Document Information

**Created**: October 24, 2025
**Status**: ✅ Downstream tasks defined and named
**Next Review**: After dataset access confirmed
**Related Files**:
- DATASETS_FOR_EVALUATION.md
- BENCHMARK_COMPARISON_FRAMEWORK.md
- PHASE_1_DATA_PREPARATION.md

---

This document formalizes the three clinical/scientific downstream evaluation tasks that will comprehensively assess SwiFT_v2 as an fMRI foundation model across neurodegenerative, psychiatric, and functional neuroscience domains.
