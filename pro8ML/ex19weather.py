# LogisticRegression 날씨 예보 (비 올지 여부)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/weather.csv")
print(data.head(2),data.shape)
data2 = pd.DataFrame()
data2 = data.drop(['Date','RainToday'], axis=1)
data2['RainTomorrow'] =data2['RainTomorrow'].map({'Yes':1,'No':0})
print(data2.head(2),data2.shape)
print(data2['RainTomorrow'].unique())

# RainTomorrow : 종속변수(범주형,label,class), 검증용(testdata)
# 데이터 분리: 학습용 / 검증용
# 모델 성능을 객관적으로 파악. 모델 학습과 검증에 사용된 자료가 같다면 오버피팅 우려 발생.
train, test = train_test_split(data2,test_size=0.3,random_state=42)
print(train.shape, test.shape)
print(train.head(3))
print(test.head(3))

# 모델 생성
col_select = "+".join(train.columns.difference(['RainTomorrow'])) # Cloud+Humidity+MaxTemp+MinTemp+Pressure+Rainfall+Sunshine+Temp+WindSpeed
print(col_select)

my_formula = 'RainTomorrow ~ ' + col_select
# model = smf.glm(formula=my_formula, data=train, family=sm.families.Binomial()).fit()
model = smf.logit(formula=my_formula, data=train).fit()
print(model.summary()) # p-value가 0.05 이상인거를 다 제거하는게 아니라, 각 행이 서로 영향을 줄 수도 있기 때문에 큰 값부터 제거함
print(model.params) # 기울기
print()
print("예측값 : ", np.rint(model.predict(test).values))
print("실제값 : ", test['RainTomorrow'].values)

# 분류 정확도
conf_met = model.pred_table()
print(conf_met)
print('분류 정확도 : ', (conf_met[0][0] + conf_met[1][1]) / len(train))
from sklearn.metrics import accuracy_score
pred = model.predict(test)
print('분류 정확도 : ', accuracy_score(test['RainTomorrow'], np.rint(pred)))