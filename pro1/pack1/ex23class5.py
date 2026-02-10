#클래스의 포함관계
#어딘가에서 필요한 부품 핸들 클래스를 작성

class PohamHandle:
    quantity = 0 #멤버 변수(필드), 핸들 회전량

    def leftTurn(self, q):
        self.quantity = q #지역변수 q를 각각 객체에게 줌
        return "좌회전"
    
    def rightTurn(self, q):
        self.quantity = q
        return "우회전"