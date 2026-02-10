# 1) set
# 2) list

# 1 2 3 4 5
# { }는 set을 의미하기 때문에 중복이 제거된다.

# print('건수 : ', end = ' ')
# count = 0
# for i in range(1,100):
#     if i % 3 == 0 or i % 4 == 0:
#         if i % 7 == 0:
#             continue
#         else:
#             print( i, end = ' ')
#             count += i
# print()
# print('배수의 총합 : ', count)

# for, while, range, break, continue, import re, re.sub, re.findall 등

# 1) 나누기 기호로 출력될때 실수(float)형식으로 출력된다.
# 2) 5를 3으로 나눈 몫이 출력된다.
# 3) 5를 3으로 나눴을때 나머지가 출력된다.

# 1)global
# 2)nonlocal

# 1) 출력 결과 :
# [1, 2, 3]
# 4
# 5

# 2) *연산자의 기능 :
# *로 인해서 v3가 5, v2가 4를 할당받고 v1이 나머지 인자들을 할당받는다.

# Hap = lambda m, n : m + n*5

# 출력 결과 : [1, 3, 5]
# 2는 range가 1에서 5까지 증가할 때 변동폭이 +2만큼 증가하게 해준다.

# try:
#     aa = int(input())
#     bb = 10 / aa 
# except ZeroDivisionError: 
#     print('에러 발생')

# for i in range(0,10):
#     for j in range(0,i):
#         msg1 = ''
#         msg1 += ' '
#         print(msg1, end = ' ')
#     for k in range(10,i,-1):
#         msg2 = ''
#         msg2 += '*'
#         print(msg2, end = ' ')
#     print()


# year = int(input('연도 입력 : '))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f'{year}년은 윤년')
# else:
#     print(f'{year}년은 평년')

#     1) i % 10 != 3
# 2) continue
# 3) break
# 4) i += 1

# dan = 3
# while dan <= 9:
#     j = 1
#     while j <= 9:
#         print(f'{dan} * {j} = {dan * j}', end = ' ')
#         j += 1
#     print()
#     dan += 2

# class Bicycle:
#     def __init__(self, name, wheel, price):
#         self.name = name
#         self.wheel = wheel
#         self.price = price
#     def display(self):
#         price = int(self.wheel * self.price)
#         print(f'{self.name}님 자전거 바퀴 가격 총액은 {price}원 입니다.')

# gildong = Bicycle('길동', 2, 50000)
# gildong.display()