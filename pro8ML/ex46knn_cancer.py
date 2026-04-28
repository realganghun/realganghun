# 최근접 이웃(K-Nearest Neighbors) - breast_cancer dataset 사용

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
x = data.data   # feature
y = data.target # label (0 : malignant, 1 : benign)

print(x[:3], x.shape)   # (569, 30)
print(y[:3], np.unique(y))   # [0 1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# Scaling 필수! (∵거리기반 모델이므로 크기가 영향을 미침)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# K-NN은 k값이 중요하다!
# k값 변황에 따른 정확도 비교로 최적의 k값 얻기
# k값이 작으면 과적합, k값이 크면 과소적합 -> 적당한 k값 찾는게 중요
train_acc = []
test_acc = []
k_range = range(3, 12)
for k in k_range:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train_scaled, y_train)

    # 예측
    y_train_pred = model.predict(x_train_scaled)
    y_test_pred = model.predict(x_test_scaled)
    # 정확도
    train_acc.append(accuracy_score(y_train, y_train_pred))
    test_acc.append(accuracy_score(y_test, y_test_pred))

# 시각화
import matplotlib.pyplot as plt
import koreanize_matplotlib

plt.figure()
plt.plot(k_range, train_acc, marker='o', label='Train acc')
plt.plot(k_range, test_acc, marker='s', label='test acc')
plt.xlabel('k value')
plt.ylabel('accuracy')
plt.title('knn acc comparison')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
# 그래프 기준으로 최적은 k=3
# test acc가 가장 크게 나옴.
# 4는 불안, 7 ~ 9가 안정적

best_k = k_range[np.argmax(test_acc)]
print('최적의 k : ', best_k)
# k=9일때 train, test가 맞닿아있기 때문에 9가 최적의 k값. 3은 과적합 우려

# 최종 모델 작성
best_k = 9
final_model = KNeighborsClassifier(n_neighbors=best_k)
final_model.fit(x_train_scaled, y_train)

# 성능 확인
y_pred = final_model.predict(x_test_scaled)
print('final_model 분류 정확도 : ', accuracy_score(y_test, y_pred))
print('분류 보고서 : \n', classification_report(y_test, y_pred))
print('Confusion Matrix : \n', confusion_matrix(y_test, y_pred))

# 새로운 자료로 예측
new_data = x[0].copy()
new_data = new_data + np.random.normal(0, 0.1, size=new_data.shape)
new_data_scaled = scaler.transform([new_data]) #Scaling
prediction = final_model.predict(new_data_scaled)
proba = final_model.predict_proba(new_data_scaled)
print('새로운 데이터 예측 결과')
print('예측 결과 : ', prediction[0], '(0 : 악성, 1 : 양성)')
print('확률 : ', proba)