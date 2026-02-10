# function : 여러 개의 수행문을 하나의 이름으로 묶은 실행단위
# 함수 고유의 실행 공간을 갖음
# 자원의 재활용

#내장함수 일부 체험
print(sum([1,2,3])) #합을 나타냄
print(bin(8)) #2진법으로 표현
print(eval('4+5')) #문자인데 계산하게 해줌
print(round(1.2), round(1.6)) #반올림

import math
print(math.ceil(1.2), ' ', math.ceil(1.2)) #근사치 정수 중 큰 값(올림)
print(math.floor(1.2), ' ', math.floor(1.2)) #근사치 정수 중 작은 값(내림)

#b_list = 
b_list = [True, 1, False]
print(all(b_list)) #모두 참이어야 참
print(any(b_list)) #하나라도 참이면 참

data1 = [10, 20, 30]
data2 = ['a', 'b']
for i in zip(data1, data2):
    print(i)
    