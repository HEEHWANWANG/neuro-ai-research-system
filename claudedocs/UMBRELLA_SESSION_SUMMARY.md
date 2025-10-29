# UMBRELLA Vision Update - Session Summary
**Date:** October 29, 2025
**Status:** Complete reframing based on presentation analysis and core vision clarification

---

## Session Overview

This session completely reframed the understanding of the BrainVLM project (code name: UMBRELLA) from a regression prediction system to a text generation framework for medical report generation from multi-modal MRI.

---

## Deliverables Completed

### 1. Three Comprehensive Vision Documents

**BRAINVLM_UMBRELLA_CORE_VISION.md** (29KB)
- Complete technical and strategic vision
- How UMBRELLA extends natural image-language models to neuroimaging
- Three-fold novel contributions with technical depth
- Two-step training strategy with code templates
- 4-phase 12-month implementation roadmap
- Caption engineering: solving "how to describe brain MRI"
- Performance metrics for text generation evaluation

**BRAINVLM_UMBRELLA_QUICK_SUMMARY.md** (10KB)
- Executive summary for quick reference
- Key insights and strategic decisions
- Implementation priorities (Week 1-2 focused)
- Architecture changes under UMBRELLA lens

**BRAINVLM_ARCHITECTURAL_CLARIFICATION.md** (UPDATED)
- Reinterpreted architectural insights under text generation framework
- Frozen/unfrozen components now understood as part of 2-step strategy
- Performance expectations realigned with Step 1/Step 2 progression
- Bottlenecks reframed: caption engineering, LLM decoder, text generation

### 2. Project Meeting Notes

**projects/BrainVLM/meeting_notes/10_24_2025/SUMMARY.md**
- 50+ page comprehensive analysis of experiments
- Suin Cho's LLaVA experiments (78.69% sex classification)
- Janice's EVA-ViT regression (R²=0.1254 age, R²=0.0183 MMSE)
- Vision encoder equivalence analysis (BLIP-2 = EVA-CLIP = EVA_ViT)
- Architectural bottleneck identification
- Recommendations aligned with UMBRELLA vision

---

## Key Paradigm Shifts

### 1. From Regression to Text Generation
**Before:**
- MRI image → scalar prediction (age=45, MMSE=28)
- Success metric: R² > 0.25, MSE < threshold

**After:**
- MRI image(s) → medical report (text generation)
- Success metric: Neurologist rating >70%, BERTScore >0.8, BLEU >0.6
- Enables: Report generation, clinical decision support, AI agent integration

### 2. Understanding Two-Step Training
**Step 1 (Current):**
- Train patchifying layer only
- Freeze vision + text encoders
- Adapt 3D/4D MRI to natural image embedding space
- Current experiments are Step 1 baselines

**Step 2 (Future):**
- Fine-tune vision encoder + projector
- Adapt vision encoder to brain-specific features
- PRIMARY GOAL: Preserve natural image-language embedding space (>95% ImageNet performance)
- Enable seamless text generation from brain MRI

### 3. Caption Engineering - The Breakthrough Solution
**The Challenge:** "We don't know how to describe brain MRI"
- Unlike natural images, no common language for MRI appearance
- Different neurologists describe same image differently
- How to train model what features mean?

**The UMBRELLA Solution:** Use structured data as "captions"
- Demographics (sex, age) → initial captions
- Brain metrics (volume, thickness) → expanded captions
- Clinical info (diagnoses, biomarkers) → detailed captions
- Model learns associations: visual features ↔ structured information ↔ text descriptions

**Why It Works:**
- Transforms "unlabeled" problem to supervised learning
- Leverages existing clinical databases
- Teaches model how clinicians think about images
- Enables progressive sophistication (demographics → metrics → clinical reports)

### 4. Google T5 as Foundational Insight
T5 demonstrated:
- Classification tasks → text generation
- Regression tasks → text generation
- Object detection (bounding boxes) → text generation

**UMBRELLA Application:**
- Age prediction → "Subject is 45 years old"
- MCI detection → "Evidence of mild cognitive impairment based on..."
- Brain volumetry → "Hippocampal volume 2.1 cm³ (5th percentile for age)"
- All neuroimaging tasks → coherent medical report

---

## How Current Experiments Map to UMBRELLA Vision

