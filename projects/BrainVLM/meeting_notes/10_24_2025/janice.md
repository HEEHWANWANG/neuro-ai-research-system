요청하신 대로, EVA-ViT 모델에 대한 설명을 문서 맨 앞에 추가하여 전체 내용을 다시 정리했습니다.

---

## 0. "EVA-ViT" 모델 소개

본 실험에서 사용된 **'EVA-ViT'** 모델은 [EVA-CLIP: Improved Training Techniques for CLIP at Scale (arXiv:2303.15389)](https://arxiv.org/pdf/2303.15389) 논문에서 제안된 **EVA-CLIP** 모델의 **Vision Encoder (시각 인코더)** 부분을 지칭합니다.

**EVA-CLIP**은 대규모 데이터셋을 활용하여 시각(Vision)과 언어(Language)를 함께 학습하는 CLIP (Contrastive Language-Image Pre-training) 모델의 성능을 향상시킨 모델입니다. 

본 실험의 'Pretrain' 방식은 이 EVA-CLIP의 Vision Encoder (ViT 아키텍처 기반)가 대규모 데이터로 사전 학습된 **pre-trained weight**를 가져와서, GARD 데이터셋의 '연령' 및 'MMSE' 예측 태스크에 맞게 미세 조정(fine-tuning)하는 것을 의미합니다.

---

## 1. 실험 개요

* **모델:** Eva-VIT
* **목표:** GARD 데이터를 활용하여 '연령'(Age) 및 'MMSE' 예측
* **데이터 규모:**
    * **연령 (Age):** N = 4,201
    * **MMSE:** n = 1,905

---

## 2. 실험 설계 (비교 항목)

* **학습 방식:**
    * **Scratch:** 모델을 처음부터 학습
    * **Pretrain:** 사전 학습된 모델 (LAVIS/BLIP2, 즉 EVA-ViT) 활용
* **손실 함수 (Loss Function):**
    * **MSE Loss:** Mean Squared Error (평균 제곱 오차)
    * **ABS Loss:** Mean Absolute Error (평균 절대 오차)
* **주요 평가지표:**
    * **Test R²:** 테스트 데이터셋에 대한 모델의 설명력 (R-squared)

---

## 3. 세부 실험 결과 (Test R² 기준)

| 대상 | 손실 함수 | 학습 방식 | Test R² | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Age** | **abs loss** | **Pretrained (BLIP2)** | **0.1254** | **(Age 예측 Best)** |
| Age | abs loss | Scratch | 0.021 | - |
| Age | mse loss | Pretrained (BLIP2) | Exploded | (학습 실패) |
| Age | mse loss | Scratch | -0.16802 | - |
| **MMSE** | **mse loss** | **Pretrained (BLIP2)** | **0.0183** | **(MMSE 예측 Best)** |
| MMSE | mse loss | Scratch | -0.90166 | - |
| MMSE | abs loss | Pretrained (BLIP2) | -0.0182 | - |
| MMSE | abs loss | Scratch | -0.41037 | - |

*(모든 최적 결과는 `lr = 0.0001` 에서 도출됨)*

---

## 4. 결과 분석 및 요약

### 4.1. 연령 (Age) 예측 (N=4201)

* **Pretrained 모델의 뚜렷한 성능 향상:**
    * 'abs loss' 기준, Pretrained 모델(**R²=0.1254**)이 Scratch 모델(**R²=0.021**) 대비 **약 6배 높은 R²** 값을 기록하며 사전 학습의 효과가 명확하게 나타났습니다.
    * Pretrained 모델은 안정적인 학습 양상(Validation R² 꾸준히 상승)을 보였습니다.
* **손실 함수 적합성:**
    * 'abs loss'가 Age 예측에 더 적합했습니다.
    * 'mse loss'를 사용한 경우, Pretrained 모델은 손실(loss)이 발산(Exploded)했고 Scratch 모델은 R² 값이 음수(-0.16802)로 나와, Age 예측에 부적합함을 확인했습니다.

### 4.2. MMSE 예측 (n=1905)

* **Pretrained 모델의 절대적 우위:**
    * 'mse loss' 기준, Pretrained 모델(**R²=0.0183**)이 유일하게 유의미한 양수 R² 값을 기록했습니다.
    * 반면, Scratch 모델(**R²=-0.90166**)은 R² 값이 매우 큰 음수로, 전혀 학습이 이루어지지 않았음을 보였습니다.
    * 검증 손실(validation loss) 및 R² 지표상, Pretrained 모델이 과적합(overfitting) 없이 더 안정적으로 학습되었습니다.
* **손실 함수 적합성:**
    * 'mse loss'가 'abs loss'보다 MMSE 예측에 더 적합했습니다.
    * 'abs loss'를 사용했을 때는 Pretrained 모델조차 R² 값이 음수(-0.0182)를 기록했습니다.
* **명확한 한계:**
    * 현재 최적 모델의 **R² 값(0.0183) 자체가 매우 낮아** 예측 성능이 높다고 보기 어렵습니다.
    * 이는 학습 데이터 수(n=1905)가 절대적으로 부족하기 때문일 수 있으며, 4,000명대 데이터로 추가 실험이 반드시 필요합니다.

---

## 5. 현재 최적 모델 및 결론

* **Age (absloss) - BLIP 2 (Pretrained):** Test R² = **0.1254** (at lr = 0.0001)
* **MMSE (mseloss) - BLIP 2 (Pretrained):** Test R² = **0.0183** (at lr = 0.0001)
* **주요 결론:** 'Scratch' 모델은 모든 조건에서 R² 값이 음수이거나 매우 낮아 유의미한 성능을 보이지 못했습니다. Age와 MMSE 예측 모두 **사전 학습(Pretrained) 모델(BLIP2/EVA-ViT)을 사용하는 것이 필수적**임을 확인했습니다.

---

## 6. UKB 모델 및 향후 계획

* **UKB 모델 현황 (Blocker):**
    * UKB 사전 학습 모델의 경우, 배치 사이즈(batch size)를 2까지 낮춰도 1 에포크(epoch) 당 1시간 30분(6,000초) 이상 소요되었습니다.
    * 리소스 한계로 인해 이 모델은 **KISTI에서 학습을 진행**할 예정입니다.
* **향후 계획:**
    * **Learning Rate 추가 탐색:** 전반적으로 낮은 `lr`(0.0001)에서 좋은 결과가 나왔으므로, `lr` 범위를 **{0.01, 0.001, 0.0001, 0.00001, 0.000001}**로 넓혀 추가 실험을 진행합니다.
    * **Pretrained 모델 적극 활용:** BLIP2(EVA-ViT)의 효과가 확인되었으므로, KISTI에서 UKB 모델 등 연관된 다른 사전 학습 모델을 적극 활용할 계획입니다.
    * **MMSE 데이터 확장:** 현재 MMSE 성능의 한계(낮은 R²)를 극복하기 위해 **4,000명대 데이터**로 추가 실험을 진행합니다.