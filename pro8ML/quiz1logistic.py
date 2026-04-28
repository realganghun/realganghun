# [로지스틱 분류분석 문제1]

# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.

# 요일,외식유무,소득수준

# 토,0,57
# 토,0,39
# 토,0,28
# 화,1,60
# 토,0,31
# 월,1,42
# 토,1,54
# 토,1,65
# 토,0,45
# 토,0,37
# 토,1,98
# 토,1,60
# 토,0,41
# 토,1,52
# 일,1,75
# 월,1,45
# 화,0,46
# 수,0,39
# 목,1,70
# 금,1,44
# 토,1,74
# 토,1,65
# 토,0,46
# 토,0,39
# 일,1,60
# 토,1,44
# 일,0,30
# 토,0,34

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import io

csv_data = """
요일,외식유무,소득수준
토,0,57
토,0,39
토,0,28
화,1,60
토,0,31
월,1,42
토,1,54
토,1,65
토,0,45
토,0,37
토,1,98
토,1,60
토,0,41
토,1,52
일,1,75
월,1,45
화,0,46
수,0,39
목,1,70
금,1,44
토,1,74
토,1,65
토,0,46
토,0,39
일,1,60
토,1,44
일,0,30
토,0,34"""

df = pd.read_csv(io.StringIO(csv_data))
# print(df)

df1 = df.loc[:, ['외식유무', '소득수준']]
# print(df1.head())

formula = '외식유무 ~ 소득수준'
result = smf.logit(formula=formula, data=df1).fit()
# print(result.summary())

while True:
    try:
        a = int(input('소득수준 입력(양의 정수) : '))
        
        if a > 0:
            # 0보다 크면 정상적인 값이므로 루프 탈출!
            break
        else:
            print("❌ 소득 수준은 0보다 커야 합니다. 다시 입력해주세요.")
            
    except ValueError:
        # 숫자가 아닌 문자 등을 입력했을 때 에러 방지
        print("⚠️ 숫자만 입력 가능합니다. 다시 입력해주세요.")

new_data = pd.DataFrame()
new_data['소득수준'] = [a]
new_pred = result.predict(new_data)

pred_value = new_pred.values[0] # 확률값 꺼내기
print(f"외식할 확률: {pred_value:.4f}")

# 분류 결과 출력
if pred_value > 0.5:
    print(f"결과: 소득수준 {a}일 때 외식할 것으로 분류됨 (1)")
else:
    print(f"결과: 소득수준 {a}일 때 외식하지 않을 것으로 분류됨 (0)")