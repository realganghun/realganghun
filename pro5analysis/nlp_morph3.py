# 웹(동아일보)에서 특정 단어 관련 문서들 검색 후 명사만 추출
# 워드클라우드 그리기
# pip install pygame
# pip install simplejson
# pip install pytagcloud

from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib.request
from konlpy.tag import Okt
from collections import Counter #단어 수를 카운팅하는 라이브러리
import pytagcloud
import matplotlib.pyplot as plt
import koreanize_matplotlib
import matplotlib.image as mpimg
import webbrowser

# keyword = input("검색어 : ")
# print(quote(keyword))
keyword = '춘분'
target_url = "https://www.donga.com/news/search?query=" + quote(keyword)
source_code = urllib.request.urlopen(target_url)

soup = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')

msg = ''

for title in soup.find_all("h4", class_="tit"):
    title_link = title.find("a")
    # print(title_link)
    article_url = title_link["href"]
    # print(article_url) #https://sports.donga.com/news/article/all/20260322/133578609/1 <-- '춘분'단어를 포함한 기사의 url이 출력됨

    try:
        source_article = urllib.request.urlopen(article_url)
        soup2 = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
        # print(soup2)
        contents = soup2.select('div.article_txt')
        # print(contents)

        for imsi in contents:
            item = str(imsi.find_all(string=True))
            msg += item
    except Exception as e:
        print("에러발생 : ", e)
    
    # print(msg)

    # 형태소 분석 후 명사 추출
    okt = Okt()
    nouns = okt.nouns(msg)

    result = []
    for imsi in nouns:
        if len(imsi) > 1:
            result.append(imsi)

# print(result)

count = Counter(result)
# print(count)

tag = count.most_common(50) #상위 50개의 단어만 추출
# print(tag) #[('기운', 17), ('스포츠동아', 12), ('오늘', 12), ('마음', 12), ('다른', 11) ..... list 안에 dict가 들어있는 형태

# 워드 클라우드 작성
taglist = pytagcloud.make_tags(tag, maxsize=100)
# print(taglist) #[{'color': (130, 176, 60), 'size': 123, 'tag': '기운'}, {'color' ..... 이런식으로 출력됨

pytagcloud.create_tag_image(taglist, 'word.png', size=(1000, 600), background=(255,255,255), fontname='korean', rectangular=False)

img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()

webbrowser.open('word.png')