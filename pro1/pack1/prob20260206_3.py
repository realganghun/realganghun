from abc import *

class Employee(metaclass = ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def data_print(self):
        pass

    def irumnai_print(self):
        print(f'이름 : {self.irum}, 나이 : {self.nai}, ', end = ' ')

class Temporary(Employee):
    def __init__(self, irum, nai, ilsu, ildang):
        self.irum = irum
        self.nai = nai
        self.ilsu = ilsu
        self.ildang = ildang
    def pay(self):
        self.wolgeub = self.ilsu * self.ildang
        return self.wolgeub
    def data_print(self):
        Employee.irumnai_print(self)
        Temporary.pay(self)
        print(f'월급 : {self.wolgeub}')

class Regular(Employee):
    def __init__(self, irum, nai, salary):
        self.irum = irum
        self.nai = nai
        self.salary = salary
    def pay(self):
        a = self.salary
        return a
    def data_print(self):
        Employee.irumnai_print(self)
        Regular.pay(self)
        print(f'급여 : {self.salary}')

class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, commission):
        self.irum = irum
        self.nai = nai
        self.salary = salary
        self.sales = sales
        self.commission = commission
    def pay(self):
        self.a = self.salary + self.sales * self.commission
        return self.a
    def data_print(self):
        Employee.irumnai_print(self)
        Salesman.pay(self)
        print(f'수령액 : {int(self.a)}')

t = Temporary('홍길동', 25, 20, 150000)
r = Regular('한국인', 27, 3500000)
s = Salesman('손오공', 29, 1200000, 5000000, 0.25)

t.data_print()
r.data_print()
s.data_print()