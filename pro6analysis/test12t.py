# Paired samples t-test(대응표본 t-검정, 동일집단표본 t-검정, 쌍체 t-검정)
# 하나의 집단에 대해 독립변수를 적용하기 전과 후의 종속변수(평균)의 수준을 측정하고
# 두 측정값의 차이가 통계적으로 유의미한지를 검정하는 방법
# 동일한 관찰 대상으로 처리 이전과 이후를 1:1 대응시킨 검정 방법
# 집단 간 비교가 아니므로 등분산 가정을 할 필요는 없음.

# 예 : 광고 전후의 상품 선호도 조사, 치료 전후의 환자 상태 조사, 교육 전후의 학생 성적 조사 등

# 살습 1 : 3강의실 학생들을 대상으로 특강이 시험 점수에 영향을 주었는가!?
# 대립가설 : 특강이 시험 점수에 영향을 준다.
# 귀무가설 : 특강이 시험 점수에 영향을 주지 않는다.

import numpy as np
import scipy.stats as stats

np.random.seed(123)
x1 = np.random.normal(loc=75, scale=10, size=100) # 특강 전 시험 점수
x2 = np.random.normal(loc=80, scale=10, size=100) # 특강 후 시험 점수

# 정규성 확인
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(x1, kde=True) # 특강 전 시험 점수의 분포, 정규성 만족
sns.displot(x2, kde=True) # 특강 후 시험 점수의 분포, 정규성 만족
plt.show()

print(stats.shapiro(x1)) # ShapiroResult(statistic=0.9841397685812816, pvalue=0.27487044002059957) > 0.05 -> 정규성 만족
print(stats.shapiro(x2)) # ShapiroResult(statistic=0.9785350464696386, pvalue=0.10214157305396593) > 0.05 -> 정규성 만족

# 대응표본 t-검정
print(stats.ttest_rel(x1, x2)) 
# Ttest_relResult(statistic=-3.003102708378836, df=99
# pvalue=0.0033837913974620218 < 0.05) -> 유의미한 차이 있음, 귀무가설 기각, 특강이 시험 점수에 영향을 준다.
