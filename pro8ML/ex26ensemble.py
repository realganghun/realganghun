import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# 앙상블 학습을 위한 보팅 분류기 및 개별 모델 로드
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from collections import Counter
import numpy as np

# 1. 유방암 데이터셋 로드
cancer = load_breast_cancer()
print(cancer.keys()) # 데이터셋의 구성 요소 확인 (data, target, feature_names 등)

# 2. 피처 데이터(x)와 타겟 레이블(y) 분리
x, y = cancer.data, cancer.target
print(x[:2]) # 첫 2개 샘플의 수치 데이터 출력
print(y[:2]) # 첫 2개 샘플의 정답(0 또는 1) 출력

# 3. 클래스 종류 확인 (0: 악성(Malignant), 1: 양성(Benign))
print('diagnosis(y) : ', np.unique(y)) 

# 4. 클래스별 데이터 분포 확인
counter = Counter(y) # 각 클래스(0, 1)별 개수 계산
total = sum(counter.values()) # 전체 데이터 개수 합산

for cls, cnt in counter.items():
    # 문제의 부분 수정: .2f%% 로 써야 % 기호가 출력됩니다.
    print(f'class {cls}:{cnt}개 ({100 * cnt / total:.4f}%)')

print()
x_train , x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12, stratify=y)
# stratify : train/test 비율 유지(불균형 데이터 모델 평가 시 왜곡방지)
y_li = y.tolist()
ytr_li = y_train.tolist()
yte_li = y_test.tolist()
print('전체 분포 : ', Counter(y_li))        #전체 분포 :  Counter({1: 357, 0: 212})
print('train 분포 : ', Counter(ytr_li))     #train 분포 :  Counter({1: 285, 0: 170})
print('test 분포 : ', Counter(yte_li))      #test 분포 :  Counter({1: 72, 0: 42})

print()
# 개별 모델
# make_pipeline : 전처리와 모델을 일체형 객체로 관리
logi = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, solver='lbfgs', random_state=12))

knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))

tree = DecisionTreeClassifier(max_depth=5, random_state=12)

# 앙상블 모델
voting = VotingClassifier(estimators=[('LR', logi), ('KNN', knn), ('DT', tree)], voting='soft')

# 개별 모델 성능 확인
named_models = [('LR', logi), ('KNN', knn), ('DT', tree)]
for name, clf in named_models:
    clf.fit(x_train, y_train)
    pred = clf.predict(x_test)
    print(f'{name} 정확도 : {accuracy_score(y_test, pred):.4f}')

# 5. 보팅 모델 학습 (앙상블 모델 자체를 학습시켜야 합니다)
voting.fit(x_train, y_train)

# 6. 보팅 모델로 예측값(vpred) 생성
# classification_report와 confusion_matrix에서 사용할 '예측 라벨'입니다.
vpred = voting.predict(x_test)

# 7. 보팅 모델의 최종 정확도 출력
print(f'Voting 최종 정확도 : {accuracy_score(y_test, vpred):.4f}')

# 선택 : 교차검증으로 안정성 확인
cvfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)
cv_score = cross_val_score(voting, x, y, cv=cvfold, scoring='accuracy')
print(f'보팅 5겹 cv 정확도 평균 : {cv_score.mean():.4f} (표준편차 : +={cv_score.std():.4f})')

print()
# 모델 성능 지표
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
print('\n 보팅 모델 상세 평가')
print(classification_report(y_test, vpred))
print('confusion_matrix : \n', confusion_matrix(y_test, vpred))
print('roc_auc_score : \n', roc_auc_score(y_test, voting.predict_proba(x_test)[:, 1]))