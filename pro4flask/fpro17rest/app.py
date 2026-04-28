from flask import Flask, jsonify, request, render_template
from db import get_connFunc

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")


# 전체 직원 조회
@app.get("/api/jikwon")
def jikwon_list():
    sql="""
        select jikwonno, jikwonname, busername, jikwonjik, jikwonpay, year(jikwonibsail) as 입사년도 
        from jikwon inner join buser on jikwon.busernum=buser.buserno
        order by jikwonno
    """

    with get_connFunc() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    return jsonify({"ok" : True, "data" : rows})

# 직원 1명 조회
@app.get("/api/jikwon/<int:no>")
def jikwon_list(no):
    sql="""
        select jikwonno, jikwonname, busername, jikwonjik, jikwonpay, year(jikwonibsail) as 입사년도 
        from jikwon inner join buser on jikwon.busernum=buser.buserno
        where jikwonno=%s
    """

    with get_connFunc() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (no,))
            row = cur.fetchone()

    return jsonify({"ok" : True, "data" : row})

# 전체 부서 조회
@app.get("/api/buser")
def buser_list():
    sql="""
        select * from buser order by buserno
    """

    with get_connFunc() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    return jsonify({"ok" : True, "data" : rows})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)