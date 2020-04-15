import types
import Pyro4
import pickle

class fa:
    def add(self):
        pass

class son(fa):
    def add(self, a, b):
        print(a+b)

a = son()
a.add(1,2)