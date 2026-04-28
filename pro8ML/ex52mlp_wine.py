# MLP - wine dataset으로 다항분리

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_wine()
# print(dataset.DESCR)

x = data.data
y = data.target
print(x[:2], ' ', x.shape) #(178, 13)
print(y[:2], ' ', y.shape, ' ', np.unique(y)) #(178,) / [0 1 2]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# 정규화(MLP는 Scaling을 권장함)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# 모델 생성
model = MLPClassifier(
    hidden_layer_sizes=(20, 10),    # hidden layer 2개
    activation='relu',              # 활성화 함수
    solver='adam',                  # 손실 최소화 함수 지정
    learning_rate_init=0.001,       # 학습률
    max_iter=150,                    # 학습 횟수
    random_state=42,
    verbose=1                       # 학습 도중 로그 출력 여부(0이면 출력 x)
)

model.fit(x_train_scaled, y_train)
pred = model.predict(x_test_scaled)
print('분류 정확도 : ', accuracy_score(y_test, pred))
print('classification_report \n', classification_report(y_test, pred))

# 혼동행렬 시각화
cm = confusion_matrix(y_test, pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('혼동 행렬')
plt.xlabel('predicted(예측값)')
plt.ylabel('actual(실제값)')
plt.show()

# train loss curve 시각화
plt.plot(model.loss_curve_)
plt.title('train loss curve')
plt.xlabel('iteration(epoch)')
plt.ylabel('loss')      # 예측값과 실제값의 차이
plt.show()

# 참고 : 미분이 MLP에서 어떻게 쓰이는가? -> 미분으로 오차를 줄여나감
# MLP 구조 : 입력 -> 신경망(Neuron) -> 출력 후 오차를 확인
# 예) 입력(x) -> 모델 -> [예측(y^) - 실제값(y)] -> 오차(loss) 발생
# 오차함수(loss function)는 L = (y - y^) 예측이 틀릴수록 값이 커지겠지
# 미분을 쓰는 이유? : 오차를 어떻게 줄일지. 즉, 오차가 줄어드는 방향으로 w를 갱신
# 전체 학습과정을 보면
# 1. 모델이 예측 -> 2. 오차 계산 -> 3. 미분(기울기 계산) -> 4. 가중치 w 갱신
# 5. (1~4) 과정 반복 - 역전파(back propergation)
# >> MLP
