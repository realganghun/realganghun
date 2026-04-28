# 어느 음식점의 매출 데이터와 기상청이 제공한 날씨 데이터를 활용하여
# 최고 온도에 따른 매출 변화 분석
# 세 집단 : 추움, 보통, 더움

# 귀무: 어느 음식점의 매출 데이터는 온도에 따라 매출액 평균 차이 없다.
# 대립: 어느 음식점의 매출 데이터는 온도에 따라 매출액 평균 차이 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

pd.set_option("display.max_columns", None)
# 매출 데이터 읽기
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/tsales.csv",
                            dtype={'YMD':'object'}) # int -> object
print(sales_data.head(3))
#         YMD    AMT  CNT
# 0  20190514      0    1
# 1  20190519  18000    1
# 2  20190521  50000    4
print(sales_data.info())
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   YMD     328 non-null    int64
#  1   AMT     328 non-null    int64
#  2   CNT     328 non-null    int64

# 날씨 데이터 읽기
weather_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/fa236a226b6cf7ff7f61850d14f087ade1c437be/testdata_utf8/tweather.csv")
print(weather_data.head(2)) # 328 * 3
#    stnId          tm  avgTa  minTa  maxTa  sumRn  maxWs  avgWs  ddMes
# 0    108  2018-06-01   23.8   17.5   30.2    0.0    4.3    1.9    0.0
# 1    108  2018-06-02   23.4   17.6   30.1    0.0    4.5    2.0    0.0
print(weather_data.info())  # 702 * 9
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   stnId   702 non-null    int64
#  1   tm      702 non-null    object
#  2   avgTa   702 non-null    float64
#  3   minTa   702 non-null    float64
#  4   maxTa   702 non-null    float64
#  5   sumRn   702 non-null    float64
#  6   maxWs   702 non-null    float64
#  7   avgWs   702 non-null    float64
#  8   ddMes   702 non-null    float64

print()
# sales: YMD 20190514, weather: tm 2018-06-01 병합을 위해 데이터 가공 필요
weather_data.tm = weather_data.tm.map(lambda x:x.replace("-",""))   # map, lambda 에 대해서는 설명필요
print(weather_data.head(2))

# YMD, tm를 merge
frame = sales_data.merge(weather_data, how="left", left_on='YMD', right_on="tm")
print(frame.columns)
# Index(['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn',
#        'maxWs', 'avgWs', 'ddMes'],
print(frame.head(), " ", len(frame)) #328
#    avgWs  ddMes
# 0    1.6    0.0
# 1    1.2    0.0
# 2    2.9    0.0
# 3    2.4    0.0
# 4    1.7    0.0   328

data = frame.iloc[:,[0,1,7,8]]  # YMD, AMT, maxTa, sumRn
print(data.head())
#         YMD     AMT  maxTa  sumRn
# 0  20190514       0   26.9    0.0
# 1  20190519   18000   21.6   22.0
# 2  20190521   50000   23.8    0.0
# 3  20190522  125000   26.5    0.0
# 4  20190523  222500   29.2    0.0

print("결측치(NaN) 확인: ", data.isnull().sum())
print()

print(data.maxTa.describe())
# plt.boxplot(data.maxTa)
# plt.show()

# 온도를 세 그룹으로 분리 (연속형 -> 범주형)
print(data.isnull().sum())
data['ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0, 1, 2])
print(data.head(3), ' ', data["ta_gubun"].unique())

# 정규성, 등분산성
x1 = np.array(data[data.ta_gubun == 0].AMT) # 추움 그룹 매출액
x2 = np.array(data[data.ta_gubun == 1].AMT) # 보통 그룹 매출액
x3 = np.array(data[data.ta_gubun == 2].AMT) # 더움 그룹 매출액

print(x1[:5])

# print(stats.levene(x1,x2,x3).pvalue) #0.03900 정규성 만족 X
# print(stats.bartlett(x1,x2,x3).pvalue) #0.009677

print(stats.shapiro(x1).pvalue) #0.2481924204382751 등분산성 만족 O
print(stats.shapiro(x2).pvalue) #0.03882572120522948
print(stats.shapiro(x3).pvalue) #0.3182989573650957

print()
# 온도별 매출액 평균
np.set_printoptions(suppress=True, precision=10)
spp = data.loc[:, ['AMT', 'ta_gubun']]
print(spp.groupby('ta_gubun').mean())
print(np.mean(x1)) #1032362.3188405797
print(np.mean(x2)) #818106.8702290077
print(np.mean(x3)) #553710.9375

group1 = x1
group2 = x2
group3 = x3

plt.boxplot([group1, group2, group3], showmeans=True)
plt.show()

print(stats.f_oneway(group1, group2, group3)) 
# f : 99.1908012029983, p-value : 2.3607371010895207e-34
# 해석 : p-value=2.3607371010895207e-34 < 0.05 
# 귀무가설 기각. 어느 음식점의 매출 데이터는 온도에 따라 매출액 평균 차이 있다.

# f_oneway() : 정규성 깨지면 stats.kruskal(), 등분산성이 깨지면 welch's ANOVA 사용
# stats.kruskal()

print(stats.kruskal(group1, group2, group3)) # f값 : 132.7022591443371, p-value : 1.5278142583114522e-29
print()
# welch's ANOVA
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(dv="AMT", between='ta_gubun', data=data)) # 귀무 기각
# f값 : 122.221242, p-value : 7.907874e-35 

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=spp['AMT'], groups=spp['ta_gubun'], alpha=0.05)
print(tukResult)
#        Multiple Comparison of Means - Tukey HSD, FWER=0.05       
# =================================================================
# group1 group2   meandiff   p-adj    lower        upper     reject
# -----------------------------------------------------------------
#      0      1 -214255.4486   0.0  -296755.647 -131755.2503   True
#      0      2 -478651.3813   0.0 -561484.4539 -395818.3088   True
#      1      2 -264395.9327   0.0 -333326.1167 -195465.7488   True
# -----------------------------------------------------------------
# 시각화
tukResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()