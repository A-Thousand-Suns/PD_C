from clientEnd import stub

proxyObj = stub.proxy('127.0.0.1:6666')
greetObj = proxyObj.creatObj('greet')
greetObj.hi()
calObj = proxyObj.creatObj('cal')
calObj.add(1,2)
proxyObj.closeConn()







