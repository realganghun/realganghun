# SVM으로 AND, OR, XOR 연산 처리하기

x_data = [      # and 연산
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

x_data2 = [      # or 연산
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

x_data3 = [      # xor 연산
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

# features, label 분리
# feature = []
# label = []
# for row in x_data:
#     p = row[0]
#     q = row[1]
#     r = row[2]
#     feature.append([p, q])
#     label.append(r)

# print(feature)
# print(label)

x_df = pd.DataFrame(x_data3)
feature = np.array(x_df.iloc[:, 0:2])
label = np.array(x_df.iloc[:, 2])
print(feature)
print(label)

lmodel = LogisticRegression() # 선형 분류 모델
smodel = svm.SVC() # 선형 / 비선형 분류 모델

lmodel.fit(feature, label)
smodel.fit(feature, label)

pred1 = lmodel.predict(feature)
print('lmodel 예측값 : ', pred1)

pred2 = smodel.predict(feature)
print('smodel 예측값 : ', pred2)

acc1 = metrics.accuracy_score(label, pred1)
print('lmodel 분류 정확도 : ', acc1)

acc2 = metrics.accuracy_score(label, pred2)
print('smodel 분류 정확도 : ', acc2)