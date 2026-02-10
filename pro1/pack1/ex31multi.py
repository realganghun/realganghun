#클래스의 다중 상속(부모가 2개 이상)

class Tiger:
    data = '호랑이'

    def cry(self):
        print('호랑이 : 어흥')

    def eat(self):
        print('호랑이 기운이 솟아난다')

class Lion:
    data = '사자'
    
    def cry(self):
        print('사자 : 스껄~')
    
    def hobby(self):
        print('아 줴줴이야~')

class Liger1(Tiger, Lion): #다중 상속은 순서가 중요
    pass

a1 = Liger1()
print(a1.data) #호랑이가 찍히는데, class Liger(Lion, Tiger)로 하면 사자가 찍힘. 부모의 순서가 중요한듯
a1.eat()
a1.hobby()
a1.cry() #---> Tiger를 먼저 적어서 cry에서 호랑이의 cry가 우선순위임

def hobby():
    print('모듈의 멤버 : 일반 함수')

class Liger2(Lion, Tiger):
    data = '라이거 만세'

    def play(self):
        print('라이거 고유 메소드')
    
    def hobby(self): #method overriding
        print('라이거는 미녀를 좋아해')
    
    def showData(self):
        self.hobby() #<-- Liger2의 hobby
        super().hobby() #<-- Lion의 hobby
        hobby() #<-- Module의 멤버 hobby

        self.eat() #<-- Liger2에 eat이 없으므로 Lion/Tiger의 eat을 찾음
        super().eat() #<-- Tiger의 eat
        print(self.data + ' ' + super().data) #Liger2의 data + Lion의 data
        
print('---'*10)
a2 = Liger2()
a2.cry()
a2.showData()