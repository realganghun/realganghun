# 일원분산분석으로 평균 차이 검정
# 강남구에 있는 GS편의점 3개 지역 알바생의 급여에 대한 평균 차이 검정

# 귀무가설 : 강남구에 있는 GS편의점 3개 지역 알바생의 급여에 차이가 없다.
# 대립가설 : 강남구에 있는 GS편의점 3개 지역 알바생의 급여에 차이가 있다.

import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
import urllib.request

uri = "https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3.txt"
# 읽기 1
data = pd.read_csv(uri, header=None)
print(data) # dataframe 형태로 읽어옴

# 읽기 2
data = np.genfromtxt(urllib.request.urlopen(uri), delimiter=",")
print(data) # numpy array 형태로 읽어옴
print(data.shape) # (22, 2)

# 3개의 집단에 월급 자료 얻기, 평균
group1 = data[data[:, 1] == 1, 0] # 지역1
group2 = data[data[:, 1] == 2, 0] # 지역2
group3 = data[data[:, 1] == 3, 0] # 지역3

print("지역1 평균:", np.mean(group1)) #316.625
print("지역2 평균:", np.mean(group2)) #256.44444444444446
print("지역3 평균:", np.mean(group3)) #278.0

print()
# 정규성 확인
print(stats.shapiro(group1)) # ShapiroResult(statistic=0.9070389354191438, pvalue=0.3336828974377483) > 0.05 -> 정규성 만족
print(stats.shapiro(group2)) # ShapiroResult(statistic=0.9469017117773169, pvalue=0.6561053962402779) > 0.05 -> 정규성 만족
print(stats.shapiro(group3)) # ShapiroResult(statistic=0.963552887640623, pvalue=0.8324811457153043) > 0.05 -> 정규성 만족

# 등분산성 확인
print(stats.levene(group1, group2, group3).pvalue) #0.04584681263418624
print(stats.bartlett(group1, group2, group3).pvalue) #0.3508032640105389

# 데이터 시각화
plt.boxplot([group1, group2, group3], showmeans=True)
plt.show()

# 일원분산분석 방법1 : anova_lm()
df = pd.DataFrame(data=data, columns=['pay', 'group'])
print(df)
lmodel = ols('pay ~ C(group)', data=df).fit() # C(group) : group은 범주형
print(anova_lm(lmodel, typ=1))
# p-value : 0.043589 < 0.05 이므로 귀무가설 기각

# 일원분산분석 방법2 : f_oneway()
f_stat, p_val = stats.f_oneway(group1, group2, group3)
print('f_stat : ', f_stat)
print('p_val : ', p_val) #0.043589334959178244
# p-value : 0.043589 < 0.05 이므로 귀무가설 기각

print()
# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group)
print(tukResult)

# 시각화
tukResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()

# 참고
# anova_lm() : 정규성, 등분산성이 깨지면 p-value 신뢰 불가
# f_oneway() : 정규성 깨지면 stats.kruskal(), 등분산성이 깨지면 welch's ANOVA 사용