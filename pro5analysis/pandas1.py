# 고수준의 자료구조(Series, DataFame)와 빠르고 쉬운 데이터 분석용 함수 제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, SQL, 시각화 ... 등을 제공
# 데이터 랭글링, 데이터 멍잉을 효율적으로 처리 가능

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Series : 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인(index)을 갖는다.
#obj = pd.Series([3, 7, -5, 4])
obj = pd.Series([3, 7, -5, '뭐']) # 요소값은 object type.
#obj = pd.Series((3, 7, -5, 4))
#obj = pd.Series({3, 7, -5, 4}) #TypeError: 'set' type is unordered


print(obj, type(obj))

obj2 = pd.Series([3, 7, -5, 4], index =['a', 'b', 'c', 'd'])
print(obj2)
print(obj2.sum(), ' ', np.sum(obj2), ' ', sum(obj2)) #pandas의 sum(내부적으로 numpy의 sum을 씀), numpy의 sum, python의 sum

print(obj2.std()) #표준편차
print(obj2.values) #list로 보고싶으면 values사용

print(obj2.index)
print(obj2['a']) #a인덱스의 값
print(obj2[['a']]) #a인덱스와, 그 값

print(obj2[['a', 'b']]) #a, b인덱스와, 그 값

print(obj2['a':'c'])

print(obj2[1:4])
print(obj2.iloc[2]) #(Integer Location): 이름이 무엇이든 상관없이 '순서(0부터 시작)'로만 접근


print(obj2.iloc[[2,1,0]]) 
# 2번 위치에 있는 데이터(-5)를 먼저 가져온다.
# 1번 위치에 있는 데이터(7)를 그다음에 가져온다.
# 0번 위치에 있는 데이터(3)를 그다음에 가져온다.
# 이 두 데이터를 합쳐서 새로운 Series 형태로 반환한다.

print('a' in obj2)
print('k' in obj2)

print('파이썬 dict 자료를 Series 객체로 생성')
names = {'mouse' : 5000, 'keyboard' : 25000, 'monitor' : 450000}
print(names)
obj3 = Series(names) #key가 index, value가 series
print(obj3, ' ', type(obj3))
obj3.index=['마우스', '키보드', '모니터']
print(obj3, ' ', type(obj3))

obj3.name = "상품가격"
print(obj3)

print('\nDataFrame 객체 -----------------')
df = pd.DataFrame(obj3)
print(df, ' ', type(df))

data = {'irum' : ['홍길동', '한국인', '신대웅', '서지민', '개병신'],
        'juso' : ('역삼동', '신사동', '상일동', '군자동', '어린이대공원'),
        'nai' : [23, 25, 26, 26, 45]
        }
frame = pd.DataFrame(data)
print(frame)

print()
print(frame['irum'])
print(frame.irum)
print(type(frame.irum))

print(DataFrame(data=data, columns=['juso', 'irum', 'nai']))

#NaN(결측치)
frame2 = pd.DataFrame(data, columns=['irum', 'nai', 'juso', 'tel'],
                    index=['a','b','c','d','e'])
print(frame2)

frame2['tel'] = '111-1111'
print(frame2)

val = pd.Series(['222-2222', '333-3333', '444-4444'], index=['b','c','e'])
print(val)
frame2['tel'] = val
print(frame2)

print()
print(frame2.T) #전치

print()
print(frame2.values) #결과는 list type
print(frame2.values[0, 1]) # 0행 1열 출력 -> 23
print(frame2.values[0:2]) #0행, 1행 출력

frame3 = frame2.drop('d')
#frame3 = frame2.drop('d', axis=0) #행삭제
print(frame3)

frame4 = frame2.drop('tel' , axis=1) #열삭제
print(frame4)

print('-------------'*10)
print(frame2)
print(frame2.sort_index(axis=0, ascending=False)) #행 단위 정렬
print(frame2.sort_index(axis=1, ascending=True)) #열 단위 정렬

print(frame2.rank(axis=0)) #순위 매김

counts = frame2['juso'].value_counts()
print(counts)

#문자열 자르기
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon' : [23, 25, 15]
}
fr = pd.DataFrame(data)
print(fr)

result1 = Series([x.split()[0] for x in fr.juso])
result2 = Series([x.split()[1] for x in fr.juso])
print(result1)
print(result2)

print(result1.value_counts())