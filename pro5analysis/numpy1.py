# numpy의 ndarry는 단순한 배열이라기보다는 벡터/행렬 연산도 가능한 다차원 수치 데이터 구조다.
import numpy as np

ss = ['tom', 'james', 'oscar', 1, True] #여러 type의 자료로 구성
print(ss, ' ', type(ss))

ss2 = np.array(ss)
print(ss2, ' ', type(ss2)) # list에서 (,)가 사라지고, 같은 type의 자료(문자열)로 구성된다.

#10, 20, 30 이런 모양의 배열을 출력하고 싶음
li = list(range(1,10))
print(li)
print(li[0], ' ', id(li[0]))
print(li * 10)

for i in li:
    print(i*10, end = ' ') #for문을 돌리면 되지만 데이터가 많아질수록 시간이 오래걸리게 됨.

num_arr = np.array(li)
print(num_arr[0], ' ', num_arr[1], ' ', id(num_arr[0]), ' ', id(num_arr[1])) #id(num_arr[0]), id(num_arr[1])의 주소 같음
print(num_arr * 10) # 벡터화 연산 가능

print()
a = np.array([1, 2, 3.5], dtype='float32')
print(a, type(a)) # ndarray는 동일 타입만 취급
# 여러 타입의 자료가 입력되면 상위타입으로 자동변환. int -> float -> complex -> str

c = np.zeros((2,2))
print(c)
d = np.ones((2,2))
print(d)
e = np.eye(3)
print(e)

print()
print(np.random.rand(5)) #균등 분포
print(np.random.randn(5)) #정규 분포

np.random.seed(0)
print(np.random.rand(2,3))

print(list(range(0,10)))
print(np.arange(10))
print()
# 인덱싱/슬라이싱
a = np.array([1,2,3,4,5])
print(a, ' ', a[1])
print(a[1:4])
print(a[1:])
print(a[1:5:2]) # 인덱스 1 이상, 인덱스 5 미만, 증가치는 2
print(a[-2:]) #인덱스 뒤에서 1번째, 뒤에서 2번째

b = a
print(a[0], ' ', b[0])

b[0] = 88
print(a[0], ' ', b[0])

c=np.copy(a)
print(a[0], ' ', c[0])

b[0] = 32
print(a[0], ' ', c[0])