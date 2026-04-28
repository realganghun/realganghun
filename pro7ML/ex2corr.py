# 공분산 / 상관계수
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv')
print(data.head(), data.shape) #(264, 3)
print(data.describe())

print('표준편차')
print(np.std(data.친밀도)) #0.968505
print(np.std(data.적절성)) #0.858027
print(np.std(data.만족도)) #0.827172

plt.hist([np.std(data.친밀도), np.std(data.적절성), np.std(data.만족도)])
plt.show()

print('공분산')
# numpy 방법
print(np.cov(data.친밀도, data.적절성)[0,1]) #0.4164218227906435
print(np.cov(data.친밀도, data.만족도)[0,1]) #0.375662518723355
print(np.cov(data.적절성, data.만족도)[0,1]) #0.5463331028920375
print()
# pandas방법
print(data.cov())
#           친밀도       적절성       만족도
# 친밀도  0.941569  0.416422  0.375663
# 적절성  0.416422  0.739011  0.546333
# 만족도  0.375663  0.546333  0.686816

print('상관계수')
print(np.corrcoef(data.친밀도, data.적절성)[0,1]) #0.49920860859323557
print(np.corrcoef(data.친밀도, data.만족도)[0,1]) #0.46714498360089685
print(np.corrcoef(data.적절성, data.만족도)[0,1]) #0.766852699640837
print()
print(data.corr())
#           친밀도       적절성       만족도
# 친밀도  1.000000  0.499209  0.467145
# 적절성  0.499209  1.000000  0.766853
# 만족도  0.467145  0.766853  1.000000
print(data.corr(method='pearson')) # 변수가 연속형, 정규성 따름
# print(data.corr(method='spearman')) # 변수가 서열형, 정규성 안따름
# print(data.corr(method='kendall')) 

# 만족도에 따른 다른 특성 사이의 상관관계
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))
# 만족도    1.000000
# 적절성    0.766853
# 친밀도    0.467145

# 시각화
data.plot(kind='scatter', x='만족도', y='적절성')
plt.show()

from pandas.plotting import scatter_matrix
attr = ['친밀도', '적절성', '만족도']
scatter_matrix(data[attr], figsize=(10,6))
plt.show()

import seaborn as sns
sns.heatmap(data.corr(), annot=True) #annot=True 있으면 map위에 숫자 나옴.
plt.show()

# heatmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()