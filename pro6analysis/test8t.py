# *단일 모집단의 평균에 대한 가설검정 (one samples t test)
# 실습 예제 1
# A 중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리
# 국어 점수 평균 검정(80) student csv

# 귀무: 학생들의 국어점수 평균은 80이다.
# 대립: 학생들의 국어점수 평균은 80이 아니다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import wilcoxon

# pd.set_option('display.max_columns')
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/student.csv")
print(data.head())
print(data.describe())
print(data['국어'].mean())  # 72.9
print(len(data))            # 20   --- 30행이 넘으면 중심극한정리에 의해 정규성을 따른다고 가정
# 30개가 넘지 않으므로 정규성 검정 실시 !
print(stats.shapiro(data['국어']))  # 샤피로테스트 결과 pvalue=0.01295, 샤피로테스트 개념정리 필요
# p값이 alpha=0.05보다 커야 정규성을 따른다고 볼 수 있다
# alpha 0.05 > pvalue 0.01295 --- 정규성을 만족하지 않음

# 정규성을 만족하지 못한 경우 대안
# wilcoxon: 비모수 검정 방법으로 정규성이 없을 때 적절한 선택이 될 수 있다.
wilcox_result = wilcoxon(data['국어']-80)
print("wilcox_result: ", wilcox_result)
# wilcox_result:  statistic=74.0, pvalue=0.39777
# alpha 0.05 < pvalue 0.39777 --- 이므로 귀무가설 채택

result = stats.ttest_1samp(data['국어'],popmean=80)
print('result: ', result)
# result:  TtestResult - statistic=-1.33218, pvalue=0.19856, df=19
# alpha 0.05 < pvalue 0.19856 --- 이므로 귀무가설 채택

# 결론: 정규성은 부족하나 귀무가설 채택이라는 동일 결론을 얻음
# 표본 수가 크다면 ttest_1samp을 써도 무관하다.
# 보고서 작성시에는 샤피로 검정 결과 정규성 가정이 다소 위배되나,
# 비모수 검정(윌콕슨) 결과도 동일하므로 ttest_1samp 결과를 신뢰할 수 있다. 라고 명시한다.

print("------------------")
# 실습예제 2
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균 2800g으로 알려져있으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때, 새로운 주장이 맞는지 검정해보자

# 귀무: 여아 신생아의 몸무게 평균은 2800g이다.
# 대립: 여아 신생아의 몸무게 평균은 2800g보다 크다.

data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/babyboom.csv")
print(data2.head(3))
print(data2.describe())
print()
fdata = data2[data2.gender == 1]     # 여아 = 1, 남아 = 2
print(fdata, ' ', len(fdata))
print("여아 몸무게 평균: ", np.mean(fdata.weight))      # 3132
# 평균의 차이가 있는가? (2800 vs 3132) -- O
print("여아 몸무게 표준편차: ",np.std(fdata.weight))    # 613.78

result2 = stats.ttest_1samp(fdata['weight'],popmean=2800)
print('result: ', result2)
# result:  TtestResult(statistic=2.233, pvalue=0.0393, df=17)
# 해석(p-value 기반): alpha 0.05 > pvalue 0.0393 --- 이므로 귀무가설 기각
# 해석(t 분포표 기반): t값 2.233, df 17, alpha 0.05, cv(임계값)?
# t값이 cv값 오른쪽(귀무 기각영역)에 있으므로 귀무가설 기각

print("---------------------------------")
# 선행조건인 정규성 검정을 한 경우
print(stats.shapiro(fdata['weight']))   # p-value 0.0129597
# alpha 0.05 > p-value 0.0129 ----> 정규성만족하지않음

# 정규성 만족 여부 시각화
sns.histplot(fdata['weight'], kde=True)     # 왜곡된 데이터 분포를 확인
plt.show()

# 정규성 만족여부 시각화 2 Quantile-Quantile plot
stats.probplot(fdata['weight'],plot=plt)    # Q-Q plot 상에서 잔차가 정규성을 만족하지 못함
plt.show()

# 정규성 만족하지 못하므로 wilconxon 비모수 검정 실시
result3 = wilcoxon(fdata['weight']-2800)
print(result3)
# WilcoxonResult(statistic=37.0, pvalue=0.03423)
# 해석: alpha 0.05 > pvalue 0.034 이므로 귀무가설 기각
