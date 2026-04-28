from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
from db import get_connFunc, insert_survey, fetchall_survey
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Agg') #Anti Grain Geometry : matplotlib의 렌더링 엔진 中 하나, 이미지 저장 시 오류 방지 - 차트 출력 없이 저장할 때 사용
import matplotlib.pyplot as plt
from analysis import analysis_func, save_barchart_func

BASE_DIR = Path(__file__).resolve().parent # 현재 파일의 경로
STATIC_DIR = BASE_DIR / 'static' / 'images' / 'vbar.png'

app = Flask(__name__)

# 전체 직원 조회
@app.get("/")
def index():
    return render_template("index.html")

@app.get("/coffee/survey")
def survey_view():
    return render_template("coffee/coffeesurvey.html")

@app.post("/coffee/surveyprocess")
def survey_process():
    gender = (request.form.get("gender") or "").strip()
    age = (request.form.get("age") or "").strip()
    co_survey = (request.form.get("co_survey") or "").strip()

    # 입력 검증
    if not gender or not co_survey or not age.isdigit():
        return redirect(url_for("survey_view"))
    
    age = int(age)
    # 데이터베이스에 설문 결과 저장
    insert_survey(gender=gender, age=age, co_survey=co_survey)

    # 조회 및 분석
    rdata = fetchall_survey()
    print(rdata)
    crossTable, result, df = analysis_func(rdata)

    # 차트 저장
    if not df.empty:
        save_barchart_func(df, STATIC_DIR)
    return render_template("coffee/result.html", 
                            crossTable=crossTable.to_html() if not crossTable.empty else "데이터가 없음",
                            result=result, df=df.to_html(index=False) if not df.empty else "데이터가 없음")

@app.get("/coffee/surveyshow")
def survey_show():
    # 저장 없이 결과만 출력
    rdata = fetchall_survey()
    crossTable, result, df = analysis_func(rdata)

    # 차트 저장
    if not df.empty:
        save_barchart_func(df, STATIC_DIR)
        
    return render_template("coffee/result.html", 
                            crossTable=crossTable.to_html() if not crossTable.empty else "데이터가 없음",
                            result=result, df=df.to_html(index=False) if not df.empty else "데이터가 없음")

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)