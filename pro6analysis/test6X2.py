# 이원카이제곱
# 동질성 검정 - 두 집단의 분포가 동일한가? 다른 분포인가? 를 검증하는 방법이다. 
# 두 집단 이상에서 각 범주(집단) 간의 비율이 서로 동일한가를 검정하게 된다. 
# 두 개 이상의 범주형 자료가 동일한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다.

# 동질성 검정실습1) 교육방법(독립변수)에 따른 교육생들의 만족도(종속변수) 분석 - 동질성 검정 survey_method.csv
# 대립가설 : 교육방법에 따른 교육생들의 만족도는 차이가 있다.
# 귀무가설 : 교육방법에 따른 교육생들의 만족도는 차이가 없다.

import pandas as pd
import scipy.stats as stats

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/survey_method.csv')
print(data.head(3))

# 만족도에 대한 설문조사 수집 자료
print(data['method'].unique()) # 교육방법 : 온라인 : 1, 오프라인 : 2, 혼합 : 3
print(data['survey'].unique()) # 만족도 : 불만족 : 1, 보통 : 2, 만족 : 3

ctab = pd.crosstab(index=data['method'], columns=data['survey'])
ctab.index = ['온라인', '오프라인', '혼합']
ctab.columns = ['불만족', '조금 불만족', '보통', '조금 만족', '만족']
print(ctab) # 관측된 분포 비율

chi2, p, dof, expected = stats.chi2_contingency(ctab)
print(f"chi2 : {chi2}, p-value : {p}, dof : {dof}") # chi2 : 6.544667820529891, p-value : 0.5864574374550608, dof : 8
print("기대도수 : \n", expected) # 예측된 분포 비율, 기대도수 : 
# [[ 7.          9.66666667 12.33333333 14.          7.        ]
#  [ 7.          9.66666667 12.33333333 14.          7.        ]
#  [ 7.          9.66666667 12.33333333 14.          7.        ]]
# p-value가 0.586으로 유의수준 0.05보다 크므로 귀무가설 채택
# 우연히 발생한 자료일 가능성이 높다. 교육방법에 따른 교육생들의 만족도는 차이가 없다.

print('--- 동질성 검정 : 실습2 ---------------')
# 동질성 검정 실습2) 연령대별 sns 이용률의 동질성 검정
# 20대에서 40대까지 연령대별로 서로 조금씩 그 특성이 다른 SNS 서비스들에 대해 이용 현황을 
# 조사한 자료를 바탕으로 연령대별로 홍보 전략을 세우고자 한다.
# 연령대별로 이용 현황이 서로 동일한지 검정해 보도록 하자.

# 대립가설 : 연령대별로 sns 이용 현황은 동일하지 않다.
# 귀무가설 : 연령대별로 sns 이용 현황은 동일하다.

data2 = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/snsbyage.csv')
print(data2.head(3))
print(data2['age'].unique()) # 연령대[1 2 3] : 20대 : 1, 30대 : 2, 40대 : 3
print(data2['service'].unique()) 
# sns 회사['F', 'T', 'K', 'C', 'E'] : 1~10 : 1, 11~20 : 2, 21~30 : 3, 31~40 : 4, 41~50 : 5

ctab2 = pd.crosstab(index=data2['age'], columns=data2['service'])
ctab2.index = ['20대', '30대', '40대']
ctab2.columns = ['페이스북', '트위터', '카카오스토리', '인스타그램', '틱톡']
print(ctab2)
chi2, p, dof, expected = stats.chi2_contingency(ctab2)
print(f"chi2 : {chi2}, p-value : {p}, dof : {dof}") # chi2 : 102.75202494484225, p-value : p-value : 1.1679064204212775e-18, dof : 8
print("기대도수 : \n", expected) # 기대도수 :  
# [[ 82.07366227  17.74565671 144.9228631  177.45656706 109.80125087]
#  [ 88.09034051  19.04656011 155.54690757 190.46560111 117.85059069]
#  [ 51.83599722  11.20778318  91.53022933 112.07783183  69.34815844]]

# 유의수준 0.05보다 p-value(1.167e-18)가 작으므로 귀무가설 기각, 연령대별로 sns 이용 현황은 동일하지 않다.

print("~~~~~~~~~~~~~~~~~"*3)
print("전체 건수 : ", len(data2)) # 전체 건수 : 1439
# 위 자료는 샘플 자료이겠으나 모집단이라 가정하고 샘플링 후 검정
sample_data = data2.sample(n=500, replace=False, random_state=1) # 샘플링
print(sample_data.head(), ' ', len(sample_data)) # 샘플링 후 건수 : 500
ctab3 = pd.crosstab(index=sample_data['age'], columns=sample_data['service'])
print(ctab3)
chi2, p, dof, expected = stats.chi2_contingency(ctab3)
print(f"chi2 : {chi2}, p-value : {p}, dof : {dof}") #chi2 : 44.89444172549492, p-value : 3.8534448390983085e-07, dof : 8
