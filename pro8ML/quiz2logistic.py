# [로지스틱 분류분석 문제2] 

# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression

# 1. 데이터 로드
data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/bodycheck.csv')
print(data.head(), ' ', data.shape)
#    번호  게임   신장  체중  TV시청  안경유무
# 0   1   2  146  34     2     0
# 1   2   6  169  57     3     1
# 2   3   9  160  48     3     1
# 3   4   1  156  38     2     0
# 4   5   4  181  87     1     0   (20, 6)

# 2. 독립변수(X)와 종속변수(y) 설정
x = data[['게임', 'TV시청']]
y = data['안경유무']

# 3. 모델 생성 (C값이 작을수록 규제가 강해져서 확률이 더 부드러워집니다)
# C=1.0이 기본값이며, 0.1이나 0.01로 줄이면 과적합을 방지합니다.
model = LogisticRegression(C=0.1, solver='lbfgs')
model.fit(x, y)

print("모델 학습 완료!")
print(f"기울기(가중치): {model.coef_}")
print(f"절편(편향): {model.intercept_}")

# 4. 새로운 데이터로 예측
while True:
    try:
        game = float(input("\n게임 시간 입력: "))
        tv = float(input("TV 시청 시간 입력: "))
        new_data = np.array([[game, tv]])
        
        # 확률 예측 (두 클래스 [0일 확률, 1일 확률]이 나옵니다)
        prob = model.predict_proba(new_data)
        
        # 최종 분류 결과 (0 또는 1)
        # np.rint를 써서 0.5 기준으로 사나이답게 반올림!
        pred = model.predict(new_data)
        
        print(f"안경 안 쓸 확률(0): {prob[0][0]:.4f}")
        print(f"안경 쓸 확률(1): {prob[0][1]:.4f}")
        print(f"최종 판정: {'안경 착용함' if pred[0] == 1 else '안경 안 씀'}")
        
        if input("계속할까요? (y/n): ").lower() != 'y': break
    except:
        print("숫자만 입력해 주세요.")