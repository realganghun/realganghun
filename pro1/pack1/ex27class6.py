#할아버지 -> 아버지 -> 나 순으로 가면서 상속받으면 내 능력이 젤 커짐(내 특성 + 아버지 특성 + 할아버지 특성)

#상속 : 자원의 재활용을 목적으로 특정 클래스의 멤버를 가져다 쓰는 것
#코드 재사용
#확장성 - 기존 클래스에 새 기능을 추가한 새로운 클래스 생성
#구조적 설계 - 공통개념은 부모 클래스, 구체적 내용은 자식 클래스에서 구현
#다형성 구사 - 메소드 오버라이딩

class Animal: # 동물들이 가져야 할 공통 속성과 행위 선언
    age = 1

    def __init__(self):
        print('Animal 생성자')
    def move(self):
        print('움직인다')


#Dog이 스스로 갖고있는 속성은 my만 있음. 상속을 받으면 Animal의 속성도 가져옴
class Dog(Animal): # Dog(Animal) <- 상속
    age = 4
    def __init__(self):
        print('Dog 생성자')
    def my(self):
        print('댕댕이')
#Animal : 부모, 조상, super, parent class
#Dog : 자식, 자손, 파생, sub, child class

#상속 : 강한 결합 - 유지, 보수 불편 그러나 다형성을 구사하려면 상속밖에 없음 ㅜ
#포함 : 약한 결합 - 탈부착이 쉬워서 많이 씀
dog1 = Dog() # -> Dog()에서 def __init__(self) 실행돼서 'Dog 생성자'가 찍힘
print('-----------------')
dog1.my()
print('-----------------')
dog1.move()
print('-----------------')
print('age : ', dog1.age)

# dog2 = Dog() # -> Dog()에서 def __init__(self) 실행돼서 'Dog 생성자'가 찍힘
# print('-----------------')
# dog2.my()
# print('-----------------')
# dog2.move()
# print()

class Horse(Animal):
    pass

horse1 = Horse() #자식에 생성자 없으면 부모 생성자로 올라감
horse1.move()