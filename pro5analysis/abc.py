# 통계량 : 데이터의 특징을 하나의 숫자로 요약한 것.
# 표본 데이터를 추출해 전체(모집단)의 데이터를 짐작 가능
# 평균, 분산, 표준편차 ....

grades = [1, 3, -2, 4] # 변량

def show_grades(grades):
    for g in grades:
        print(g, end=' ')

show_grades(grades)
print()

def grades_sum(grades):
    tot = 0
    for g in grades:
        tot += g
    return tot

print('합 : ', grades_sum(grades))

def grades_ave(grades):
    ave = grades_sum(grades) / len(grades)
    return ave

print('평균 : ', grades_ave(grades))

#분산 : 편차 제곱의 평균, 평균값 기준으로 다른 값들의 흩어진 정도
def grades_variance(grades):
    ave = grades_ave(grades)
    vari = 0
    for su in grades:
        vari += (su - ave) ** 2
    return vari/len(grades)
    # return vari / (len(grades) - 1)로도 할 수 있는데, 데이터가 ㅈㄴ 많으면 데이터 수나 데이터 -1 이나 별 차이가 없음. 
    # python에서는 / len() 이고, R에서는 / len() - 1임.

print('분산 : ', grades_variance(grades))

#표준 편차
def grades_std(grades):
    return grades_variance(grades) ** 0.5
print('표준편차 : ', grades_std(grades))

# numpy 진원 함수 사용
import numpy as np
print('합 : ', np.sum(grades))
print('평균 : ', np.mean(grades))
print('분산 : ', np.var(grades))
print('표준편차 : ', np.std(grades))