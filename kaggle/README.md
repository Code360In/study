# 데이터가 뛰어노는 AI 놀이터, 캐글 
## 사이트
- 캐글 공식 블로그 [Link](https://medium.com/kaggle-blog)
- 캐글 슬랙 [Link](https://kagglenoobs.slack.com/)
- 과거 솔루션 정리 [Link](https://www.kaggle.com/sudalairajkumar/winning-solutions-of-kaggle-competitions)

## 클라우드
- 구글 클라우드 플랫폼(GCP,인기), 아마존 웹 서비스(AWS)
  * CPU나 메모리는 클라우드의 가성비가 매우 우수
  * GPU의 경우 계속해서 자주 사용할 때는 로컬 PC쪽이 가성비가 좋을 것으로 판단되지만 일시적으로 리소스를 늘릴 수 있는 등 클라우드의 장점도 있음
  * GCP의 선점형 인스턴스 등을 사용하면 절약(실행 도중 강제로 인스턴스를 멈출 기능성이 있긴 하지만 저렴한 가격으로 이용 가능)
  * 구글 빅쿼리 등 클라우드형 DB를 이용하여 큰 데이터에서 고속으로 특징을 생성

## 용어 설명
- 목적 변수 : 예측하려는 레이블이나 값 
- 특징 : 각 행 데이터는 목적변수 예측에 필요한 다양한 값을 포함 
- 태스크 : 대회에 출제되는 문제
- 셰이크 업(shake up) : Public Leaderboard 페이지와 Private Leaderboard 페이지의 순위가 크게 바뀌는 현상 
- 캐글러 : 캐글에 모이는 사용자나 대회 참가자
- 캐글링 : 캐글에서 활동하거나 경진 대회에 참가하는 행동

## 경진대회
### 회귀
- 대표 경진 대회 : House Prices, Zillow's Prize
- RMSL,MAE

### 이진 분류
- 대표 경진 대회 : Titanic, Home Creidit Default Risk
- F1-score, 로그 손실, AUC

### 다중 클래스 분류
- 다중 클래스 분류 : Two Sigma Connect : Rental Listing Inquiries
- 다중 레이블 분류 : Human Protein Atlas Image Classification
- 다중 클래스 분류 일때 다중 클래스 로그 손실, 다중 레이블 분류 일때 mean-F1, macro-F1

### 추천 문제
-  대표 경진 대회 : Santander Prodcut Recommendation, Instacart Market Basket Analysis
- 순위를 매겨 예측값을 제출할 때는 : MAP@k, 순위를 매기지 않을 때는 mean-F1, macro-F1

### 객체 탐지
- 이미지에 포함된 물체의 클래스와 해당 물체가 존재하는 직사각형의 경계 박스 영역을 추정하는 문제 
- 대표 경진 대회 : Google AI Open Images - Object Detection Track

### 세분화
- 이미지에 포함된 물체의 영역을 이미지 픽셀 단위로 추정하는 문제
- 대표 경진 대회 : TGS Salt Identification Challenge

## 평가지표
### RMSE(제곱근평균제곱오차)
- 각 행 데이터에 대한 예측값과 실제값의 차이를 제곱하고 , 그 값의 평균을 내 제곱근을 구함 
- RMSE의 값을 최소화했을 때 결과과, 오차가 정규분포를 따른다는 전제하에 구할 수 있는 최대가능도방법과 같아짐 
- MAE에 비교하면 이상치의 영향을 받기 쉬우므로 이상치를 제외한 처리 등을 미리 해두지 않으면 이상치에 과적합한 모델을 만들 가능성이 있음 
```python
from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_true,y_pred))

### RMSLE
- RMSE가 실제값과 예측값 차의 평균제곱 제곱근인데 반해, RMSLE는 실제값과 예측값의 로그를 각각 취한 후 , 그 차의 제곱평균제곱제곱근으로 계산되는 지표
- 목적변수의 분포가 한쪽으로 치우치면 큰 값의 영향력이 일반적인 RMSE보다 강해지기 때문에 이를 방지하려고 사용
- 실제값과 예측 값의 비율을 측정 지표로 사용하고 싶을 경우에 사용 

###  MAE
- 실제값과 예측값의 차에 대한 절대값의 평균으로 계산되는 지표 
- 이상치의 영향을 상대적으로 줄여주는 평가에 적절한 함수 

### 결정계수
- 회귀분석의 적합성을 나타냄

### 각 행 데이터가 양성인지 음성인지 예측값으로 하는 평가지표
- 혼동행렬(confusion matrix) : 모델의 성능을 평가할 때 주로 사용하는 지표 
- 정확도 : 예측이 정확한 비율
- 오류율 : 예측이 잘못된 비율 
- 정밀도(precision) : 양성으로 예측한 값 중에서 실제값도 양성일 비율 -> 잘못된 예측을 줄이고 싶다면 정밀도를 중시
- 재현율(recall) :  실제값이 양성인 것 중에 예측값이 양성일 비율  -> 실제 양성인 데이터를 양성으로 올바르게 예측하고 싶다면 재현율을 중시
 * 정밀도와 재현율은 어느 한 쪽의 값을 높이려 할 때 다른 쪽의 값은 낮아지는 트레이드 오프(Trade off) 관계 
- F1-score : 정밀도와 재현율의 조화 평균으로 계산되는 지표 
- Fbeta_score : 정밀도와 재현율의 균형(조화 평균)에서 계수 베타에 따라 재현율에 가중치를 주어 조정한 지표 
- 매튜상관계수(MCC) : 불균형한 데이터의 모델 성능을 적절히 평가하기 쉬운 지표(-1~1, 1:완벽한 예측, 0:랜덤한 예측, -1:완전 반대 예측) - matthews_corrcoef
 * F1-score와 달리 양성과 음성을 대칭취급하므로 실제값과 예측값의 양성과 음성을 서로 바꿔도 점수 같음 
 
 ### 각 행 데이터가 양성일 확률을 예측할 때의 평가지표
 - 로그 손실 : 분류 문제의 대표적인 평가지표로 교차 엔트로피(cross-entropy), 로그 손실이 낮을 수록 좋은 지표 
 - AUC : ROC곡선을 이용하여 계산, 양성과 음성을 각각 랜덤 선택했을 때 양성 예측값이 음성 예측값보다 클 확률 
  * FPR(거짓 양성 비율) : 실제 거짓인 행 데이터를 양성으로 잘못 예측한 비율(FP/(FP+TN))
  * TPR(참 양성 비율) : 실제 참인 행 데이터를 양성으로 올바르게 예측한 비율(TP/(TP+FN))
  * 양성이 매우 적은 불균형 데이터의 경우 양성인 예측값을 얼마나 높은 확률로 예측할 수 있을지 AUC에 크게 영향을 미침, 음성인 예측값의 오차 영향은 그리 안큼 
  * 지니 계수는 Gini=2AUC-1, AUC와 선형 관계 -> roc_auc_score

### multi_class
- multi_class-accuracy :예측이 올바른 비율을 나타내는 지표로, 예측이 정답인 행 데이터 수를 모든 행 데이터 수로 나눈 결과 
- multi-class-logloss : 다중 클래스 로그 손실, 로그 손실을 다중 클래스 분류로 확장, 각 클래스의 예측 확률을 제출하고, 행 데이터가 속한 클래스의 예측 확률을 로그를 취해 부호를 반전시킨 값
- mean-F1 : 행 데이터 단위로 F1-score를 계산하고 그 평균값이 평가지표 점수 
- macro-F1: 각 클래스별 F1-score를 계산하고 이들의 평균값을 평가지표로 점수 
- QWK(Quadratic Weighted Kappa) 다중 클래스 분류에서 클래스 간에 순서 관계가 있을 때 사용, 각 행 데이터의 예측값이 어느 클래스에 속하는지 제출 -> cohen_kappa_score
- MAP@K : Mean Average Precision At(@) K의 약자, 각 행 데이터가 하나 또는 여러 클래스에 속할 때 ,포함될 가능성이 높을 것으로 예측한 순서대로 K개의 클래스를 예측값으로 삼음 

- 목적함수 : 모델 학습 시 최적화되는 함수(회귀 : RMSE, 분류 : 로그 손실 많이 사용) 
