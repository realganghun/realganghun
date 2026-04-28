# # RandomForest 분류 알고리즘
# 랜덤 포레스트(Random Forest)는 여러 개의 결정 트리(Decision Tree)를 훈련하여 그 결과를 종합(투표)해 분류하는 앙상블 학습 알고리즘입니다. 
# 부트스트랩(무작위 데이터 추출)과 배깅(Bagging) 기법을 활용해 과적합(Overfitting)을 줄이고, 일반화 성능과 예측 정확도를 높인 것이 핵심입니다. 

# 랜덤 포레스트 주요 특징 및 동작 원리
# 앙상블 기반 분류: 다수의 의사결정 나무를 생성하고, 개별 나무들의 투표 결과 중 가장 많은 득표를 받은 카테고리로 최종 분류합니다.
# 부트스트랩 (Bootstrapping): 전체 데이터셋에서 복원 무작위 추출을 통해 여러 개의 작은 데이터셋을 만들어 각 나무를 학습시킵니다.
# 특성 무작위 선택: 트리의 노드를 분할할 때 전체 특성(Feature) 중에서 일부만 무작위로 선택하여 최적의 분할을 찾습니다. 
# 이 방식은 나무 간의 상관관계를 낮춰 모델의 다양성을 확보합니다.
# 장점: 대용량 데이터에서 성능이 우수하고, 의사결정 나무의 과적합 문제를 해결하며, 어떤 변수가 중요한지(Feature Importance) 파악할 수 있습니다. 

# 핵심 매개변수 (Hyperparameters)
# n_estimators: 숲을 구성할 나무의 수로, 많을수록 성능이 우수할 수 있으나 학습 시간이 증가합니다.
# max_depth: 각 트리의 최대 깊이로, 모델의 과적합을 방지하기 위해 설정합니다. 

# 주로 파이썬의 scikit-learn 라이브러리를 사용하여 구현하며, 복잡한 데이터에서도 높은 정확도를 보여 분류 문제에서 매우 선호되는 알고리즘입니다.

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/titanic_data.csv')
print(df.head(2))
print(df.info())
print(df.shape) #(891, 12)
print(df.isnull().any())
df = df.dropna(subset=['Pclass', 'Age', 'Sex'])
print(df.shape) #(714, 12)


# 전처리
df_x = df[['Pclass', 'Age', 'Sex']] #feature
print(df_x.head())
# Sex 열 : Label Encoding(문자 범주형 - 정수형)
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df_x['Sex'] = encoder.fit_transform(df_x['Sex'])
print(df_x.head()) # female : 0, male : 1

df_y = df['Survived'] # label(class)
print(df_y.head()) # 0 : 사망, 1 : 생존

print()
x_train , x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.3, random_state=12)
print(x_train.shape , x_test.shape, y_train.shape, y_test.shape) #(499, 3) (215, 3) (499,) (215,)

# 모델 생성
model = RandomForestClassifier(criterion='gini', n_estimators=500, random_state=12)

# n_estimators : 결정트리 수
model.fit(x_train, y_train)
pred = model.predict(x_test)
print('예측값 : ', pred[:5])
print('실제값 : ', np.array(y_test[:5]))
print('맞춘 갯수 : ', sum(y_test == pred))
print('전체 대비 맞춘 비율 : ', sum(y_test == pred)/len(y_test))
print('분류 정확도 : ', accuracy_score(y_test, pred))