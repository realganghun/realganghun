# Car --> prototype, 원형클래스
#--------------------------
# |---handle = 1(변수)    |
# |---name(변수)          |
# |---speed(변수)         | ---> 객체공간
# |----------------------|
# |---showdata(메소드)    |
#--------------------------
# ---> UML(Unified Modeling Language)를 그릴줄 알아야함
# +는 public -는 private.

class Car:
    handle = 1 #멤버 변수
    speed = 0

    def __init__(self, name, speed):
        self.name = name #현재 객체의 name에게 지역변수 name 인자값 치환
        self.speed = speed #

    def showData(self):
        km = '킬로미터'
        msg = '속도 :' + str(self.speed) + km
        return msg
    def printHandle(self): #<--- self는 필수!!
        return self.handle #<--- 여기도 self는 필수!!

print(Car.handle) #원형(prototype) 클래스의 멤버 호출
car1 = Car('Ferrari', 100) #instance화 : 생성자 호출 후 객체(car1) 생성
print('car1 객체 주소 = ', car1)
print('car1 name = ', car1.name)
print('car1 speed = ', car1.speed)
print('car1 handle = ', car1.handle) #handle은 변수로 주지는 않았는데 prototype에는 handle이 있음. 
#만들어놓은 객체에 handle이 없으므로 원형으로 가서 handle을 찾는다.
car1.color = 'blue' #따로 car1에 color를 추가함
print('car1 color =', car1.color)

car2 = Car('Genesis', 120)
print('car2 객체 주소 = ', car2)
print('car2 name = ', car2.name)
print('car2 speed = ', car2.speed)
print('car2 handle = ', car2.handle)
#print('Car color =', Car.color)  #--> error 발생!
#print('car2 color =', car2.color) #--> error 발생!


print('Car 객체 주소 = ', id(Car))
print('car1 객체 주소 = ', id(car1))
print('car2 객체 주소 = ', id(car2)) #주소 다름 --> 객체 3개가 만들어진 것임!
print(car1.__dict__) #{'name': 'Ferrari', 'speed': 100, 'color': 'blue'} --> color라는 member 추가
print(car2.__dict__) #{'name': 'Genesis', 'speed': 120}

#------------------------------------Method-----------------------------------------
print('car1 speed : ', car1.showData()) #Method니까 ()붙여야 함, 객체의 주소가 인수로 들어감
print('car2 speed : ', car2.showData())
# car1 speed :  속도 :100킬로미터
# car2 speed :  속도 :120킬로미터


car1.speed = 150 #member값 변경
car2.speed = 200

print('car1 speed : ', car1.showData())
print('car2 speed : ', car2.showData())
# car1 speed :  속도 :150킬로미터
# car2 speed :  속도 :200킬로미터

print('car1 handle : ', car1.printHandle())
print('car2 handle : ', car2.printHandle())
# car1 handle :  1
# car2 handle :  1

car1.handle = 2
car2.handle = 4

print('car1 handle : ', car1.printHandle()) #member값 변경
print('car2 handle : ', car2.printHandle())
# car1 handle :  2
# car2 handle :  4