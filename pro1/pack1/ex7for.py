#반복문 for
#for i in [1,2,3,4,5]: #[1,2,3,4,5] <- 묶음형 자료
#for i in (1,2,3,4,5): #tuple가능
#for i in {1,2,3,4,5}: #set가능
#    print(i, end = ' ')


#print('분산/표준편차 -----------------') #편차 제곱의 합을 전체 갯수로 나누면 분산, 분산에 루트씌우면 표준편차
# numbers = [1,3,5,7,9] #합은 25, 평균은 5.0
# #numbers = [3,4,5,6,7] #합은 25, 평균은 5.0
# #numbers = [-3,4,5,7,12] #합은 25, 평균은 5.0
# tot = 0
# for a in numbers:
#     tot += a
# print(f'합은 {tot}, 평균은 {tot / len(numbers)}')

# avg = tot / len(numbers)
# #편차의 합 구하기
# hap = 0
# for i in numbers:
#     hap += (i-avg)**2
# print(f'편차 제곱의 합{hap}')
# vari = hap / len(numbers)
# print(f'분산은 {vari}')
# print(f'표준편차는 {vari**0.5}')

# print()
# colors=['r','g','b']
# for v in colors:
#     print(v, end = ' ')

# print('iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어주는 함수')
# iterator = iter(colors)
# for v in iterator:
#     print(v, end = ', ')
# print()

# for idx, d in enumerate(colors): #enumerate : index와 값을 반환해줌.
#     print(idx, ' ', d)

# print('사전형----------------------------------------------------------------------------------')
# datas = {'python' : '만능언어', 'java' : '웹용언어', 'mariadb' : 'RDBMS'}
# for i in datas.items():
#     #print(i)
#     print(i[0], '~~', i[0])

# for k, v in datas.items():
#     print(k, '--', v)

# for k in datas.keys():
#     print(k, end = ' ')

# print()
# for val in datas.values():
#     print(val, end = ' ')

# print('다중 for -------------------------------------------------------------------------')
# for n in [2,3]:
#     print('--{}단--'.format(n))
#     for i in [1,2,3,4,5,6,7,8,9]:
#         print('{} * {} = {}'.format(n, i, n * i))

# print('continue, break ------------------------------------------------------------------------------')
nums = [1,2,3,4,5]
for i in nums:
    if i == 2: continue
    #if i == 4: break
    print(i, end = ' ')
else:
    print('정상종료')

print('\n정규 표현식 + for')
str = """현대모비스가 지난해 현대차와 기아를 제외한 글로벌 완성차 업체를 대상으로 총 91.7억불(한화 약 13.2조원) 규모의 수주 성과를 달성했다고 2일 밝혔다. 당초 계획했던 목표 수주액 74.5억불 대비 23%를 상회한 수치다. 현대모비스는 이번 실적의 배경으로 대규모 전동화 부품 신규 수주와 고부가가치 전장 부품 공급 확대, 중국 및 인도 등 신흥시장 공략을 꼽았다. 특히 최근 수년간 선도 기술 확보를 위해 연구개발 역량을 집중해 온 결과, 해외 고객사로부터의 수주가 본격적인 궤도에 올랐다는 분석이다. 지난해 실적은 북미와 유럽의 글로벌 메이저 고객사 두 곳으로부터 따낸 대형 수주가 견인했다. 현대모비스는 각각 전동화 핵심 부품인 배터리시스템(BSA)과 섀시모듈을 공급하기로 하는 계약을 체결했다. 보안 유지와 양산 변동성을 고려해 구체적인 고객사명은 공개되지 않았지만, 이번 수주는 지난해 전체 실적에서 상당한 비중을 차지한 것으로 알려졌다."""

import re
str2 = re.sub(r'[^가-힣\s]', '', str) #^은 부정, 한글과 공백 이외의 문자는 공백처리
print(str2)


str3 = str2.split(' ') #공백을 구분자로 문자열 분리, \n은 enter
print(str3)

# cou = {} #{}은 dict 아니면 set임
# for i in str3:
#     if i in cou:
#         cou[i] += 1 #같은 단어가 있으면 누적
#     else:
#         cou[i] = 1 #최초 단어인 경우, '단어' : 1

# print(cou)
# import re

# print('정규 표현식 좀 더 연습 -----------------------------------------')
# for test_ss in ['111-1234', '일이삼-일이삼사', '222-1234', '333&1234']:
#     if re.match(r'^\d{3}-\d{4}$', test_ss): #^\d는 첫번째라는 의미, $는 마지막이라는 의미
#         print(test_ss, '전화번호 O')
#     else:
#         print(test_ss, '전화번호 X')

# print('comprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현')
# a = [1,2,3,4,5,6,7,8,9,10]
# li = []
# for i in a:
#     if i % 2 == 0:
#         li.append(i)
# print(li)

# print(list(i for i in a if i % 2 == 0))

# # datas = [1, 2, 'a', True, 3.0]
# datas = {1, 2, 'a', True, 3.0, 1, 2, 3, 4, 5}
# li2 = [i*i for i in datas if type(i) == int]
# print(li2)

# id_name = {1:'tom', 2:'oscar'}
# name_id = {val:key for key, val in id_name.items()}
# print(name_id)
# print()

# print([1,2,3])
# print(*[1,2,3]) #* : unpack

# aa = [(1,2), (3,4), (5,6)]
# for a, b in aa:
#     print(a+b)

# print([a + b for a, b in aa])
# print(*[a + b for a, b in aa], sep='\n')

#수열 쉽게 만들기!(range)--------------------------------------------------------------------------------
# print(list(range(1,6))) #[1, 2, 3, 4, 5]
# print(tuple(range(1,6,2))) #(1, 3, 5)

# print(list(range(-10,-100,-20))) #[-10, -30, -50, -70, -90]
# print(set(range(1,6,2)))

# for i in range(6):
#     print(i, end = ' ')
# print()
# for _ in range(6):
#     print('반복')

# tot = 0
# for i in range(1, 11):
#     tot += i
# print('tot = ', tot) # = print('tot = ', sum([1,11])) <- 내장함수 이용

# for i in range(1,10):
#     print(f'2 * {i} = {2 * i}')

#문제 1: for문을 사용해서 2 ~ 9구구단 출력(단은 행 단위 출력)------------------------------------------------
for i in range(2,10):
    print(f'{i}단 구구단-------------------')
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}', end = ' ')
    print()


#문제 2: 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# p = int(input('첫번째 주사위 : '))
# q = int(input('두번째 주사위 : '))
# r = p + q
# if r % 4 == 0:
#     print('첫번째 주사위 수 + 두번째 주사위 수 = %d' %r)
# else:
#     print('4의 배수가 아니네용')

for i in range(1,7):
    for j in range(1,7):
        k=i+j
        if k % 4 == 0:
            print(f'두 수의 합({i} + {j} = {k})이 4의 배수입니다')
print('\nend')
