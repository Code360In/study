# Recommender systems
# 내용 기반 추천
- 상품의 속성, 즉 '어떤' 상품인지를 사용해서 추천
- 한 유저의 평점이 다른 유저의 평점에 영향을 미치지 않는다 -> 유저들의 평점이 서로 독립적이다 
  * 좋아요/ 싫어요 -> 분류
  * 평점 1~5값 회귀 알고리즘
- 장점
  * 상품을 추천할 때 다른 유저 데이터가 필요하지 않다
  * 새롭게 출시한 상품이나, 인기가 없는 상품을 추천할 수 있다
- 단점
  * 적합한 속성을 고르는 것이 어렵다
  * 고른 속성 값들이 주관적으로 선정될 수 있다
  * 유저가 준 데이터를 벗어나는 추천을 할 수 없다
  * 인기가 많은 상품들을 더 추천해 줄 수 없다

- 선형 회귀
     
     ![image](https://user-images.githubusercontent.com/47103479/124145383-b4b46380-dac7-11eb-95a8-921fe69002bd.png)

- 경사 하강법
  * 손실을 가장 빨리 줄이는 방향으로 세타값들을 바꿔주는 방법

  ![image](https://user-images.githubusercontent.com/47103479/124145641-ef1e0080-dac7-11eb-8868-3718def4a28e.png)

## sklearn으로 유저 평점 예측하기
```python
# 필요한 도구들을 가지고 오는 코드
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np

# 유저 평점 + 영화 속성 데이터 경로 정의
MOVIE_DATA_PATH = './data/movie_rating.csv'

# pandas로 데이터 불러 오기
movie_rating_df = pd.read_csv(MOVIE_DATA_PATH)

features =['romance', 'action', 'comedy', 'heart-warming'] # 사용할 속성들 이름

# 입력 변수와 목표 변수 나누기
X = movie_rating_df[features]
y = movie_rating_df[['rating']]

# 입력 변수와 목표 변수들을 각각의 training/test 셋으로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# 코드를 쓰세요.
model = LinearRegression()
model.fit(X_train,y_train)
y_test_predict = model.predict(X_test)
# 실행 코드
y_test_predict
```
## numpy
- print(np.nansum(A)) - nan 값들만 제외하고 계산
- print(np.nanmean(A)) - nan인 원소를 제외한 다른 모든 원소들의 평균값을 계산

# 협업 필터링 
- 수많은 유저 데이터들이 협업해서 상품 추천 
- 비슷한 유저를 찾아내서, 이 유저들의 평점을 이용해서 추천
- 유클리드 거리
  
  ![image](https://user-images.githubusercontent.com/47103479/124386339-e40be000-dd14-11eb-9694-5c9f43d5851a.png)
  
```python 
import numpy as np
from math import sqrt


def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    return sqrt(np.sum(np.square(user_1 - user_2)))
    # 코드를 쓰세요 

def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    return sqrt(np.sum((user_1 - user_2)**2))

# 실행 코드
user_1 = np.array([0, 1, 2, 3, 4, 5])
user_2 = np.array([0, 1, 4, 6, 1, 4])

distance(user_1, user_2)
```
- 코사인 유사도 

- ![image](https://user-images.githubusercontent.com/47103479/124489958-84810380-ddec-11eb-936a-0bbfb2124822.png)
  
- 전처리 방법
 * 0으로 계산하기 -> 유사도 계산
 * 유저 별 평균 평점으로 계산하기
 * Mean Normalization으로 계산하기 -> 유저 평점에서 각 유저의 평균 평점을 다시 빼주는 것

- 유클리드 거리(작은) vs 코사인 유사도(큰)
 * 코사인 유사도는 각 벡터, 또는 선의 크기가 중요하지 않다는 점
 * 유클리드 거리는 클수록 두 데이터가 다르고, 작을수록 두 데이터가 비슷하다는 의미였고, 코사인 유사도는 클수록 두 데이터가 비슷하고, 작을수록 두 데이터가 다르다는 의미
 * 유저 A와 가장 '비슷한' 유저들을 찾을 때 유클리드 거리는 거리가 가장 작은 유저들을 찾아야 되고요. 코사인 유사도는 유사도가 가장 큰 유저들을 찾아야함!

- 상품추천하기
 * r(x) : 유저 x에 대한 평점 데이터 벡터.
 * ri(x) : 유저 x의 영화 i에 대한 평점
 * N: 상품 i를 평가한 유저 중 유저 x와 가장 비슷한 k명의 집합
 
 ![image](https://user-images.githubusercontent.com/47103479/125152190-03c45d80-e186-11eb-929b-c33d99a35330.png)

- 코딩
