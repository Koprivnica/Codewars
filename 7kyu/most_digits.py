"""
Find the number with the most digits.
If two numbers in the argument array have the same number of digits, return the first one in the array.
"""


def find_longest(array):
    return max(array, key = lambda x: len(str(x)))


print(find_longest([1, 234, 45678, 234, 789, 567890]))