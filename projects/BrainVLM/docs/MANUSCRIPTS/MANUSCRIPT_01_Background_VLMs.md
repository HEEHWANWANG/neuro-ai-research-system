# Manuscript 01: Background - Evolution of Vision-Language Models

**Slides Covered**: Pages 2-9
**Word Count**: ~1450 words
**Date**: November 12, 2025

---

## The Rise of Vision-Language Foundation Models

The integration of visual and linguistic modalities represents one of the most transformative developments in artificial intelligence over the past five years. Vision-language models (VLMs) have evolved from simple image-text matching systems into sophisticated multi-modal foundation models capable of complex reasoning, zero-shot learning, and cross-domain transfer. This evolutionary trajectory provides essential context for understanding UMBRELLA (Universal Framework for Multimodal Brain Representation Learning by Embedding Large Language Models), a novel approach that adapts these powerful architectures for neuroimaging analysis.

## CLIP: The Contrastive Learning Foundation

The journey begins with CLIP (Contrastive Language-Image Pre-training), introduced by OpenAI in 2021. CLIP established the fundamental paradigm of aligning visual and textual representations through contrastive learning. The architecture employs separate encoders for images and text, trained to maximize the cosine similarity between corresponding image-text pairs while minimizing similarity for non-matching pairs.

The CLIP loss function elegantly captures this objective:

```
L_NCE = -log[exp(z_i · z_j /τ) / Σ_k exp(z_i · z_k /τ)]
```

where `z_i` and `z_j` represent image and text embeddings, and τ is a temperature parameter. This contrastive approach enables CLIP to learn rich, aligned representations from 400 million image-text pairs scraped from the internet, without requiring manually annotated datasets.

CLIP's significance extends beyond its technical architecture. It demonstrated that vision-language alignment at scale produces emergent zero-shot capabilities—the model can classify images into categories it has never explicitly seen during training, simply by comparing image embeddings to text descriptions of those categories. This property makes CLIP a powerful foundation for transfer learning across diverse visual domains.

## BLIP: Bootstrapping with Frozen Encoders

Building upon CLIP's success, BLIP (Bootstrapping Language-Image Pre-training) introduced architectural innovations that enhanced multi-modal understanding. BLIP employs three key components: an image encoder, a text encoder, and a multimodal encoder-decoder that enables more flexible interaction between visual and linguistic information.

BLIP's training strategy incorporates three complementary objectives:
1. **Image-Text Matching**: Binary classification determining whether an image and text correspond
2. **Image-Text Contrastive Learning**: Similar to CLIP's contrastive objective
3. **Image-Grounded Text Generation**: Autoregressive language generation conditioned on visual input

This multi-objective training enables BLIP to excel at both discriminative tasks (image-text retrieval) and generative tasks (image captioning), demonstrating greater versatility than CLIP. The Q-Former architecture, introduced in BLIP-2, further refined this approach by learning a set of query tokens that extract task-relevant visual features through cross-attention mechanisms. Crucially, BLIP-2 keeps the pre-trained image encoder and language model frozen, training only the lightweight Q-Former to bridge these modalities—a strategy that dramatically reduces computational requirements while maintaining performance.

## Flamingo: Few-Shot Multi-Modal Learning

Flamingo, developed by DeepMind, extended vision-language models into the few-shot learning domain. Flamingo's architecture interleaves frozen vision encoders with frozen large language models through learned gated cross-attention layers. This design enables the model to process arbitrarily interleaved sequences of images and text, supporting tasks like visual question answering with contextual examples.

Flamingo's key innovation lies in its training approach: massive-scale pre-training on billions of image-text pairs, followed by few-shot adaptation. The model demonstrates that large language models can be adapted to visual reasoning with minimal task-specific fine-tuning, provided the right architectural bridges exist between modalities. Flamingo's success on visual question answering benchmarks with just a handful of examples highlighted the potential of in-context learning for multi-modal systems.

## LLaVA: Instruction Tuning for Visual Assistants

LLaVA (Large Language and Vision Assistant) represents a paradigm shift toward instruction-following vision-language models. Unlike CLIP and BLIP, which focus on aligning representations, LLaVA emphasizes natural conversational interaction. The architecture connects a CLIP vision encoder to a large language model (Vicuna) through a simple linear projection layer.

LLaVA's distinctive contribution is its training methodology. Rather than relying on existing image-text datasets, LLaVA uses GPT-4 to generate rich, instruction-following training data from images. These generated conversations include detailed descriptions, complex reasoning questions, and multi-turn dialogues—enabling LLaVA to engage in sophisticated visual reasoning tasks.

The training pipeline follows two stages:
1. **Pre-training**: Align visual and language representations using image-caption pairs
2. **Instruction tuning**: Fine-tune on GPT-4-generated visual instruction data

This approach produces a model that can answer open-ended questions about images, provide detailed descriptions, and engage in contextual reasoning—capabilities that prove valuable for specialized domains like medical imaging and neuroscience.

