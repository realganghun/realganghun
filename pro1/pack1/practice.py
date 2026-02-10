# while 문을 사용 : 1 ~ 100 사이의 정수 중에서 3으로 끝나는 숫자만 출력하는 코드를 작성 하시오.

# 출력 결과는 아래와 같다.
# 3 13 23 33 43 53 63 73 83 93 (배점:10)

# a = 1
# while a <= 100:
#     if a % 10 == 3:
#         print(a, end = ' ')
#     a += 1


# 아래 소스 코드의 빈 칸을 차례대로 채우시오.
# i = 0
# while True:
#     if 1)__________:
#         i += 1
#         2)_________       

#     if i > 100: 3)________

#     print(i, end=' ')
#     4)________
# i = 0
# while True:
#     if i % 10 != 3:
#         i += 1
#         continue
#     if i > 100: 
#         break

#     print(i, end=' ')
#     i += 1


# dan = 3
# while dan <= 9:
#     j = 1
#     while j <= 9:
#         print(f'{dan} * {j} = {dan * j}', end = ' ')
#         j += 1
#     print()
#     dan += 2

# 아래 코드가 동작하도록 자전거 클래스(Bicycle class)를 정의하시오.

# 조건1 : 멤버 변수는 name, wheel, price 이다.
# 조건2 : 바퀴 가격은 바퀴수 * 가격이다.

# 실행 및 출력 결과)
# gildong = Bicycle('길동', 2, 50000) # 생성자로 name, wheel, price 입력됨
# gildong.display()

# 길동님 자전거 바퀴 가격 총액은 100000원 입니다. (배점:10)

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


# year = int(input('연도 입력 : '))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f'{year}년은 윤년')
# else:
#     print(f'{year}년은 평년')

# gg = lambda x, y:x + y
# print(gg(1,2))

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

# *v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(v1)
# print(v2)
# print(v3)