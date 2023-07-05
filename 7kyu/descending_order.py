"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.
"""


def decending_digits(num):
    return int("".join(sorted(str(num), reverse = True)))



print(decending_digits(175034))