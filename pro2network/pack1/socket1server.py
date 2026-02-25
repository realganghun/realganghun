# 일회용 서버

from socket import *

serversocket = socket(AF_INET, SOCK_STREAM) #socket 객체 생성
serversocket.bind(('127.0.0.1', 8888)) #socket을 특정 컴과 바인딩
serversocket.listen(5) #client와 연결정보 수. 리스너 설정
print('서버 서비스 중...')

conn, addr = serversocket.accept() #수동적으로 연결을 받아들임
print('클라이언트 주소 : ', addr)
print('클라이언트 메세지 : ', conn.recv(1024).decode())

conn.close()
serversocket.close()