#client

from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 8888))
clientsock.send('ㅎㅇㅎㅇ'.encode(encoding='utf-8', errors='strict'))

clientsock.close()