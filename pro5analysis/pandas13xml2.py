print("\n서울시 제공 도서관 정보 XML 샘플 자료 5개 읽기 --------")

import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTimeInfo/1/5/"
plainText = req.urlopen(url).read().decode()
# print(plainText) #<string> type임.

xmlObj = BeautifulSoup(plainText, 'xml')
libData = xmlObj.select('row')
# print(libData)

rows = []
for data in libData:
    name = data.find("LBRRY_NAME").text
    addr = data.find("ADRES").text
    print('도서관명 : ', name)
    print('주소 : ', addr)
    print()
    rows.append({"도서관명": name, "주소":addr})

df = pd.DataFrame(rows)
print(df)
print("건수 : ", len(df))