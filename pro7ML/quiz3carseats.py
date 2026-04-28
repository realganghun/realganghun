# 회귀분석 문제 3)    

# kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음) Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import statsmodels.formula.api as smf

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Carseats.csv')
print(df.head(5))
print(df.shape)
print(df.info())
df = df.drop([df.columns[6], df.columns[9], df.columns[10]], axis=1)
print(df.corr())

lm = smf.ols(formula = "Sales ~ Income + Advertising + Price + Age", data=df).fit()
print(lm.summary())

print("\n선형 회귀 모델의 적절성 조건 체크 후 모델 사용")
print(df.columns) # ['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price', 'Age', 'Education']
df_lm = df.iloc[:, [0, 2, 3, 5, 6]]
print(df_lm.head(2))
# 잔차항 구하기
fitted=lm.predict(df_lm)
residual = df_lm['Sales'] - fitted
print('residual ', residual[:3])
print('residual 평균 ', np.mean(residual))

print('잔차의 정규성 : 잔차가 정규성을 따르는지 확인')
from scipy.stats import shapiro
import statsmodels.api as sm

stat, p = shapiro(residual)
print(f"통계량 : {stat}, p-value : {p}")
print("정규성 만족" if p > 0.05 else "정규성 불만족")

# Q-Q plot(Quantile-Quantile Plot)으로 시각화, 정규성 검정
sm.qqplot(residual, line='s')
plt.title("Q-Q plot으로 정규성 만족 확인")
plt.show()

print("선형성 검정 : 독립변수의 변화에 종속변수도 변화하나 특정한 패턴이 있으면 안됨")
# 독립변수와 종속변수간의 선형 형태로 적절하게 모델링 되었는지 검정
from statsmodels.stats.diagnostic import linear_reset # 선형성 확인 모듈
reset_result = linear_reset(lm, power=2, use_f=True)
print(f'reset_result 결과 : {reset_result.pvalue:.5f}')
print('선형성 만족' if reset_result.pvalue > 0.05 else '선형성 위배')
# 시각화
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color='grey')
plt.show()

print("등분산성 검정 : 모든 x값에서 오차의 퍼짐이 유사해야 한다")
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(residual, sm.add_constant(df_lm['Sales']))
bp_stat, bp_pvalue = bp_test[0], bp_test[1]
print(f"breuschapagan test : 통계량 : {bp_test}, p-value : {bp_pvalue}" )
print('등분산성 만족' if reset_result.pvalue > 0.05 else '등분산성 위배')
# 시각화는 선형성 참고

print("독립성 : 다중회귀 분석 시  독립변수의 값이 서로 관련되지 않아야 한다.")
# 잔차가 자기상관(인접 관측치의 오차가 상관됨)이 있는지 확인
# Durbin-Watson : 잔차의 자기상관(autocorrelation) 검정 지표. 잔차들이 서로 독립적인가? 시간 흐름 데이터에서 중요 (시계열)
#    값의 범위는 0 ~ 4 이고   2이면 정상 (자기상관 없음).   < 2이면 양의 자기상관,  > 2이면 음의 자기상관
# model.summary()로도 확인 가능, Durbin-Watson : 1.931
import statsmodels.api as sm
print('Durbin-Watson : ', sm.stats.stattools.durbin_watson(residual)) # Durbin-Watson :  1.9314981270829594 이므로 잔차의 자기상관 X

print("다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다.")
# vif : variance_inflation_factor, 분산 팽창지수, 분산 인플레 요인
# : 값이 10을 넘으면 다중 공선성이 발생하는 변수라고 할 수 있다.
from statsmodels.stats.outliers_influence import variance_inflation_factor
df_ind = df[['Income', 'Advertising', 'Price', 'Age']]  # 독립변수들 목록
vifdf = pd.DataFrame()
vifdf['변수'] = df_ind.columns
vifdf['vif_value'] = [variance_inflation_factor(df_ind.values, i) for i in range(df_ind.shape[1])]
print(vifdf) # 10을 초과하지 않았으므로 모두 만족
#             변수  vif_value
# 0       Income   5.971040
# 1  Advertising   1.993726
# 2        Price   9.979281
# 3          Age   8.267760

# 시각화
sns.barplot(x='변수', y='vif_value', data=vifdf)
plt.title('VIF')
plt.show()





# 유의한 모델이므로 생성된 모델을 파일로 저장하고 이를 재사용
# 방법1
# import pickle
# with open('carseat.pickle', 'wb') as obj: # 저장
#     pickle.dump(lm, obj)

# with open('carseat.pickle', 'rb') as obj:
#     mymodel = pickle.load(obj)

# 방법 2: joblib 사용 (주로 머신러닝 모델 저장에 더 선호됨)
import joblib

# 모델 저장 (확장자는 .pkl 또는 .joblib을 주로 씁니다)
joblib.dump(lm, 'carseat_model.pkl')
print("모델이 성공적으로 저장되었습니다.")

# 모델 불러오기
mymodel2 = joblib.load('carseat_model.pkl')

# 불러온 모델로 예측 테스트 (기존 모델과 결과가 같은지 확인)
print("새로운 값으로 Sales 예측 ")
new_df = pd.DataFrame({"Income":[35,62], "Advertising":[6,3], "Price":[105,88], "Age":[35,55]})
pred = mymodel2.predict(new_df)
print("Sales 예측 결과 : ", pred.values)