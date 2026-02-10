"""
v1 = 3 #치환 연산자
v1 = v2 = v3 = 5

print(v1, v2, v3)
print('출력1', end = ' ')
print('출력2')
print('출력3')

"""
'''
v1, v2 = 10, 20
print(v1, v2)

v2, v1 = v1, v2
print(v1, v2)

print('값 할당 : packing 연산')
v1 = 1,2,3,4,5 #v1 = (1,2,3,4,5)
v1 = [1,2,3,4,5]
*v1, v2 = [1,2,3,4,5] #끝에있는거만 v2에 대입, 나머지는 v1
print(v1, ' ', v2)

v1, *v2 = [1,2,3,4,5]
print(v1, ' ', v2)

*v1, v2, v3 = [1,2,3,4,5]
print(v1, ' ', v2, ' ', v3)

print()

print(format(1.5678, '10.3f')) #전체 10자리, 소수 이하 셋째자리까지.

print('나는 나이가 %d 이다.'%23) 

print('나는 나이가 %s 이다.'%'스물셋')

print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))

print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))

print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))

print('이름은 {0}, 나이는 {1}'.format('한국인', 33))

print('이름은 {}, 나이는 {}'.format('신선해', 33))

print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))

abc=123
print(f"abc의 값은 {abc}임")
'''



print('\n본격적 연산 ----------------') #\n은 라인스킾
print('\b본격적 연산 ----------------') 
print('\t본격적 연산 ----------------') #\t는 탭

print(5 + 3, 5 - 3, 5 * 3, 5/3, 5//3, 5%3, 5**3)
#8 2 15 1.6666666666666667 1 2 125
print(divmod(5,3), ' ', 5 % 3)
result = 3 + 4 * 5 + (2 + 3) / 2 
print(result) # () -> ** -> 단항 -> 산술연산자(* , / -> + , -) -> 관계연산자(<, >) -> 논리(not -> and -> or) -> 치환(=)

print(5 > 3, 5 < 3, 5 == 3, 5 != 3, 5 <= 3)

print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3))
print(True or False and False) #둘 중에 하나 True면 True임, 논리연산자 우선순위 주의
print(True and False or False) 

print(4 + 5) #산술 연산
print('4' + '5') #문자열 더하기
print('한' + '국' + '만세')
print('한국' * 10)

print('누적')
a = 10
a = a + 1 #a += 1과 같음, -=, *=, /= 도 있음
print(f"a는 {a}")

#print(a++) #a++, a-- : 증감 연산자는 python에 없음
print(--a) #--a는 부호 그대로
print(-a) #-a는 부호 반대
print(a*-1)

#print(('1' + '1') + 1) #문자와 숫자의 합은 불가능(error뜸)
print(int('1' + '1') + 1)  #int(문자열) -> 정수화
print(float('1' + '1') + 1) #float(문자열) -> 실수화
print(str(1 + 1) + '1') #str(숫자) -> 문자화

print('boolean 처리 : ', bool(True), bool(False))
print(bool(1), bool(12.3), bool('ok'), bool([1,2])) #데이터 있으면 True
print(bool(0), bool(0.0), bool(''), bool([]), bool(None)) #데이터 없으면 False

# r 선행문자
print('aa\tbb')
print('aa\nbb')

print(r'aa\tbb') #r은 ''안을 데이터 자체로 보게 해줌

