#오버라이딩 : 결제 시스템

class Payment: #공통 규칙 선언
    def pay(self, amount):
        print(f'{amount}원 결제 처리')

#Payment의 자식은 결제를 pay()라는 동일 메소드를 이용하기를 기대
#동일 인터페이스 구사

class CardPayment(Payment):
    #얘만의 고유멤버 추가 가능
    def pay(self, amount):
        print(f'{amount}원 카드 결제 완료')
    
class CashPayment(Payment):
    def pay(self, amount):
        print(f'{amount}원 현금 결제 완료')

payments = [CardPayment(), CashPayment()]

for p in payments:
    p.pay(5000) #이게 바로 다형성! <-- 동일한 이름인데 다른 결과값이 나옴