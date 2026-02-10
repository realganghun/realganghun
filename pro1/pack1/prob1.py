# 문1) 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
a = 0
sum1=0   # <-- sum은 python keyword이므로 변수로 쓰기에 적합하지 않음
while a <= 99:
    a += 1
    if a % 3 == 0:
        continue
    elif a % 2 == 0:
        continue
    else:
        sum1 += a
print('1. sum = ', sum1)
# 문2) 2 ~ 5 까지의 구구단 출력
print('2. ')
for i in range(2,6):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}', end = ' ')
    print()
# 문3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
k = 0
while k <= 100:
    k += 1
    sum = 0
    if k % 2 == 0:
        sum += k
    else:
        sum -= k
print('3. sum = ', sum)
# 문4) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
aa = 0
n=0
sum4 = 0
while n <= 49:
    n += 1
    aa = (-1)**n * (2*n - 1)
    sum4 += aa
print('4. sum = ', sum4)
# 문5) 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력
print('5.', end = ' ')
for i in range(1,100):
    a = i%10
    b = i//10
    c = a + b
    if c >= 10:
        print(i, end = ' ')
# 예) 29 → 2 + 9 = 11 (출력)
# 문6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력
print()
a6 = 0
sum6 = 0
while True:
    a6 += 1
    sum6 += a6
    if sum6 > 1000:
        break
print('6. 1000을 넘을때의 숫자 : ', a6, 'sum = ', sum6)
# 힌트: 언제 멈출지 미리 모름 → while 적합
# 문7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
print('7. ', end = ' ')
for i in range(1,10):
    for j in range(1,10):
        k = i * j
        if k <= 30:
            print(f'{i} * {j} = {k}', end = ' ')
        else:
            print()
            break

# 문8) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
sum8=0
print('8. sum = ', end = ' ')
for i in range(2,1000):
    for j in range(2,1000):
        if i%j==0:
            if i//j==1:
                print(i, end = ' ')
                sum8 += 1
            else:
                break
print('sum = ', sum8)
# 힌트: 이 문제는 반복이 두 단계다. 2부터 1000까지 하나씩 검사한다. 각 숫자마다 소수인지 확인한다.
# 그래서 while 안에 while 구조가 필요하다.
# continue 연습 문제
# 문제1) 1부터 50까지의 숫자 중 3의 배수는 건너뛰고 나머지 수만 출력하라
a9 = 0
print('9. ', end = ' ')
while a9 <= 50:
    a9 += 1
    if a9%3 != 0:
        print(a9, end = ' ')
    else:
        continue

# 문제2) 1부터 100까지 출력하되 4의 배수, 6의 배수는 건너뛴다. 그 외의 수 중 5의 배수만 출력하고 그들의 합도 출력하라
print()
a10 = 0
sum10=0

while a10 <= 99:
    a10 += 1
    if a10%4==0:
        continue
    elif a10%6==0:
        continue
    elif a10%5==0:
        print('5의 배수 : ', a10)
        sum10 += a10
    else:
        print(a10, end = ' ')
    print()

print('sum = ', sum10)