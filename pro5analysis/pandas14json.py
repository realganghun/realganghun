# json 자료 : XML에 비해 경량. 배열 개념만 있으면 처리 가능

import json

dict = {'name':'tom', 'age': 25, 'score' : ['90', '80', '20']} #dict type
print(dict, type(dict))

print('json 인코딩 : dict -> str ---------')
str_val = json.dumps(dict)  #dumps하면 dict가 str로 바뀜
# str_val = json.dumps(dict, indent=4) #indent는 들여쓰기 기능
print(str_val, type(str_val)) #<class 'str'>
# print(str_val['name']) #error발생 : 이 명령어는 string에 없음.
print('*****'*8)
print(str_val[0:20]) #문자열 관련 함수만 사용 가능

print('json decoding : str -> dict -----------')
json_val = json.loads(str_val)
print(json_val, type(json_val)) #dict 관련 명령 사용 가능
print(json_val['name'])

for k in json_val.keys():
    print(k)

for v in json_val.values():
    print(v)