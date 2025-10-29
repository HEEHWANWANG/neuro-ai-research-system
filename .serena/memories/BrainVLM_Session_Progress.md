# BrainVLM Research Session Progress
**Date**: October 29, 2025
**Status**: Analysis complete with architectural clarification applied

## Key Architectural Understanding
- **BLIP-2 vision encoder** = EVA_CLIP = EVA_ViT (same foundation)
- This explains similar performance profiles between BLIP-2 and EVA_ViT baselines
- Vision encoder architecture is NOT the differentiator between models
- Key differentiator: How the vision encoder is integrated with language model

## Critical Bottleneck Identified
- **Multi-modal projector is FROZEN** → prevents semantic alignment
- Estimated improvement: 10-20% if unfrozen
- This is THE single most important architectural fix for next week

## Performance Summary
| Task | Model | Performance | Issue |
|------|-------|-------------|-------|
| Sex Classification | LLaVA | 78.69% | Moderate - reasonable baseline |
| Age Regression | EVA-ViT | R²=0.1254 | Weak - only 12.5% variance explained |
| MMSE Regression | EVA-ViT | R²=0.0183 | Critical - essentially zero predictive power |

## Major Findings from Experiments
1. **Pretraining essential**: Scratch training fails universally
2. **Prompting matters**: Simple beats complex (Chain-of-Thought -5.5% performance drop)
3. **Template risk**: Complex descriptions → 0.64 accuracy (near random)
4. **Task-specific losses**: Age regression needs MAE, MMSE needs MSE (opposite optimization patterns)
5. **Frozen projector**: CRITICAL CONSTRAINT limiting all downstream performance

## Vision Encoder Clarification
- BLIP-2 uses EVA_CLIP (= EVA_ViT) as vision encoder
- LLaVA uses its own vision encoder architecture (ViT-L)
- Similar performance between BLIP-2 and EVA_ViT due to shared backbone
- The difference lies in how projector integrates vision→language features

## Next Actions (Prioritized)
1. **CRITICAL (Week 1)**: 
   - Unfreeze multi-modal projector (requires_grad=True)
   - Expand MMSE dataset (1,905→4,000 samples for statistical power)
   - Implement learning rate scheduling for unfrozen components
   
2. **Important (Week 2)**:
   - Systematic ablation studies (frozen vs unfrozen component comparison)
   - Confidence calibration metrics
   - Cross-validation for robustness assessment

3. **Quality (Week 3)**:
   - Statistical rigor improvements (confidence intervals, p-values, effect sizes)
   - Comparison with published baselines
   - Multiple random seed runs for stability

## Research Assessment
- **Overall**: 7/10 (honest systematic work, but architectural flaw must be fixed)
- **Strength**: Critical bottleneck identified and solution is clear/actionable
- **Weakness**: Low absolute performance until projector unfrozen prevents robust conclusions
