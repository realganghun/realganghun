# * 카이제곱 검정
import pandas as pd
import scipy.stats as stats
import pymysql

# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오

#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/cleanDescriptive.csv')
df_clean = df.dropna(subset=['level', 'pass'])
cross_tab = pd.crosstab(index=df_clean['level'], columns=df_clean['pass'])
print(cross_tab)

chi2, p, dof, expected = stats.chi2_contingency(cross_tab)
print(f"chi2 : {chi2}, p-value : {p}, dof : {dof}") # chi2 : 18.910915739853955, p-value : 0.0.0008182572832162924, dof : 4
print("기대도수 : \n", expected)
# 유의수준 0.05보다 p-value(0.0008)가 작으므로 귀무가설 기각, 부모의 학력 수준과 자녀의 진학여부는 관련성이 있다.



# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 

# 그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.

# DB 연결
conn = pymysql.connect(
    host='localhost',
    user='root', 
    password='123', 
    db='test', 
    charset='utf8')
# SQL 쿼리 실행
sql = "SELECT jikwonjik, jikwonpay FROM jikwon"
df = pd.read_sql(sql, conn)
conn.close()

df_clean = df.dropna(subset=['jikwonjik', 'jikwonpay']) # NA가 있는 행 제외
bins = [1000, 3000, 5000, 7000, 10000] # 연봉 구간화 기준, 1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4
labels = [1, 2, 3, 4] # 직급 구간화
df_clean['jikwonpay'] = pd.cut(df_clean['jikwonpay'], bins=bins, labels=labels, right=False) # 연봉 구간화

cross_tab = pd.crosstab(index=df_clean['jikwonjik'], columns=df_clean['jikwonpay'])
print(cross_tab)

chi2, p, dof, expected = stats.chi2_contingency(cross_tab)
print(f"chi2 : {chi2}, p-value : {p}, dof : {dof}") # chi2 : 37.40349394195548, p-value : 0.00019211533885350577, dof : 12
print("기대도수 : \n", expected)
# 유의수준 0.05보다 p-value(0.000192)가 작으므로 귀무가설 기각, A회사의 직급과 연봉은 관련성이 있다.