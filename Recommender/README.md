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
- 장점
 * 속성을 찾거나 정할 필요가 없다
 * 좀 더 폭넓은 상품을 추천할 수 있다
 * 내용 기반 추천보다 성능이 더 좋게 나오는 경우가 많다
- 단점
   * 데이터가 많아야 한다
     * 유저 한 명이 열심히 평점을 줘도 다른 사람들도 열심히 평점을 줘야 한다.
     * 새로운 물건이나 유저에게 추천해 주기 힘들다
   * 인기가 많은 소수의 상품이 추천 시스템을 장악할 수 있다
   * 어떤 상품이 왜 추천됐는지 정확히 알기 힘들다
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

- 이웃들 구하기
```python 
import pandas as pd
import numpy as np
from math import sqrt

RATING_DATA_PATH = './data/ratings.csv'  # 받아올 평점 데이터 경로 정의

np.set_printoptions(precision=2)  # 소수점 둘째 자리까지만 출력

def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    return sqrt(np.sum((user_1 - user_2)**2))
    
    
def filter_users_without_movie(rating_data, movie_id):
    """movie_id 번째 영화를 평가하지 않은 유저들은 미리 제외해주는 함수"""
    return rating_data[~np.isnan(rating_data[:,movie_id])]
    
    
def fill_nan_with_user_mean(rating_data):
    """평점 데이터의 빈값들을 각 유저 평균 값으로 체워주는 함수"""
    filled_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    row_mean = np.nanmean(filled_data, axis=0)  # 유저 평균 평점 계산
    
    inds = np.where(np.isnan(filled_data))  # 비어 있는 인덱스들을 구한다
    filled_data[inds] = np.take(row_mean, inds[1])  #빈 인덱스를 유저 평점으로 채운다
    
    return filled_data
    
    
def get_k_neighbors(user_id, rating_data, k):
    """user_id에 해당하는 유저의 이웃들을 찾아주는 함수"""
    distance_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    # 마지막에 거리 데이터를 담을 열 추가한다
    distance_data = np.append(distance_data, np.zeros((distance_data.shape[0], 1)), axis=1)
    
    # 코드를 쓰세요.
    for i in range(len(distance_data)):
        row = distance_data[i]
        if i == user_id:  # 같은 유저면 거리를 무한대로 설정
            row[-1] = np.inf
        else:  # 다른 유저면 마지막 열에 거리 데이터를 저장
            row[-1] = distance(distance_data[user_id][:-1], row[:-1])
            
    
    # 데이터를 거리 열을 기준으로 정렬한다
    distance_data = distance_data[np.argsort(distance_data[:, -1])]
    
    # 가장 가까운 k개의 행만 리턴한다 + 마지막(거리) 열은 제외한다
    return distance_data[:k, :-1]
    

# 실행 코드
# 영화 3을 본 유저들 중, 유저 0와 비슷한 유저 5명을 찾는다
rating_data = pd.read_csv(RATING_DATA_PATH, index_col='user_id').values  # 평점 데이터를 불러온다
filtered_data = filter_users_without_movie(rating_data, 3)  # 3 번째 영화를 보지 않은 유저를 데이터에서 미리 제외시킨다
filled_data = fill_nan_with_user_mean(filtered_data)  # 빈값들이 채워진 새로운 행렬을 만든다
user_0_neighbors = get_k_neighbors(0, filled_data, 5)  # 유저 0과 비슷한 5개의 유저 데이터를 찾는다
user_0_neighbors
```

