# LinearRegression 클래스 사용 : 평가 score 정리 - mtcars dataset 사용
from sklearn.linear_model import LinearRegression
import statsmodels.api
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
print('상관계수 : \n', mtcars.corr(method='pearson'))
print()

# hp가 mpg에 영향을 주는 인과관계
x = mtcars[['hp']].values # 2차원
print(x[:5])
y = mtcars['mpg'].values # 1차원
print(y[:5])

# 모델 새성
lmodel = LinearRegression().fit(x, y)
print('slope : ', lmodel.coef_)
print('intercept : ', lmodel.intercept_)

plt.scatter(x, y)
plt.plot(x, lmodel.coef_ * x + lmodel.intercept_, c='r')
plt.show()

# mpg를 예측
pred = lmodel.predict(x)
print('예측값 : ', np.round(pred[:5], 1))   #예측값 :  [22.6 22.6 23.8 22.6 18.2]
print('실제값 : ', y[:5])                   #실제값 :  [21.  21.  22.8 21.4 18.7]

# 모델 성능 지표
# 회귀 평가 지표는 고정된 점구 번위가 없다.(데이터 스케일에 따라 다름)
# 따라서 모델끼리 상대적인 비교를 한다.
print('MSE : ', mean_squared_error(y, pred))            #MSE(모델 내부 비교, 계산 편리(단위가 제곱한 값)) :  13.989822298268805
print('RMSE : ', np.sqrt(mean_squared_error(y, pred)))  #RMSE(보고/해석용, 원래 단위) :  3.7402970868994894
print('r2_score : ', r2_score(y, pred))                 #r2_score :  0.602437341423934

# r2_score만 보고 모델 판단 X(이상치에 민감, 변수가 많으면 증가...), 설명력만 봄
# 모델 성능은 r2_score와 MSE또는 RMSE를 사용함.

# 새로운 hp로 mpg예측
new_hp = [[100], [110], [120], [130]]
new_pred = lmodel.predict(new_hp)
print("예측 결과 : ", np.round(new_pred.flatten(), 2))               #예측 결과 :  [23.28 22.59 21.91 21.23]
