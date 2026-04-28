# kaggle의 Santander Customer satisfaction dataset 사용
# Santander 은행의 고객만족 여부 분류 처리
# 클래스(label)명은 target이고 0:만족, 1:불만족

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from xgboost import plot_importance
from sklearn.model_selection import train_test_split

# pd.set_option('display.max_columns', None) # dataframe의 모든 column 보이게 하기

df = pd.read_csv('train_san.csv', encoding='latin-1')
# print(df.head(2)) 
# print(df.shape) #(76020, 371)
# print(df.info()) # dtypes: float64(111), int64(260)

# 전체 데이터에서 만족과 불만족의 비율
print(df['TARGET'].value_counts()) # 0(만족) : 73012 \ 1(불만족) : 3008
unsatisfied_cnt = df[df['TARGET'] == 1].TARGET.count()
total_cnt = df.TARGET.count()
print(f'불만족 비율은 {unsatisfied_cnt / total_cnt}') # 불만족 비율은 0.0395685345961589

print(df.describe()) # feature의 분포 확인. var3 : outlier 존재.
df['var3'].replace(-999999, 2, inplace=True)
df.drop('ID', axis=1, inplace=True) # ID는 식별자이므로 제거
print(df.describe())

# feature / label 분리 작업 필요
x_features = df.iloc[:, :-1]
y_label = df.iloc[:, -1]
print('x_features shape : ', x_features.shape) # (76020, 369)
print('y_label shape : ', y_label.shape) # (76020,)

# train / test split
x_train, x_test, y_train, y_test = train_test_split(x_features, y_label, test_size=0.2, random_state=0)
train_cnt = y_train.count() # 60816
test_cnt = y_test.count() # 15204
# print(train_cnt, test_cnt)
print(x_train.shape, x_test.shape) #(60816, 369) (15204, 369)
print('학습데이터 레이블 값 분포 비율 : ', y_train.value_counts() / train_cnt)
# 학습데이터 레이블 값 분포 비율 :  TARGET
# 0    0.960964
# 1    0.039036
# Name: count, dtype: float64
print('검증데이터 레이블 값 분포 비율 : ', y_test.value_counts() / test_cnt)
# 검증데이터 레이블 값 분포 비율 :  TARGET
# 0    0.9583
# 1    0.0417
# Name: count, dtype: float64

# 1. 모델 생성 시 조기 종료와 평가 지표를 미리 설정합니다.
xgb_clf = XGBClassifier(
    n_estimators=5, 
    # early_stopping_rounds=2, # 생성자로 이동,  # early_stopping_rounds : 조기 종료
    # eval_metric='auc'        # 오타 수정 및 생성자로 이동
)

# 2. fit()에서는 학습 데이터와 검증용 데이터셋(eval_set)만 넣어줍니다.
xgb_clf.fit(
    x_train, y_train, 
    eval_set=[(x_train, y_train), (x_test, y_test)]
)
xgb_roc_score = roc_auc_score(y_test, xgb_clf.predict_proba(x_test)[:, 1])
print(f'xgb_roc_score : {xgb_roc_score:.5f}') # xgb_roc_score : 0.83389

pred = xgb_clf.predict(x_test)
print('예측값 : ', pred[:5])            # 예측값 :  [0 0 0 0 0]
print('실제값 : ', y_test[:5].values)   # 실제값 :  [0 0 0 0 0]

from sklearn import metrics
print('분류 정확도 : ', metrics.accuracy_score(y_test, pred)) # 분류 정확도 :  0.9583004472507235

# 최적의 parameter 구하기
print()
params = {'max_depth' : [5, 7], 'min_child_weight' : [1, 3], 'colsample_bytree' : [0.5, 0.75]}
# max_depth : 트리 깊이, min_child_weight : 관측치 가중치 합의 최소, colsample_bytree : feature 비율

gridcv = GridSearchCV(xgb_clf, param_grid=params)
gridcv.fit(x_train, y_train, eval_set=[(x_train, y_train), (x_test, y_test)])
print('gridcv 최적의 파라미터 : ', gridcv.best_params_)
# gridcv 최적의 파라미터 :  {'colsample_bytree': 0.5, 'max_depth': 5, 'min_child_weight': 3}
xgb_roc_score = roc_auc_score(y_test, gridcv.predict_proba(x_test)[:,1], average='macro')
# 매크로 평균(Macro-average)은 클래스별 지표를 먼저 계산한 후 산술 평균을 내는 방식(모든 클래스 동일 가중치)이며, 
# 마이크로 평균(Micro-average)은 전체 데이터의 TP/FP/FN 수를 합쳐 계산하는 방식(샘플 수 비례)
print(f'xgb_roc_score : {xgb_roc_score:.5f}') # xgb_roc_score : 0.82045

print() # 위 파라미터로 모델 생성
xgb_clf2 = XGBClassifier(n_estimator = 5, random_state = 12, max_depth=5, min_child_weight=3, colsample_bytree=0.5)
xgb_clf2.fit(
    x_train, y_train, 
    eval_set=[(x_train, y_train), (x_test, y_test)]
)
xgb_roc_score2 = roc_auc_score(y_test, xgb_clf2.predict_proba(x_test)[:, 1], average='macro')
print(f'xgb_roc_score2 : {xgb_roc_score2:.5f}') # xgb_roc_score2 : 0.83222

pred2 = xgb_clf2.predict(x_test)
print('예측값 : ', pred2[:5])            # 예측값 :  [0 0 0 0 0]
print('실제값 : ', y_test[:5].values)   # 실제값 :  [0 0 0 0 0]
print('분류 정확도 : ', metrics.accuracy_score(y_test, pred2)) # 분류 정확도 :  0.9577084977637463

# 중요 feature 시각화
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
plot_importance(xgb_clf2, ax=ax, max_num_features=20)
plt.show()