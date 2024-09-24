'''
Author: Abu Sayiem
Pledge: I pledge that I abide by the Stevens Honor System.
'''
#Problem 1
def addOne(L):
    """given a list of numbers, returns a list of number after adding 1 to each value"""
    if (L == []):
        return []
    else:
        return [L[0]+ 1] + addOne(L[1:])
    
#Problem 2
def explode(S):
    '''given a string, returns a list with each letter'''
    
    if (S == ""):
        return []
    else:
        return [(S[0])] + explode(S[1:])


#Problem 3
def myFilter(func,L):
    ''' given a function and a list, returns a filtered list of values that return true with the function'''

    if L == []:
        return []
    elif (func(L[0])):
        return [L[0]] + myFilter(func, L[1:])
    else:
        return myFilter(func, L[1:])

def even(n):
    return n % 2 == 0
def odd(n):
    return n % 2 != 0

#Problem 4
def sumPos(L):
    '''given a list of numbers, returns the sum of positive numbers'''
    if L == []:
        return 0
    elif(L[0] >= 0):
         return L[0] + sumPos(L[1:])
    else:
        return sumPos(L[1:])
