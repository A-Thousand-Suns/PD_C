import socket
import threading
import pickle
from serverEnd import serInterface

class greet(serInterface.greetInter):
    def hi(self):
        return 'hi'

class cal(serInterface.calInter):
    def add(self, a, b):
        return (a+b)

def deal(conn):

    while True:
        try:
            mesg = pickle.loads(conn.recv(1024))
            print(mesg)
        except EOFError:
            continue
        option = list(mesg.keys())[0]
        parameter = mesg[option]

        if (option == 'findstu.hi'):
            obj = greet()
            data = obj.hi()
            result = data.encode('utf-8')
            conn.send(result)

        if (option == 'cal.add'):
            obj = cal()
            data = obj.add(parameter[0], parameter[1])
            result = str(data).encode('utf-8')
            conn.send(result)

        if (option == 'close'):
            break

    conn.close()
    print('服务器断开与服务器代理连接')


if (__name__ == '__main__'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 6667))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=deal, args=(conn,))
        t.run()