- 유저 평점 예측하기
```python
import pandas as pd
import numpy as np
from math import sqrt

RATING_DATA_PATH = './data/ratings.csv'  # 받아올 평점 데이터 경로 정의

np.set_printoptions(precision=2)  # 소수점 둘째 자리까지만 출력

def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    return sqrt(np.sum((user_1 - user_2)**2))
    
    
def filter_users_without_movie(rating_data, movie_id):
    """movie_id 번째 영화를 평가하지 않은 유저들은 미리 제외해주는 함수"""
    return rating_data[~np.isnan(rating_data[:,movie_id])]
    
    
def fill_nan_with_user_mean(rating_data):
    """평점 데이터의 빈값들을 각 유저 평균 값으로 체워주는 함수"""
    filled_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    row_mean = np.nanmean(filled_data, axis=0)  # 유저 평균 평점 계산
    
    inds = np.where(np.isnan(filled_data))  # 비어 있는 인덱스들을 구한다
    filled_data[inds] = np.take(row_mean, inds[1])  #빈 인덱스를 유저 평점으로 채운다
    
    return filled_data
    
    
def get_k_neighbors(user_id, rating_data, k):
    """user_id에 해당하는 유저의 이웃들을 찾아주는 함수"""
    distance_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    # 마지막에 거리 데이터를 담을 열 추가한다
    distance_data = np.append(distance_data, np.zeros((distance_data.shape[0], 1)), axis=1)
    
    # 코드를 쓰세요.
    for i in range(len(distance_data)):
        row = distance_data[i]
        
        if i == user_id:  # 같은 유저면 거리를 무한대로 설정
            row[-1] = np.inf
        else:  # 다른 유저면 마지막 열에 거리 데이터를 저장
            row[-1] = distance(distance_data[user_id][:-1], row[:-1])
    
    # 데이터를 거리 열을 기준으로 정렬한다
    distance_data = distance_data[np.argsort(distance_data[:, -1])]
    
    # 가장 가까운 k개의 행만 리턴한다 + 마지막(거리) 열은 제외한다
    return distance_data[:k, :-1]
    
def predict_user_rating(rating_data, k, user_id, movie_id,):
    """예측 행렬에 따라 유저의 영화 평점 예측 값 구하기"""
    # movie_id 번째 영화를 보지 않은 유저를 데이터에서 미리 제외시킨다
    filtered_data = filter_users_without_movie(rating_data, movie_id)
    # 빈값들이 채워진 새로운 행렬을 만든다
    filled_data = fill_nan_with_user_mean(filtered_data)
    # 유저 user_id와 비슷한 k개의 유저 데이터를 찾는다
    neighbors = get_k_neighbors(user_id, filled_data, k)
    
    # 코드를 쓰세요
    return np.mean(neighbors[:, movie_id])
    
    
# 실행 코드   
# 평점 데이터를 불러온다
rating_data = pd.read_csv(RATING_DATA_PATH, index_col='user_id').values
# 5개의 이웃들을 써서 유저 0의 영화 3에 대한 예측 평점 구하기
predict_user_rating(rating_data, 5, 0, 3)  
```

- 상품 기반 필터링
 * 비슷한 상품을 써서 예측: 상품 기반 협업 필터링 
 * 유저들이 상품보다 복잡하기 때문에 유저 기반 협업 필터링에 비해 성능이 더 좋은 경우가 많다
 * r_i : 영화 i에 대한 평점 데이터 벡터
 * r_i(x) : 유저 x의 영화 i에 대한 평점
 * N: 유저 x가 평가한 영화 중, 영화 i와 가장 비슷한 영화 k 개의 집합

![image](https://user-images.githubusercontent.com/47103479/125294046-ed252e80-e35e-11eb-8d5d-ac2cfc042357.png)

## 행렬 인수분해
- 인수분해
  * 자연수나 다항식을 여러 개의 인수의 곱으로 변형하는 수학 개념

- 내용 기반
  * 영화 속성(입력 변수) + 평점 데이터(목표 변수) ->(학습) 유저 취향 / 선형 회귀 경사 하강법으로 학습
- 유저 취향과 영화 속성 모두 머신러닝으로 학습 
 
- 데이터 표현하기
   * 영화 속성 
![image](https://user-images.githubusercontent.com/47103479/125304894-eb606880-e368-11eb-9585-ac1d83ea2b15.png)
![image](https://user-images.githubusercontent.com/47103479/125304930-f0bdb300-e368-11eb-8074-1cdf481670b2.png)

   * 유저 취향
![image](https://user-images.githubusercontent.com/47103479/125305023-03d08300-e369-11eb-84bd-99d8601b5c8a.png)
![image](https://user-images.githubusercontent.com/47103479/125305123-15b22600-e369-11eb-8173-bcc984f6f1ff.png)

   * 평점 예측 값
![image](https://user-images.githubusercontent.com/47103479/125305221-25316f00-e369-11eb-9acc-68fbebcbabd8.png)

  * 평점 실제 데이터
![image](https://user-images.githubusercontent.com/47103479/125305313-38443f00-e369-11eb-830e-94343e2e9ecd.png)

  * 평점 데이터가 있는지 없는지(줬으면1, 아니면 0)
![image](https://user-images.githubusercontent.com/47103479/125305396-46925b00-e369-11eb-8805-34c1a13bb095.png)

  
