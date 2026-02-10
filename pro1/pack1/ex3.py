#기본 자료형 : int, float, bool, complex
#묶음 자료형 : str, list, tuple, set, dictionary

#1. str : 문자열 묶음 자료형. 순서O, 수정X
s = 'sequence'
print(s, id(s))
print('길이 : ', len(s))
print('길이 : ', s.find('e'), s.find('e',3), s.rfind('e')) #문자열 관련 함수

print(s[5])
print(s[2:5])
print(s[:], ' ', s[0:len(s)], s[::1])
print(s[0:7:2])
print(s[-1], ' ', s[-4:-1:1])
print(s, id(s))
s = 'sequenc' #수정X, 변경O
print(s, id(s))
s='bequence'
print(s, id(s))

#2. list : 다양한 종류의 자료 묶음형. 순서O, 수정O, 중복O
a = [1,2,3]
print(a, a[0], a[0:2])
b = [10, a, 10, 20.5, True, '문자열']
print(b, ' ', b[1], b[1][0])

family = ['엄', '빠', '나', '여동생']
print(family, id(family))

family.append('형') #추가
print(family, id(family))

family.remove('나') #삭제
family.insert(0 , '할') #삽입
family.extend(['삼','고','조']) #복수 추가
family += ['이모'] #추가
print(family)
print(family.index('빠'))
print('마' in family, '나' in family)

family.remove('여동생') #값에 의한 삭제
del family[4] #순서에 의한 삭제
print(family)

print()
kbs = ['123', '34', '234']
kbs.sort() #문자열 정렬(사전순)
print(kbs)

mbc = [123, 34, 234]
mbc.sort() #숫자 정렬(오름차순) mbc.sort(reverse=True) -> 내림차순
print(mbc)

sbs = [123, 34, 234]
ytn = sorted(sbs)
print('sbs =', sbs)
print('ytn =', ytn)
print()
name = ['tom','james','oscar']
name2 = name

print(name, id(name))
print(name2, id(name2))

import copy
name3 = copy.deepcopy(name)
print(name3, id(name3))

name[0] = '길동'
print(name)
print(name2)
print(name3)

#3. tuple : 리스트와 유사, 읽기 전용. 수정X
t = (1, 2, 3, 4)
t = 1, 2, 3, 4 #위와 동일

print(t, type(t))

tu = (1)
print(tu, type(tu)) # <-- 하나인 경우에는 int로 분류됨

tup = (1,)
print(tup, type(tup))

print(t[0], ' ', t[0:2])
#t[0] = 5 -> tuple은 수정불가이므로 error발생

imsi = list(t)
imsi[0] = 5
t = tuple(imsi)
print(t)

#4. set : 순서X, 중복X, 수정O
ss = {1,3,1,2}
print(ss) #1은 중복돼서 제거됨

ss2 = {3, 4}
print(ss.union(ss2)) #ss와 ss2의 합집합
print(ss.intersection(ss2)) #ss와 ss2의 교집합
print(ss - ss2, ss | ss2, ss & ss2) #차, 합집합, 교집합
#print(ss[0]) #set에는 순서가 없기때문에 index같은거를 못 계산함

ss.update({6, 7})
print(ss)

ss.discard(7) #값 삭제
ss.remove(6) #값 삭제
#discard와 remove의 차이 : discard는 없으면 skip하지만, remove는 없으면 error발생

print(ss)

li = ['aa', 'aa', 'bb', 'cc', 'aa']
print(li)
imsi2 = set(li)
li = list(imsi2)
print(li)

#5. dictionary : 사전 자료형{'키' : 값} 형태
#방법1
mydic = dict(k1 = 1, k2 = 'ok', k3 = 123.4)
print(mydic, type(mydic))

#방법2
dic = {'파이썬' : '뱀', '자바' : '커피', '인사' : '안녕', '자바' : '자박자박'}
print(dic)
print(len(dic))
print(dic['자바'])
ff = dic.get('자바')
print(ff)

print(dic['인사'])
#print(dic[0]) -> error발생. dic에는 index가 없음

dic['금요일'] = '나이스' #추가

print(dic)

del dic['인사']
print(dic)
print(dic.keys())
print(dic.values())