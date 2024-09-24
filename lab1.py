#Abu Sayiem
#I pldege my honor that I have abided by the Stevens Honor System.
from cs115 import *
from math import factorial


def inverse(n):
    """ take a value n, returns the inverse of that value"""
    return 1/n
def e(n):
    """ takes a value n, returns e up to n"""
    def add(x,y):
        return x + y
    x = map(factorial, range((n + 1)))
    y = map(inverse, x)
    return reduce(add, y)

def teste():
    print(e(3))
    print(e(2))
    print(e(4))

    
    


