# pandas 문제 7)
import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}
#  a) MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.

#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
conn = pymysql.connect(**config)
cursor = conn.cursor()
sql = """
    select jikwonno, jikwonname, busername, jikwonpay, jikwonjik from jikwon inner join buser on jikwon.busernum=buser.buserno
    """
cursor.execute(sql)

with open('pandasDB2quiz.csv', mode='w', encoding='utf-8') as fobj:
    writer = csv.writer(fobj)
    for row in cursor.fetchall():
        writer.writerow(row)

#      - DataFrame의 자료를 파일로 저장
df = pd.read_csv('pandasDB2quiz.csv', header=None, names=['사번', '이름', '부서명', '연봉', '직급'])
print(df.head(3))

#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
buser_paysum = df.groupby(['부서명'])['연봉'].sum()     #부서명별 연봉합
print('부서명별 연봉의 합 : ', buser_paysum)
buser_paymax = df.groupby(['부서명'])['연봉'].max()     #부서명별 연봉합
print('부서명별 최대연봉 : ', buser_paymax)
buser_paymin = df.groupby(['부서명'])['연봉'].min()     #부서명별 연봉합
print('부서명별 최소연봉 : ', buser_paymin)

#      - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
ctab = pd.crosstab(df['부서명'], df['직급'])
print('교차표\n : ', ctab)

#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
sql_gogek = """
    SELECT jikwonname, gogekno, gogekname, gogektel 
    FROM jikwon LEFT OUTER JOIN gogek ON jikwonno = gogekdamsano
"""
cursor.execute(sql_gogek)

# 2. DataFrame 생성
df_gogek = pd.DataFrame(cursor.fetchall(), 
                        columns=['직원명', '고객번호', '고객명', '고객전화'])

# 3. 결측치(None/NaN) 처리
# '고객번호'가 비어있다면 담당 고객이 없다는 뜻이므로 "담당 고객 X"로 채웁니다.
# 숫자인 고객번호를 문자열과 섞어 쓰려면 전체를 문자열(object)로 취급하는 게 편합니다.
df_gogek = df_gogek.fillna('X')

# 4. 출력
print("\n[직원별 담당 고객 자료]")
print(df_gogek)


#      - 연봉 상위 20% 직원 출력  : quantile()
# 1. 연봉 데이터의 80% 지점(상위 20% 기준선) 값을 구합니다.
pay_threshold = df['연봉'].quantile(0.8)

# 2. 그 기준선보다 연봉이 크거나 같은 직원만 필터링합니다.
top_20_employees = df[df['연봉'] >= pay_threshold]

# 3. 결과 출력 (연봉 높은 순으로 정렬하면 더 보기 좋습니다)
print(f"연봉 상위 20% 기준선: {pay_threshold}")
print(top_20_employees.sort_values(by='연봉', ascending=False))

#      - SQL로 1차 필터링 후 pandas로 분석 
#             - 조건: 연봉 상위 50% (df['연봉'].median() ) 만 가져오기  후 직급별 평균 연봉 출력
pay_median = df['연봉'].median()
df_top_50 = df[df['연봉'] >= pay_median]

print(f"전체 연봉 중앙값: {pay_median}")
print(f"상위 50% 인원 수: {len(df_top_50)}명")

# 4. 결과 출력: 상위 50% 인원들의 직급별 평균 연봉
jik_pay_mean = df_top_50.groupby('직급')['연봉'].mean()

print("\n[연봉 상위 50% 인원들의 직급별 평균 연봉]")
print(jik_pay_mean)
#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
buser_paymean = df.groupby(['부서명'])['연봉'].mean()
bars = plt.barh(buser_paymean.index, buser_paymean, color='skyblue', alpha=0.6)
plt.bar_label(bars, padding=5, fmt='%.1f')
plt.title('부서별 연봉 평균')
plt.xlabel('평균 연봉')
plt.xlim(0, buser_paymean.max() * 1.2) # 숫자가 잘리지 않게 x축 범위를 살짝 늘려줍니다.
plt.ylabel('부서명')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


