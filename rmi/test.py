class father:
    def __init__(self, b):
        self.a = 0
        self.b = b

class son(father):
    c = 3
    def test(self):
        print(self.b)

if (__name__ == '__main__'):
    test = son(9)
    test.test()
