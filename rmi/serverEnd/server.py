import socket
import threading
from serverEnd import serInterface

class findstu(serInterface.findstuInter):
    def hi(self):
        print('hi')
        return 'hi'

class cal(serInterface.calInter):
    def add(self, a, b):
        return (a+b)

def deal(conn):
    while True:
        data = conn.recv(1024).decode('utf-8')
        if (data == 'findstu.hi'):
            obj = findstu()
            data = obj.hi()
            result = data.encode('utf-8')
            conn.send(result)


if (__name__ == '__main__'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 6667))
    s.listen()
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=deal, args=(conn,))
        t.run()
