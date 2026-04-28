# paired t-test : 대응표본 t-검정

# 실습) 복부 수술 전 9명의 몸무게와 복부 수술 후 몸무게 변화
# 대립가설 : 복부 수술이 몸무게에 영향을 준다.
# 귀무가설 : 복부 수술이 몸무게에 영향을 주지 않는다.
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

print(np.mean(baseline), np.mean(follow_up)) # 78.41 71.5
print("평균의 차이 : ", np.mean(baseline) - np.mean(follow_up)) # 6.91

# 시각화
plt.bar(np.arange(2), [np.mean(baseline), np.mean(follow_up)], color=['blue', 'orange'])
plt.xlim(0, 1)
plt.xlabel('수술 전후', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.ylabel('몸무게', fontdict={'fontsize': 12})
plt.title('복부 수술 전후 몸무게 비교', fontdict={'fontsize': 14})
plt.show()

result = stats.ttest_rel(baseline, follow_up)
print(result) 
# Ttest_relResult(statistic=3.6681166519351103, pvalue=0.006326650855933662) < 0.05
# -> 유의미한 차이 있음, 귀무가설 기각, 복부 수술이 몸무게에 영향을 준다.