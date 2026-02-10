# Method Overriding(재정의)
# 부모에서 정의된 메소드를 자식이 동일명의 메소드로 내용만 변경해 사용
# 부모 메소드의 기능을 대체하는 새로운 기능
# 동작의 구체화(공통 틀은 부모가, 실제 행동은 자식) 실현
# 다형성(Polymorphism) - 같은 method이나 객체에 따라 다른 기능을 수행
# 확장, 유지 보수에 도움 - 부모 코드는 유지한 채로 자식 코드만 변경

class Parent:
    def printData(self):
        pass

class Child1(Parent):
    def abc():
        print('Child 고유 메소드')
    def printData(self): #<-- Method Overriding
        a = 12 + 23
        print('Child1에서 printData 재정의') 
        print('12 + 23 = ', a)

class Child2(Parent):
    def printData(self): #<-- Method Overriding
        print('Child2에서 printData 재정의') 
        msg = '부모와 동일 메소드명이나 내용은 다름'
        print(msg)

c1 = Child1()
c1.printData()
print()
c2 = Child2()
c2.printData()
print('\n다형성 --------------------------------')
par = Parent()
par = c1
par.printData()
print()
par = c2
par.printData()

imsi = c1
imsi.printData()
imsi = c2
imsi.printData()