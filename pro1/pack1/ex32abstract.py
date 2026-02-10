#추상 클래스(abstract class) --> overriding 강요!! <-- 이게 ㄹㅇ 다임
#추상 메소드를 가진 클래스를 추상 클래스라고 하고
#스스로 instance할 수 없다. 객체 생성 불가
#부모 클래스로만 사용됨.


from abc import *

class AbstractClass(metaclass=ABCMeta):  #추상클래스
    @abstractmethod
    def abcMethod(self):     #추상메소드
        pass

    def normalMethod(self):  #일반메소드
        print('추상클래스 내의 일반 메소드')



#parent = AbstractClass()    #에러:추상클래스는 객체 생성 불가, 부모타입으로만 씀

class Child1(AbstractClass):
    name = '난 child1'
    def abcMethod(self):     #추상메소드
        print('부모가 가진 abcMethod 재정의') #overriding안하면 error발생

c1 = Child1()
print('name : ', c1.name)
c1.abcMethod()
c1.normalMethod()

class Child2(AbstractClass):
    def abcMethod(self):     #추상메소드
        print('추상 클래스 내의 abcMethod 재정의')
    def normalMethod(self): #일반메소드 재정의
        print('일반 메소드 내 맘대로 내용 변경')

c2 = Child2()
c2.abcMethod()
c2.normalMethod()

print('---'*10)
happy = c1
happy.abcMethod()
happy = c2
happy.abcMethod() #<-- 다형성