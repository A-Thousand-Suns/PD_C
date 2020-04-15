import socket
import threading
import pickle

class assist:
    def __init__(self, conn):
        self.conn = conn

    def connState(self):
        if (self.conn):
            return True
        else:
            return False

    def commu(self):
        sCommu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sCommu.connect(('127.0.0.1', 6667))

        while True:
            try:
                mesg = pickle.loads(self.conn.recv(1024))
            except EOFError:
                mesg={'noOption':[0]}

            print(mesg)
            option = list(mesg.keys())[0]
            sCommu.send(pickle.dumps(mesg))

            if (option == 'close'):
                self.conn.close()
                print('服务器代理断开与客户端连接')
                break

            result = sCommu.recv(1024).decode('utf-8')
            self.conn.send(result.encode('utf-8'))

        sCommu.close()
        print('服务器代理断开与服务器连接')




def deal(conn):
    assidObj = assist(conn)
    assidObj.commu()

if (__name__ == '__main__'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 6666))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=deal, args=(conn,))
        t.run()



