# 여러 개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함 관계 사용
# 다른 클래스를 자신의 멤버처럼 선언하고 사용함
from ex23class5 import PohamHandle

class PohamCar:
    turnShowMessage = '정지'

    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle() #---> class의 포함관계, 자원의 재활용
    
    def turnHandle(self, q):
        if q > 0 :
            self.turnShowMessage = self.handle.rightTurn(q)
        elif q < 0 :
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0 :
            self.turnShowMessage = '직진'


if __name__ == '__main__' :
    tom = PohamCar('톰')
    tom.turnHandle(10)
    print((tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + ' ' + str(tom.handle.quantity)))

    john = PohamCar('존')
    john.turnHandle(0)
    print((john.ownerName + '의 회전량은 ' + john.turnShowMessage + ' ' + str(john.handle.quantity)))

    john = PohamCar('존')
    john.turnHandle(-20)
    print((john.ownerName + '의 회전량은 ' + john.turnShowMessage + ' ' + str(john.handle.quantity)))
