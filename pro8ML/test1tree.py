# 이하 소스 코드를 적으시오.
# 1) train_test_split (7:3), random_state=12
# 2) 의사결정나무 클래스를 사용해 분류 모델 작성
# 3) 예측결과로 분류 정확도를 출력

from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/titanic_data.csv', usecols=['Survived', 'Pclass', 'Sex', 'Age','Fare'])
print(data.head(2), data.shape)    # (891, 12)
data['Sex'] = data['Sex'].replace(['male', 'female'], [0, 1])
print(data["Sex"].head(2))
print(data.columns)

feature = data[["Pclass", "Sex", "Age", "Fare"]]
label = data["Survived"]

x_train, x_test, y_train, y_test = train_test_split(feature, label, test_size=0.3, random_state=12)

model = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
model.fit(x_train, y_train)

# 모델 성능 점수
pred = model.predict(x_test)
print('실제결과 : ', y_test)

print("분류 정확도 확인1")
print(f"{accuracy_score(y_test, pred)}")