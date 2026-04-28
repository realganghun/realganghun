print("\n서울시 제공 도서관 정보 json 샘플 자료(5개) 읽기")
import json
import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd


url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTimeInfo/1/5/"
plainText = req.urlopen(url).read().decode()
# print(plainText, type(plainText)) #<class 'str'>

jsonData = json.loads(plainText) #str ---> dict로 바꿈
# print(jsonData, type(jsonData)) #<class 'dict'>

print(jsonData["SeoulLibraryTimeInfo"]["row"][0]["LBRRY_NAME"])

# dict의 get() 사용
print()
libData = jsonData.get("SeoulLibraryTimeInfo").get("row")
# print(libData)

name = libData[0].get("LBRRY_NAME")
print(name)

print()
datas=[]
for ele in libData:
    name = ele.get("LBRRY_NAME")
    tel = ele.get("TEL_NO")
    addr = ele.get("ADRES")
    print(name, ' ', tel, ' ', addr)
    datas.append([name, tel, addr])

df = pd.DataFrame(datas, columns=['도서관명', '전화', '주소'])
print(df)