# pandas 문제 8)
# MariaDB에 저장된 jikwon, buser 테이블을 이용하여 아래의 문제에 답하시오.
# Django 또는 Flask 모듈을 사용하여 결과를 클라이언트 브라우저로 출력하시오.
from flask import Flask, render_template, request
import pymysql
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from markupsafe import escape
import os
import koreanize_matplotlib

app = Flask(__name__)

db_config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8mb4'
}

def get_connection():
    return pymysql.connect(**db_config)

#    1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)
#        : 부서번호, 직원명 순으로 오름 차순 정렬 
@app.route("/")
def number1():
    dept = request.args.get("dept", "").strip()
    sql = """
        select j.jikwonno as 사번, j.jikwonname as 직원명, b.busername as 부서명, j.jikwonjik as 직급, j.jikwonpay as 연봉, DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y') AS '근무년수'
        from jikwon j inner join buser b on j.busernum=b.buserno order by buserno, jikwonname
    """

    #SQL 실행
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description] #description : 컴럼등 정보 얻기
    
    df = pd.DataFrame(rows, columns=cols)
    
    #직원 정보 html로 전송
    if not df.empty:
        jikwondata = df[['사번', '직원명', '부서명', '직급', '연봉', '근무년수']].to_html(index=False)
    else:
        jikwondata = "직원 자료 없음"

    return render_template("index.html", dept=escape(dept), #xss 방지
                            jikwondata=jikwondata)

#    2) 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.
@app.route("/number2")
def number2():
    # 1. 데이터 가져오기 (부서명, 직급, 연봉 정보가 필요함)
    sql = """
        SELECT b.busername AS 부서명, j.jikwonjik AS 직급, j.jikwonpay AS 연봉
        FROM jikwon j INNER JOIN buser b ON j.busernum = b.buserno
    """
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description]
            
    df = pd.DataFrame(rows, columns=cols)

    # 2. 부서명, 직급별로 그룹화하여 연봉 합계와 평균 계산
    if not df.empty:
        # agg를 사용해 여러 집계 함수를 동시에 적용
        summary_df = df.groupby(['부서명', '직급'])['연봉'].agg(['sum', 'mean','count']).reset_index().round(2)
        
        # 컬럼명을 보기 좋게 변경
        summary_df.columns = ['부서명', '직급', '연봉합계', '연봉평균','직원 수']
        
        # HTML 테이블로 변환
        result_html = summary_df.to_html(classes='table table-striped', index=False)
    else:
        result_html = "데이터가 존재하지 않습니다."

    # 3. 새로운 템플릿(number2.html)으로 데이터 전송
    return render_template("number2.html", result_table=result_html)

#    3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.
@app.route("/number3")
def number3():
    sql = """
        SELECT b.busername AS 부서명, j.jikwonpay AS 연봉
        FROM jikwon j INNER JOIN buser b ON j.busernum = b.buserno
    """
    # 그래프를 새로 그리지 않고, 이미 저장된 파일 이름만 전달합니다.
    chart_url = '/static/dept_chart.png'
    
    # 표(Table) 데이터가 필요하다면 DB에서 읽어오는 로직만 수행합니다.
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description]
            
    df = pd.DataFrame(rows, columns=cols)

    # 2. 부서명, 직급별로 그룹화하여 연봉 합계와 평균 계산
    if not df.empty:
        # agg를 사용해 여러 집계 함수를 동시에 적용
        summary_df = df.groupby(['부서명'])['연봉'].agg(['sum', 'mean']).reset_index().round(2)
        
        # 컬럼명을 보기 좋게 변경
        summary_df.columns = ['부서명', '연봉합계', '연봉평균']
        
        # HTML 테이블로 변환
        result_html = summary_df.to_html(classes='table table-striped', index=False)

    return render_template("number3.html", result_table=result_html, chart_url=chart_url)

def update_charts():
    """데이터를 읽어와서 그래프 이미지를 미리 생성해두는 함수"""

    sql = """
        SELECT b.busername AS 부서명, j.jikwonpay AS 연봉
        FROM jikwon j INNER JOIN buser b ON j.busernum = b.buserno
    """
    # 1. 데이터 가져오기 (기존 DB 연동 로직 활용)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description]
            
    df = pd.DataFrame(rows, columns=cols)

    # 2. 부서명, 직급별로 그룹화하여 연봉 합계와 평균 계산
    if not df.empty:
        # agg를 사용해 여러 집계 함수를 동시에 적용
        summary_df = df.groupby(['부서명'])['연봉'].agg(['sum', 'mean']).reset_index().round(2)

    # 2. 그래프 그리기 (plt.subplots를 직접 호출)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    axes[0].bar(summary_df['부서명'], summary_df['sum'], color='skyblue')
    axes[0].set_title('부서별 연봉 합계')
    
    axes[1].bar(summary_df['부서명'], summary_df['mean'], color='salmon')
    axes[1].set_title('부서별 평균 연봉')
    
    plt.tight_layout()
    
    fig.savefig('static/dept_chart.png') # fig 객체에서 직접 저장
    plt.close(fig) # 해당 figure 메모리 해제
    print("그래프 이미지 업데이트 완료!")

