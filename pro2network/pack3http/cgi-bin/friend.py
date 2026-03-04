#------------------------------------------get 방식----------------------------------------------
# # -*- coding: utf-8 -*-   
# # 위 명령 안 먹으면 아래 방법 사용
# import sys
# sys.stdout.reconfigure(encoding='utf-8')

# import os
# import urllib.parse

# # 웹 서버가 URL의 ? 뒤 부분을 환경변수 QUERY_STRING에 넣어줌
# # 그 값을 가져오는 코드
# query = os.environ.get("QUERY_STRING", "")
# # 문자열을 딕셔너리 형태로 변환
# # {'name': ['홍길동'], 'age': ['20'] }
# params = urllib.parse.parse_qs(query)

# # 값 꺼내기  - 첫 번째 값 꺼내기 [0]
# irum = params.get("name", [""])[0] # 없으면 빈 리스트 대신 [""] 사용
# junhwa = params.get("phone", [""])[0]
# gen = params.get("gen", [""])[0]

# print("Content-Type: text/html; charset=utf-8")
# print()
# print("""
# <html lang="ko">
# <head>
#     <meta charset="UTF-8">
#     <title>world</title>
# </head> 
# <body>
#     입력한 값 : 이름은 {0}, 전화는 {1}, 성별은 {2}
# </body>
# </html>
# """.format(irum, junhwa, gen))

# -----------------------------------post 방식 ----------------------------------------------
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import urllib.parse

method = os.environ.get("REQUEST_METHOD", "")

if method == "POST":
    length = int(os.environ.get("CONTENT_LENGTH", 0))
    body = sys.stdin.read(length)
    params = urllib.parse.parse_qs(body)
else:
    query = os.environ.get("QUERY_STRING", "")
    params = urllib.parse.parse_qs(query)

irum = params.get("name", [""])[0]
junhwa = params.get("phone", [""])[0]
gen = params.get("gen", [""])[0]

print("Content-Type: text/html; charset=utf-8")
print()

print(f"""
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>friend</title>
</head>
<body>
    입력한 값 : 이름은 {irum}, 전화는 {junhwa}, 성별은 {gen}
    <br/>
    <img src="../images/bungsin.jpg" width="400" height="550">
    <br/>
</body>
</html>
""")