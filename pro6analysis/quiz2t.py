import numpy as np
import scipy.stats as stats
print('------문제 1------'*6)
# [two-sample t 검정 : 문제1] 

# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.

# 수집된 자료 :  
blue = np.array([70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80])
red = np.array([60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66])

# 대립가설 : 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.
# 귀무가설 : 포장지 색상에 따른 제품의 매출액에 차이가 존재하지 않는다.

shapiro_blue = stats.shapiro(blue)
shapiro_red = stats.shapiro(red)
print("Shapiro-Wilk Test for Blue:", shapiro_blue) # ShapiroResult(statistic=0.971, pvalue=0.898) > 0.05 -> 정규성 만족
print("Shapiro-Wilk Test for Red:", shapiro_red) # ShapiroResult(statistic=0.964, pvalue=0.791) > 0.05 -> 정규성 만족

levene = stats.levene(blue, red)
print("Levene's Test for Equal Variances:", levene) 
# LeveneResult(statistic=0.6230769230769228, pvalue=0.43916444685083794) > 0.05 -> 등분산성 만족
t_stat, p_val = stats.ttest_ind(blue, red, equal_var=True)
print(f"t-statistic: {t_stat}, p-value: {p_val}") # t-statistic: 2.9280203225212174, p-value: 0.008316545714784409 < 0.05
# -> 유의미한 차이 있음, 귀무가설 기각, 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.

result1 = stats.ttest_rel(blue, red)
print(result1) # Ttest_relResult(statistic=2.9280203225212174, pvalue=0.008316545714784409) < 0.05
# -> 유의미한 차이 있음, 귀무가설 기각, 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.

print('------문제 2------'*6)
# [two-sample t 검정 : 문제2]  

# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.

# 수집된 자료 :  
boys = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8] #23
girls = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4] #20

# 대립가설 : 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있다.
# 귀무가설 : 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 없다.

boys_sample = np.random.choice(boys, size=15, replace=False)
girls_sample = np.random.choice(girls, size=15, replace=False)

shapiro_boys = stats.shapiro(boys_sample)
shapiro_girls = stats.shapiro(girls_sample)
print("--- 2. 정규성 검정 결과 ---")
print(f"남자 p-value: {shapiro_boys.pvalue:.4f}")
print(f"여자 p-value: {shapiro_girls.pvalue:.4f}")
if shapiro_boys.pvalue > 0.05 and shapiro_girls.pvalue > 0.05:
    # 등분산성 확인
    levene = stats.levene(boys_sample, girls_sample)
    is_equal = levene.pvalue > 0.05
    t_stat, p_val = stats.ttest_ind(boys_sample, girls_sample, equal_var=is_equal)
    test_name = "독립표본 t-검정"

else:
    # Mann-Whitney U 검정 수행
    u_stat, p_val = stats.mannwhitneyu(boys_sample, girls_sample, alternative='two-sided')
    test_name = "Mann-Whitney U 검정"


print(f"분석 방법: {test_name}")
print(f"p-value: {p_val:.4f}")

alpha = 0.05
if p_val < alpha:
    print("\n결론: p-value가 0.05보다 작으므로 귀무가설을 기각")
    print("남녀 간 콜레스테롤 양에 통계적으로 유의미한 차이가 존재")
else:
    print("\n결론: p-value가 0.05보다 크므로 귀무가설을 채택")
    print("남녀 간 콜레스테롤 양에 통계적으로 유의미한 차이가 있다고 볼 수 없음.")
print('------문제 3------'*6)
# [two-sample t 검정 : 문제3]

# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
import MySQLdb
import pandas as pd

def main():
    CONFIG = {"host": "127.0.0.1", "user": "root", "passwd": "123", "db": "test", "port": 3306, "charset": "utf8"}
    
    # 1. SQL: 부서명(busername)을 함께 가져와야 그룹화가 가능합니다.
    sql = """
    SELECT busername, jikwonpay 
    FROM jikwon 
    INNER JOIN buser ON jikwon.busernum = buser.buserno 
    WHERE busername IN ('총무부', '영업부')
    """
    
    conn = MySQLdb.connect(**CONFIG)
    df = pd.read_sql(sql, conn) # pandas의 read_sql을 쓰면 더 편합니다.
    conn.close()

    # 2. 결측치 처리 (해당 부서의 평균연봉으로 채우기)
    # groupby를 사용하여 부서별 평균을 구하고 결측치를 채웁니다.
    df['jikwonpay'] = df['jikwonpay'].fillna(df.groupby('busername')['jikwonpay'].transform('mean'))
    print(df)

    # 3. 부서별로 데이터 분리
    chongmu = df[df['busername'] == '총무부']['jikwonpay']
    youngup = df[df['busername'] == '영업부']['jikwonpay']

    # 4. Two-sample t-test 수행 (독립 표본 t-검정)
    # 먼저 등분산성 검정(levene)을 하는 것이 정석입니다.
    levene_p = stats.levene(chongmu, youngup).pvalue
    
    # 등분산성 여부에 따라 equal_var 옵션 조절
    t_stat, p_val = stats.ttest_ind(chongmu, youngup, equal_var=(levene_p > 0.05))

    print(f"총무부 평균 연봉: {chongmu.mean():.2f}")
    print(f"영업부 평균 연봉: {youngup.mean():.2f}")
    print(f"p-value: {p_val}")

    if p_val < 0.05:
        print("결론: 두 부서 간 연봉 평균에 유의미한 차이가 있습니다. (귀무가설 기각)")
    else:
        print("결론: 두 부서 간 연봉 평균에 유의미한 차이가 없습니다. (귀무가설 채택)")

if __name__ == "__main__":
    main()

print('------문제 4------'*6)
# [대응표본 t 검정 : 문제4]

# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

# 수집된 자료 :  
mid = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

# 대립가설 : 이 학급의 학업능력이 변화했다.
# 귀무가설 : 이 학급의 학업능력이 변화하지 않았다.
print(np.mean(mid), np.mean(final)) # 74.16666666666667 81.66666666666667
print("평균의 차이 : ", np.mean(mid) - np.mean(final)) # -7.5
result4 = stats.ttest_rel(mid, final)
print('result4 : ', result4) # Ttest_relResult(statistic=-2.6281127723493998, pvalue=0.023486192540203194) < 0.05
# -> 유의미한 차이 있음, 귀무가설 기각, 이 학급의 학업능력이 변화했다.