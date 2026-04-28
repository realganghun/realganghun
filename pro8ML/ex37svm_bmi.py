# BMI(Body Mass Index)는 체질량지수로, 몸무게(kg)를 키의 제곱(m²)으로 나눈 값을 뜻합니다. 
# 키와 몸무게로 체지방량을 추정하여 비만도를 간편하게 측정하는 지표
# ex) 키 : 173cm, 몸무게 : 65kg --> 65 / (1.73)²

import random
random.seed(12)

# print(65/(1.73)**2)

# def calc_bmiFunc(h, w):
#     bmi = w / (h/100)**2
#     if bmi < 18.5 : return 'thin'
#     if bmi < 25.0 : return 'normal'
#     return 'fat'

# print(calc_bmiFunc(170, 68))

# fp = open('bmi.csv', mode='w')
# fp.write('height,weight,label\n') # 제목

# # 무작위 데이터 생성
# cnt = {'thin' : 0, 'normal' : 0, 'fat' : 0}
# for i in range(50000):
#     h = random.randint(150, 200)
#     w = random.randint(35, 100)
#     label = calc_bmiFunc(h, w)
#     cnt[label] += 1
#     fp.write('{0}, {1}, {2}\n'.format(h,w,label))
# fp.close()

# bmi data를 SVM으로 분류
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bmi.csv')
print(df.head(2), df.shape) #(50000, 3)
print(df.info())

# ... (데이터 로드 부분)
df = pd.read_csv('bmi.csv')

# 컬럼명 공백 제거 (혹시 모르니 실행)
df.columns = df.columns.str.strip()

# 데이터(글자) 공백 제거 ★이 코드가 핵심입니다!
df['label'] = df['label'].str.strip()

label = df['label']
print(label[:2])

w = df['weight'] / 100 # 정규화
print(w[:2].values)

h = df['height'] / 200 # 정규화
print(h[:2].values)

wh = pd.concat([w, h], axis=1)
print(wh.head(2))

# label은 dummy화
label = label.map({'thin':0, 'normal':1, 'fat':2})
print(label[:5])

x_train, x_test, y_train, y_test = train_test_split(wh, label, test_size=0.3, random_state=1)
print(x_train.shape, x_test.shape) # (35000, 2) (15000, 2)

# model
model = svm.SVC(C=0.01, kernel='rbf').fit(x_train, y_train)
print(model)

pred = model.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10].values)

sc_score = metrics.accuracy_score(y_test, pred)
print('sc_score : ', sc_score) # 0.9705333333333334

# 교차 검증
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, wh, label, cv=3)
print('3회 각 정확도 : ', cross_vali) # [0.96940061 0.96586068 0.96681867]
print('평균 정확도 : ', cross_vali.mean()) # 0.9673599891736715

# 새로운 값으로 예측
new_data = pd.DataFrame({'weight':[66,88], 'height':[188, 160]})
new_data['weight'] = new_data['weight'] / 100
new_data['height'] = new_data['height'] / 200
new_pred = model.predict(new_data)
print('새로운 값 예측 결과 : ', new_pred) # [1 2]

# 시각화
df2 = pd.read_csv('bmi.csv', index_col=2)
df2.index = df2.index.str.strip()
def scatterFunc(lbl, color):
    b = df2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label=lbl)

plt.figure(figsize=(8, 6)) # 그래프 크기 조절 (선택)
scatterFunc('fat', 'red')
scatterFunc('normal', 'yellow')
scatterFunc('thin', 'blue')
plt.xlabel('weight')
plt.ylabel('height')
plt.title('BMI Visualization')
plt.legend()
plt.show()