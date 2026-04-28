# 독립 표본 t-test (independant two sample t-test)
# 실습: 두가지 교육방법에 따른 평균 시험 점수에 대한 검정 수행 two_sample csv

# 귀무: 두 가지 교육방법에 다른 평균 시험점수에 차이가 없다
# 대립: 두 가지 교육방법에 다른 평균 시험점수에 차이가 있다
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/two_sample.csv")
print(data.head())

# print(data.isnull().sum())
# print(data['score'].isnull().sum())
# print(data.isnull().any)

# 교육방법별 분리
ms = data[['method', 'score']]
m1 = ms[ms['method']==1]    # 방법1
m2 = ms[ms['method']==2]    # 방법2

print(m1.head(3))
print(m2.head(3))

# 교육방법에서 score만 별도 기억
score1 = m1['score']
score2 = m2['score']
print(score1.isnull().sum())    # 0 -- NaN 없음
print(score2.isnull().sum())    # 2 -- NaN 2개

score2 = score2.fillna(score2.mean())   # NaN을 평균값으로 채움

# 정규성 검정
print(stats.shapiro(score1))    # 0.36799 -- 정규성 만족(>0.05)
print(stats.shapiro(score2))    # 0.67142 -- 정규성 만족(>0.05)

# 시각화
sns.histplot(score1, kde=True)                  # seaborn 역할이뭐임?
sns.histplot(score2, kde=True, color='blue')

# 등분산성 검정
from scipy.stats import levene
leven_p = levene(score1, score2).pvalue
print("등분산성: ",leven_p)     # 0.4568 -- 정규성 만족(>0.05)

result = stats.ttest_ind(score1,score2, equal_var=True)
print("result: ", result)
# TtestResult(statistic=-0.1964, pvalue=0.845, df=48.0)
# 해석: pvalue 0.845 > 0.05 이므로 귀무가설 채택
plt.show()














