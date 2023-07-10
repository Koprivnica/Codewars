"""
Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's
decimal digits.

For example: (Input --> Output)
10 --> 1
99 --> 18
-32 --> 5
"""



def sum_of_digits(number):
    sum = 0
    number = abs(number)
    while number:
        sum = sum + number % 10
        number //= 10
    return sum


print(sum_of_digits(-32))