kor = 100 #모듈의 전역 변수

def abc():
    kor = 0 #함수 내의 지역 변수
    print('모듈의 멤버 함수')

class My:
    kor = 80 #My 멤버 변수(필드)
    def abc(self):
        print('My 멤버 메소드')

    def show(self):
        kor = 77 #method 내의 지역 변수
        print('kor = ', kor) #<-- 지역 변수에서 찾고, 지역 변수에 없으면 전역 변수에서 찾음. 클래스 내에서 찾는게 아님! 클래스 내는 self.kor로 찾는거
        print(self.kor)
        self.abc()
        abc()

my = My()
my.show()
#my.abc()
#print(my.kor)
#--------------------------------------------------------------------------------------------------------
print(My.kor)
tom = My()
print(tom.kor)
tom.kor = 88
print(tom.kor)

oscar = My()
print(oscar.kor)