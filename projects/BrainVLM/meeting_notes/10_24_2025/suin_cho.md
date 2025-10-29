알겠습니다. `` 태그를 모두 제거하고 다시 정리한 내용입니다.

---

# BrainVLM 실험 결과 요약 (alignment style: LLaVA)
* **Dataset: ABCD (Adolescent Braib Cognitive Development)** 
* **N_samples: about 12,000** 
* **input data: T1-weighted MRI** 
* **prediction target: biological sex (via text generation. Like Google T5, perform classification task via text generation framework)** 
* **model evaluation metric: Accuracy** 
* **aim: designing prompt to find the best way to apply natural image and text pre-trained model to neuroimaging data analysis**

## 슬라이드 2: 실험 결과 

### 1. Training: QnA & Inference: QnA
* Example of prompt used for training : 
    1. "QnA" format "Default":  
        ```
        User: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.
            Estimate sex of subject from this image.

        ASSISTANT: 
            male
        ```
    2. "QnA" format "CoT": 
        ```
        USER: <image>\n
           As a neurologist, analyze this T1-weighted MRI for sex classification.
           Consider these features in order:
           - Overall brain volume relative to skull
           - Gray/white matter distribution patterns 
           - Ventricular size and shape
           - Cortical thickness patterns
           Estimate sex of subject from this image.

        ASSISTANT: 
            male
        ```
    3. "QnA" format "Contrastive": 
        ```
        USER: <image>\n
            As a neurologist, analyze this T1-weighted MRI for sex classification.
            If this were a MALE brain, you would expect: larger intracranial volume and a higher proportion of white matter.  
            If this were a FEMALE brain, you would expect: a higher gray-to-white matter ratio and stronger interhemispheric connectivity.
            Estimate sex of subject from this image.

        ASSISTANT: 
            male
        ```

* Example of prompt used for inference : 
    1. "QnA" format "Default":  
        ```
        User: <image>
        You are a neurologist and now you are analyzing T1-weighted MRI images.
        What is the biological sex of this subject? 

        ASSISTANT: 
        male
        ```
    2. "QnA" format "CoT": 
        ```
        USER: <image>\n
           As a neurologist, analyze this T1-weighted MRI for sex classification.
           Consider these features in order:
           - Overall brain volume relative to skull
           - Gray/white matter distribution patterns 
           - Ventricular size and shape
           - Cortical thickness patterns
           Estimate sex of subject from this image.

        ASSISTANT: 
            male
        ```

    3. "QnA" format "Contrastive": 
        ```
        USER: <image>\n
            As a neurologist, analyze this T1-weighted MRI for sex classification.
            If this were a MALE brain, you would expect: larger intracranial volume and a higher proportion of white matter.  
            If this were a FEMALE brain, you would expect: a higher gray-to-white matter ratio and stronger interhemispheric connectivity.
            Estimate sex of subject from this image.

        ASSISTANT: 
            male
        ```

* **Default:** 0.7869
* **CoT:** 0.7315
* **Contrastive:** 0.7580

**분석:**
* Training과 Inference가 같은 포맷일 때 format mismatch가 없습니다.
* Default가 가장 높은 성능을 보였습니다.
* CoT가 의외로 낮은 성능을 보였는데, 이는 CoT instruction이 오히려 모델을 혼란스럽게(confuse) 만들 수 있음을 시사합니다.
* CoT가 Brain volume이나 gray-to-white ratio 같은 feature가 실제로 중요한지, 아니면 잘못된 사전 정보(wrong prior)를 줄 수도 있습니다.

### 2. Training: Description & Inference: QnA
* Example of prompt used for training : 
    1. "Description" format "Default-simple":  
        ```
        User: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.

        ASSISTANT: 
            The brain shows male characteristics.
        ```
    2. "Description" format "Default-complex":  
        ```
        User: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.

        ASSISTANT: 
            The brain shows typical male characteristics including larger overall brain volume, 
            lower gray-to-white matter ratio, increased ventricular size, and lower cortical thickness.
        ```
    

* Example of prompt used for inference : 
    1. "QnA" format "Default-simple":  
        ```
        User: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.
            Estimate sex of subject from this image.

        ASSISTANT: 
            male
        ```
    2. "QnA" format "Default-complex":  
        ```
        User: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.
            Estimate sex of subject from this image.

        ASSISTANT: 
            male
        ```

