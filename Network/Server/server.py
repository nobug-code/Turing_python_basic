from socket import *
import socketserver
from threading import Thread


'''
socket 의 첫번째 인자는 패밀리, 타입이다. 
패밀리란 주소 체계가 어떻게 되어 있는냐에 대한 것이다. 
AF_INET, AF_INET6 를 많이 사용하v는데 
AF_INT 는 IP4v
AF_INET6는 Ip6v 가 사용된다. 

타입은 소켓 타입이다. raw 소켓, stream  소켓, 데이터그램 소켓이 있다. 
어떤 형식으로 데이터 타입을 지정해서 보내는가 이다. 

바인드는 프로그램 인터페이스인 소켓과 네트워크 자원인 포트를 연결하는 행위이다. 

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
#들을 준비가 되었다.
serverSock.listen(1)

#서버가 연결이 되면 두가지를 리턴하게 된다.
#소켓, 주소 정보를 리턴하게 된다.

connectionSock, addr = serverSock.accept()

print(str(addr), "접속이 확인되었습니다. ")

#recv 는 소켓으로 부터 입력을 받는 함수이다.

data = connectionSock.recv(1024)

print("받은 데이터 ", data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')
'''

#send, senall  의차이점은 send 은 더 기계적으로 가갑고 sendall은 더 high-api 이다.
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSock.bind(('', 8080))

'3+5'
'8'

#listen 의 입력에 따라 갯수가 정해진다.
while True:

    BUF_SIZE = 2048
    serverSock.listen(3)
    conn, addr = serverSock.accept()
    data = conn.recv(BUF_SIZE)
    msg = data.decode()
    print(msg)
    conn.send("kkkkkkkk".encode())

    if (msg == 'bye'):
        conn.close()
        break

serverSock.close()
#222.100.117.211
'''
연결이 안되있었던 문제는 같은 ip 를 공유하니깐 해결되었다. 
다른 와이파이가 연결되어 있어서 접근이 불가 했다. 
그럼 만약 다른 ip 에서 접근을 할려그러면 어떻게 해야 될까
ip 주소는 192.168.0.49 처럼 내부 ip 를 사용했다. 
'''
\
