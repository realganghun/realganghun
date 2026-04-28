# 이원분산분석 : 요인 복수 - 각 요인의 레벨(그룹)도 복수
# 두 개의 요인에 대한 집단(독립변수) 각각이 종속변수(평균)에 영향을 주는지 검정
# 주효과 : 독립변수들이 각각 독립적으로 종속변수에 미치는 영향을 검정하는 것
# 상호작용효과(교호작용) : 독립변수들이 서로 연관되어 종속변수에 미치는 영향을 검정
# 분산분석(ANOVA)이나 회귀분석에서 한 독립변수가 종속변수에 미치는 영향이 다른 독립변수의 수준에 따라 달라지는 현상
# Ex) 초밥 - 간장, 감자튀김 - 케첩 // 초밥 - 케첩(???)

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

pd.set_option('display.max_columns', None)

# 실습1 : 태아 수와 관측자 수가 태아의 머리둘레 평균에 영향을 주는가?
# 주효과 가설
# 귀무가설 : 태아 수와 태아의 머리둘레 평균은 차이가 없다.
# 대립가설 : 태아 수와 태아의 머리둘레 평균은 차이가 있다.
# 귀무가설 : 관측자 수와 태아의 머리둘레 평균은 차이가 없다.
# 대립가설 : 관측자 수와 태아의 머리둘레 평균은 차이가 있다.
# 교호작용 가설
# 귀무가설 : 교호작용은 없다. - 태아 수와 관측자 수는 관련이 없다
# 대립가설 : 교호작용은 있다. - 태아 수와 관측자 수는 관련이 있다

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3_2.txt')
print(data.head(3), data.shape) #(36, 3)
print(data['태아수'].unique()) # [1 2 3]
print(data['관측자수'].unique()) # [1 2 3 4]

# 시각화 - 데이터가 어떤 형태로 분포돼있는지 직관적으로 확인하기
# data.boxplot(column='머리둘레', by='태아수')
# plt.show()
# data.boxplot(column='머리둘레', by='관측자수')
# plt.show()

# linreg = ols("머리둘레 ~ C(태아수) + C(관측자수)", data=data).fit() # 교호작용 X
# linreg = ols("머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수)", data=data).fit() # 교호작용 O
linreg = ols("머리둘레 ~ C(태아수) * C(관측자수)", data=data).fit() # 교호작용 O, 이원분산분석은 교호작용 있는게 일반적
result = anova_lm(linreg, typ=2)
print(result)
#                         sum_sq      df               F        PR(>F)
# C(태아수)              324.008889   2.0    2113.101449  1.051039e-27 --> 귀무가설 기각
# C(관측자수)             1.198611    3.0       5.211353  6.497055e-03 --> 귀무가설 기각
# C(태아수):C(관측자수)    0.562222    6.0       1.222222  3.295509e-01 --> 귀무가설 채택
# Residual                1.840000   24.0           NaN           NaN

# 태아수 : 귀무가설 기각, 태아 수와 태아의 머리둘레 평균은 차이가 있다.
# 관측자수 : 귀무가설 기각, 관측자 수와 태아의 머리둘레 평균은 차이가 있다.
# 교호작용 : 귀무가설 채택, 태아 수와 관측자 수는 관련이 없다.
# 해석 :
# 태아 수와 관측자 수는 각각 종속변수에 유의한 영향을 미친다.
# 그러나 태아 수와 관측자 수 간의 상호작용(교호작용) 효과는 유의하지 않다.

print('--------실습2--------'*5)
# 실습2 : poison과 treat가 독 퍼짐 시간의 평균에 영향을 주는가?
# 주효과 가설
# 귀무가설 : poison 종류와 독 퍼짐 시간의 평균은 차이가 없다.
# 대립가설 : poison 종류와 독 퍼짐 시간의 평균은 차이가 있다.
# 귀무가설 : treat(응급처치) 방법과 독 퍼짐 시간의 평균은 차이가 없다.
# 대립가설 : treat(응급처치) 방법과 독 퍼짐 시간의 평균은 차이가 있다.
# 교호작용 가설
# 귀무가설 : 교호작용이 없다.(poison 종류와 treat(응급처치) 방법은 관련이 없다.)
# 대립가설 : 교호작용이 없다.(poison 종류와 treat(응급처치) 방법은 관련이 있다.)

data2 = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/poison_treat.csv', index_col=0)
print(data2.head(3), data2.shape) #(48, 3)
print(data2['poison'].unique()) # [1 2 3]
print(data2['treat'].unique()) # ['A', 'B', 'C', 'D']

print(data2.groupby('poison').agg(len))
print(data2.groupby('treat').agg(len))
print(data2.groupby(['poison','treat']).agg(len)) 
# 요인별 레벨의 표본수는 4로 동일(모든 집단 별 표본수 동일하므로 균형설계가 잘 됨)

result2 = ols("time ~ C(poison)*C(treat)", data=data2).fit()
print(anova_lm(result2))
#                       df    sum_sq   mean_sq          F        PR(>F)
# C(poison)            2.0  1.033012  0.516506  23.221737  3.331440e-07 --> 귀무가설 기각
# C(treat)             3.0  0.921206  0.307069  13.805582  3.777331e-06 --> 귀무가설 기각
# C(poison):C(treat)   6.0  0.250138  0.041690   1.874333  1.122506e-01 --> 귀무가설 채택
# Residual            36.0  0.800725  0.022242        NaN           NaN

# poison : 귀무가설 기각, poison 종류와 독 퍼짐 시간의 평균은 차이가 있다.
# treat : 귀무가설 기각, treat(응급처치) 방법과 독 퍼짐 시간의 평균은 차이가 있다.
# 교호작용 : 귀무가설 채택, poison 종류와 treat(응급처치) 방법은 관련이 없다.
# 해석 :
# poison와 treat는 각각 종속변수에 유의한 영향을 미친다.
# 그러나 poison과 treat 간의 상호작용(교호작용) 효과는 유의하지 않다.

# 사후 분석
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tkResult1 = pairwise_tukeyhsd(endog=data2.time, groups=data2.poison)
print(tkResult1)
tkResult1.plot_simultaneous(xlabel='mean of time', ylabel='poison')
plt.show()
plt.close()

tkResult2 = pairwise_tukeyhsd(endog=data2.time, groups=data2.treat)
print(tkResult2)
tkResult2.plot_simultaneous(xlabel='mean of time', ylabel='treat')
plt.show()
plt.close()