* Example of prompt used for inference : 
* **Default-complex:** 0.6402
* **Default-simple:** 0.7405

**분석 (Complex):**
* Complex(Open ended) 케이스는 0.64로 거의 random performance에 가깝습니다.
* 발생한 문제점들은 다음과 같습니다:
    1.  Deterministic template 암기
    2.  Visual feature 무시: Template 암기로 loss를 낮출 수 있어 이미지를 제대로 보지 않음
    3.  Inference collapse: Visual feature가 약해 male/female 판단을 못하고 random guess

**분석 (Simple):**
* Simple 케이스는 0.7405로 괜찮은 성능을 보였습니다.
* **이유:**
    * 암기할 template이 없음
    * Visual feature를 사용할 수밖에 없음
    * 짧은 generation이라 안정적

**종합:**
* **흥미로운 점:** Simple (0.7405)이 QnA→QnA (0.7869)보다는 낮지만, 여전히 합리적인(reasonable) 수준입니다.
* Description training이 더 풍부한 supervision을 제공하는 효과가 있지만, format mismatch로 인한 약간의 성능 하락이 존재합니다.

---

## 슬라이드 3: Training: Description (CoT-complex) & Inference: QnA

* Example of prompt used for training : 
    1. "Description" format "CoT-complex": 
        ```
        USER: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.
            Considering these features in order: 
                - Overall brain volume relative to skull
                - Gray/white matter distribution patterns 
                - Ventricular size and shape
                - Cortical thickness patterns


        ASSISTANT: 
            The brain shows typical male characteristics including larger overall brain volume, 
            lower gray-to-white matter ratio, increased ventricular size, and lower cortical thickness.
        ```

* Example of prompt used for inference : 
    1. "QnA" format "CoT-complex": 
        ```
        USER: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.
            Considering these features in order: 
                - Overall brain volume relative to skull
                - Gray/white matter distribution patterns 
                - Ventricular size and shape
                - Cortical thickness patterns
            Estimate sex of subject from this image.


        ASSISTANT: 
            male
        ```

* **CoT-complex: 0.6142**

* **성능 저하 이유:**
    1.  CoT instruction이 길어서 더 복잡함
    2.  Complex answer도 길어서 open-ended generation의 어려움이 증폭됨
    3.  두 가지가 결합되어 성능이 더 악화됨

* CoT가 "Consider these features in order: Overall brain volume, Gray/white matter distribution..."처럼 구체적인 feature를 나열하는 것이 오히려:
    * Visual attention을 방해하거나
    * 잘못된 사전 정보(Wrong prior)를 제공하거나
    * Text에 더 의존하게 만들 수 있습니다

---

## 슬라이드 4: CoT-simple 결과

* Example of prompt used for training : 
    1. "Description" format "CoT-complex": 
        ```
        USER: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.
            Considering these features in order: 
                - Overall brain volume relative to skull
                - Gray/white matter distribution patterns 
                - Ventricular size and shape
                - Cortical thickness patterns


        ASSISTANT: 
            The brain shows male characteristics.
        ```

* Example of prompt used for inference : 
    1. "QnA" format "CoT-complex": 
        ```
        USER: <image>\n
            You are a neurologist and now you are analyzing T1-weighted MRI images.
            Considering these features in order: 
                - Overall brain volume relative to skull
                - Gray/white matter distribution patterns 
                - Ventricular size and shape
                - Cortical thickness patterns
            Estimate sex of subject from this image.

        ASSISTANT: 
            male
        ```

* **CoT-simple: 0.7387**
* Simple answer를 사용하니 CoT도 어느 정도 작동합니다.
* 하지만 여전히 Default-simple (0.7405)보다 약간 낮습니다.

---

## 슬라이드 5: Multi-modal Projector Frozen 문제

### 현재 설정

* Patch Embedding만 학습
* Visual Encoder body: Freeze
* **Projector: Freeze ← 문제!**
* Language Model: Freeze

### Projector가 Freeze될 경우

1.  Dimension matching은 되지만 semantic alignment는 안 됨
2.  Brain MRI의 "large volume" feature가 language model의 embedding space에서 엉뚱한 위치로 mapping됨
3.  Language model이 visual token을 이해하지 못함

### 결과

* **Complex text:** Visual feature를 못 쓰고 template 암기 → 0.64
* **Simple text:** 어쩔 수 없이 약한 visual signal이라도 사용 → 0.74
---
