"""
In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:
    years divisible by 4 are leap years
    but years divisible by 100 are not leap years
    but years divisible by 400 are leap years

Only valid years (positive integers) will be tested, so you don't have to validate them
"""


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


print(is_leap_year(2020))