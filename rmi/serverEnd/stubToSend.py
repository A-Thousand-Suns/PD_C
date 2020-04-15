import socket
import pickle

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

class greet():
    def __init__(self, proxy):
        self.s = proxy.s

    def hi(self):
        option = 'findstu.hi'
        parameter = []
        sendDic = {option: parameter}
        self.s.send(pickle.dumps(sendDic))
        result = self.s.recv(1024).decode('utf-8')
        print(result)

class cal():
    def __init__(self, proxy):
        self.s = proxy.s

    def add(self, a, b):
        option = 'cal.add'
        parameter = [a, b]
        sendDic = {option: parameter}
        self.s.send(pickle.dumps(sendDic))
        result = self.s.recv(1024).decode('utf-8')
        print(result)
