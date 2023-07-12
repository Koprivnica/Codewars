"""
Write a function that returns a sequence (index begins with 1) of all the even characters from a string. If the string is smaller than
two characters or longer than 100 characters, the function should return "invalid string".

For example:
"abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
"a"             --> "invalid string"
"""


def even_chars(input_string):
    if len(input_string) < 2 or len(input_string) > 100:
        return "invalid string"
    else:
        return [char for i, char in enumerate(input_string) if i % 2 != 0]


print(even_chars("a"))