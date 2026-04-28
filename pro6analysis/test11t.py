# 어느 음식점의 매출 데이터와 기상청이 제공한 날씨 데이터를 활용하여
# 강수 여부에 따른 매출 변화 분석
# 두 집단: 강수량이 있을 때, 맑을 때

# 귀무: 어느 음식점의 매출 데이터는 강수 여부에 따라 매출액 평균 차이 없다.
# 대립: 어느 음식점의 매출 데이터는 강수 여부에 따라 매출액 평균 차이 있다.

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
print(frame.head(), " ", len(frame))
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

print("----- 독립표본 t-test -----")

# print(data["sumRn"] > 0)
# 0      False
# 1       True  강수량 있으면 True
# 2      False

# 컬럼 추가: 강수량이 있으면 1, 없으면 0 
# data['rain_yn'] = (data["sumRn"] > 0).astype(int)
# print(data.head())

# print(True*1, ' ', False*1) # 1  0 출력됨
data['rain_yn'] = (data.loc[:,("sumRn")] > 0).astype(int) * 1
print(data.head())
#         YMD     AMT  maxTa  sumRn  rain_yn
# 0  20190514       0   26.9    0.0        0
# 1  20190519   18000   21.6   22.0        1
# 2  20190521   50000   23.8    0.0        0
# 3  20190522  125000   26.5    0.0        0
# 4  20190523  222500   29.2    0.0        0
print()

# box plot으로 시각화
sp = np.array(data.iloc[:,[1,4]])   # AMT(매출액), rain_yn(강수여부)
# print(type(sp))
# print(sp)
tg1 = sp[sp[:,1] == 0, 0]           # 표현식 이해 잘 안됨.. 강수X 매출액
tg2 = sp[sp[:,1] == 1, 0]           # 강수O 매출액
print(tg1[:3])                      # [     0  50000 125000]
print(tg2[:3])                      # [ 18000 274000 318000]
print("맑은 날 매출액 평균: ", np.mean(tg1))    # 761040
print("비 온날 매출액 평균: ", np.mean(tg2))    # 757331

plt.boxplot([tg1, tg2], meanline=True, showmeans=True, notch=True)
# meanline, showmeans의 차이는 뭐고 notch는 뭔지 설명추가필요
plt.show()

# 정규성 검정
print(len(tg1), '   ', len(tg2))    # 236     92
print(stats.shapiro(tg1).pvalue)    # 0.0560 > 0.05 이므로 정규성 만족
print(stats.shapiro(tg2).pvalue)    # 0.8827 > 0.05 이므로 정규성 만족
print()
# 등분산 검정
print(stats.levene(tg1, tg2).pvalue)# 0.7123 > 0.05 이므로 등분산 만족
print(stats.ttest_ind(tg1,tg2, equal_var=True)) # 만족하지못하면 False
# statistic=0.1011, pvalue=0.9195, df=326
# 해석: 정규성과 등분산성 조건 충족하였음
# pvalue=0.9195 > alpha=0.05 이므로 귀무가설 채택 >> 강수 여부에 따른 매출액 평균 차이는 없다



