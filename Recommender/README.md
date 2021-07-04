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

# 협업 필터링 
- 수많은 유저 데이터들이 협업해서 상품 추천 
- 비슷한 유저를 찾아내서, 이 유저들의 평점을 이용해서 추천
- 유클리드 거리
  
  ![image](https://user-images.githubusercontent.com/47103479/124386339-e40be000-dd14-11eb-9694-5c9f43d5851a.png)
