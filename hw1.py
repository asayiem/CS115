#Abu Sayiem
#CS-115 HW1
#I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *

def mult(x, y):
    """Returns the product of x and y"""
    return x * y

def factorial(n):
    """Returns the factorial of the value n"""
    return(reduce(mult, range(1, n+1)))
           
def add(x, y):
    """Returns the sum of x and y"""
    return x + y

def mean(L):
    """Returns the mean of a list L"""
    return (reduce(add, L)) / len(L)
 
