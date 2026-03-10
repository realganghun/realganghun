from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

COOKIE_AGE = 60*60*24*7 #1주일간 보관
@app.get("/") #웹페이지 처음 접속할때는 무조건 get으로만 들어가서 여기는 get으로 고정해야댐
def home():
    return render_template("index.html")

@app.get("/login")
def loginfunc():
    name = request.cookies.get("name")
    visits = request.cookies.get("visits") #이거 문자열임 ㅋㅋ

    if name:
        visits = int(visits or '0') + 1 #visit이 있으면 + 1 하는거고 없으면 0에서 +1
        msg = f"안녕하세요 {name}님 {visits}번째 방문이네요"
    else:
        visits = None
        msg = "이름을 입력하면 방문 횟수를 쿠키로 기억합니다"

    resp = make_response(render_template('login.html', msg = msg, name = name, visits = visits))

    if name:
        resp.set_cookie( #로그인 상태면 visits 쿠키 갱신
            "visits",
            str(visits),
            max_age=COOKIE_AGE,
            samesite="Lax"
        )
    return resp

@app.post("/login")
def loginfunc2():
    name = (request.form.get("name") or "").strip()
    resp = make_response(redirect(url_for("loginfunc")))
    resp.set_cookie("name", name, max_age = COOKIE_AGE, samesite="Lax")
    resp.set_cookie("visits", "0", max_age = COOKIE_AGE, samesite="Lax")
    return resp


@app.post("/logout")
def logoutfunc():
    #쿠키 삭제 후 로그인 화면으로 이동
    resp = make_response(redirect(url_for("loginfunc")))
    resp.delete_cookie("name")
    resp.delete_cookie("visits")
    return resp


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)