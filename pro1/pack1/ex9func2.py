#사용자 정의 함수

"""
def 함수명(가인수):
    return 반환값 #1개만 반환, return이 없으면 return None

함수명(실인수) #함수 호출
"""

# def doFunc1():
#     print('doFunc1 수행') #return이 따로 없으면 return None과 같음.

# def doFunc2(name):
#     print('name : ', name)

# def doFunc3(arg1, arg2):
#     re = arg1 + arg2
#     return re

# def doFunc4(a1, a2):
#     imsi = a1 + a2
#     if imsi % 2 == 1:
#         return
#     else:
#         return imsi

# doFunc1() #함수 호출
# print('함수 주소는 ', doFunc1) #함수의 주소를 불러옴 -> <function doFunc1 at 0x000002B77951F920>
# print('함수 주소는', id(doFunc1))
# imsi = doFunc1
# imsi() # <- 함수의 주소를 치환함
# print(doFunc1()) #함수 수행 후 갖고 돌아온 정보인 None을 print함 -> doFunc1 수행 None

#----------------------------------------------------------------------------------------------------------
# doFunc2(7)
# doFunc2('으아아')
#-------------------------------------------------------------------------------
# print(doFunc3('신대웅', '개병신'))
# print(doFunc3(5, 6))
# result = doFunc3(5, 6)
# print(result)

# print(doFunc4(3,4))
# print(doFunc4(3,5))
#------------------------------------------------------------------------------
# def triArea(a, h):
#     c = a*h/2
#     triAreaPrint(c) #다른 함수 호출

# def triAreaPrint(cc):
#     print('삼각형의 면적은 ', cc)

# triArea(20,30)
#---------------------------------------------------------------------------------------
# def passResult(kor, eng):
#     ss = kor + eng
#     if ss >= 50:
#         return True
#     else:
#         return False
    
# if passResult(20, 60):
#     print('합격')
# else:
#     print('불합격')

# print()
# def swapFunc(a,b):
#     return b, a

# a = 10
# b = 20

# print(a, ' ', b)
# print(swapFunc(a,b)) #함수는 하나의 값만 반환하므로 (20, 10)의 형태(tuple)로 반환됨

#----------------------------------------------------------------------------------------
# def funcTest():
#     print('funcTest 멤버 처리')
#     def funcInner():
#         print('내부 함수')
#     funcInner()

# funcTest()
#-------------------------------------------------------------------------------------------
# def isOdd(para):
#     return para%2==1 #홀수면 True 반환

# mydict = {x:x*x for x in range(11) if isOdd(x)}
# print(mydict)

#변수의 생존 범위(scope rule)---------------------------------------------------------------------------
#변수가 저장되는 이름공간은 변수가 어디서 선언되었는가에 따라 생존 시간이 다름
#전역, 지역 변수


# player = '전국대표' #전역변수 (현재 모듈 어디서든 호출 가능)
# name = '한국인'

# def funcSoccer():
#     name = '홍길동' #지역변수 (현재 함수 내에서만 호출 가능)
#     player = '박지성'
#     city = '서울'
#     print(f'이름은 {name} 수준은{player}')
#     print(f'지역은 {city}')

# funcSoccer()
# print(f'이름 : {name} 수준 : {player}')
#print(f'지역 : {city}')

#Local -> Enclosing function -> Global -> Built-in 순서------------------------------------------
# print()
a = 10
b = 20
c = 30
def Foo():
    a = 7 # --> 지역변수
    b = 100
    def Bar():
        global c #c가 Bar 함수의 멤버가 아니라 파일의 멤버가 된다. 한마디로 전역변수가 됨
        nonlocal b #현재 function의 한단계 상위 멤버가 됨. Bar의 멤버가 아니라 Foo의 멤버가 되는 것
        b = 8 # --> 지역변수
        print(f'Bar 함수 수행 후 a : {a}, b : {b}, c : {c}')
        c = 3
        b = 200
    Bar()
    print(f'Foo 함수 수행 후 a : {a}, b : {b}, c : {c}')

Foo()
print(f'함수 수행 후 a : {a}, b : {b}, c : {c}')
# --------> 함수는 별도의 공간을 갖고 있음!

g = 1
def func():
    global g
    a = g
    g = 2 # <--- 이때, g는 지역변수가 됨
    return a

print(func())
print('g : ', g)