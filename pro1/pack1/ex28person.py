#상속

class Person:
    say = '지예아~ 나는 다채로운 래핑과 라이밍' #<-- 접근 권한 : public
    age = '110.12'
    __msg = 'Good : private member' #변수 앞에 __붙이면 private member가 됨. (현재 클래스에만 인식됨)

    def __init__(self, age):
        print('Person 생성자')
        self.age = age

    def printInfo(self): #<-- 접근 권한 : public
        print(f'나이 : {self.age}, 이야기 : {self.say}')

    def helloMethod(self):
        print('ㅎㅇㅎㅇ')
        print('hello : ', self.say, self.age, self.__msg)

print(Person.say, Person.age)
#Person.printInfo() #--> error 발생

per = Person('27')
per.printInfo() #<-- 이건 오류 안남
per.helloMethod()

class Employee(Person):
    subject = '근로자'
    say = '아 줴줴이야~' #hiding/shadowing이라 부름

    def __init__(self):
        print('Employee 생성자')

    def ePrintInfo(self): #Person에 있는 method를 Employee에 부름
        print(self.subject, self.say, self.age)
        #print(self.__msg) ---> __msg가 private member라서 error발생 : Person class에서만 유효
        self.helloMethod()
        self.printInfo()
        print(super().say)  #<-- super()가 붙으면 부모의 함수, 변수를 씀!!, super()는 두 단계 이상의 상위로는 못감. 한단계 상위로만 가능
        super().printInfo()

    def printInfo(self): #<-- 접근 권한 : public
        print('Employee 클래스의 printInfo 호출됨')

emp = Employee()
print(emp.subject, emp.say, emp.age)
emp.ePrintInfo() #<-- self때문에 say에서 줴줴이야가 찍히는 것임.

class Worker(Person):
    def __init__(self, age):
        print('Worker 생성자')
        super().__init__(age) # 부모 클래스의 생성자 호출
    def wPrintInfo(self):
        print('Worker - wPrintInfo 처리')
        #self.printInfo()
        super().printInfo()
print('---'*10)
worker1 = Worker('23')
print(worker1.say, worker1.age)
worker1.wPrintInfo()

print('---'*10)
print('---'*10)
class Programmer(Worker):
    def __init__(self, age):
        print('Programmer 생성자')
        super().__init__(age) #Bound call
        # =Worker.__init__(self, age) <-- Unbound call
    def pPrintInfo(self):
        print('Programmer - pPrintInfo 처리')
        super().wPrintInfo()
    def wPrintInfo(self): #부모 메소드와 동일 메소드 선언
        print('Programmer에서 overriding')

programmer1 = Programmer('25')
print(programmer1.say, programmer1.age)
programmer1.pPrintInfo()
programmer1.wPrintInfo()

print('\n클래스 타입 확인')
a = 3; print(type(a))
print(type(programmer1))
print(type(worker1))
print(Person.__bases__) #모든 클래스의 superclass는 object임.
print(Employee.__bases__)
print(Worker.__bases__)
print(Programmer.__bases__)