# [GaussanNB 문제] 
# 독버섯(poisonous)인지 식용버섯(edible)인지 분류
# https://www.kaggle.com/datasets/uciml/mushroom-classification
# feature는 중요변수를 찾아 선택, label:class
# 참고 : from xgboost import plot_importance


# 데이터 변수 설명 : 총 23개 변수가 사용됨.

# 여기서 종속변수(반응변수)는 class 이고 나머지 22개는 모두 입력변수(설명변수, 예측변수, 독립변수).
# 변수명 변수 설명
# class      edible = e, poisonous = p
## cap-shape    bell = b, conical = c, convex = x, flat = f, knobbed = k, sunken = s
# cap-surface  fibrous = f, grooves = g, scaly = y, smooth = s
# cap-color     brown = n, buff = b, cinnamon = c, gray = g, green = r, pink = p, purple = u, red = e, white = w, yellow = y
## bruises        bruises = t, no = f
# odor            almond = a, anise = l, creosote = c, fishy = y, foul = f, musty = m, none = n, pungent = p, spicy = s
# gill-attachment attached = a, descending = d, free = f, notched = n
# gill-spacing close = c, crowded = w, distant = d
# gill-size       broad = b, narrow = n
# gill-color      black = k, brown = n, buff = b, chocolate = h, gray = g, green = r, orange = o, pink = p, purple = u, red = e, white = w, yellow = y
## stalk-shape  enlarging = e, tapering = t
# stalk-root    bulbous = b, club = c, cup = u, equal = e, rhizomorphs = z, rooted = r, missing = ?
## stalk-surface-above-ring fibrous = f, scaly = y, silky = k, smooth = s
# stalk-surface-below-ring fibrous = f, scaly = y, silky = k, smooth = s
## stalk-color-above-ring brown = n, buff = b, cinnamon = c, gray = g, orange = o, pink = p, red = e, white = w, yellow = y
## stalk-color-below-ring brown = n, buff = b, cinnamon = c, gray = g, orange = o,pink = p, red = e, white = w, yellow = y
# veil-type      partial = p, universal = u
# veil-color     brown = n, orange = o, white = w, yellow = y
# ring-number none = n, one = o, two = t
## ring-type     cobwebby = c, evanescent = e, flaring = f, large = l, none = n, pendant = p, sheathing = s, zone = z
# spore-print-color black = k, brown = n, buff = b, chocolate = h, green = r, orange =o, purple = u, white = w, yellow = y
# population abundant = a, clustered = c, numerous = n, scattered = s, several = v, solitary = y
# habitat       grasses = g, leaves = l, meadows = m, paths = p, urban = u, waste = w, woods = d

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/mushrooms.csv")
print(df.head(3))
print(df.info())

# 전처리
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for col in df.columns:
    df[col] = encoder.fit_transform(df[col])

print(df.head())
x = df.drop('class', axis=1) # feature
y = df['class'] # label

# train / test 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 중요 변수 찾기
import matplotlib.pyplot as plt
from xgboost import XGBClassifier, plot_importance
# XGBoost로 학습 후 어떤 변수가 '독' 판별에 기여도가 높은지 확인
xgb = XGBClassifier().fit(x_train, y_train)
plot_importance(xgb)
plt.tight_layout()
plt.show()

x_train_selected = x_train.drop(['cap-shape', 'bruises', 'stalk-shape', 'stalk-surface-above-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'ring-type'], axis=1)
x_test_selected = x_test.drop(['cap-shape', 'bruises', 'stalk-shape', 'stalk-surface-above-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'ring-type'], axis=1)
# 모델 생성
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(x_train_selected, y_train)

# 예측 및 평가
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
pred = model.predict(x_test_selected)
print('분류 정확도 : ', accuracy_score(y_test, pred)) # 분류 정확도 : 0.696
print('confusion_matrix : \n', confusion_matrix(y_test, pred))
#  [[387 433]
#  [ 61 744]]
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, x, y, cv=5)
print(f'교차 검증 결과에서 각 fold : {scores}, 평균 : {scores.mean()}')
# 교차 검증 결과에서 각 fold : [0.65538462 0.93169231 0.51384615 0.48492308 0.49445813]
# 평균 : 0.6160608563849943