'''
var1 = "안녕 파이썬"
print(var1) #주석

"""
여러줄
주석
"""

var1 = 5
var1 = 10
var1 = 5.6
print(var1)

var2 = var1
var3=7
print(id(var1), id(var2), id(var3))

Var3=8
print(var3, Var3)

a = 5
b = a
c = 5

print(a is b, a == b) #is  : 주소 비교 연산
print(b is c, b == c) # == : 값 비교 연산

aa = [5]
bb = [5]

print(aa, bb)
print(aa is bb)
print(aa == bb)


print('------')  # =print("------")
import keyword #키워드 목록 확인용 모듈 읽기
print('예약어 목록 :', keyword.kwlist)
'''
print('type(자료형) 확인')

kbs = 9.8
print(isinstance(kbs, int)) #int=정수
print(isinstance(kbs, float)) #float=실수
print(5 , type(5))
print(5.6 , type(5.6))
print(5 + 4j , type(5 + 4j)) #complex=복소수
print((True , type(True))) #bool=참, 거짓
print('good' , type('good')) #str = 문자열
print((1,) , type((1,)))
print([1] , type([1]))
print({1} , type({1}))
print({'k':1} , type({'k':1}))