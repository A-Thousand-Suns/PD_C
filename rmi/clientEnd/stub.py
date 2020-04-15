import socket
from clientEnd import serInterface

class proxy:
    def __init__(self, ip):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect = self.s.connect((ip.split(':')[0], int(ip.split(':')[1])))
        self.interface = False

    def connState(self):
        if (self.s):
            return True
        else:
            return False

    def recInter(self):
        filesize = int(self.s.recv(1024).decode('utf-8'))

        if (filesize):
            self.s.send('接收到文件容量数据'.encode('utf-8'))

        recvsize = 0
        file = open('serInterface.py', 'wb')

        while recvsize < filesize:
            data = self.s.recv(1024)
            file.write(data)
            recvsize = recvsize + len(data)

        file.close()
        self.interface = True
        print('接口文件接收完成')

class findstu(serInterface.findstuInter):
    def __init__(self, proxy):
        self.s = proxy.s

    def hi(self):
        option = 'findstu.hi'
        self.s.send(option.encode('utf-8'))
        result = self.s.recv(1024).decode('utf-8')
        print(result)