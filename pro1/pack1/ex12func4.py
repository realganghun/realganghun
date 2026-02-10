#----------------------함수 장식자---------------------------------
#기존 함수 코드를 고치지 않고 함수의 앞/뒤 동작을 추가하기
#함수를 받아서 기능을 덧붙인 새 함수로 바꿔치기하는 것
#meta기능 보유

def make2(fn):
    return lambda:'ㅎㅇ' + fn()

def make1(fn):
    return lambda:'ㅎㅇㅎㅇ' + fn()

def hello():
    return '진강훈'

hi = make2(make1(hello)) #장식자 없이 실행
print(hi())

@make2 #-> make2(make1(hello))
@make1 #-> make1(hello)
def hello2():
    return '신기루'

print(hello2())
#-------------------------------------------------------------------------------------
def traceFunc(func):
    def wrapperFunc(a,b):
        r = func(a,b)
        print(f'함수명 : {func.__name__} (a = {a}, b = {b} -> {r})') #__name__은 현재 이름을 의미함
        return r #함수 반환값을 반환
    return wrapperFunc #closure #함수 주소 반환

@traceFunc
def addFunc(a,b):
    return a + b

print(addFunc(10,20))