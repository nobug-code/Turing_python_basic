
'''
print('연결 확인 됐습니다.')
clientSock.send('I am a client'.encode('utf-8'))

print('메시지를 전송했습니다.')

data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))
print('connection')
clientSock.send('I am a client'.encode('utf-8'))
data = clientSock.recv(BUF_SIZE)
print(data.decode())
'''


from socket import *
from threading import Thread

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))
BUF_SIZE = 1024

for i in range(10):
    data = input(">>")
    clientSock.sendall(data.encode())
    if(data == "bye"):
        clientSock.close()
        break
    res = clientSock.recv(1024)
    print(res.decode())








#함수화 시키기

