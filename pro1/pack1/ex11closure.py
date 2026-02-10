#Closure : Scope에 제약을 받지 않는 변수들을 포함하고 있는 code block임.
#내부 함수의 주소를 반환해 함수 밖에서 함수 내의 멤버를 참조하기

def funcTimes(a, b):
    c = a * b
    return c

print(funcTimes(2,3))

kbs = funcTimes(2,3)
print(kbs)
kbs = funcTimes
print(kbs)
print(kbs(2,3))
print(id(kbs), id(funcTimes))

mbc = sbs = kbs

del funcTimes #funcTimes 변수 삭제

print(mbc(2,3)) #funcTimes를 없애도 funcTimes를 대입시켜놓은 mbc는 활성화돼있음(주소를 가지고 있음)
#--------------------------------클로저를 사용하지 않은 경우---------------------------------------------
def out():
    count = 0
    def inn():
        nonlocal count #nonlocal 붙이니까 색깔이 같아지네?
        count += 1
        return count
    print(inn())

out()
out()
#----------------------------------------클로저를 사용한 경우---------------------------------------------
def outer():
    count = 0
    def inner():
        nonlocal count #nonlocal 붙이니까 색깔이 같아지네?
        count += 1
        return count
    return inner #<-- 이게 closure, 실행한 결과를 return함. 내부함수의 주소를 반환하는 것.

var1 = outer() #내부함수의 주소를 변수에 저장
print('var1 주소 : ', var1)
print(var1())
print(var1())
myvar = var1()
print(myvar)

var2 = outer() #새로운 객체(inner 함수 생성), 같은 설계도로 2개를 만들었다고 생각하면 됨.
print(var2())
print(var2())

print(var1, var2)
#---------------------------------수량 * 단가 * 세금을 출력하는 함수 작성----------------------------------

def outer2(tax): #tax는 지역변수
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2 #<---- 이게 closure

#1분기에는 su * dan에 대한 tax는 0.1부과
q1 = outer2(0.1)  #q1은 inner2의 주소를 기억함.
print('1분기')
result1 = q1(5,50000)
print('수량 * 단가 * 세금 = ', result1)

result2 = q1(2,10000)
print('수량 * 단가 * 세금 = ', result2)

#2분기에는 tax가 0.05
print('2분기')
q2 = outer2(0.05)
result3 = q2(5,50000)
print('수량 * 단가 * 세금 = ', result3)
result4 = q2(2,10000)
print('수량 * 단가 * 세금 = ', result4)
#-----------------------------------------1급 함수---------------------------------------------------
#1급 함수 : 함수 안에 함수, 인자로 함수 전달, 반환값이 함수
def func1(a,b):
    return a + b

func2 = func1
print(func1(3,4))
print(func2(3,4))
print()
def func3(fu): #인자로 함수 전달
    def func4(): #함수 안의 함수
        print('내부함수')
    func4()
    return fu #반환값이 함수

mbc = func3(func1)
print(mbc(3,4))
#-----------------------------------축약함수 Lambda function---------------------------------
#Lambda function : 이름이 없는 한 줄짜리 함수
#형식 : lambda 매개변수들,,,:반환식 <-- return 없이 결과

def hapFunc(x,y):
    return x + y
print(hapFunc(1,2))

#람다로 같은 의미의 코드
print((lambda x, y:x + y)(1,2))

gg = lambda x, y:x + y
print(gg(1,2))

kbs = lambda a, su = 10: a + su
print(kbs(5))

sbs = lambda a, *tu, **di : print(a, tu, di)
sbs(1,2,3,var1 = 4, var2 = 7)

li = [lambda a, b:a+b, lambda a,b:a*b]
print(li[0](3,4))
print(li[1](3,4))

#-------------------------------다른 함수에서 람다 사용하기-------------------------------------
print(list(filter(lambda a:a < 5, range(10))))
print(list(filter(lambda a:a % 2, range(10)))) #0이면 false, 1이면 true이므로 true만 나옴.

#문제. filter를 사용하여 1~100사이의 정수 중 5의 배수이거나 7의 배수만 출력
print(list(filter(lambda a:a%5 ==0 or a%7==0,range(1,101))))