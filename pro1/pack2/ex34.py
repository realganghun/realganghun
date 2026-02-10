#-----------------------------파일처리-----------------------------
#파일, 데이터베이스, 네트워크 작업할 때는 try, except문을 꼭 쓰는게 좋다!
import os


try:
    print('파일 읽기 ------------------')
    print(os.getcwd())
    f1 = open(os.getcwd() + r'\ftext.txt', encoding = 'utf-8') #<-- utf-8은 전세게 언어를 다 번역해줌
    #=C:\work\projects\pro1\pack2\ftext.txt 와 같음.
    #f1 = open(r'C:\work\projects\pro1\pack2\ftext.txt', encoding = 'utf-8')
    f1 = open('ftext.txt', mode = 'r', encoding = 'utf-8')
    print(f1)
    print(f1.read())
    f1.close()

    print('파일 저장 ------------------')
    f2 = open('ftext2.txt', mode='w', encoding='utf-8')
    f2.write('내 친구들\n')
    f2.write('홍길동, 한국인')
    f2.close()
    print('파일 저장 성공')

    print('파일 내용 추가 ------------------')
    f3 = open('ftext2.txt', mode='a', encoding='utf-8')
    f3.write('\n사오정')
    f3.write('\n손오공')
    f3.close()
    print('파일 추가 성공')

    f4 = open('ftext.txt', mode = 'r', encoding = 'utf-8')
    print(f4)
    print(f4.read())
    f4.close()
except Exception as e:
    print('파일 처리 오류 원인 : ', e)