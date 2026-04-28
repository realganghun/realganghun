# naive-Bayes' algorithm을 이용한 분류 - weather.csv

import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/weather.csv")
print(df.head(2))
print(df.info())

# 전처리
df = df.drop('Date', axis=1)
df['Sunshine'] = df['Sunshine'].fillna(df['Sunshine'].mean()) # 결측치 처리

# 범주형 처리
df['RainToday'] = df['RainToday'].map({'Yes':1, 'No':0})
df['RainTomorrow'] = df['RainTomorrow'].map({'Yes':1, 'No':0})
print(df.head(2))

x = df.drop('RainTomorrow', axis=1) # feature
y = df['RainTomorrow'] # label

# train / test 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# Naive Bayes 모델 학습
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB # 연속형은 Gaussian
model = GaussianNB()
model.fit(x_train, y_train)

# 예측 및 평가
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
pred = model.predict(x_test)
print('분류 정확도 : ', accuracy_score(y_test, pred)) # 분류 정확도 :  0.8783783783783784
print('confusion_matrix : \n', confusion_matrix(y_test, pred))
# confusion_matrix : 
#  [[55  6]
#  [ 3 10]]

# 교차 검증
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, x, y, cv=5)
print(f'교차 검증 결과에서 각 fold : {scores}, 평균 : {scores.mean()}')
# 교차 검증 결과에서 각 fold : [0.72972973 0.82191781 0.79452055 0.8630137  0.83561644], 평균 : 0.8089596445760829

print()
# feature 중요도 분석
# feature가 정규분포를 따른다는 가정하에 클래스별 평균
# GaussianNB의 멤버로 theta_가 있음. -> 각 클래스별 feature 평균을 구해줌
mean_0 = model.theta_[0] # RainTomorrow가 0인 경우(비가 안온 날)의 평균
mean_1 = model.theta_[1] # RainTomorrow가 1인 경우(비가 온 날)의 평균

# 각 feature가 '비가 온 날 vs 비가 안온 날'에서 얼마나 차이가 나는지
importance = np.abs(mean_1 - mean_0) 

feat_imp = pd.DataFrame({'feature' : x.columns,
                        'importance' : importance
                        }).sort_values(by='importance', ascending=False)
print('feature 중요도 : \n', feat_imp)

# importance에 대한 시각화
import matplotlib.pyplot as plt
import koreanize_matplotlib

plt.figure()
plt.bar(feat_imp['feature'], feat_imp['importance'])
plt.xlabel('feature')
plt.ylabel('중요도(평균 차이)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print('새로운 자료로 예측')
new_data = pd.DataFrame([{
    'MinTemp': 10,
    'MaxTemp': 30,
    'Rainfall': 2.7,
    'Sunshine': 12,
    'WindSpeed': 15,
    'Humidity': 60,
    'Pressure': 1035,
    'Cloud':3,
    'Temp':20.0,
    'RainToday':0
}])

new_pred = model.predict(new_data)
print('예측 결과 : ', '비 옴' if new_pred==1 else '비 안옴')
print('확률은 ', model.predict_proba(new_data)) # [9.99535033e-01 4.64967194e-04] 비 안올 확률(0) : 99.9%