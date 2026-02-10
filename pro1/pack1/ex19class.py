#opps(객체 중심 프로그래밍 기능) : 새로운 타입 생성, 포함, 상속, 다형성 등을 구사
#class(설계도)로 instance해서 객체를 생성(별도의 이름 공간을 갖음)
#객체는 멤버필드(변수)와 메소드로 구성(속성과 행위를 가짐)
#모듈의 멤버 : 변수, 명령문, 함수, 모듈, 클래스

def abc():
    print('aaa')

class TestClass:
    aa = 1 #멤버필드(변수), 현재 클래스 내에서 전역

    def __init__(self):
        print('생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당')
    
    def __del__(self): #<-- 얘는 거의 안씀
        print('소멸자 : 프로그램 종료시 자동실행. 마무리 작업')

    def printMsg(self): #일반 메소드
        name = '한국인' #지역변수 : printMsg 에서만 유효함
        print(name)

print(TestClass)
test = TestClass() #객체 생성
print('test 객체의 멤버 aa : ', test.aa)

#method call
test.printMsg() #1. Bound Method Call
TestClass.printMsg(test) #2. Unbound Method Call

print(type(1)) #<class 'int'>
print(type(1.0)) #<class 'float'>
print(type(test)) #<class '__main__.TestClass'> <-- 새로운 type을 만들은거임
print(id(test)) 
print(id(TestClass))

test2 = TestClass() #또 다른 객체 생성
print(id(test2))
