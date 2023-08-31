"""
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!
"""


def sum_of_numbers(num_a, num_b):
    num_sum = 0
    for i in range(min(num_a, num_b), max(num_a, num_b) + 1):
        num_sum += i
    
    return num_sum


print(sum_of_numbers(5, 5))               