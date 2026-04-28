# 독립 표본 t-test (independant two sample t-test)
# 서로 다른 두 집단의 평균에 대한 통계 검정에 사용된다
# 비교를 위해 평균과 표준편차 통계량을 사용한다
# 두 집단의 평균과 표준편차 비율에 대한 재조 검정법이다.

# 두 집단의 가설검정 실습 시 분산을 알지못하는 것으로 한정하겠다.
# 남녀의 성적 A반과 b반의 키, 경기도와 충청도의 소득 따위의 서로 독립인
# 두 집단에서 얻은 표본을 독립 표본(Two samples)이라한다

# 실습: 남녀 두 집단 간 파이썬 시험의 평균 차이 검정
# 남녀의 시험 평균이 우연히 같을 확률은 얼마나 될까?
# 만약 우연히 발생했다면 평균은 같은 것이고, 우연이 아니면 평균은 다른 것이다.
# 95% 신뢰 구간에서 우연히 발생할 확률이 5% 이상이면 귀무가설 채택이다.

# 귀무: 남녀 두 집단 간 파이썬 시험의 평균 차이 없다.
# 대립: 남녀 두 집단 간 파이썬 시험의 평균 차이 있다.
from scipy import stats
import pandas as pd
import numpy as np

male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

print(np.mean(male), ' ', np.mean(female))      # 83.8 72.24

# 두 개의 표본에 대한 '독립 표본 t-검정' 수행
two_sample = stats.ttest_ind(male,female)
print(two_sample)

tv, pv = two_sample
print('t test 통계량: ', tv)
print('p값: ', pv)
# t test 통계량:  1.233193127514512
# p값:  0.2525076844853278
# 해석: p-value 0.2525 > alpha 0.05 이므로 귀무 채택

# 선행 조건
# 1) 두 집단이 정규분포를 따라야 한다.
# 2) 두 집단의 분산이 같다는 가정이 필요하다. 등분산성*

print('male의 정규성: ', stats.shapiro(male))
# male의 정규성:  ShapiroResult(statistic=np.float64(0.930585895438102), pvalue=np.float64(0.6003714029870378))
print('female의 정규성: ', stats.shapiro(female))
# female의 정규성:  ShapiroResult(statistic=np.float64(0.9557386984528726), pvalue=np.float64(0.778043110871599))
# 만약 집단의 표본수가 30개 이상인 경우, 정규분포를 따른다고 가정하므로 정규성 검정 필요없음
# 만약 정규성을 만족하지 못하면 비모수 검정인 Mann-whitney test를 한다
# stats.mannwhitneyu(group1, group2) << pvalue가 0.05보다 크면 차이 증거 없음 아니면 두 집단 간 평균 차이 존재(?)

# 선행조건 2) 두 집단의 분산이 같다는 가정이 필요하다.(등분산성)
from scipy.stats import levene, bartlett

# levene 정규성과 상관없이 사용, 이상치에 민감
# bartlett 정규성이 있을 때만 사용, 이상치에 덜 민감

leven_stat, leven_p = levene(male,female)
print("p value: ", leven_p)     # p value: 0.4956
# two_sample = stats.ttest_ind(male,female, equal_var=True) # 이거 사용
# 만약 등분산성 만족 못할 때 Welch's t-test 수행
two_sample = stats.ttest_ind(male, female, equal_var=False)










