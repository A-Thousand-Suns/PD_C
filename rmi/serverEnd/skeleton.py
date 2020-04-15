import socket
import threading
import os

class assist:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('127.0.0.1', 6666))
        self.s.listen(10)
        self.conn, self.addr = self.s.accept()

    def connState(self):
        if (self.s):
            return True
        else:
            return False

    def sendInter(self):
        path = 'serInterface.py'
        filesize = str(os.path.getsize(path))
        print("发现接口文件,大小为：", filesize)
        self.conn.send(filesize.encode('utf-8'))
        mesg = self.conn.recv(1024)
        print(mesg.decode('utf-8'))
        print('开始发送接口文件')
        file = open(path, 'rb')
        for i in file:
            self.conn.send(i)
        file.close()

    def commu(self):
        mesg = self.conn.recv(1024).decode('utf-8')
        sCommu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sCommu.connect(('127.0.0.1', 6667))

        if (mesg == 'findstu.hi'):
            sCommu.send(mesg.encode('utf-8'))
            result = sCommu.recv(1024).decode('utf-8')
            self.conn.send(result.encode('utf-8'))

def deal():
    assidObj = assist()
    assidObj.sendInter()
    assidObj.commu()

if (__name__ == '__main__'):
    while True:
        t = threading.Thread(target=deal)
        t.run()



