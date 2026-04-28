# 재색인
from pandas import Series, DataFrame

# Series의 재색인
data = Series([1, 3, 2], index=(1, 4, 2))
print(data)
data2 = data.reindex((1,2,4))
print(data2)

print('\n재색인 할 때 값 채워넣기')
data3 = data2.reindex([0,1,2,3,4,5])
print(data3)

# fill_value : 대응값이 없는 index에는 특정 값으로 채움
data3 = data2.reindex([0,1,2,3,4,5], fill_value=777)
print(data3)

print('---'*10)
# NaN앞 값으로 NaN을 채움
data3 = data2.reindex([0,1,2,3,4,5], method='ffill') #NaN의 앞 index의 값으로 NaN을 채움
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='pad') #NaN의 뒤 index의 값으로 NaN을 채움
print(data3)

# NaN뒤 값으로 NaN을 채움
data3 = data2.reindex([0,1,2,3,4,5], method='bfill') #NaN의 앞 index의 값으로 NaN을 채움
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='backfill') #NaN의 뒤 index의 값으로 NaN을 채움
print(data3)

print('---'*10)
print('\nDataFrame : bool처리')
import numpy as np
df = DataFrame(np.arange(12).reshape(4,3), index=['1월','2월','3월','4월'], columns=['강남','강북','서초'])
print(df)

print(df['강남']) # -> 강남 column만 나옴.
print(df['강남']>3)
print(df[df['강남']>3])

print(df < 3)
df[df<3] = 0 
print(df)

print('\n슬라이싱 관련 메소드 : loc() : label지원, iloc() : 숫자 지원')
print(df.loc['3월', :]) #3월 행의 모든 값
print(df.loc[:'2월']) #2월 이하 모든 값
print(df.loc[:'2월',['서초']])
print()
print(df.iloc[2])
print(df.iloc[:2])