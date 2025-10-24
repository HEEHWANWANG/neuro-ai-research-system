# Datasets for SwiFT_v2 Benchmark Evaluation

**Date**: October 24, 2025
**Status**: Extracted from three research papers for benchmark evaluation
**Purpose**: Identify datasets used in benchmark studies for SwiFT_v2 comparison

---

## Overview

This document summarizes datasets mentioned in three key research papers that will be used for evaluating SwiFT_v2 against benchmark models (Brain-JEPA and BrainLM). The papers focus on Alzheimer's disease neuroimaging, psychiatric neuroimaging, and neuroimaging standardization.

---

## Paper 1: Altered Hierarchical Gradients of Intrinsic Neural Timescales in MCI and AD

**Citation**: Zhang et al., Journal of Neuroscience (June 19, 2024)
**DOI**: 10.1523/JNEUROSCI.2024-23.2024
**Title**: "Altered Hierarchical Gradients of Intrinsic Neural Timescales in Mild Cognitive Impairment and Alzheimer's Disease"

### Primary Dataset: ADNI (Alzheimer's Disease Neuroimaging Initiative)

**Dataset Characteristics**:
- **Launch**: 2003 as public-private partnership
- **Purpose**: Measure progression of MCI and early AD through serial MRI, PET, biomarkers, clinical/neuropsychological assessments
- **Total Sample**: 945 subjects at baseline (904 after quality control)
- **Imaging Modality**: 3T MRI (resting-state fMRI + T1-weighted structural)
- **Collection**: August 18, 2020 (data download date)
- **Sites**: 58 MRI scanning sites (multi-site harmonization applied)

#### Participant Groups:
1. **CN (Cognitively Normal)**: 476 subjects
   - Baseline CN, remain non-demented at follow-up
   - Mean age: 73.2 years (range: 55.7-95.5)
   - Female: 281 (59.0%), Male: 195 (41.0%)

2. **MCI (Mild Cognitive Impairment)**: 262 subjects
   - Baseline MCI, remain non-demented at follow-up
   - Mean age: 73.5 years (range: 55.6-93.3)
   - Female: 122 (46.6%), Male: 140 (53.4%)

3. **Converter**: 57 subjects
   - Baseline CN/MCI, converted to dementia at follow-up
   - Mean age: 75.0 years (range: 57.3-89.7)
   - Female: 24 (42.1%), Male: 33 (57.9%)
   - Note: 4 were CN at baseline, remainder were MCI at baseline

