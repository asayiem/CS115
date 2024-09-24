# Name: Abu Sayiem
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# CS 115 - lab2

def dot(L, K):
    '''given two integer lists of equal length, returns the dot product of the two lists'''
    if L == []:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

def ind(e, L):
    '''returns the index at which element e appears in L. If e is not in L, the length of L is returned'''
    x = 0
    if L == []:
        return len(L)
    elif L[0] == e:
        return x
    else:
        return ind(e, L[1:]) + (x+1)


def removeAll(e, L):
    '''returns a new list, with all instances of e removed from L'''
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

def squareList(L):
    '''returns a new list, with the squares of all of the elements of L'''
    if L == []:
        return []
    else:
        return [L[0] ** 2] + squareList(L[1:])
