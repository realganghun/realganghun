#조건 판단문 if

var = 5

if var >= 3:
    print('커')
else:
    print('작')
print()

money = 1000
age = 25

if money >= 500:
    item = '사과'
    if age <= 30:
        msg = "참 참"
    else:
        msg = '참 거짓'
else:
    item = '한라봉'
    if age >= 20:
        msg = "거짓 참"
    else:
        msg = '거짓 거짓'
print(f'중복 if 수행후 결과 {item} {msg}')
print()

data = input('점수 : ') #입력 값은 모두 문자열 타입
score = int(data)

if 90<= score <=100 :
    print('A+')
elif score >= 80:
    print('A0')
elif score >= 70:
    print('B+')
elif score >= 60:
    print('B0')
elif score >= 50:
    print('C+')
elif score >= 40:
    print('C0')
else:
    print('F')


names=['홍길동', '신선해', '이기자']
if '홍길동' in names:
    print("친구")
else:
    print("누기야")

if (count := len(names)) >= 3: #:= 대입 표현식
    print(f'인원수가 {count}명이므로 단체할인')
else:
    print("까비요")

scores = [95, 88, 76, 92, 81]
if (avg := sum(scores) / len(scores)) >= 80:
    print(f'우수반 : 평균점수 {avg}')

print('삼항 연산')
a = 'kbsa'
b = 9 if a == 'kbs' else 11
print('b : ', b)

a = 11
b = 'mbc' if a==9 else 'kbs'
print('b : ', b)

a = 3
if a < 5:
    print(0)
elif a < 10:
    print(1)
else:
    print(2)

print(0 if a<5 else 1 if a<10 else 2)
print('end')