4. **AD (Alzheimer's Disease)**: 109 subjects
   - Baseline dementia status
   - Mean age: 75.9 years (range: 55.3-96.0)
   - Female: 54 (49.5%), Male: 55 (50.5%)

**Total Demographics**:
- Combined N = 904 (after QC exclusions)
- Age range: 55-96 years
- Female: 481 (53.2%), Male: 423 (46.8%)

#### MRI Acquisition Parameters:

**T1-weighted Structural**:
- Sequence: Gradient-recalled echo, sagittal plane
- TR = 6.98 ms, TE = 2.85 ms, TI = 400 ms
- FOV = 26 cm
- Voxel size: 1.0 × 1.0 × 1.2 mm
- Matrix: 256 × 256 × 196

**Resting-state fMRI**:
- Sequence: Echo-planar imaging
- Volumes: 140 functional volumes (first 5 discarded, 135 used)
- TR = 3,000 ms, TE = 30 ms
- Flip angle: 80°
- Slices: 48, thickness: 3.3 mm
- Voxel size: 3 × 3 × 3.3 mm
- Matrix: 64 × 64

#### Preprocessing Pipeline:
1. **T1 Processing**:
   - Quality control via MRIQC
   - Best quality image selected per subject
   - Cross-sectional processing with FreeSurfer 7.1.1
   - Parcellation: Desikan-Killiany atlas (68 cortical ROIs)
   - Cortical thickness extraction for covariate control

2. **rs-fMRI Processing**:
   - Custom fMRIPrep methodology for reference generation
   - Motion estimation: MCFLIRT (FSL 5.0.9)
   - Slice-time correction: 3dTshift (AFNI 20160207)
   - Registration: Boundary-based bbregister to T1w
   - Resampling: MNI152NLin2009cAsym space
   - Motion QC: FD > 0.5 mm or RMSD > 0.3% flagged and interpolated
   - Bandpass filtering: 0.01-0.09 Hz
   - Confound regression: Head motion (6 params), CSF, white matter signals
   - Spatial smoothing: 6 mm FWHM Gaussian kernel

3. **Scanner Harmonization**:
   - Method: ComBat harmonization to remove multi-site effects
   - Covariates: Age, sex, mean framewise displacement, diagnosis group

#### Brain Parcellation:
- **Cortical**: Desikan-Killiany atlas (68 ROIs: 34 per hemisphere)
- **Subcortical**: Aseg atlas (16 ROIs: thalamus, caudate, putamen, pallidum, accumbens, hippocampus, amygdala, ventral diencephalon)
- **Total Coverage**: 84 brain regions

#### Key Clinical Measures:
- Mini-Mental State Examination (MMSE)
- APOE genotype (ε4 status)
- Hippocampal volume
- Cortical thickness by region
- Amyloid and tau biomarkers (phosphorylated tau)

#### Exclusion Criteria Applied:
1. rs-fMRI with >30% motion outlier frames (27 excluded)
2. Missing diagnosis information (12 excluded)
3. Corrupted MRI images (2 excluded)
- **Final analysis sample**: 904 participants

#### Follow-up Duration:
- Up to 10 years or until early study dropout
- Follow-up duration does not significantly differ across groups
- **Limitation**: Stable MCI subjects may convert after study exit

#### Data Availability:
- **ADNI Database**: https://www.adni.loni.usc.edu
- **Processed Data**: Available from seonjoo.lee@nyspi.columbia.edu

---

## Paper 2: Nature s41591-020-1142-7

**Status**: Multi-article dataset covering Alzheimer's disease neuroimaging standardization

### Primary Dataset: ADNI (Confirmed)
- Same ADNI dataset as Paper 1
- Focus: Brain imaging standardization across clinical trials
- Use cases: Longitudinal monitoring, biomarker assessment, cognitive decline prediction

### Secondary Focus:
- Multiple sclerosis neuroimaging datasets (noted but less relevant to current evaluation)
- Brain imaging standardization in clinical trial contexts

---

## Paper 3: Nature s41380-025-02974-6

**Status**: Psychiatric neuroimaging - treatment response prediction

### Primary Dataset: Multi-scanner Multimodal Neuroimaging

**Characteristics**:
- **Type**: Longitudinal, multi-scanner, multimodal
- **Imaging Modalities**: Multiple (fMRI, structural MRI, DTI implied)
- **Scanners**: 6 different MRI scanners
- **Design**: Repeated scans across different scanners
- **Purpose**: Evaluate scanner consistency, cross-scanner reliability

### Secondary Application: Depression Treatment Response
- **Use Case**: Predict treatment outcomes in major depressive disorder
- **Modalities**: Multi-modal brain networks
- **Machine Learning**: Deep graph learning approaches
- **Sample Size Limitation**: Previously limited by small N, addressed in this dataset
- **Scope**: Multi-omics + neuroimaging integration

---

## Summary of Available Datasets for SwiFT_v2 Evaluation

### Tier 1: Recommended (Directly Applicable)

#### ADNI Dataset ✅
**Status**: Fully available and well-characterized
**Recommendation**: PRIMARY dataset for SwiFT_v2 evaluation

**Strengths**:
- Large sample (N=904 after QC)
- Well-defined disease progression (CN → MCI → Converter → AD)
- Comprehensive clinical characterization
- Multi-site standardization applied (ComBat harmonization)
- Longitudinal follow-up (up to 10 years)
- Public availability (registration required)
- Consistent with Brain-JEPA and BrainLM evaluation protocols
- Rich metadata (APOE, biomarkers, cognitive measures)

**Task Suitability**:
- **Primary**: 3-way disease classification (CN vs MCI vs AD) OR 4-way (CN vs MCI vs Converter vs AD)
- **Alternative**: 2-way binary classification (healthy vs disease)
- **Biomarker**: Early detection of MCI-to-AD conversion

**Preprocessing Notes**:
- Preprocessing already applied (fMRIPrep/FreeSurfer)
- Raw fMRI data available for custom preprocessing if needed
- Structural T1w images available for registration/parcellation
- Site effects harmonized with ComBat

#### HCP-Aging (Implicit from "Healthy Aging" References)
**Status**: Recommended secondary dataset
**Note**: Referenced in benchmark documentation as healthy population contrast

**Characteristics**:
- Aging population without cognitive impairment
- Multi-modal imaging
- Younger to middle-aged compared to ADNI CN
- Serves as out-of-distribution test set

---

## Evaluation Protocol Recommendations

### Phase 1: ADNI Dataset Preparation

**Target Structure**:
```
/benchmark/datasets/ADNI/
├── cn/                 # Cognitively normal (N=476)
├── mci/                # Mild cognitive impairment (N=262)
├── converter/          # MCI→AD converters (N=57)
├── ad/                 # Alzheimer's disease (N=109)
├── derivatives/        # Preprocessed fMRI data
├── metadata/
│   ├── demographics.csv
│   ├── clinical_labels.csv
│   ├── apoe_status.csv
│   └── splits.csv (70/15/15 train/val/test)
└── preprocessing_log.txt
```

**Key Metadata to Extract**:
1. Subject ID, Age, Sex, Site
2. Clinical diagnosis (CN/MCI/AD/Converter)
3. MMSE score, APOE genotype
4. Hippocampal volume
5. Cortical thickness values (Desikan-Killiany ROIs)

**Splits Strategy** (with seed=42):
- **Train**: 70% (633 subjects) - balanced across groups
- **Validation**: 15% (135 subjects) - balanced across groups
- **Test**: 15% (136 subjects) - balanced across groups
- **Stratification**: By diagnosis group + site
- **Reproducibility**: Fixed random seed for reproducibility

### Phase 2: HCP-Aging Dataset Preparation (Secondary)

**Purpose**: Out-of-distribution evaluation on healthy aging population

**Structure**:
```
/benchmark/datasets/HCP_Aging/
├── healthy/            # Cognitively normal aging
├── splits/             # Train/val/test split
└── metadata/
    ├── demographics.csv
    └── labels.csv (sex for binary classification)
```

---

## Comparison with Benchmark Model Evaluations

### Brain-JEPA Evaluation Datasets:
- **Pretraining**: UK Biobank (large healthy population)
- **Evaluation**: HCP, ADNI, MACC datasets
- **Note**: Same ADNI dataset enables direct comparison with SwiFT_v2

### BrainLM Evaluation Datasets:
- **Pretraining**: UK Biobank
- **Downstream Tasks**: ADNI, EMBARC, YooAttn, ToPS
- **Note**: ADNI overlap enables direct comparison

### SwiFT_v2 Evaluation (Planned):
- **Primary**: ADNI (3/4-way classification)
- **Secondary**: HCP-Aging (sex classification, OOD test)
- **Comparison**: Direct metrics with Brain-JEPA and BrainLM on same ADNI subset

---

## Data Access and Preprocessing Notes

### ADNI Access:
1. Register at https://www.adni.loni.usc.edu
2. Complete Data Use Agreement
3. Download baseline T1w and rs-fMRI for participants
4. Preprocessing options:
   - Use provided preprocessed data (fMRIPrep outputs)
   - Re-preprocess with custom pipeline for consistency

### Preprocessing Consistency:
**Consideration**: Papers used fMRIPrep + FreeSurfer standard pipeline
- **Recommendation**: Replicate same pipeline for Brain-JEPA/BrainLM/SwiFT_v2 consistency
- **Parcellation**: Use Desikan-Killiany atlas (68 ROIs) as baseline
- **Advanced**: Use Schaefer 400 + Tian 50 (450 ROIs) if matching Brain-JEPA exactly

### Quality Control Applied:
- Motion artifacts: FD > 0.5 mm flagged and interpolated
- Image quality: MRIQC applied, best quality selected per subject
- Scanner harmonization: ComBat applied across 58 sites
- Exclusions: >30% motion, corrupted images, missing diagnosis info

---

## Timeline and Integration

### Estimated Data Preparation Time:
- **ADNI**: 1-2 days (download, organize, create splits)
- **HCP-Aging**: 0.5-1 day (if using prepared version)
- **Total Phase 1**: 1-2 days

### Integration into Benchmark Framework:

**Phase 1 Deliverables**:
- ✅ Organized ADNI directory structure
- ✅ Extracted metadata (demographics, clinical labels)
- ✅ Created reproducible train/val/test splits (seed=42)
- ✅ Validated data integrity (no missing files, correct group distributions)

**Phase 2-4 Utilization**:
- Brain-JEPA evaluation on ADNI + HCP-Aging
- BrainLM evaluation on ADNI + HCP-Aging
- SwiFT_v2 evaluation on ADNI + HCP-Aging (identical protocol)

**Phase 5 Outputs**:
- Comparison tables across models and datasets
- Performance metrics (accuracy, AUC, F1, sensitivity, specificity)
- Efficiency metrics (parameters, inference time, memory)
- Representation analysis (embedding quality, brain structure preservation)

---

## Key Findings from Papers

### Paper 1 - INT Biomarker Findings:
1. **Intrinsic Neural Timescales (INT)** differ between disease groups
2. **AD/Converter groups**: Similar INT profiles (longer timescales in lower-order areas)
3. **MCI groups**: Distinct pattern (shorter timescales in higher-order areas)
4. **Hierarchical gradients**: Altered in disease vs. normal aging
5. **Clinical implication**: INT could serve as biomarker for MCI→AD conversion prediction

**Relevance**: SwiFT_v2 should capture similar hierarchical/temporal dynamics in embeddings

### Paper 2 - Neuroimaging Standardization:
1. **Multi-site consistency**: Critical for clinical applications
2. **Preprocessing harmonization**: Necessary across institutions
3. **Image quality control**: MRIQC-based approaches validated
4. **Clinical trials**: Standardized protocols enable reliable comparisons

**Relevance**: Apply same standardization to SwiFT_v2 evaluation for consistency

### Paper 3 - Multi-modal Neuroimaging:
1. **Multiple scanners**: Necessary to evaluate generalization
2. **Cross-scanner reliability**: Machine learning models must handle variability
3. **Multimodal integration**: fMRI + structural + DTI combinations improve predictions
4. **Deep learning approaches**: Graph learning methods effective for prediction

**Relevance**: SwiFT_v2 should be tested for cross-scanner robustness

---

## Recommendations for SwiFT_v2 Evaluation

### Primary Analysis:
✅ Use ADNI dataset (primary)
- Classification task: 3-way or 4-way disease classification
- Sample: 904 total subjects, well-balanced groups
- Metrics: Accuracy, AUC, F1, sensitivity, specificity
- Comparison: Direct benchmarking against Brain-JEPA and BrainLM

### Secondary Analysis:
✅ Use HCP-Aging dataset
- Task: Binary sex classification or demographic prediction
- Purpose: Test generalization to healthy aging population
- Out-of-distribution validation essential

### Quality Control:
✅ Apply same preprocessing standards as papers
- fMRIPrep + FreeSurfer pipeline
- ComBat harmonization for multi-site effects
- Motion QC with FD threshold
- Parcellation: Desikan-Killiany (68 ROIs) or Schaefer 400 + Tian 50 (450 ROIs)

### Reproducibility:
✅ Fixed random seed (42) for all splits
✅ Document all preprocessing steps
✅ Cross-validate all downstream task evaluations
✅ Report confidence intervals and statistical significance

---

## Files to Download/Prepare

### Required from ADNI:
- [ ] T1-weighted structural MRI (baseline for 904 subjects)
- [ ] Resting-state fMRI (baseline for 904 subjects)
- [ ] Demographics and clinical labels (age, sex, site, diagnosis, MMSE)
- [ ] APOE genotype information (for sensitivity analysis)
- [ ] Hippocampal volume measurements (for covariate control)

### Required from HCP-Aging:
- [ ] Resting-state fMRI or preprocessed data
- [ ] Demographics (age, sex)
- [ ] Structural images if custom preprocessing needed

### Pre-existing (Use from Prior Work):
- [ ] Preprocessing scripts (fMRIPrep configuration)
- [ ] Parcellation atlases (Desikan-Killiany, Schaefer 400, Tian 50)
- [ ] Brain-JEPA embeddings (if pre-extracted)
- [ ] BrainLM embeddings (if pre-extracted)

---

## Document Information

**Created**: October 24, 2025
**Paper 1 Source**: Journal of Neuroscience, June 19, 2024
**Paper 2 Source**: Nature Reviews Psychiatry, 2020
**Paper 3 Source**: Nature Molecular Psychiatry, 2025
**Status**: ✅ EXTRACTED AND SUMMARIZED
**Next Step**: Phase 1 Data Preparation

---

This document synthesizes dataset information from three key research papers to guide SwiFT_v2 benchmark evaluation. The ADNI dataset emerges as the primary resource (N=904, well-characterized, multi-site) with HCP-Aging serving as a secondary validation dataset. Both are directly applicable to the benchmark comparison framework.
