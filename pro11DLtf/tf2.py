# tf.constant(), tf.Varibale(), autograph 기능
import tensorflow as tf
import numpy as np

node1 = tf.constant(3, dtype=tf.float32)    # tf.Tensor(3.0, shape=(), dtype=float32)
node2 = tf.constant(4.0)                    # tf.Tensor(4.0, shape=(), dtype=float32)
print(node1)
print(node2)

adddata = tf.add(node1, node2)
print('adddata : ', adddata)

print()
node3 = tf.Variable(3, dtype=tf.float32)    # <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=3.0>
node4 = tf.Variable(4.0)                    # <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=4.0>
print(node3)
print(node4)

imsi1 = tf.add(node3, node4) # 변수를 텐서 더하기 연산
print('imsi1 : ', imsi1) # imsi1 :  tf.Tensor(7.0, shape=(), dtype=float32)
node4.assign_add(node3) # 변수값에 더하기 후 치환
print(node4) # <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=7.0>

print()
a = tf.constant(5)
b = tf.constant(10)
# c = tf.multiply(a, b)
# print('c : ', c) # c :  tf.Tensor(50, shape=(), dtype=int32)

# 조건 처리
result = tf.cond(a < b, lambda:tf.add(10, a), lambda:tf.square(a))
# result = tf.cond(a < b, tf.add(10, a), tf.square(a)) <-- lambda안쓰면 error발생
print('result : ', result) # result :  tf.Tensor(15, shape=(), dtype=int32)

# autograph 기능  : 파이썬 코드를 텐서플로 그래프(Graph) 코드(그래프 연산)로 자동변환
# 텐서플로의 두가지 실행방법
# 1) Eager Execution : 파이썬 코드처럼 즉시 실행 (기본)
# 2) Graph Execution : 별도 운영이 가능한 계산 그래프를 만들어 최적화 후 실행(텐서 처리에 효율적)

@tf.function    # autograph가 개입함 (텐서플로 그래프 연산을 함)
def calcFunc1(a, b):    # 위 tf.cond()를 autograph 사용한 경우
    if (a < b):
        return tf.add(10, a)
    else:
        return tf.square(a)
    
result2 = calcFunc1(a, b)
print('result2 : ', result2)

# 참고 : @tf.function 안에서 if, for, while, break, continue, return 등을 사용하면 autograph가 개입함.

print()
# 반복문 처리
@tf.function
def calcFunc2(n):
    hap = tf.constant(0)
    for i in tf.range(n):
        hap += i
    return hap
print('hap : ', calcFunc2(10)) # hap :  tf.Tensor(45, shape=(), dtype=int32)

print()
imsi = tf.constant(0)
@tf.function
def calcFunc3():    # 1부터 3까지 증가
    # imsi = tf.constant(0) # 가능함
    global imsi # imsi가 local이 아님을 알림
    su = 1
    for _ in range(3):
        # imsi = imsi + su # 파이썬 연산자(비추천)
        imsi = tf.add(imsi, su) # 텐서 연산자(권장)

    return imsi
print('imsi : ', calcFunc3())   # imsi :  tf.Tensor(3, shape=(), dtype=int32)

print("\n구구단 3단 출력")
@tf.function
def calcFunc4(dan):
    for i in range(1, 10):
        result = tf.multiply(dan, i)

        tf.print(dan, '*', i, '=', result)

calcFunc4(3)