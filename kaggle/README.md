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
