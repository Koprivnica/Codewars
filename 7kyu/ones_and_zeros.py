"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11

However, the arrays can have varying lengths, not just limited to 4.
"""


def bin_to_dec(array):
    return int("".join(map(str, array)), 2)

def bin_to_dec2(array):
    sum = 0
    for i, elem in enumerate(array[::-1]):
        sum = sum + elem * 2 ** i
    
    return sum
        


print(bin_to_dec([0, 0, 1, 0]))