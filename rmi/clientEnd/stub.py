import socket
import pickle

class proxy:
    def __init__(self, ip):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect = self.s.connect((ip.split(':')[0], int(ip.split(':')[1])))

    def connState(self):
        if (self.s):
            return True
        else:
            return False

    def creatObj(self, className):
        classDic = {'greet': greet,
                    'cal': cal}
        return classDic[className](self.s)

    def closeConn(self):
        self.s.send(pickle.dumps({'close':[]}))
        self.s.close()
        print('断开与服务器连接')

class greet:
    def __init__(self, s):
        self.s = s

    def hi(self):
        option = 'findstu.hi'
        parameter = []
        sendDic = {option:parameter}
        self.s.send(pickle.dumps(sendDic))
        result = self.s.recv(1024).decode('utf-8')
        print(result)

class cal:
    def __init__(self, s):
        self.s = s

    def add(self, a, b):
        option = 'cal.add'
        parameter = [a, b]
        sendDic = {option:parameter}
        self.s.send(pickle.dumps(sendDic))
        result = self.s.recv(1024).decode('utf-8')
        print(result)
