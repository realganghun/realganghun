import sys
sys.stdout.reconfigure(encoding='utf-8')

s1 = "이영빈"
s2 = "방구냄새 지독해"

print('Content-Type:text/html;charset=utf-8\n')

print('''<html lang="kr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>World</title>
</head>
<body>
    <h1>World 페이지</h1>
    자료 출력 : {0} {1}
    <br/>
    <img src="../images/bungsin.jpg" width="400" height="550">
    <br/>
    <a href="../index.html">메인으로</a>
</body>
</html>
'''.format(s1,s2))