## Scaling to Multi-Modal Diversity

Recent architectures have expanded beyond image-text pairs to encompass broader modality spaces. OneLLM introduces a universal projection module that can align multiple modalities (images, video, audio, point clouds, IMU data) with language models through learned routing weights. X-Instruct BLIP employs BLIP-style alignment with cross-attention for diverse modality tokenization. AnyMAL uses LLaVA-style concatenation with modality-specific encoders and multi-modal instruction tuning.

These architectures share a common insight: **strong feature extractors are paramount**. Regardless of the alignment strategy (cross-attention vs concatenation), success hinges on pre-trained encoders that capture meaningful representations of their respective modalities. This observation proves critical for UMBRELLA's design philosophy.

## Medical Domain Adaptation: Med-Gemini and Med-BLIP

The medical imaging community has rapidly adapted vision-language architectures for clinical applications. Med-Gemini, built upon Google's Gemini foundation model, demonstrates state-of-the-art performance across multiple medical imaging modalities (radiology, pathology, dermatology) through domain-specific fine-tuning and self-training with synthetic reasoning chains.

Med-BLIP applies BLIP's Q-Former architecture to medical visual question answering, aligning medical images with clinical text through contrastive learning and instruction tuning. Both models highlight a crucial pattern: foundation models trained on natural images can be effectively adapted to medical domains through appropriate fine-tuning, despite significant distributional differences between natural and medical images.

However, an important limitation exists: neither Med-Gemini nor Med-BLIP explicitly addresses confounder handling. Med-Gemini explicitly excludes demographic metadata (age, sex, medical history) from its reasoning, focusing purely on visual features. This design choice, while simplifying the model, leaves unaddressed a critical challenge in medical AI: disentangling disease-specific features from demographic confounders.

## BrainHarmonix: Brain-Specific Multi-Modal Foundations

The emergence of BrainHarmonix signals a new frontier: brain-specific multi-modal foundation models. BrainHarmonix integrates structural MRI (sMRI) with functional MRI (fMRI) exhibiting heterogeneous temporal repetition times, learning joint representations that span brain morphology and dynamics.

BrainHarmonix employs two training paradigms:
1. **Unimodal Encoding**: Independent encoders for structural and functional brain data
2. **Multimodal Fusion**: A "Brain Hub" that learns cross-modal relationships through geometric harmonics and biological constraints

This architecture demonstrates that brain-specific inductive biases—incorporating known neuroscientific principles—can enhance multi-modal learning for neuroimaging. BrainHarmonix's success suggests that specialized foundation models for neuroscience are not only feasible but may outperform generic vision models for brain imaging tasks.

## Key Insights for Neuroimaging

The evolution of vision-language models reveals several principles applicable to neuroimaging:

1. **Foundation model leverage**: Pre-trained models on large-scale data enable efficient transfer to specialized domains
2. **Alignment architecture diversity**: Both cross-attention (BLIP-2) and concatenation (LLaVA) approaches succeed when encoders are strong
3. **Language as interface**: Text generation frameworks provide natural integration with reasoning systems
4. **Scalability through language**: Language-centric architectures scale better with modality and task diversity
5. **Domain adaptation works**: Natural image encoders transfer surprisingly well to medical/neuroimaging domains

However, existing medical vision-language models exhibit a critical gap: **they do not explicitly model confounders**. Brain imaging faces unique challenges—age-related atrophy, sex differences in brain structure, genetic predispositions—that confound disease diagnosis if not properly disentangled. Addressing this gap requires moving beyond format diversity (the redundant multi-tasking of Med-Gemini) toward **complementary multi-tasking** that explicitly separates disease-specific features from demographic and genetic confounders.

## From Vision-Language Models to Brain-Language Models

The stage is now set for UMBRELLA's innovation: adapting vision-language architectures to brain imaging while introducing a revolutionary approach to confounder handling through **unified language generation**. Rather than designing explicit weighted loss functions for multiple tasks (disease classification, age prediction, sex classification, genetic risk estimation), UMBRELLA encodes all this complementary information as text, training a single language model to generate comprehensive brain descriptions from neuroimaging.

This paradigm shift—from prediction frameworks to text generation frameworks—enables unprecedented extensibility. Adding new confounders, biomarkers, or clinical targets requires no architectural changes or loss function re-engineering. It simply involves extending the target text to include additional information. As we will explore in subsequent sections, this approach eliminates hyperparameter tuning for task weights while maintaining—and potentially exceeding—the performance of traditional multi-task learning.

The evolution from CLIP to UMBRELLA represents not merely an application of existing techniques to a new domain, but a fundamental rethinking of how multi-modal medical AI should handle the complexity inherent in brain imaging analysis.

---

**Next**: Manuscript 02 introduces UMBRELLA's core concepts, architectural design, and the unified language generation paradigm that distinguishes it from traditional multi-task learning approaches.
