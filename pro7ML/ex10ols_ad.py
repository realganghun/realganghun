# 선형회귀분석 모형의 적절성 선행조건

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import statsmodels.formula.api as smf

advdf = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv', usecols=[1,2,3,4]) # no column 삭제
print(advdf.head(5))
#       tv  radio  newspaper  sales
# 0  230.1   37.8       69.2   22.1
# 1   44.5   39.3       45.1   10.4
# 2   17.2   45.9       69.3    9.3
# 3  151.5   41.3       58.5   18.5
# 4  180.8   10.8       58.4   12.9
print(advdf.shape) #(200, 4)
print(advdf.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 200 entries, 0 to 199
# Data columns (total 4 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   tv         200 non-null    float64
#  1   radio      200 non-null    float64
#  2   newspaper  200 non-null    float64
#  3   sales      200 non-null    float64
# dtypes: float64(4)
# memory usage: 6.4 KB
# None
print(advdf.corr())
#                  tv     radio  newspaper     sales
# tv         1.000000  0.054809   0.056648  0.782224
# radio      0.054809  1.000000   0.354104  0.576223
# newspaper  0.056648  0.354104   1.000000  0.228299
# sales      0.782224  0.576223   0.228299  1.000000

print("-----------단순선형회귀모델 - ols 사용---------"*3)
# 단순선형회귀모델 - ols 사용
# x : tv, y : sales
lm = smf.ols(formula='sales ~ tv', data=advdf).fit()
print(f"coeffients : {lm.params}, p-value : {lm.pvalues}, r-squared : {lm.rsquared}") 
# coeffients : (절편 : 7.032594, 기울기 : 0.047537), p-value : 1.467390e-42, r-squared : 0.611875050850071")
print('상관계수(corr) 제곱하면 r-squared', 0.782224**2)
print(lm.summary())
print('******************'*3)
print(lm.summary().tables[0])
print(lm.summary().tables[1]) # 테이블 끊어서 보기도 가능
print()

print("-------- 예 측 -------"*5)
x_new = pd.DataFrame({'tv' : advdf.tv[:3]})
print(x_new)
print('실제값 : ', advdf.sales[:3].values)
print('예측값 : ', lm.predict(x_new).values)
print('직접 계산 : ', lm.params.tv * 230.1 + lm.params.Intercept)

# 경험하지 않은 tv 광고비에 따른 상품 판매량 예측
my_new = pd.DataFrame({'tv':[100, 350, 780]})
print('예측 상품 판매량 : ', lm.predict(my_new).values) # [11.78625759 23.6704177  44.11117309]

# 시각화
plt.scatter(advdf.tv, advdf.sales)
plt.xlabel('tv 광고비')
plt.ylabel('상품 판매량')
ypred = lm.predict(advdf.tv)
plt.plot(advdf.tv, ypred, c='r')
plt.title('단순선형회귀')
plt.grid(True)
plt.show()

print('\n 단순선형회귀 모델이므로 적절성 선행조건 중 정규성, 선형성, 등분산성 확인')
# 잔차(Residual)
# 잔차(Residual)는 통계학 및 회귀 분석에서 실제 관측값과 모델을 통해 예측된 값의 차이를 의미
# 모델이 데이터를 얼마나 잘 설명하는지(적합도)를 나타내는 지표로,
# 보통 최소제곱법을 통해 이 잔차의 제곱합을 최소화하는 방식으로 회귀 모델을 추정

fitted = lm.predict(advdf)
residual = advdf['sales'] - fitted
print('실제값 : ', advdf['sales'][:5].values)
print('예측값 : ', fitted[:5].values)
print('잔차값 : ', residual[:5].values)
print('잔차평균값 : ', np.mean(residual[:5]))

print('잔차의 정규성 : 잔차가 정규성을 따르는지 확인')
from scipy.stats import shapiro
import statsmodels.api as sm

stat, p = shapiro(residual)
print(f"통계량 : {stat}, p-value : {p}") # 통계량 : 0.9905306561484947, p-value : 0.21332551436716007 > 0.05 => 정규성 만족
print("정규성 만족" if p > 0.05 else "정규성 불만족")

# Q-Q plot(Quantile-Quantile Plot)으로 시각화, 정규성 검정
sm.qqplot(residual, line='s')
plt.title("Q-Q plot으로 정규성 만족 확인")
plt.show()

print("선형성 검정 : 독립변수의 변화에 종속변수도 변화하나 특정한 패턴이 있으면 안됨")
# 독립변수와 종속변수간의 선형 형태로 적절하게 모델링 되었는지 검정
from statsmodels.stats.diagnostic import linear_reset # 선형성 확인 모듈
reset_result = linear_reset(lm, power=2, use_f=True)
print('reset_result 결과 : ', reset_result.pvalue)
print('선형성 만족' if reset_result.pvalue > 0.05 else '선형성 위배')
# 시각화
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color='grey')
plt.show()

print("등분산성 검정 : 모든 x값에서 오차의 퍼짐이 유사해야 한다")
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(residual, sm.add_constant(advdf['tv']))
bp_stat, bp_pvalue = bp_test[0], bp_test[1]
print(f"breuschapagan test : 통계량 : {bp_test}, p-value : {bp_pvalue}" )
print('등분산성 만족' if reset_result.pvalue > 0.05 else '등분산성 위배')

# 참고 : Cook's distance - 특정 데이터가 회귀모델에 얼마나 영향을 주는지 확인
# 영향력있는 관측치(이상치)를 탐지하는 진단 방법
# 데이터가 적을 때, 이상치가 의심스러울 때, 모델 결과가 이상하게 나올 때...
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm).cooks_distance # cook's distance, index 반환

# cook's distance가 가장 큰 5개 확인
print(cd.sort_values(ascending=False).head())
# 35     0.060494
# 178    0.056347
# 25     0.038873
# 175    0.037181
# 131    0.033895
# cook's distance가 가장 큰(영향력이 큰) 원본 확인 : outlier
print(advdf.iloc[[35, 178, 25, 175, 131]]) # 대부분 tv광고비는 매우 높으나, sales가 낮음. - 모델의 입장에서 모델이 예측하기 어려운 point들.

# 시각화
fig = sm.graphics.influence_plot(lm, alpha=0.05, criterion="cooks")
plt.show()

# 다중선형회귀모델 - ols 사용
# x : tv, radio, newspaper y : sales
lm_mul = smf.ols(formula='sales ~ tv + radio + newspaper', data=advdf).fit()
print(lm_mul.summary()) # newspaper 0.860 > 0.05 --> 빼는게 좋음!