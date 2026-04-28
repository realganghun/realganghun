# [ANOVA 예제 1]

# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.
# 수집된 자료 :

# kind quantity
# 1 64
# 2 72
# 3 68
# 4 77
# 2 56
# 1 NaN
# 3 95
# 4 78
# 2 55
# 1 91
# 2 63
# 3 49
# 4 70
# 1 80
# 2 90
# 1 33
# 1 44
# 3 55
# 4 66
# 2 77

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

# 1. 데이터 생성
data = {
    'kind': [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2],
    'quantity': [64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]
}
df = pd.DataFrame(data)

# 2. 결측치(NaN) 처리: 해당 칼럼(quantity)의 평균값으로 대체
df['quantity'] = df['quantity'].fillna(df['quantity'].mean())

# 3. 그룹별 데이터 분리 (기름 종류 1, 2, 3, 4)
g1 = df[df['kind'] == 1]['quantity']
g2 = df[df['kind'] == 2]['quantity']
g3 = df[df['kind'] == 3]['quantity']
g4 = df[df['kind'] == 4]['quantity']

# 4. 등분산성 검정 (Bartlett 또는 Levene)
# 아까 에러 났던 Bartlett 대신 안정적인 Levene을 써봅시다.
l_stat, l_p = stats.levene(g1, g2, g3, g4)
print(f"등분산성 검정 p-value: {l_p:.4f}")

# 5. 일원 분산분석(One-way ANOVA) 수행
f_stat, p_val = stats.f_oneway(g1, g2, g3, g4)

print(f"\nANOVA 통계량: {f_stat:.4f}") #0.2669
print(f"ANOVA p-value: {p_val:.4f}") #0.8482 > 0.05

#결론: 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다. (귀무가설 채택)
# --- [추가] 6. 사후검정 (Tukey HSD) ---
# ANOVA 결과가 유의미하지 않더라도(p > 0.05), 연습을 위해 수행해봅니다.
# 그룹 간 구체적인 차이를 확인하는 방법입니다.
tk = pairwise_tukeyhsd(endog=df['quantity'], groups=df['kind'], alpha=0.05)
print("\n--- Tukey HSD 사후검정 결과 ---")
print(tk)

# --- [추가] 7. 시각화 (Boxplot) ---
plt.figure(figsize=(8, 6))

# Seaborn을 이용한 박스플롯: 데이터의 분포와 중앙값을 한눈에 보여줍니다.
sns.boxplot(x='kind', y='quantity', data=df, palette='Set2')
sns.swarmplot(x='kind', y='quantity', data=df, color="0.25") # 실제 데이터 포인트 추가

plt.title('기름 종류별 빵의 기름 흡수량 차이', fontsize=15)
plt.xlabel('기름 종류 (Kind)', fontsize=12)
plt.ylabel('흡수량 (Quantity)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 한글 깨짐 방지 설정 (필요 시 주석 해제)
# plt.rcParams['font.family'] = 'Malgun Gothic' 

plt.show()

# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 
# 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오. 
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import koreanize_matplotlib
from pingouin import welch_anova
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pymysql

config = {
    'host':'127.0.0.1', 'user':'root', 'password':'123',
    'database':'test', 'port':3306, 'charset':'utf8mb4'
}
try:
    conn = pymysql.connect(**config)
    sql = """
        select b.busername, j.jikwonpay 
        from jikwon j 
        join buser b on j.busernum = b.buserno
    """
    df = pd.read_sql(sql,conn)
except Exception as e:
    pass
finally:
    conn.close()
df = df.dropna(subset=['jikwonpay']) # jikwonpay Na 제거
gc = df[df['busername'] == '총무부']['jikwonpay']
gy = df[df['busername'] == '영업부']['jikwonpay']
gj = df[df['busername'] == '전산부']['jikwonpay']
gg = df[df['busername'] == '관리부']['jikwonpay']
print(gg)
# 정규성
print(stats.shapiro(gc).pvalue)
print(stats.shapiro(gy).pvalue)
print(stats.shapiro(gj).pvalue)
print(stats.shapiro(gg).pvalue)
# 0.026044936412817302  <- 정규성 만족 X
# 0.06420810634182218
# 0.41940720517769636
# 0.9078027897950541
print()
# 등분산성
print(stats.levene(gc,gy,gj,gg).pvalue)
# 0.7860663814082607
# p > a 이므로 등분산성 만족
# 정규성 X 등분산성 O -> stats.kruskal()
print()
print(stats.kruskal(gc,gy,gj,gg).pvalue)
# p 0.7869924082758515 > a 이므로 귀무 채택 

# 사후 검정 
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=df.jikwonpay, groups=df.busername)
print(tukResult)
# 시각화 
tukResult.plot_simultaneous(xlabel="mean",ylabel='group')
plt.show()