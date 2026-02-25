# 소켓(Socket) 통신은 네트워크상에서 두 컴퓨터(서버-클라이언트)가 포트(Port)를 통해 실시간으로 양방향 데이터를 주고받는 방식
# TCP/IP 기반의 프로그래머 인터페이스로 연결을 지속하며, 채팅이나 온라인 게임처럼 서버가 클라이언트에게 즉각적인 정보를 보낼 때 주로 사용
# 통신 기기간 대화가 가능하도록 하는 통신방식으로 클라이언트/서버 모델에 기초한다.

# 연결지향 : TCP/IP
# 비연결지향 : 

#socket 통신 확인
import socket

print(socket.getservbyname('http', 'tcp')) #www 환경 전송규약
print(socket.getservbyname('ssh', 'tcp')) # 원격 컴 접속
print(socket.getservbyname('ftp', 'tcp')) # 파일 전송
print(socket.getservbyname('smtp', 'tcp')) # 메일 송수신
print(socket.getservbyname('pop3', 'tcp')) # 이메일

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
print(socket.getaddrinfo('www.daum.net', 80, proto=socket.SOL_TCP))