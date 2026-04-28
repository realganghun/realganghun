# 선호도 분석 실습
# 일원카이제곱 검정
# 5개의 스포츠 음료에 대한 선호도에 차이가 있는지 검정하기

# 대립가설 : 기대치와 관찰치는 차이가 있다. 스포츠 음료의 선호도에 차이가 있다.
# 귀무가설 : 기대치와 관찰치는 차이가 없다. 스포츠 음료의 선호도에 차이가 없다.

import pandas as pd
import scipy.stats as stats

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinkdata.csv')

print(data)
print(stats.chisquare(data['관측도수'])) # X² 통계량(20.488188976377952)과 p-value(0.00039991784008227264)
exp = [data['관측도수'].sum() / len(data)] * len(data) # 기대도수 계산
print(exp) # 기대도수 : 50.8
stat, p = stats.chisquare(f_obs=data['관측도수'], f_exp=exp) # 기대도수 전달
print('stat : ', stat) # X² 통계량(20.488188976377952)과 p-value(0.00039991784008227264)
print('p : ', p)

# 유의수준 0.05보다 p-value(0.0004)가 작으므로 귀무가설 기각, 스포츠 음료의 선호도에 차이가 있다.

# 시각화
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np

# 기대도수
total = data['관측도수'].sum()
expected = [total / len(data)] * len(data)
x = np.arange(len(data['음료종류']))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, data['관측도수'], width=width, label='관측도수')
plt.bar(x + width/2, expected, width=width, label='기대도수', alpha = 0.6)
plt.xticks(x, data['음료종류'])
plt.xlabel('음료 종류')
plt.ylabel('도수')
plt.title('음료 종류별 관측도수와 기대도수')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 카이제곱 검정결과와 그래프를 근거로 어떤 음료가 더 인기있는지 분석
data['기대도수'] = expected
data['차이'] = data['관측도수'] - data['기대도수']
data['차이비율(%)'] = np.round((data['차이'] / data['기대도수']) * 100, 2)
pd.set_option('display.max_columns', None)
print(data)
data.sort_values(by='차이', ascending=False, inplace=True)
data.reset_index(drop=True, inplace=True)
print(data)