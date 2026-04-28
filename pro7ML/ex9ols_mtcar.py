# 선형회귀분석 : mtcars dataset

import pandas as pd
import seaborn as sns
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api
import matplotlib.pyplot as plt
import koreanize_matplotlib

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)
print(mtcars.columns)
#mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
print(mtcars.info())
# x : hp(마력수), y : mpg(연비)

# print(mtcars.corr())
print(np.corrcoef(mtcars.hp, mtcars.mpg)) #-0.77616837 hp : 마력수, mpg : 연비
print(np.corrcoef(mtcars.wt, mtcars.mpg)) #-0.86765938 wt : 차제무게

# 시각화
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel('마력수')
# plt.ylabel('연비')
# plt.show()

print('-----------단순선형회귀-----------'*3)
result = smf.ols(formula='mpg ~ hp', data=mtcars).fit()
print(result.summary()) # p-value : 1.79e-07, 설명력 : 0.602, 절편 : 30.0989, 기울기 : -0.0682
# yhat = -0.0682*x + 30.0989 + err
print('마력수 110에 대한 연비 예측값 : ', -0.0682 * 110 + 30.0989) #22.5969
print('마력수 110에 대한 연비 예측값 : ', result.predict(pd.DataFrame({'hp':[110]})).values) #22.59374995 error값 때문에 오차발생

print('-----------다중선형회귀-----------'*3)
result2 = smf.ols(formula='mpg ~ hp + wt', data=mtcars).fit()
print(result2.summary()) #절편 : 37.2273 기울기 : -0.0318, -3.8778
print('마력수 110, 무게 5에 대한 연비 예측값 : ', (-0.0318 * 110) + (-3.8778 * 5) + 37.2273) # 14.3403
print('마력수 110, 무게 5에 대한 연비 예측값 : ', result2.predict(pd.DataFrame({'hp':[110], 'wt':[5]})).values) #14.34309224

print('-----------추정치 구하기(차체무게를 입력해 연비 추정)-----------'*3)
result3 = smf.ols(formula='mpg ~ wt', data=mtcars).fit()
print(result3.summary())
print('결정계수 : ', result3.rsquared)
pred = result3.predict() # 0.7528327936582646
print('result3 연비 예측값 : ', pred[:5]) # 23.28261065 21.9197704  24.88595212 20.10265006 18.90014396

# 새로운 차체 무게로 연비 추정
print('-----------추정치 구하기-----------' * 3)

# 1. 사용자로부터 무게 하나만 입력받습니다.
user_wt = float(input('차체무게 입력 (예: 3.5): '))

# 2. 예측을 위해 데이터프레임 형태로 만듭니다. (컬럼명 'wt'를 맞춰줘야 합니다)
new_df = pd.DataFrame({'wt': [user_wt]})

# 3. 모델로 예측합니다.
new_pred = result3.predict(new_df)

# 4. 출력합니다. (new_pred는 결과가 1개 들어있는 시리즈이므로 .values[0]으로 꺼냅니다)
print(f'차체무게 {user_wt}일 때 예상 연비는 {new_pred.values[0]:.2f}입니다.')