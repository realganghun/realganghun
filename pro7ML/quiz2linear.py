# 회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 
# : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용

# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량에 대한 데이터는 아래와 같다.
#  - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 운동 10시간 초과는 이상치로 한다.  


# 구분,지상파,종편,운동
# 1,0.9,0.7,4.2
# 2,1.2,1.0,3.8
# 3,1.2,1.3,3.5
# 4,1.9,2.0,4.0
# 5,3.3,3.9,2.5
# 6,4.1,3.9,2.0
# 7,5.8,4.1,1.3
# 8,2.8,2.1,2.4
# 9,3.8,3.1,1.3
# 10,4.8,3.1,35.0
# 11,NaN,3.5,4.0
# 12,0.9,0.7,4.2
# 13,3.0,2.0,1.8
# 14,2.2,1.5,3.5
# 15,2.0,2.0,3.5


import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import koreanize_matplotlib
import io

# 1. 데이터 생성
csv_data = """구분,지상파,종편,운동
1,0.9,0.7,4.2
2,1.2,1.0,3.8
3,1.2,1.3,3.5
4,1.9,2.0,4.0
5,3.3,3.9,2.5
6,4.1,3.9,2.0
7,5.8,4.1,1.3
8,2.8,2.1,2.4
9,3.8,3.1,1.3
10,4.8,3.1,35.0
11,NaN,3.5,4.0
12,0.9,0.7,4.2
13,3.0,2.0,1.8
14,2.2,1.5,3.5
15,2.0,2.0,3.5"""

df = pd.read_csv(io.StringIO(csv_data))

# 2. 전처리 (Preprocessing)
# (1) 결측치 처리: 지상파 칼럼의 평균값으로 대체
df['지상파'] = df['지상파'].fillna(df['지상파'].mean())

# (2) 이상치 제거: 운동 10시간 초과인 행 제거 (10번 행이 제거됨)
df = df[df['운동'] <= 10]
print("--- 전처리 후 데이터 ---")
print(df.head())

# --- 분석 1: 지상파 시청 시간 -> 운동 시간 예측 ---
print("\n[분석 1] 지상파 시청 시간 vs 운동 시간")

# 방법 1: scipy.stats.linregress (권장 방식)
slope, intercept, r_value, p_value, std_err = stats.linregress(df['지상파'], df['운동'])
print(f"회귀계수(기울기): {slope:.4f}, 절편: {intercept:.4f}")
print(f"상관계수: {r_value:.4f}, p-value: {p_value:.4f}")

# 예측 예시: 지상파 3시간 시청 시 운동 시간은?
new_jisang = 3.0
pred_exercise = slope * new_jisang + intercept
print(f"예측 결과: 지상파 {new_jisang}시간 시청 시 예상 운동 시간은 {pred_exercise:.2f}시간입니다.")

x = df.지상파
y = df.운동

plt.scatter(x,y)
plt.plot(x, slope*x+intercept, c='r')
plt.show()
# --- 분석 2: 지상파 시청 시간 -> 종편 시청 시간 예측 ---
print("\n[분석 2] 지상파 시청 시간 vs 종편 시청 시간")

# 방법 2: statsmodels ols
model = smf.ols(formula='종편 ~ 지상파', data=df).fit()
# ~ (물결표): "왼쪽(Y)은 오른쪽(X)에 의해 결정된다"는 뜻입니다.
# 종편 ~ 지상파:
# 왼쪽 (종편): 우리가 예측하고 싶은 결과값, 
# 즉 종속변수(Y)입니다.
# 오른쪽 (지상파): 원인이 되는 값, 즉 독립변수(X)입니다.
# 해석: "지상파 시청 시간이 종편 시청 시간에 어떤 영향을 주는지 모델을 만들어라(Y = aX + b)"라는 명령입니다.
print(model.summary()) # 요약 결과 중 계수 테이블만 출력

# --- [추가] 분석 2: statsmodels 시각화 ---
plt.scatter(df['지상파'], df['종편'], color='blue', label='실제 데이터')

# 모델의 예측값을 이용해 선 그리기 (predict 함수 활용)
plt.plot(df['지상파'], model.predict(df['지상파']), color='red', label='OLS 회귀선')

# 또는 직접 수식으로: y = model.params.지상파 * x + model.params.Intercept
plt.title('지상파 vs 종편 시청 시간 (statsmodels)')
plt.xlabel('지상파 시청 시간')
plt.ylabel('종편 시청 시간')
plt.legend()
plt.show()

# 방법 3: sklearn LinearRegression
# sklearn은 x를 2차원 배열로 넣어줘야 합니다.
x_sk = df[['지상파']]
y_sk = df['종편']
lr_model = LinearRegression().fit(x_sk, y_sk)

# 예측 예시: 지상파 5시간 시청 시 종편 시청 시간은?
pred_jongpyun = lr_model.predict([[5.0]])
print(f"예측 결과: 지상파 5시간 시청 시 예상 종편 시간은 {pred_jongpyun[0]:.2f}시간입니다.")

# --- [추가] 분석 2: sklearn 시각화 ---
plt.scatter(x_sk, y_sk, color='green', label='실제 데이터')

# lr_model.predict()를 사용하여 회귀선 그리기
plt.plot(x_sk, lr_model.predict(x_sk), color='orange', linewidth=2, label='Sklearn 회귀선')

# 속성 확인용 (참고)
# 기울기: lr_model.coef_[0], 절편: lr_model.intercept_

plt.title('지상파 vs 종편 시청 시간 (sklearn)')
plt.xlabel('지상파 시청 시간')
plt.ylabel('종편 시청 시간')
plt.legend()
plt.show()