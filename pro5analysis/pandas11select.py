#css 셀렉터를 이용
from bs4 import BeautifulSoup
html_page = """
<html>
<body>
<div id="hello">
    <a href="https://www.naver.com>naver</a><br>
    <span>
        <a href="https://www.daum.net>daum</a><br>
    </span>
    <ul class="world">
        <li>안녕</li>
        <li>방가방가</li>
    </ul>
</div>
<div id="hi" class="good">
    두번째 div
</div>
</body>
</html>
"""

soup = BeautifulSoup(html_page, 'lxml')

# aa = soup.select_one("div") #첫번째 div
# aa = soup.select_one("div#hello") #id가 hello
# aa = soup.select_one("div.good") #class가 good
aa = soup.select_one("div#hello > a") #div의 자식
# aa = soup.select_one("div#hello a") #div의 자손
print('aa : ', aa, ' ', aa.string)

print()
# bb = soup.select("div")
# bb = soup.select("div#hello > ul.world") #자식
# bb = soup.select("div#hello ul.world") #자손
bb = soup.select("div#hello ul.world > li")
print('bb : ', bb)
for i in bb:
    print(i, ' ', i.text)

print("--------- 위키백과 사이트에서 이순신으로 검색된 자료 읽기 -----------")
import requests
url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
headers = {"User-Agent" : "Mozilla/5.0"}
wiki = requests.get(url=url, headers=headers)
# print(wiki.text[:100])

soup = BeautifulSoup(wiki.text, 'html.parser')
result = soup.select("p#mwHw") # <-- 이거는 id가 mwHw인 문단만 가져온 것.
result = soup.select("#mw-content-text p") # <-- 문단 전체
# print(result)
for s in result:
    for sup in s.find_all("sup"):
        sup.decompose() #tag삭제

    print(s.get_text(strip=True))


print("--------- 교촌치킨 사이트에서 메뉴, 가격 자료 읽기 ------------")
import pandas as pd
url = "https://kyochon.com/menu/chicken.asp"
headers = {"User-Agent" : "Mozilla/5.0"}
response = requests.get(url, headers=headers)
# print(response.text)

soup2 = BeautifulSoup(response.text, 'html.parser')
# 메뉴명 얻기
# names = soup2.select("dl.txt > dt")
# print(names)

names = [tag.text.strip() for tag in soup2.select("dl.txt > dt")]
print(names)

# 가격 가져오기
prices = [int(tag.text.strip().replace(',', '')) for tag in soup2.select("p.money strong")]
print(prices)

df = pd.DataFrame({"상품명":names, "가격":prices})
print(df.head())
print(f"가격 평균 : {df['가격'].mean():.2f}")
print(f"가격 표준편차 : {df['가격'].std():.2f}")
cv = df['가격'].std() / df['가격'].mean() * 100
print(f"가격 변동계수(CV) : {cv:.2f}%") # --> CV : 28.31이 나옴. 평균 대비 적당히 퍼져있는 편.