#    4) 성별, 직급별 빈도표를 출력하시오.
@app.route("/number4")
def number4():
    # 1. 성별(jikwongen)과 직급(jikwonjik) 데이터를 가져옵니다.
    sql = "SELECT jikwongen AS 성별, jikwonjik AS 직급 FROM jikwon"
    
    with get_connection() as conn:
        # pandas의 read_sql을 사용하면 커서 선언 없이 바로 DF로 만들 수 있어 편합니다.
        df = pd.read_sql(sql, conn)
    
    # 2. 성별, 직급별 빈도표(교차표) 작성
    # index에 성별, columns에 직급을 넣으면 표 형태가 됩니다.
    ctab = pd.crosstab(df['성별'], df['직급'])
    
    # 3. HTML로 변환 (표 디자인을 위해 부트스트랩 클래스 추가)
    result_html = ctab.to_html(classes='table table-bordered table-hover text-center')
    
    return render_template("number4.html", result_table=result_html)
#    5) 부서별 최고 연봉자 출력 : 부서명별로 가장 연봉이 높은 직원 1명씩 출력 
#        출력 항목: 부서명, 직원명, 연봉
@app.route("/number5")
def number5():
    # 1. 부서명, 직원명, 연봉 데이터를 조인해서 가져옵니다.
    sql = """
        SELECT b.busername AS 부서명, j.jikwonname AS 직원명, j.jikwonpay AS 연봉
        FROM jikwon j INNER JOIN buser b ON j.busernum = b.buserno
    """
    
    with get_connection() as conn:
        df = pd.read_sql(sql, conn)
    
    if not df.empty:
        # 2. 부서명으로 그룹화하고, 연봉이 최대인 행의 인덱스를 찾습니다.
        # idxmax()는 "값이 가장 큰 놈의 번호(ID)가 뭐야?"라고 묻는 함수입니다.
        top_indices = df.groupby('부서명')['연봉'].idxmax()
        
        # 3. 찾아낸 번호들(top_indices)에 해당하는 행만 전체 데이터에서 추출합니다.
        top_employees = df.loc[top_indices]
        
        # 연봉 높은 순으로 정렬하면 더 보기 좋겠죠?
        top_employees = top_employees.sort_values(by='연봉', ascending=False)
        
        result_html = top_employees.to_html(classes='table table-dark table-striped', index=False)
    else:
        result_html = "데이터가 없습니다."
        
    return render_template("number5.html", result_table=result_html)
#    6) 부서별 직원 비율 계산 : 전체 인원 대비 각 부서 인원 비율(%) 
#        비율 계산 (%)은 dept_ratio = (dept_count / total * 100).round(2)
#       결과를 DataFrame으로 출력
#       예: 총 인원: 30명
#            영업부 20%
#            총무부 30%
#            전산부 5%
#            ...
@app.route("/number6")
def number6():
    # 1. 부서명 데이터를 가져옵니다.
    sql = "SELECT b.busername AS 부서명 FROM jikwon j JOIN buser b ON j.busernum = b.buserno"
    
    with get_connection() as conn:
        df = pd.read_sql(sql, conn)
    
    if not df.empty:
        # 2. 전체 인원수 계산
        total_count = len(df)
        
        # 3. 부서별 인원수 계산 (value_counts 활용)
        dept_counts = df['부서명'].value_counts()
        
        # 4. 비율 계산 (%) : (부서별 인원 / 전체 인원 * 100)
        # 비율 계산 후 소수점 2자리까지 반올림(round)
        dept_ratio = ((dept_counts / total_count) * 100).round(2).reset_index()
        
        # 컬럼명 정리
        dept_ratio.columns = ['부서명', '비율(%)']
        
        # 5. 결과 HTML 생성
        total_str = f"<h3> 전체 인원: {total_count}명 </h3>"
        result_html = total_str + dept_ratio.to_html(classes='table table-hover', index=False)
    else:
        result_html = "데이터가 없습니다."
        
    return render_template("number6.html", result_table=result_html)

if __name__ == '__main__':
    update_charts()
    app.run(debug=True)