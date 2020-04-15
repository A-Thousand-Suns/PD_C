from clientEnd import stub

proxyObj = stub.proxy('127.0.0.1:6666')
proxyObj.recInter()
findstuObj = stub.findstu(proxyObj)
findstuObj.hi()






