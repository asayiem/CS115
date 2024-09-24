# NAME: Abu Sayiem          
# PLEDGE: I pledge my honor that I have abided by the Stevens Honor System.
# DATE: 11.16.23       

## CS 115 Fall 2023 - Lab 9


## TASK 1: factorial


def factorial(n):
    '''iterative implementation of factorial function. assume n >= 0'''
    result = 1
    
    for i in range(1, n + 1):
        result *= i
        assert result == result
    return result
    

## TASK 2: doubleString

def doubleString(s):
    '''returns a new string, where each character is doubled'''
    result = ""
    for i in range(len(s)):
        result += 2*s[i]
    return result


## TASK 3: myMap
def inc(x):
    return x + 1

def myMap(func, L):
    '''maps func to each element of the list L, and returns the new list. assume L is always a list'''
    result = []
    for i in range(len(L)):
        result += [func(L[i])]
    return result


## TASK 4: polynomial

def polynomial(coeff, x):
    '''iteratively evaulates a polynomial at a given x value'''
    result = 0
    for i in range(len(coeff)):
        if coeff[i] != 0:
            result += coeff[i] * (x ** i)
    return result
