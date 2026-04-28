# beautifulsoup 모듈로 xml문서 처리
from bs4 import BeautifulSoup

# 1. 파일 읽기 단계
# 'my.xml' 파일을 읽기 모드('r'), 인코딩은 'utf-8'로 열기
with open('my.xml', mode='r', encoding='utf-8') as f:
    xmlfile = f.read()  # 파일의 전체 내용을 문자열로 읽어와 xmlfile 변수에 저장
    print(xmlfile, type(xmlfile)) # 읽어온 내용과 데이터 타입(<class 'str'>) 출력

print('-------2--------')
# 2. 파싱(Parsing) 단계
# 문자열(xmlfile)을 lxml 엔진을 사용해 BeautifulSoup 객체로 변환 (데이터를 구조화함)
soup = BeautifulSoup(xmlfile, 'lxml')
print(soup, type(soup)) # 구조화된 객체와 타입(<class 'bs4.BeautifulSoup'>) 출력

print('-------3--------')
# 3. 데이터 추출 연습
# 모든 <item> 태그를 찾아서 리스트 형태로 반환
itemTag = soup.find_all('item')
print(itemTag[1])  # 0부터 시작하므로 두 번째 <item> 태그의 전체 내용 출력

print('-------4--------')
# 모든 <name> 태그를 찾아서 리스트로 반환
nameTag = soup.find_all('name')
# 첫 번째 <name> 태그 안에 있는 'id' 속성값(예: <name id="1"> 이면 "1") 출력
print(nameTag[0]['id'])

print('-------5--------')

# 4. 반복문을 이용한 상세 데이터 추출
for i in itemTag:  # 각 <item> 태그를 하나씩 꺼내서 반복
    # 현재 <item> 태그 안에서 다시 모든 <name> 태그를 찾음
    nameTag = i.find_all('name')
    for j in nameTag:  # <name> 태그가 여러 개일 경우를 대비한 반복
        # j["id"]: <name> 태그의 id 속성값 / j.text: 태그 사이의 문자열 내용
        print("id : " + j["id"] + " name : " + j.text)
        
        # 현재 <item> 태그 내에서 첫 번째로 발견되는 <tel> 태그 찾기
        tel = i.find("tel")
        print("tel : ", tel.text)  # <tel>태그 안의 전화번호 텍스트 출력
    
    # 현재 <item> 태그 내의 모든 <exam> 태그를 찾아서 반복
    for j in i.find_all('exam'):
        # <exam kor="90" eng="80"> 형태라면 각 속성값을 키(key)로 접근하여 출력
        print("kor : " + j["kor"] + ", eng : " + j["eng"])
    print()  # 하나의 <item> 처리가 끝나면 한 줄 띄움