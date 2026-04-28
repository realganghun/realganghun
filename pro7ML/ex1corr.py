# 공분산 / 상관계수
# 변수가 하나인 경우에는 분산은 거리와 관련있음.
# 변수가 2개인 경우에는 분산은 방향과 관련있음.

import numpy as np

#cov : 공분산
print(np.cov(np.arange(1, 6), np.arange(2, 7))) # 우상향
print(np.cov(np.arange(10, 60, 10), np.arange(20, 70, 10))) # 우상향
print(np.cov(np.arange(100, 600, 100), np.arange(200, 700, 100))) # 우상향
print(np.cov(np.arange(1, 6), np.array([3,3,3,3,3]))) # 직선(수평선)
print(np.cov(np.arange(1, 6), np.arange(6,1,-1))) # 우하향

print()
x = [8,3,6,6,9,4,3,9,3,4]
print('x 평균 : ', np.mean(x))
print('x 분산 : ', np.var(x))
y = [6,2,4,6,9,5,1,8,4,5]
print('y 평균 : ', np.mean(y))
print('y 분산 : ', np.var(y))

import matplotlib.pyplot as plt
plt.plot(x, y, 'o')
plt.show()

# x, y의 공분산
print('x와 y의 공분산 : \n', np.cov(x,y))
print('x와 y의 공분산 : \n', np.cov(x,y)[0,1])
plt.plot(x, y, 'o')

x2 = [80,30,60,60,90,40,30,90,30,40]
y2 = [60,20,40,60,90,50,10,80,40,50]
print('x2와 y2의 공분산 : \n', np.cov(x2,y2)[0,1])

x3 = [80,30,60,60,90,40,30,90,30,40]
y3 = [6,2,4,6,9,5,1,8,4,5]
print('x3와 y3의 공분산 : \n', np.cov(x3,y3)[0,1])
plt.plot(x3, y3, 'o')
plt.show()

print()
# 두 데이터의 단위에 따라 패턴이 일치하더라도 공분산의 크기가 달라지므로 절대적 크기 판단이 어려움..
# 공분산을 표준화해서 -1 0 1 범위로 만든 것이 상관계수(r)
print('x, y의 상관계수 : ', np.corrcoef(x,y)) # 피어슨 상관계수
print('x, y의 상관계수 : ', np.corrcoef(x,y)[0,1]) #0.8663686463212855
print('x3, y3의 상관계수 : ', np.corrcoef(x3,y3)[0,1]) #0.8663686463212853

from scipy import stats
print("scipy 모듈 사용 : ", stats.pearsonr(x,y))

# 비선형 데이터인 경우 공분산, 상관계수 의미없음 ㅜㅜ(상관계수 0)
print()
m = [-3,-2,-1,0,1,2,3]
n = [9 ,4 , 1,0,1,4,9]

print(np.cov(m,n)[0,1]) # 0.0
print(np.corrcoef(m,n)[0,1]) # 0.0
plt.plot(m,n,'o')
plt.show()