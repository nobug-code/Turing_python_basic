import socketserver
import sys


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('클라이언트 접속 : {0}'.format(self.client_address[0]))
        sock = self.request

        rbuff = sock.recv(1024)  # 데이터를 수신하고 그 결과를 rbuff에 담는다. rbuff는 bytes 형식이다.
        received = str(rbuff, encoding="utf-8")
        print('수신 : {0}'.format(received))

        # 수신한 데이터를 그대로 돌려보냄.
        sock.send(rbuff)  # 수신한 데이터를 그대로 클라이언트에게 다시 송신한다.
        print('송신 : {0}'.format(received))
        sock.close()


if __name__ == '__main__':


    bindPort = 8080  #

    server = socketserver.TCPServer(('', bindPort), MyTCPHandler)

    print('메아리 서버 시작...')
    server.serve_forever()  #