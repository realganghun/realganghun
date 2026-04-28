# 전통적 방법의 선형회귀(기계학습 중 지도학습)
# 각 데이터에 대한 잔차제곱합(거리제곱합)이 최소가 되는 추세선(회귀선)
# 이를 통해 독립변수가 종속변수에 얼마나 영향을 주는지 인과관계를 분석
# 독립변수 : 연속형, 종속변수 : 연속형 - 두 변수는 상관관계 및 인과관계가 있어야 함
# 정량적인 모델을 생성

import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

np.random.seed(12)

# 모델 맛보기
# 방법1 : make_regression사용. model 생성 X
print('-----------방법1-------------'*3)
x, y, coef = make_regression(n_samples=50, n_features=1, bias=100, coef=True)
# n_samples=50: 데이터를 50개 만들겠다는 뜻입니다. (행의 개수)
# n_features=1: 독립변수($x$)의 개수가 1개라는 뜻입니다. (열의 개수)
# bias=100: 절편($b$)을 100으로 설정합니다. $x$가 0일 때 $y$값이 100에서 시작한다는 의미입니다.
# coef=True: 이 함수가 내부적으로 설정한 가중치(기울기, $w$) 값을 함께 반환해달라는 뜻입니다.

print(x) #[-1.70073563] [-0.67794537] [ 0.31866529] ...
print()
print(y) # 예측되는 y값, -52.17214291   39.34130801  128.51235594
print()
print(coef) # 기울기, 89.47430739278907

# y = wx + b --> 89.47430739278907*x + 100
y_pred = 89.47430739278907*-1.70073563 + 100
print('예측값 : ', y_pred)

# 방법 2 : LinearRegression 사용. model 생성 O
print('-----------방법2-------------'*3)
xx = x
yy = y
from sklearn.linear_model import LinearRegression
model = LinearRegression()
fit_model = model.fit(xx, yy) # 최소제곱법으로 기울기, 절편 반환
print('기울기(slope) : ', fit_model.coef_)
print('y절편(bias) : ', fit_model.intercept_)

# 예측값 확인
y_newpred = fit_model.predict(xx[[0]])
print('예측값1 : ', y_newpred)
y_newpred2 = fit_model.predict(np.array([[0.12345],[0.3],[0.5]]))
print('예측값2 : ', y_newpred2)

# 방법 3 : ols사용, model 생성
# 잔차제곱합(RSS)을 최소화하는 가중치 벡터를 행렬 미분으로 구하는 방법
import statsmodels.formula.api as smf
print(xx.ndim) #2
x1 = xx.flatten() # 차원 축소
print(x1.ndim) # 1
y1 = yy

import pandas as pd
data = np.array([x1, y1])
df = pd.DataFrame(data.T)
df.columns = ['x1', 'y1']
print(df.head(3))

model2 = smf.ols(formula = "y1 ~ x1", data=df).fit()
print(model2.summary())
print('기울기 : ', model2.params['x1']) 
print('절편 : ', model2.params['Intercept'])

# 예측값 확인
new_df = pd.DataFrame({'x1':[-1.70073563, -0.67794537]}) # 기존 자료 검증
print('예측값1 : ', model2.predict(new_df))
new_df2 = pd.DataFrame({'x1':[0.1234, 0.2345]})
print('예측값2 : ', model2.predict(new_df2))