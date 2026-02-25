import socket
import sys

#HOST = '127.0.0.1' # <-- 이거는 특정 사용자에게 가능
HOST = '' # <-- 이거는 모든 사용자에게 가능
port = 7788

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket 객체 생성

try:
    serversocket.bind((HOST, port))
    serversocket.listen(5)
    print('서버(무한 루프) 서비스 중...')

    while True:
        conn, addr = serversocket.accept()
        print('client info : ', addr[0], ' ', addr[1])
        print('클라이언트 메세지 : ', conn.recv(1024).decode()) #수신 메세지 출력
        # 메세지 송신 to client
        conn.send(('from server : ' + str(addr[1]) + '이영빈 M자탈모').encode('utf_8'))
except Exception as e:
    print('err is ', e)
    sys.exit()
finally:
    conn.close()
    serversocket.close()