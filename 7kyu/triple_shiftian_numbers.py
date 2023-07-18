"""
Much cooler than your run-of-the-mill Fibonacci numbers, the Triple Shiftian are so defined: T[n] = 4 * T[n-1] - 5 * T[n-2] + 3 * T[n-3].

You are asked to create a function which accept a base with the first 3 numbers and then returns the nth element.

triple_shiftian([1,1,1],25) == 1219856746
triple_shiftian([1,2,3],25) == 2052198929
triple_shiftian([6,7,2],25) == -2575238999
triple_shiftian([3,2,1],35) == 23471258855679
triple_shiftian([1,9,2],2) ==  2
"""


def triple_shiftian(base,n):
    for i in range(3, n+1):
        base.append(4*base[i-1] - 5*base[i-2] + 3*base[i-3])
    return base[n]



print(triple_shiftian([1,1,1],25))