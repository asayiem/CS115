'''
Created on  11.06.23
@author(s): Abu Sayiem
Partner: Angelia Knight
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
# You may write helpers if you see fit. Remember: do not
# import anything, and do not use loops.

def numToBinary(n):
    '''Returns the string with the binary representation of n.'''
    if n == 0:
        return ""
    return numToBinary(int(n / 2)) + str(n%2)

def binaryToNum(s):
    '''Returns the integer of the binary representation of s.'''
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def fill(s):
    '''fill a binary value with 0's '''
    return "0" * (5 - len(s)) + s


def compress(S):
    '''compresses a 64-bit binary image (represented as 1's
    and 0's) using a run-length encoding'''

    def comp_helper(S, x):
        '''return ["0", 0] where the 1st num shows if it's  a 1 or 
        0 and the 2nd num shows how long the 1 or 0 is'''
        if S == "":
            return [x]
        if S[0] != x[0] and x[1] != 0:
            return [x] + comp_helper(S[1:], [S[0]] + [1])

        return comp_helper(S[1:], [S[0]] + [x[1] + 1])

    def compress_more(y):
        '''takes the result from comp_helper(), returns binary string of base 10. Split if consecutive 1 or 0 is larger than MAX_RUN_LENGTH'''
        if y == []:
            return ""
        if y[0][1] > MAX_RUN_LENGTH:
            return "1111100000" + compress_more([[y[0][0]] + [y[0][1]-31]] + y[1:])

        return fill(numToBinary(y[0][1])) + compress_more(y[1:])
    if S[0] == "1":
        return "00000" + compress_more(comp_helper(S, ["0",0]))
    else:
        return "" + compress_more(comp_helper(S, ["0",0]))





def uncompress(C):
    '''uncompresses a run-length encoding to its original
    64-bit binary image'''

    def uncompress_more(C):
        '''uncompress binary and return a list of numbers of consecutive 0 and 1'''
        if C == "":
            return []
        return [binaryToNum(C[0:COMPRESSED_BLOCK_SIZE])] + uncompress_more(C[COMPRESSED_BLOCK_SIZE:])

    def uncomp_helper(y, z):
        '''takes result from uncompress_more() and gives the original binary string '''
        if y == []:
            return ""
        if z:
            return "0" * y[0] + uncomp_helper(y[1:], not z)
        else:
            return "1" * y[0] + uncomp_helper(y[1:], not z)


    return uncomp_helper(uncompress_more(C), True)
