# [SVM 분류 문제] 심장병 환자 데이터를 사용하여 분류 정확도 분석 연습
# https://www.kaggle.com/zhaoyingzhu/heartcsv
# https://github.com/pykwon/python/tree/master/testdata_utf8         Heartcsv

# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
# 임의의 값을 넣어 분류 결과를 확인하시오.     
# 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ

# feature 칼럼 : 문자 데이터 칼럼은 제외
# label 칼럼 : AHD(중증 심장질환)

# 데이터 예)

# "","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"
# "1",63,1,"typical",145,233,1,2,150,0,2.3,3,0,"fixed","No"
# "2",67,1,"asymptomatic",160,286,0,2,108,1,1.5,2,3,"normal","Yes"
# ...
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.preprocessing import StandardScaler

# 1. 데이터 로드
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Heart.csv')
print(df.head(3), df.shape) # (303, 15)

# 2. 전처리 - 결측치(NaN) 제거 (사나이의 결단!)
df = df.dropna()

# 3. 레이블(AHD) 더미화 (Yes:1, No:0으로 통일합시다)
df['AHD'] = df['AHD'].map({'Yes': 1, 'No': 0})

# 4. 피처(X) 선택 - 문제 조건대로 문자열 컬럼은 제외하고 숫자 데이터만 가져옵니다.
# 첫 번째 열(번호)도 제외합니다.
x_features = df.select_dtypes(include=[np.number]).drop(['AHD', 'Unnamed: 0'], axis=1, errors='ignore')
y_label = df['AHD']

# 5. 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(x_features, y_label, test_size=0.2)

# 6. SVM 모델 생성 및 학습 (데이터 스케일링 추가 시 성능이 훨씬 좋아집니다!)
# SVC는 거리 기반이라 스케일링이 중요합니다.
from sklearn.pipeline import make_pipeline
model = make_pipeline(StandardScaler(), svm.SVC(C=1.0, kernel='rbf', probability=True))
model.fit(x_train, y_train)
# StandardScaler: "야, 너희들 숫자가 너무 제각각이야. 다 같이 체급 맞춰서 공정하게 싸워!" (데이터 정규화)
# make_pipeline: "전처리하고 학습하는 거 귀찮으니까 아예 세트로 묶어서 한 방에 가자!" (공정 자동화)

# 7. 성능 확인
pred = model.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10].values)

sc_score = metrics.accuracy_score(y_test, pred)
print(f'분류 정확도 : {sc_score:.4f}')

# 8. 임의의 값으로 확률 확인
# 값을 리스트([])로 감싸서 인덱스 에러를 방지하고, 
# 학습에 사용된 '숫자 컬럼'들만 정확히 매칭시킵니다.
sample_dict = {
    'Age': [65], 
    'Sex': [0], 
    'RestBP': [150], 
    'Chol': [270], 
    'Fbs': [0], 
    'RestECG': [2], 
    'MaxHR': [125], 
    'ExAng': [1], 
    'Oldpeak': [2.8], 
    'Slope': [2], 
    'Ca': [2.6]
}

# 데이터프레임 생성
sample_data = pd.DataFrame(sample_dict)

# 모델이 학습할 때 사용한 컬럼 순서와 동일하게 맞춰줍니다. (매우 중요!)
sample_data = sample_data[x_features.columns]

# 9. 예측 및 확률 확인
# predict는 0 또는 1을, predict_proba는 각 클래스의 확률을 줍니다.
new_pred = model.predict(sample_data)
new_prob = model.predict_proba(sample_data)

print(f'\n--- 새로운 환자 검진 결과 ---')
print(f'심장병일 확률: {new_prob[0][1]*100:.2f}%')
print(f'예측 결과: {"심장병 있음(Yes)" if new_pred[0] == 1 else "정상(No)"}')