#  b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
import seaborn as sns
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
sql_b = """
    SELECT jikwonname, busername, jikwonpay, jikwongen 
    FROM jikwon INNER JOIN buser ON jikwon.busernum = buser.buserno
"""
cursor.execute(sql_b)
df_b = pd.DataFrame(cursor.fetchall(), 
                    columns=['이름', '부서명', '연봉', '성별'])
gender_pay_pivot = df_b.pivot_table(index='성별', values='연봉')
print("[성별 연봉 평균]")
print(gender_pay_pivot)
#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
plt.figure(figsize=(6, 5))
plt.bar(gender_pay_pivot.index, gender_pay_pivot['연봉'], color=['pink', 'skyblue'], alpha=0.7)
plt.title('성별 평균 연봉 비교')
plt.ylabel('평균 연봉')
plt.show()
#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
ctab_b = pd.crosstab(df_b['부서명'], df_b['성별'])
print("\n[부서별 성별 인원수 교차표]")
print(ctab_b)


#  c) 키보드로 사번, 직원명을 입력받아 로그인에 성공하면 console에 아래와 같이 출력하시오.
#       조건 :  try ~ except MySQLdb.OperationalError as e:      사용
#      사번  직원명  부서명   직급  부서전화  성별
#      ...
#      인원수 : * 명
#     - 성별 연봉 분포 + 이상치 확인    <== 그래프 출력
#     - Histogram (분포 비교) : 남/여 연봉 분포 비교    <== 그래프 출력
try:
    # 1. 키보드 입력 받기
    input_no = input("사번을 입력하세요: ")
    input_name = input("직원명을 입력하세요: ")

    # 2. 로그인 확인 및 데이터 추출 (해당 사번과 이름이 일치하는지 확인)
    # 로그인 성공 시 출력할 항목들을 조인해서 가져옵니다.
    sql_login = """
        SELECT jikwonno, jikwonname, busername, jikwonjik, busertel, jikwongen, jikwonpay
        FROM jikwon INNER JOIN buser ON busernum = buserno
        WHERE jikwonno = %s AND jikwonname = %s
    """
    cursor.execute(sql_login, (input_no, input_name))
    login_data = cursor.fetchone() # 한 명의 정보만 가져옴

    if login_data:
        print("\n[로그인 성공! 직원 정보]")
        print(f"사번: {login_data[0]}, 이름: {login_data[1]}, 부서명: {login_data[2]}, "
            f"직급: {login_data[3]}, 부서전화: {login_data[4]}, 성별: {login_data[5]}")
        
        # 전체 직원 자료 다시 불러오기 (시각화용)
        cursor.execute("SELECT jikwongen, jikwonpay FROM jikwon")
        df_all = pd.DataFrame(cursor.fetchall(), columns=['성별', '연봉'])
        print(f"전체 인원수 : {len(df_all)}명")

        # --- 시각화 1: 성별 연봉 분포 + 이상치 확인 (Boxplot) ---
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1) # 1행 2열 중 첫 번째
        sns.boxplot(x='성별', y='연봉', data=df_all)
        plt.title('성별 연봉 분포 및 이상치 확인')

        # --- 시각화 2: 남/여 연봉 분포 비교 (Histogram) ---
        plt.subplot(1, 2, 2) # 1행 2열 중 두 번째
        # 성별로 나누어 히스토그램 그리기
        sns.histplot(data=df_all, x='연봉', hue='성별', kde=True, element="step")
        plt.title('남/여 연봉 분포 비교 (Histogram)')
        
        plt.tight_layout()
        plt.show()

    else:
        print("로그인 실패: 사번 또는 이름이 일치하지 않습니다.")

except pymysql.OperationalError as e:
    print("DB 연결 운영 오류 : ", e)
except Exception as e:
    print("기타 처리 오류 : ", e)

cursor.close()
conn.close()