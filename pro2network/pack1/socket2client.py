#client

from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 7788))
clientsock.send('ㅎㅇㅎㅇ'.encode(encoding='utf-8', errors='strict'))

print('수신자료 : ', clientsock.recv(1024).decode())
clientsock.close()