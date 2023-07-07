"""
Your job is to create a simple password validation function, as seen on many websites.
The rules for a valid password are as follows:
    There needs to be at least 1 uppercase letter.
    There needs to be at least 1 lowercase letter.
    There needs to be at least 1 number.
    The password needs to be at least 8 characters long.
You are permitted to use any methods to validate the password.
"""


def pass_validator(string):
    upper = False
    lower = False
    number = False
    if len(string) < 8:
        return False
    for char in string:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            number = True
        if upper and lower and number:
            return True
    return False


print(pass_validator("Gq%Wj;.q"))