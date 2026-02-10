#while문 기초
# a = 1
# while a <= 5:
#     print(a, end=' ') #한줄씩 찍는게 아니라 옆으로 찍고싶으면 end=' '활용.
#     a += 1
# else:
#     print('수행성공')

# print('end')  #무한루프 빠졌을때 ctrl+c누르면 강제종료
#while문에는 변수에 초기값을 주고 while문 안에 변수에 변화를 줘야함
#else는 while문 안의 조건을 완료해야 실행함

# i = 1
# while i <= 3:
#     j = 1
#     while j <= 4:
#         print('i = ' + str(i) + ' / j = ' + str(j))
#         j += 1
#     i += 1
# print('end')

# print('1 ~ 100 사이의 정수 중 3의 배수의 합 ---------------------------------------------------')
# number = 1 ; sum = 0
# while number <= 100:
#     #print(number)
#     if number % 3 ==0:
#         #print(number)
#         sum += number
#     number += 1
# print('합 = ', sum)

# colors=["빨", "파", "노"]
# num = 0
# while num < len(colors):
#     print(colors[num])
#     num += 1

# print('\n별찍기------------------------------------------------------------------------------------')
# i = 1
# while i <= 10:
#     j = 1
#     msg =' '
#     while j <= i:
#         msg += '*'
#         j += 1
#     print(msg)
#     i += 1

# print('if 블럭 내 while 블럭 사용 --------------------------------------------------------------')

# import time
# sw = input('폭탄 스위치를 누르겠습니까? [y/n]')
# print('sw : ', sw)
# if sw == 'y' or sw == 'Y':
#     count = 5
#     while count >= 1:
#         print('%d초 남았습니다' %count)
#         time.sleep(1) #1초의 시간 텀을 줌
#         count -= 1
#     print('펑!!!')
# elif sw == 'n' or sw == 'N':
#     print('작업 취소')
# else:
#     print('y또는 n을 누르셈')

# print('\ncontinue/break ---------------------------------------------------------------')
# a = 0
# while a < 10:
#     a += 1
#     if a == 3 or a == 5:
#         continue #아래 문을 무시하고 while로 돌아감, a값은 늘어났지만 print하지는 않음.
#     #if a == 7:
#     #    break #while문 무조건 탈출!, break가 있으면 else문으로 안들어가게 됨
#     print(a)
# else:
#     print('정상 종료')
# print('while 수행 후 %d' %a)

# print('\n키보드로 숫자 입력받아 홀 짝 확인(무한 반복) ------------------------------------------------------')
# while True: #True, 1, 100, -12, 4.5, 'ok' --> 참(데이터가 있으면 True), 무한루프를 빠져나오려면 break밖에 없음
#     mysu = int(input('확인할 숫자 입력(0누르면 종료) : '))
#     if mysu == 0:
#         print('프로그램 종료')
#         break
#     elif mysu % 2 == 0:
#         print('%d은(는) 짝수' %mysu)
#     elif mysu % 2 == 1:
#         print('%d은(는) 홀수' %mysu)        

print('end')