### Suin Cho's LLaVA Experiments (78.69% sex classification)
**Stepping Stone Value:**
- Tests prompt design for MRI domain
- Simple prompts outperform complex (lesson for caption engineering)
- Identifies template memorization risk
- Foundation for UMBRELLA prompt strategy

**Connection to Vision:**
- Currently: Text generation for sex classification
- UMBRELLA goal: Extend to sex + age + diagnosis + metrics in single report

### Janice's EVA-ViT Regression (R²=0.1254 age, R²=0.0183 MMSE)
**Stepping Stone Value:**
- Validates EVA-CLIP vision encoder for brain MRI (preserves ImageNet >95%)
- Identifies Step 1 baseline performance
- Shows vision encoder adaptation is possible

**Connection to Vision:**
- Currently: Step 1 training (patchifying layer only)
- Phase 1 Target: Complete Step 1, achieve robust baselines
- Phase 2 Target: Step 2 training (fine-tune vision encoder + projector)
- Phase 3 Target: Text generation framework
- Phase 4 Target: Full medical report generation

### Both Experiments Together
- Establish that natural image pretraining transfers to brain MRI
- Show performance limits and bottlenecks
- Identify caption engineering as next critical step
- Provide foundation for text generation transition

---

## UMBRELLA Strategic Positioning

### Novel Contributions (3-fold)

**1. Multi-modal MRI Understanding via Text Generation**
- First framework treating neuroimaging as text generation problem
- Enables integration with LLM ecosystem (agents, CoT, RAG)
- Achieves what regression alone cannot: medical report generation

**2. Prompt Design for Neuroimaging Domain**
- Systematic approach to training MRI-based VLMs
- Simple > complex (learned from current experiments)
- Template design that avoids memorization

**3. Caption Engineering - Information Injection Strategy**
- Solves fundamental neuroscience challenge: "How to describe brain?"
- Transforms unstructured images + structured data → unified training signal
- Enables progressive sophistication (demographics → metrics → clinical reasoning)
- Scalable: uses existing clinical databases

### Competitive Advantage
- **vs Brain-JEPA**: Adds language understanding (foundation model only predicts, UMBRELLA explains)
- **vs BrainLM**: Adds structured data integration (uses embeddings, UMBRELLA uses captions)
- **vs MultiModal VLMs**: Brain-specific training strategy (CLIP-aligned but brain-adapted)
- **vs Regression**: Enables report generation (scalar → narrative)

---

## Implementation Roadmap (12 Months)

### Phase 1 (Months 1-3): Foundation
**Deliverables:**
- Text generation framework (replace regression heads with LLM decoder)
- Initial caption engineering pipeline
- Prompt design validation
- Step 1 baseline establishment

**Key Metrics:**
- Sex classification via text: >75% accuracy
- Age text: MAE <5 years via generation
- Neurologist rating of generated text: >5/10

### Phase 2 (Months 4-6): Multi-Modal Integration
**Deliverables:**
- Step 2 fine-tuning (vision encoder + projector)
- Caption expansion (demographics + brain metrics)
- Clinical data integration
- Performance recovery validation (>95% ImageNet)

**Key Metrics:**
- Age text generation: MAE <3 years
- MCI detection via report: AUC >0.75
- Neurologist rating: >7/10

### Phase 3 (Months 7-9): Clinical-Grade Reports
**Deliverables:**
- Comprehensive medical report generation
- Multi-imaging integration (T1w + T2w + DTI + resting fMRI)
- Differential diagnosis reasoning
- Clinical evidence integration

**Key Metrics:**
- Report utility rating: >7.5/10 from neurologists
- Differential diagnosis accuracy: >70%
- Report completeness: covers anatomy, pathology, clinical correlation

### Phase 4 (Months 10-12): AI Agent Integration
**Deliverables:**
- Integration with clinical AI workflows
- Multi-agent reasoning (radiologist + clinician + AI agents)
- Structured output (JSON reports compatible with EHR)
- Clinical deployment infrastructure

**Key Metrics:**
- Clinical decision support accuracy: >75%
- Clinician adoption: >50% usage
- Workflow integration: seamless with existing systems

---

## Revised Performance Expectations

