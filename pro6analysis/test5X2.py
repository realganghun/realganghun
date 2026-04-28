# 이원카이제곱 - 교차분할표 이용
# : 두 개 이상의 변인(집단 또는 범주)을 대상으로 검정을 수행한다.
# 분석대상의 집단 수에 의해서 독립성 검정과 동질성 검정으로 나뉜다.
# 독립성(관련성) 검정
# - 동일 집단의 두 변인(학력수준과 대학진학 여부)을 대상으로 관련성이 있는가 없는가?
# - 독립성 검정은 두 변수 사이의 연관성을 검정한다.

# 교육수준(독립변수, x)와 흡연율(종속변수, y) 간의 관련성 검정
# 대립가설 : 교육수준과 흡연율은 관련성이 있다.
# 귀무가설 : 교육수준과 흡연율은 관련성이 없다.

import pandas as pd
import scipy.stats as stats

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/smoke.csv")
print(data.head(3))
print(data['education'].unique()) # 교육수준 : 대학원졸 : 1, 대졸 : 2, 고졸 : 3
print(data['smoking'].unique()) # 흡연율 : 꼴초 : 1, 보통 : 2, 노담 : 3

# 학력 수준별 흡연 빈도수 : 교차표 사용
cross_tab = pd.crosstab(index = data['education'], columns = data['smoking'])
cross_tab.index = ['대학원졸', '대졸', '고졸']
cross_tab.columns = ['꼴초', '보통', '노담']
print(cross_tab)

# 이원카이제곱 검정
chi_result = [cross_tab.loc['대학원졸'], cross_tab.loc['대졸'], cross_tab.loc['고졸']]
chi2, p, dof, expected = stats.chi2_contingency(cross_tab)

print(f"chi2 : {chi2}, p-value : {p}, dof : {dof}") # chi2 : 18.910915739853955, p-value : 0.0.0008182572832162924, dof : 4
print("기대도수 : \n", expected) 
# 기대도수 : 
# [[68.94647887 83.8056338  58.24788732]
#  [16.9915493  20.65352113 14.35492958]
#  [30.06197183 36.54084507 25.3971831 ]]

# 유의수준 0.05보다 p-value(0.0008)가 작으므로 귀무가설 기각, 교육수준과 흡연율은 관련성이 있다.

print('--- 독립성 검정 : 실습2 ---------------')
# 남성과 여성의 스포츠 음료 선호도 검정
# 대립가설 : 남성과 여성의 스포츠 음료 선호도는 관련성이 있다.
# 귀무가설 : 남성과 여성의 스포츠 음료 선호도는 관련성이 없다.

data= pd.DataFrame({
    '게토레이' :[30, 20],
    '포카리' : [20, 30],
    '파워에이드' : [10, 30]}, index=['남성', '여성']
)
print(data)
chi2, p, dof, expected = stats.chi2_contingency(data)
print(f"chi2 : {chi2}, p-value : {p}, dof : {dof}") # chi2 : 11.375, p-value : 0.003388052521834713, dof : 2
print("기대도수 : \n", expected)
# 기대도수 : 
# [[21.42857143 21.42857143 17.14285714]
#  [28.57142857 28.57142857 22.85714286]]
# 유의수준 0.05보다 p-value(0.0033)가 작으므로 귀무가설 기각, 남성과 여성의 스포츠 음료 선호도는 관련성이 있다.