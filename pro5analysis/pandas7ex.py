import pandas as pd
import numpy as np
# 1)

import pandas as pd
import numpy as np

df=pd.read_csv('titanic_data.csv')

bins=[1,20,35,60,150]
labels=["소년","청년","장년","노년"]
df['나이대']=pd.cut(df['Age'],bins=bins,labels=labels)
result=df.groupby('나이대',observed=True)['Survived'].sum()
result=result.reset_index()
result.columns=['나이대','생존자수']
print(result)
print()

# 2)
import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')

# 나이대 컬럼 생성
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
df['나이대'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 샘플1 
pivot1 = df.pivot_table(
    values='Survived',
    index='Sex',
    columns='Pclass',
    aggfunc='mean'
)
print(pivot1)
print()

# 샘플2 
pivot2 = df.pivot_table(
    values='Survived',
    index=['Sex', '나이대'],
    columns='Pclass',
    aggfunc='mean'
)
pivot2 = (pivot2 * 100).round(2)
print(pivot2)


df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/human.csv',skipinitialspace=True)
#skipinitialspace=True : '쉼표(,) 뒤에 따라오는 공백을 무시하고 데이터를 읽어라'라는 뜻
print(df)

df.columns = df.columns.str.strip() #데이터프레임의 '칼럼 이름(열 제목)'들에 붙어있는 불필요한 공백을 한꺼번에 싹 지워주는 아주 유용한 코드
# - Group이 NA인 행은 삭제
print(df.dropna(subset=["Group"]))

df1 = df.dropna(subset=["Group"])
# Career, Score 칼럼을 추출하여 데이터프레임을 작성
print(df1[['Career', 'Score']])
# Career, Score 칼럼의 평균계산
print(df1[['Career', 'Score']].mean())

# 2)
df3 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tips.csv")
print(df3.info())
print(df3.head(3))
print(df3.describe())
print(df3["smoker"].value_counts())
print(df3["day"].unique())