### Step 1 Baselines (Current)
- Sex classification: 78.69% (Suin Cho)
- Age regression: R²=0.1254 (Janice)
- MMSE regression: R²=0.0183 (Janice)

### Step 2 Targets (After Fine-tuning)
- Sex classification: >85% accuracy
- Age prediction: MAE <3 years
- MMSE prediction: R² >0.20
- **NEW: Medical report quality**: Neurologist rating >7/10

### Phase 3+ Targets
- MCI detection from reports: AUC >0.80
- Disease classification: >75% accuracy
- Clinical utility: Physician adoption >50%

---

## Critical Resources & Dependencies

### Data Requirements
- **Demographic captions**: Available (age, sex, ethnicity)
- **Brain metrics**: Requires extraction (volume, thickness, connectivity)
- **Clinical captions**: Requires structured EHR data integration
- **Validation data**: Requires neurologist review

### Computational Resources
- **Phase 1**: Current GPU setup sufficient
- **Phase 2+**: KISTI resources (1.5 hours/epoch limitation)
- **Full pipeline**: Estimated 500-1000 GPU hours for all phases

### Team Skills Needed
- **Vision-Language Models**: Current (BLIP-2, EVA-CLIP expertise)
- **Text Generation**: New (LLM fine-tuning, prompt engineering)
- **Medical Domain**: Requires clinician collaboration
- **Data Engineering**: Caption pipeline and data harmonization

---

## Success Criteria by Phase

### Phase 1 Success
- ✓ Text generation framework operational
- ✓ Sex classification >75% via generated text
- ✓ Initial captions generate coherent descriptions
- ✓ Neurologist rates text as "understandable" (>5/10)

### Phase 2 Success
- ✓ Vision encoder fine-tuning preserves ImageNet >95%
- ✓ Caption expansion to metrics works smoothly
- ✓ Age prediction MAE <3 years in text
- ✓ Neurologist rates text as "clinically useful" (>7/10)

### Phase 3 Success
- ✓ Multi-imaging fusion produces coherent reports
- ✓ Differential diagnosis accuracy >70%
- ✓ Reports include anatomy + pathology + clinical correlation
- ✓ Neurologist rates text as "clinically accurate" (>8/10)

### Phase 4 Success
- ✓ Reports integrate with EHR systems
- ✓ Clinician adoption >50%
- ✓ Clinical decision support accuracy >75%
- ✓ System ready for clinical deployment

---

## Key Documents for Reference

### Core Vision Documentation
1. **BRAINVLM_UMBRELLA_CORE_VISION.md** - Technical deep dive
2. **BRAINVLM_UMBRELLA_QUICK_SUMMARY.md** - Executive summary
3. **BRAINVLM_ARCHITECTURAL_CLARIFICATION.md** - Updated architecture understanding

### Project Context
4. **projects/BrainVLM/meeting_notes/10_24_2025/SUMMARY.md** - Experiment analysis
5. **claudedocs/BRAINVLM_ARCHITECTURAL_CLARIFICATION.md** - Previous architectural analysis

### Related Work
- **Brain-JEPA** papers and code in benchmark comparison
- **BrainLM** foundation model analysis
- **Google T5** paper reference for text generation tasks

---

## Conclusion

The UMBRELLA vision represents a fundamental paradigm shift for neuroimaging AI:
- **From**: Predicting scalars from images
- **To**: Generating medical reports from multi-modal data
- **Enabler**: Caption engineering solving "how to describe brain"
- **Outcome**: Neuroimaging joins language-centric AI revolution

Current experiments (Suin Cho's sex classification, Janice's regression) are not endpoints but **stepping stones** toward comprehensive medical report generation from brain MRI.

The project is strategically positioned at the intersection of:
- Vision-language models (CLIP/BLIP-2 expertise)
- Text generation systems (LLM capabilities)
- Neuroscience domain (clinical knowledge)
- Structured data integration (EHR systems)

Success in UMBRELLA would represent a breakthrough in neuroimaging AI that enables:
- Automated clinical report generation
- Integration with clinical AI workflows
- Training of models on real clinical data at scale
- Deployment of neuroimaging AI in clinical practice

---

**Status:** Complete vision reframing committed to git (3c3532c)
**Ready for:** Phase 1 implementation (text generation framework + caption engineering)
**Team Focus:** Should shift to text generation task design and prompt engineering
