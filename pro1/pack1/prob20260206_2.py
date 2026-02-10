class Animal:
    def move(self):
        print('동물이 움직인다')

class Dog(Animal):
    name = '개'
    def move(self):
        print('개가 움직인다')

class Cat(Animal):
    name = '고양이'
    def move(self):
        print('고양이가 움직인다')

class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    def move(self):
        print('여우가 움직인다')
    def foxMethod(self):
        print('Fow 고유 메소드')

animals = [Dog(), Cat(), Wolf(), Fox()]
for p in animals:
    p.move()