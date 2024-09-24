'''
Created on 10.19.23
@author:   Abu Sayiem
Pledge:    I pledge that I abide by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if (n % 2 != 0):
        return True
    else:
        return False

''' The binary of 42 is 101010. This is done by dividing 42 by 2's.
1st we get 42/2 = 21 = 0
2nd we get 21/2 = 10 = 1
3rd we get 10/2 = 5 = 0
4th we get 5/2 = 2 = 1
5th we get 2/2 = 1 = 0
6th we get 1/2 = 0 = 1
The binary is the reverse of the order above. The numbers with a remiander
get the binary value of 1, while numbers without get a value of 0.
'''
#The least bit for an odd number would be 1 because an odd number would always have a remainder.
#The least bit for an even number would be 0 because it can be divisible by 2.
#Removing the least bit is essentially dividing the number by 2 so it would change the value of the original number by dividing by 2.

'''
We can deduce the value of N given Y by looking at the remiander of after integer division of 2
if there is a remainder, we know its an odd number with a binary value of 1
if there isn't a remainder, we know its an even number with a binary value of 0
'''



def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''

    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + str(1) 
    else: 
        return numToBinary(n // 2) + str(0)
	

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return binaryToNum(s[:-1]) * 2 + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if len(s) == 8:
        n = binaryToNum(s) + 1
        inc = numToBinary(n)
    if len(inc) > 8:
        return '00000000'
    else:
        return '0' * (8 - len(inc)) + inc
            

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if len(s) == 8 and n >= 0:
        if n == 0:
            print(s)
        else:
            print(s)
            inc = increment(s)
            count(inc, n - 1)

'''
59 using ternary

59 / 3 = 19 = remainder 2
19 / 3 = 6 = remainder 1
6/3 = 2 = remainder 0
2/3 = 0 = remainder 2

2012
'''
    

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    else:
        rem = n % 3
        return numToTernary(n // 3) + str(rem)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return ternaryToNum(s[:-1]) * 3 + int(s[-1])

    
